# Auto-évaluation MB-800

| | |
|---|---|
| Objet | Situer ton niveau sur les 21 groupes du référentiel officiel |
| Date | |
| Durée | 30 minutes, pas plus |

> [!objectif] Pourquoi cette fiche passe avant tout le reste
> - Le rétroplanning suit l'ordre du référentiel, qui n'est pas l'ordre de tes faiblesses.
> - Réviser ce qu'on pratique depuis quinze ans, c'est payer plein tarif pour ce qu'on sait déjà.
> - Les prochains labs seront produits là où ta confiance est faible, pas au hasard du barème.

> [!attention] Juge les 21 groupes, pas les 125 objectifs
> Évaluer les 125 objectifs un par un dès la première passe, c'est abandonner au trentième.
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

### Configure financials — 30-35 %

| Groupe | Objectifs | Confiance | Note |
|---|---|---|---|
| 2.1 Set up financial management | 12 | `0`  `1`  `2`  `3` | |
| 2.2 Manage the chart of accounts | 3 | `0`  `1`  `2`  `3` | |
| 2.3 Set up posting groups | 5 | `0`  `1`  `2`  `3` | |
| 2.4 Set up journals and bank accounts | 4 | `0`  `1`  `2`  `3` | |
| 2.5 Set up accounts payables | 4 | `0`  `1`  `2`  `3` | |
| 2.6 Set up accounts receivables | 5 | `0`  `1`  `2`  `3` | |
| 2.7 Configure fixed assets | 3 | `0`  `1`  `2`  `3` | |

### Perform Business Central operations — 30-35 %

| Groupe | Objectifs | Confiance | Note |
|---|---|---|---|
| 4.1 Perform basic tasks in Business Central | 8 | `0`  `1`  `2`  `3` | |
| 4.2 Process purchases | 9 | `0`  `1`  `2`  `3` | |
| 4.3 Process sales | 9 | `0`  `1`  `2`  `3` | |
| 4.4 Process financial documents | 10 | `0`  `1`  `2`  `3` | |
| 4.5 Process journals and payments | 11 | `0`  `1`  `2`  `3` | |
| 4.6 Process fixed asset transactions | 3 | `0`  `1`  `2`  `3` | |
| 4.7 Process inventory transactions | 6 | `0`  `1`  `2`  `3` | |

### Set up Business Central — 20-25 %

| Groupe | Objectifs | Confiance | Note |
|---|---|---|---|
| 1.1 Create and configure a company | 5 | `0`  `1`  `2`  `3` | |
| 1.2 Manage security | 6 | `0`  `1`  `2`  `3` | |
| 1.3 Set up core functionality | 4 | `0`  `1`  `2`  `3` | |
| 1.4 Set up dimensions | 6 | `0`  `1`  `2`  `3` | |

### Configure sales and purchasing — 10-15 %

| Groupe | Objectifs | Confiance | Note |
|---|---|---|---|
| 3.1 Set up inventory | 6 | `0`  `1`  `2`  `3` | |
| 3.2 Configure master data for sales and purchasing | 2 | `0`  `1`  `2`  `3` | |
| 3.3 Manage pricing and discounts | 4 | `0`  `1`  `2`  `3` | |

## Report dans le dépôt

Une fois la grille remplie, reporte-la dans `mb800/referentiel.csv` :

- `confiance` : la note du groupe sur chacun de ses objectifs, en première approximation.
- `date_evaluation` : la date du jour, format `AAAA-MM-JJ`.
- `statut` : `acquis` si `3`, `en_cours` si `2`, sinon `a_travailler`.

Puis réordonne `mb800/planning.md` : les groupes à fort poids et faible confiance passent devant,
quel que soit leur numéro. C'est cette fiche qui décide du plan, pas l'inverse.
