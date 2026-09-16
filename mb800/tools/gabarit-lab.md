# Gabarit d'un lab MB-800

Contrat de mise en page respecté par l'agent `doc-didactique` **et** par le convertisseur
`md2pdf.py`. Toute syntaxe absente d'ici n'est pas garantie au rendu PDF.

## Structure imposée

```
# Lab <id> — <Titre EN de l'objectif>

<bloc méta : tableau à 2 colonnes, 4 lignes>

> [!objectif] Ce que tu sauras faire à la fin
> 3 à 5 puces, verbe d'action à l'infinitif.

## 1. Praticabilité on-prem
## 2. Pré-requis          (checklist)
## 3. Mission             (étapes numérotées)
## 4. Points de contrôle  (checklist)
## 5. Pièges d'examen     (callouts [!piege])
## 6. Questions de contrôle (EN) + bloc réponses
## 7. Nettoyage
## 8. Lexique EN → FR     (tableau)
```

## Callouts

Syntaxe Obsidian, un type par bloc :

```
> [!objectif] Titre
> contenu markdown
```

| Type | Usage | Rendu |
|---|---|---|
| `objectif` | Ce qui est su faire à la fin. Une seule occurrence, en tête. | Encadré accentué |
| `prerequis` | Condition bloquante avant de commencer | Encadré neutre |
| `attention` | Risque de casse : production, irréversible, sauvegarde | Encadré rouge |
| `piege` | Confusion classique sanctionnée à l'examen | Encadré ambre |
| `astuce` | Raccourci de terrain, non exigible à l'examen | Encadré vert |
| `reponses` | Corrigé des questions de contrôle | Encadré + saut de page avant |

## Règles de forme

1. **Tout terme d'interface est en `code`** : `` `Value Posting` ``, `` `General Journal` ``.
   C'est ce qui rend le document scannable et ce qui ancre le vocabulaire anglais.
2. Checklists en `- [ ]` pour tout ce qui s'exécute ou se vérifie. Le lab s'imprime et se coche.
3. Une étape de mission = un paragraphe court + éventuellement des sous-puces. Jamais de pavé.
4. Les questions de contrôle sont en anglais. Les réponses vont dans un bloc `[!reponses]`,
   précédé d'un saut de page : on ne lit pas le corrigé par accident.
5. Pas de gras décoratif. Le gras marque une contrainte ou une valeur à saisir, rien d'autre.
6. Pas d'emoji.

## Génération du PDF

```
python3 mb800/tools/md2pdf.py mb800/labs/1.4-dimensions.md
```

Dépendances : `pip install markdown` et un binaire Chromium
(auto-détecté : `$CHROMIUM_BIN`, `/opt/pw-browsers/*/chrome-linux/chrome`, `chromium`, `google-chrome`).
Sortie : `mb800/labs/pdf/<nom>.pdf`.
