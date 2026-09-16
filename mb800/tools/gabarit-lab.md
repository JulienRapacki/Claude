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
## 3. Mission             (sous-sections ###, chemin {nav:} + actions champ/valeur)
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

## Chemins d'accès

Syntaxe dédiée, sur sa propre ligne, avant les actions qu'elle rend possibles :

```
{nav: Tell Me (Alt+Q) > Dimensions > New}
{nav: Sales > Customers > (sélectionner le client) > Navigate > Dimensions ?}
```

- Séparateur `>`. Rendu en fil d'Ariane accentué, détaché du texte : le chemin doit se voir sans lire.
- Une étape entre parenthèses décrit une sélection ou une condition, pas un clic de menu.
- Les chemins donnés en exemple dans ce gabarit sont **illustratifs, pas vérifiés** : ne les recopie
  jamais dans un lab sans les marquer.
- **Un `?` en fin de chemin marque un chemin non certain.** Il se rend en gris avec la mention
  « chemin à confirmer ». Mieux vaut un chemin marqué douteux qu'un chemin faux affirmé.

## Format d'une étape de mission

Une sous-section `###` par étape, puis le chemin, puis les actions. Une action = un champ, une valeur :

```
### 3.2 Poser la default dimension sur le client

{nav: Sales > Customers > (ouvrir le client) > Related > Customer > Dimensions}

- Dans `Dimension Code`, sélectionne `PROJECT`.
- Dans `Value Posting`, sélectionne `Code Mandatory`.
- Laisse `Dimension Value Code` vide.
```

Les étapes mécaniques sont entièrement guidées : chemin, champ, valeur. Les étapes qui **constituent
l'apprentissage** (un arbitrage, un diagnostic, une prévision de comportement) gardent leur formulation
ouverte — on donne le chemin vers la bonne page, jamais la réponse.

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
