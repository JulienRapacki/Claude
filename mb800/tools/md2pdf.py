#!/usr/bin/env python3
"""Convertit un lab MB-800 (Markdown) en PDF paginé.

    python3 mb800/tools/md2pdf.py mb800/labs/1.4-dimensions.md [...]

Dépendances : pip install markdown, plus un binaire Chromium.
Le gabarit de source attendu est décrit dans mb800/tools/gabarit-lab.md.
"""

import glob
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Dépendance manquante : pip install markdown")

TOOLS = Path(__file__).resolve().parent
CSS = TOOLS / "lab.css"
OUT_DIR = TOOLS.parent / "labs" / "pdf"

CALLOUT_TITLES = {
    "objectif": "Objectif d'apprentissage",
    "prerequis": "Pré-requis",
    "attention": "Attention",
    "piege": "Piège d'examen",
    "astuce": "Astuce de terrain",
    "reponses": "Réponses",
}

CHROMIUM_CANDIDATES = [
    os.environ.get("CHROMIUM_BIN", ""),
    "/opt/pw-browsers/chromium-*/chrome-linux/chrome",
    "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/google-chrome",
]


def find_chromium():
    for pattern in CHROMIUM_CANDIDATES:
        if not pattern:
            continue
        for path in sorted(glob.glob(pattern), reverse=True):
            if os.access(path, os.X_OK):
                return path
    sys.exit("Aucun binaire Chromium trouvé. Renseigne CHROMIUM_BIN.")


def expand_callouts(text):
    """> [!type] Titre  ->  <div class="callout callout-type" markdown="1">"""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        m = re.match(r"^>\s*\[!(\w+)\]\s*(.*)$", lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind = m.group(1).lower()
        title = m.group(2).strip() or CALLOUT_TITLES.get(kind, kind.capitalize())
        body, i = [], i + 1
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^>\s?", "", lines[i]))
            i += 1
        out += [
            f'<div class="callout callout-{kind}" markdown="1">',
            f'<div class="callout-title">{title}</div>',
            "",
            *body,
            "",
            "</div>",
            "",
        ]
    return "\n".join(out)


def meta_table(html):
    """Premier tableau = bloc méta : en-tête vide retiré, 1re colonne en <th>."""
    m = re.search(r"<table>(.*?)</table>", html, re.S)
    if not m:
        return html
    tbl = m.group(1)
    rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)
    # Garde-fou : un bloc méta fait 2 colonnes et peu de lignes. Sinon on ne touche à rien.
    if not rows or any(len(re.findall(r"<t[dh][\s>]", r)) != 2 for r in rows) or len(rows) > 8:
        return html
    tbl = re.sub(r"<thead>\s*<tr>(?:\s*<th[^>]*>\s*</th>)+\s*</tr>\s*</thead>", "", tbl, flags=re.S)
    tbl = re.sub(r"<tr>\s*<td([^>]*)>(.*?)</td>", r"<tr><th\1>\2</th>", tbl, flags=re.S)
    return html[: m.start()] + f'<table class="meta">{tbl}</table>' + html[m.end() :]


def expand_nav(text):
    """{nav: A > B > (condition) > C}  ->  fil d'Ariane. Un '?' final = chemin douteux."""

    def repl(m):
        path = m.group(1).strip()
        doubt = path.endswith("?")
        path = path.rstrip("? ").strip()
        chunks = []
        for step in [p.strip() for p in path.split(">") if p.strip()]:
            cls = "cond" if step.startswith("(") and step.endswith(")") else "step"
            chunks.append(f'<span class="{cls}">{step}</span>')
        body = '<span class="sep">&rsaquo;</span>'.join(chunks)
        if doubt:
            body += '<span class="doubt">chemin à confirmer sur ta base</span>'
        cls = "nav nav-doubt" if doubt else "nav"
        return f'<div class="{cls}">{body}</div>'

    return re.sub(r"^\{nav:\s*(.+?)\}\s*$", repl, text, flags=re.M)


def postprocess(html):
    html = meta_table(html)
    return checklists(html)


def checklists(html):
    """Une <ul> dont les <li> commencent par "[ ]" devient une liste à cocher."""

    def repl(m):
        block = m.group(0)
        if "<li>[ ]" not in block:
            return block
        block = re.sub(r"<li>\[ \]\s*", "<li>", block)
        return block.replace("<ul>", '<ul class="checklist">', 1)

    return re.sub(r"<ul>(?:(?!</?ul>).)*?</ul>", repl, html, flags=re.S)


def build_html(md_path):
    raw = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(
        expand_nav(expand_callouts(raw)),
        extensions=["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists"],
    )
    body = postprocess(body)
    css = CSS.read_text(encoding="utf-8")
    foot = f"MB-800 — {md_path.stem} — source : mb800/labs/{md_path.name}"
    return (
        "<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'>"
        f"<title>{md_path.stem}</title><style>{css}</style></head>"
        f"<body>{body}<div class='docfoot'>{foot}</div></body></html>"
    )


def to_pdf(md_path, chromium):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf = OUT_DIR / f"{md_path.stem}.pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(build_html(md_path))
        html = fh.name
    try:
        subprocess.run(
            [
                chromium,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                "--no-pdf-header-footer",
                "--generate-pdf-document-outline",
                f"--print-to-pdf={pdf}",
                f"file://{html}",
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
    finally:
        os.unlink(html)
    return pdf


def main():
    targets = sys.argv[1:] or sorted(
        str(p) for p in (TOOLS.parent / "labs").glob("*.md")
    )
    if not targets:
        sys.exit("Aucun lab à convertir.")
    chromium = find_chromium()
    for t in targets:
        md = Path(t).resolve()
        if not md.is_file():
            print(f"ignoré (introuvable) : {t}")
            continue
        pdf = to_pdf(md, chromium)
        print(f"{md.name} -> {pdf.relative_to(Path.cwd())} ({pdf.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
