#!/usr/bin/env python3
"""Génère la fiche d'auto-évaluation des groupes du référentiel MB-800.

    python3 mb800/tools/fiche-evaluation.py

Produit mb800/evaluation/auto-evaluation-groupes.md, puis son PDF via md2pdf.py.
Les groupes sont triés par poids de domaine décroissant : le premier groupe jugé
doit être un groupe qui compte.
"""

import csv
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
MB800 = TOOLS.parent
SORTIE = MB800 / "evaluation" / "auto-evaluation-groupes.md"


def poids_tri(poids):
    """'30-35' -> 35, pour trier du plus lourd au plus léger."""
    return -int(poids.split("-")[-1])


def main():
    groupes = OrderedDict()
    for r in csv.DictReader(open(MB800 / "referentiel.csv")):
        g = groupes.setdefault(r["groupe"], {"domaine": r["domaine"], "poids": r["poids"], "n": 0})
        g["n"] += 1

    ordonnes = sorted(groupes.items(), key=lambda kv: (poids_tri(kv[1]["poids"]), kv[0]))

    lignes = []
    domaine_courant = None
    for nom, g in ordonnes:
        if g["domaine"] != domaine_courant:
            domaine_courant = g["domaine"]
            lignes.append(f"\n### {domaine_courant} — {g['poids']} %\n")
            lignes.append("| Groupe | Objectifs | Confiance | Note |")
            lignes.append("|---|---|---|---|")
        lignes.append(f"| {nom} | {g['n']} | `0`  `1`  `2`  `3` | |")

    corps = "\n".join(lignes)
    total = sum(g["n"] for g in groupes.values())

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(
        f"""# Auto-évaluation MB-800

| | |
|---|---|
| Objet | Situer ton niveau sur les {len(groupes)} groupes du référentiel officiel |
| Date | |
| Durée | 30 minutes, pas plus |

> [!objectif] Pourquoi cette fiche passe avant tout le reste
> - Le rétroplanning suit l'ordre du référentiel, qui n'est pas l'ordre de tes faiblesses.
> - Réviser ce qu'on pratique depuis quinze ans, c'est payer plein tarif pour ce qu'on sait déjà.
> - Les prochains labs seront produits là où ta confiance est faible, pas au hasard du barème.

> [!attention] Juge les {len(groupes)} groupes, pas les {total} objectifs
> Évaluer les {total} objectifs un par un dès la première passe, c'est abandonner au trentième.
> Tu descends au niveau objectif **seulement** sur les groupes que tu notes `0` ou `1`.

## Échelle de confiance

| | |
|---|---|
| `0` | Jamais vu. Je ne saurais pas où commencer. |
| `1` | Notion floue. J'en ai entendu parler, je ne sais pas faire. |
| `2` | Je sais faire en cherchant, en m'appuyant sur la documentation ou un exemple. |
| `3` | Je paramètre sans documentation, et je sais expliquer pourquoi. |

Sois sévère sur le `3` : la question d'examen ne porte pas sur ce que tu fais au quotidien,
mais sur le comportement du produit dans un cas que tu n'as jamais rencontré.

## Grille
{corps}

## Report dans le dépôt

Une fois la grille remplie, reporte-la dans `mb800/referentiel.csv` :

- `confiance` : la note du groupe sur chacun de ses objectifs, en première approximation.
- `date_evaluation` : la date du jour, format `AAAA-MM-JJ`.
- `statut` : `acquis` si `3`, `en_cours` si `2`, sinon `a_travailler`.

Puis réordonne `mb800/planning.md` : les groupes à fort poids et faible confiance passent devant,
quel que soit leur numéro. C'est cette fiche qui décide du plan, pas l'inverse.
""",
        encoding="utf-8",
    )

    print(f"{SORTIE.relative_to(Path.cwd())} — {len(groupes)} groupes, {total} objectifs")
    r = subprocess.run([sys.executable, str(TOOLS / "md2pdf.py"), str(SORTIE)], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())


if __name__ == "__main__":
    main()
