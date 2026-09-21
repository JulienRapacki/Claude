# Préparation MB-800

Certification visée : *Microsoft Certified: Dynamics 365 Business Central Functional Consultant Associate*.
Examen : **novembre 2026** — date exacte à figer ici : `à définir`.
Study guide officiel : <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800>

> **Référentiel recalé sur la source officielle.** Les 125 objectifs de `referentiel.csv` sont
> repris mot pour mot du study guide Microsoft, compétences mesurées **au 30 juin 2026**
> (page datée du 30/05/2026). Ils ne sont plus une reconstitution de mémoire.

## Langue

L'examen se passe en anglais. **Toutes les dénominations d'interface, de pages, de champs et de tables
sont écrites en anglais** dans le référentiel, les labs et les journaux. Le français reste la langue du
raisonnement et des notes. La base de test étant en français, chaque lab porte un **lexique EN → FR**
isolé en dernière section, et `lexique.csv` en cumule les termes.

C'est un vrai mode d'échec, pas une coquetterie : la confusion de terminologie est une cause d'erreur
à part entière dans `erreurs.csv`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `referentiel.csv` | Les 125 objectifs officiels, regroupés en 21 groupes, avec confiance et statut. C'est le tableau de bord. |
| `planning.md` | Rétroplanning 10 semaines, pondéré par le poids des domaines. Provisoire jusqu'à l'auto-évaluation. |
| `journal.csv` | Une ligne par session de travail. |
| `erreurs.csv` | Une ligne par erreur commise en quiz ou en blanc. Le fichier le plus utile du dispositif. |
| `lexique.csv` | Termes d'interface EN → FR, cumulés au fil des labs. |
| `labs/` | Les labs pratiques, générés par l'agent `mb800-lab`. Markdown = source. Nom de fichier = numérotation officielle. |
| `labs/INDEX.md` | Correspondance labs → objectifs officiels, règle de nommage, et liste des objectifs sans lab. |
| `tools/chemins-verifies.csv` | Registre des 88 chemins d'accès, un verdict sourcé par chemin. |
| `labs/pdf/` | Les mêmes labs en PDF paginé, à imprimer et à cocher. Généré, jamais édité à la main. |
| `tools/` | Gabarit de mise en page, feuille de style d'impression, convertisseur Markdown → PDF. |

## Conventions de saisie

- `confiance` : `0` jamais vu · `1` notion floue · `2` je sais faire en cherchant · `3` je paramètre sans documentation.
  Première passe au niveau du **groupe** (21 lignes à juger), puis descente au niveau objectif sur les groupes faibles.
  Évaluer 125 objectifs un par un dès le départ, c'est abandonner au trentième.
- `statut` : `a_evaluer` → `a_travailler` → `en_cours` → `acquis`.
- `cause` (erreurs) : `connaissance` · `confusion` · `lecture` · `terminologie` · `piege_examen`.
- `type` (journal) : `lecture` · `pratique` · `lab` · `quiz` · `blanc`.
- Dates au format `YYYY-MM-DD`. Champ non renseigné = `NA`, jamais de valeur devinée.
- Plusieurs objectifs dans une même cellule : séparateur `;` (ex. `2.4.2;2.4.3`).

## Boucle de travail

1. Générer le lab d'un objectif : agent `mb800-lab`, en lui passant l'id de l'objectif (ex. `2.4.4`).
   Un id de groupe (`2.4`) n'est pas un id valide : le référentiel n'en contient pas.
   Il produit le Markdown **et** le PDF.
2. Imprimer le PDF et l'exécuter sur la base de test. Jamais sur la production.
3. Répondre aux 3 questions de contrôle du lab.
4. Journaliser la session dans `journal.csv`.
5. Verser chaque réponse fausse dans `erreurs.csv`, avec sa cause.
6. Fiche de connaissance dans Obsidian (skill `obsidian-fiche`) **seulement si l'objectif résiste** après le lab.
7. Mettre à jour `confiance` et `statut` dans `referentiel.csv`.

Un objectif ne passe `acquis` qu'après un lab exécuté **et** trois questions de contrôle réussies.
La lecture seule ne suffit jamais.

## Labs : Markdown en source, PDF en sortie

Le format de travail est le Markdown, versionné par git. Le PDF est **généré**, jamais édité :

```
python3 mb800/tools/md2pdf.py mb800/labs/1.4-dimensions.md   # un lab
python3 mb800/tools/md2pdf.py                                # tous les labs
```

Dépendances : `pip install markdown` et un binaire Chromium (auto-détecté ; sinon renseigne
`CHROMIUM_BIN`). La mise en page est contractualisée dans `tools/gabarit-lab.md` — c'est ce fichier
que lisent l'agent `mb800-lab` (qui rédige) et l'agent `doc-didactique` (qui remet en page un document
existant et regénère le PDF).

Un PDF qu'on corrige à la main est un PDF perdu à la prochaine génération : les corrections se font
dans le `.md`.

## Chemins d'accès : vérifiés, pas devinés

Les 88 chemins `{nav:}` des labs ont été confrontés à deux sources primaires clonées en local :
la documentation Business Central officielle (`MicrosoftDocs/dynamics365smb-docs`, 2 643 pages,
c'est la source de learn.microsoft.com) et les 25 labs officiels du cours MB-800
(`microsoftlearning/MB-800-...`).

Résultat au 21/09/2026, sur 123 lignes de registre : **98 attestés** (73 par la doc, 25 par les
labs officiels), **24 corrigés**, **1 encore douteux**. Chaque ligne de
`tools/chemins-verifies.csv` porte sa citation `fichier:ligne`. Un chemin sans citation reste
marqué d'un `?`, qui se rend en gris dans le PDF — la vraisemblance n'est pas une preuve.

Le registre compte 123 lignes pour 122 chemins présents dans les labs : la ligne en trop est
`G/L Account Categories`, vérifiée lors de la première passe puis retirée du lab `2.1`. Elle est
conservée — c'est un nom de page attesté, réutilisable par un prochain lab.

Les accès réutilisables sont repris dans `tools/gabarit-lab.md`, section « Chemins vérifiés » :
les prochains labs les recopient au lieu de les réinventer.

Les labs `2.4.1` à `2.4.4` ont été passés au registre le 21/09/2026 : leurs 35 chemins y ont
chacun leur ligne. Les 5 qui portaient un `?` sont tranchés — 4 attestés tels quels, 1 corrigé
(`Data Exch. Definitions` → `Data Exchange Definitions`). Plus aucun chemin douteux dans ces
quatre labs.

Cette passe-là s'est faite sur un corpus **reconstitué et partiel** : 991 des 1 004 pages de doc
du tronc commun, mais seulement 14 des 25 labs officiels, le réseau de l'environnement ne laissant
passer que `raw.githubusercontent.com`. Un silence de `labs-ms` n'y vaut donc pas réfutation.

Reste que la doc n'est pas ta base : une version ou une personnalisation peut déplacer une action.
Un chemin attesté reste à confirmer au premier lab exécuté — mais tu ne cherches plus à l'aveugle.

## Répartition des rôles

Ce dépôt porte **le pilotage et la pratique**. Les fiches de connaissance vivent dans le coffre Obsidian :
pas de duplication du savoir, pas de backlinks cassés.

## Prochaines actions

- [ ] Figer la date d'examen en tête de ce fichier et l'inscrire dans `planning.md`.
- [ ] Auto-évaluer les 21 groupes, puis les objectifs des groupes faibles — semaine du 21/09.
- [ ] Réordonner `planning.md` : fort poids et faible confiance en premier.
- [ ] Confirmer sur la base les chemins d'accès marqués « à confirmer » dans les labs, et me les donner :
      je les injecte comme références vérifiées et le taux de doute s'effondre sur les labs suivants.
- [ ] Remplir la colonne `libelle_fr` de `lexique.csv` depuis la base française.
- [ ] Décider si l'agent `mb800-quiz` vaut le coup, une fois le référentiel priorisé.
