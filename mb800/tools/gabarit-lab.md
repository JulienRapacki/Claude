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

## Chemins vérifiés

Ces accès sont attestés par la documentation Business Central officielle
(`MicrosoftDocs/dynamics365smb-docs`) ou par les labs officiels du cours MB-800
(`microsoftlearning/MB-800-...`). **Recopie-les tels quels, sans les marquer d'un `?`.**
Le registre complet, avec citation fichier et ligne pour chacun, est dans
`mb800/tools/chemins-verifies.csv`.

| Chemin | Source |
|---|---|
| `Tell Me (Alt+Q) > Accounting Periods` | doc-bc |
| `Tell Me (Alt+Q) > Adjust Exchange Rates` | doc-bc |
| `Tell Me (Alt+Q) > Analysis Views` | doc-bc |
| `Tell Me (Alt+Q) > Analysis Views > (sélectionner la vue) > Analysis by Dimensions` | doc-bc |
| `Tell Me (Alt+Q) > Bank Account Ledger Entries` | doc-bc |
| `Tell Me (Alt+Q) > Bank Account Posting Groups > New` | labs-ms |
| `Tell Me (Alt+Q) > Bank Account Reconciliation > New` | doc-bc |
| `Tell Me (Alt+Q) > Bank Accounts > New` | labs-ms |
| `Tell Me (Alt+Q) > Calculate Depreciation` | doc-bc |
| `Tell Me (Alt+Q) > Cash Receipt Journals` | doc-bc |
| `Tell Me (Alt+Q) > Chart of Accounts > (ouvrir un G/L account utilisable en ligne de facture) > Posting` | doc-bc |
| `Tell Me (Alt+Q) > Chart of Accounts > (ouvrir un des comptes Posting créés) > Account Category` | doc-bc |
| `Tell Me (Alt+Q) > Chart of Accounts > (sélectionner le(s) compte(s)) > Account > Dimensions-Multiple > Dimensions - Multiple` | labs-ms |
| `Tell Me (Alt+Q) > Chart of Accounts > New` | labs-ms |
| `Tell Me (Alt+Q) > Column Definitions` | doc-bc |
| `Tell Me (Alt+Q) > Currencies > New` | doc-bc |
| `Tell Me (Alt+Q) > Currency Exchange Rates` | doc-bc |
| `Tell Me (Alt+Q) > Customer Ledger Entries` | doc-bc |
| `Tell Me (Alt+Q) > Customer Posting Groups > (ouvrir le Customer Posting Group du client test)` | labs-ms |
| `Tell Me (Alt+Q) > Customer Posting Groups > (ouvrir ou créer le Customer Posting Group du client test)` | labs-ms |
| `Tell Me (Alt+Q) > Customers > (ouvrir le client test) > Payments FastTab` | labs-ms |
| `Tell Me (Alt+Q) > Customers > (ouvrir le client) > Customer > Dimensions` | labs-ms |
| `Tell Me (Alt+Q) > Customers > (ouvrir le client) > Invoicing FastTab` | labs-ms |
| `Tell Me (Alt+Q) > Customers > (ouvrir un client de test) > Invoicing` | doc-bc |
| `Tell Me (Alt+Q) > Default Dimension Priorities` | doc-bc |
| `Tell Me (Alt+Q) > Depreciation Books > New` | doc-bc |
| `Tell Me (Alt+Q) > Dimension Combinations` | doc-bc |
| `Tell Me (Alt+Q) > Dimensions > (sélectionner la dimension) > Dimension > Dimension Values` | labs-ms |
| `Tell Me (Alt+Q) > Dimensions > New` | labs-ms |
| `Tell Me (Alt+Q) > FA G/L Journals` | doc-bc |
| `Tell Me (Alt+Q) > FA Ledger Entries` | doc-bc |
| `Tell Me (Alt+Q) > FA Posting Groups > (ouvrir LAB-EQUIP)` | doc-bc |
| `Tell Me (Alt+Q) > FA Posting Groups > New` | doc-bc |
| `Tell Me (Alt+Q) > Finance Charge Memos > action Create Finance Charge Memos` | doc-bc |
| `Tell Me (Alt+Q) > Finance Charge Terms > New` | doc-bc |
| `Tell Me (Alt+Q) > Financial Reports` | doc-bc |
| `Tell Me (Alt+Q) > Fixed Assets > (ouvrir la fiche créée) > Related > Fixed Asset > Depreciation Books` | doc-bc |
| `Tell Me (Alt+Q) > Fixed Assets > New` | doc-bc |
| `Tell Me (Alt+Q) > G/L Account Categories` | doc-bc |
| `Tell Me (Alt+Q) > Gen. Business Posting Groups > New` | doc-bc |
| `Tell Me (Alt+Q) > General Journal Templates > (sélectionner ton template) > Batches` | labs-ms |
| `Tell Me (Alt+Q) > General Journal Templates > New` | labs-ms |
| `Tell Me (Alt+Q) > General Journals` | labs-ms |
| `Tell Me (Alt+Q) > General Journals > (Batch Name = ton batch)` | labs-ms |
| `Tell Me (Alt+Q) > General Ledger Entries` | doc-bc |
| `Tell Me (Alt+Q) > General Ledger Setup` | doc-bc |
| `Tell Me (Alt+Q) > General Posting Setup > New` | labs-ms |
| `Tell Me (Alt+Q) > General Product Posting Groups > New` | labs-ms |
| `Tell Me (Alt+Q) > Items > (ouvrir l'article) > Costs & Posting FastTab` | doc-bc |
| `Tell Me (Alt+Q) > Items > (ouvrir un second article, avec un Gen. Prod. Posting Group différent) > Costs & Posting FastTab` | doc-bc |
| `Tell Me (Alt+Q) > Payment Journals` | doc-bc |
| `Tell Me (Alt+Q) > Payment Methods > New` | doc-bc |
| `Tell Me (Alt+Q) > Payment Terms > New` | doc-bc |
| `Tell Me (Alt+Q) > Posted Sales Invoices > (ouvrir la facture postée de l'étape 3.5) > Find entries` | doc-bc |
| `Tell Me (Alt+Q) > Posted Sales Invoices > (ouvrir la facture postée) > Find entries` | doc-bc |
| `Tell Me (Alt+Q) > Purchase Invoices > New` | doc-bc |
| `Tell Me (Alt+Q) > Reminder Terms > New` | doc-bc |
| `Tell Me (Alt+Q) > Reminders > (page Reminder) > action Create Reminders` | doc-bc |
| `Tell Me (Alt+Q) > Row Definitions` | doc-bc |
| `Tell Me (Alt+Q) > Sales Invoice` | doc-bc |
| `Tell Me (Alt+Q) > Sales Invoices > New` | doc-bc |
| `Tell Me (Alt+Q) > VAT Business Posting Groups > New` | doc-bc |
| `Tell Me (Alt+Q) > VAT Posting Setup` | doc-bc |
| `Tell Me (Alt+Q) > VAT Product Posting Groups > New` | doc-bc |
| `Tell Me (Alt+Q) > VAT Statement` | doc-bc |
| `Tell Me (Alt+Q) > Vendor Ledger Entries > (sélectionner la facture postée)` | doc-bc |
| `Tell Me (Alt+Q) > Vendor Posting Groups > New` | labs-ms |
| `Tell Me (Alt+Q) > Vendors > (ouvrir le vendor de test)` | labs-ms |

### Ce que la vérification a appris

- **Le préfixe `Sales >`, `Purchasing >` ou tout autre segment de barre de navigation
  n'est attesté nulle part** : il dépend du Role Center. Passe toujours par `Tell Me (Alt+Q)`.
- **`Navigate` n'a pas disparu** : il subsiste comme groupe de ruban (`Navigate > Sales Prices`).
  Mais la recherche d'écritures depuis un document validé s'appelle désormais **`Find entries`**.
- **Le patron `Related > <entité> > Dimensions` est faux** sur les fiches client et compte général.
  La doc écrit `Customer > Dimensions`, sans niveau `Related`.
- **Les noms abrégés sont les bons** : `Gen. Business Posting Groups`, pas `General Business…`.
- **Un nom de traitement par lots n'est pas un nom de page** : `Create Reminders` est une action
  de la page `Reminders`, pas une cible de `Tell Me`. Même piège avec `Create Finance Charge Memos`.
- **Les listes sont au pluriel** : `Sales Invoices`, `Payment Journals`, `General Ledger Entries`.
  Le singulier est le titre de la fiche qui s'ouvre ensuite.

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
