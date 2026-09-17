# Index des labs

Correspondance entre les labs produits et les objectifs du study guide officiel
(compétences mesurées au 30 juin 2026). **La colonne « Objectifs officiels » fait foi** :
c'est elle qui dit ce qu'un lab couvre réellement, le nom de fichier n'en est qu'un raccourci.

## Règle de nommage

Depuis le recalage du référentiel, le nom de fichier porte la numérotation officielle :

- **Numéro de groupe** (`2.3-posting-groups.md`) quand le lab est le lab principal de son groupe.
- **Numéro d'objectif** (`2.4.1-bank-account-setup.md`) quand le lab traite un objectif isolé,
  ou complète un groupe dont un autre lab porte déjà le numéro.
- **`hors-referentiel-`** pour un lab qui ne couvre aucun objectif mesuré.

Un lab à cheval sur plusieurs groupes prend le numéro de son groupe dominant ; les autres
objectifs qu'il couvre apparaissent dans la colonne ci-dessous et dans son bloc méta.

## Labs

| Lab | Objectifs officiels couverts | Remarque |
|---|---|---|
| `1.4-dimensions.md` | 1.4.1 à 1.4.6 | Groupe `1.4 Set up dimensions` en entier. |
| `2.1-finance-setup.md` | 2.1.4, 2.1.5, 2.1.10 · 2.2.1 | General ledger setup, accounting periods, G/L accounts, account categories. Ne couvre que 3 des 12 objectifs du groupe 2.1. |
| `2.1.8-currency-exchange-rates.md` | 2.1.8 · 4.5.9 | Paramétrage des devises, et ajustement des taux côté opérations. |
| `2.2.2-financial-reports-analysis-views.md` | 2.2.2 | Financial reports, row/column definitions, analysis views. Ne couvre pas `2.2.3` general ledger allocations. |
| `2.3-posting-groups.md` | 2.3.1 à 2.3.3 | Ne couvre pas `2.3.4 Configure inventory posting setup` ni `2.3.5 Allow multiple posting groups`. |
| `2.4.1-bank-account-setup.md` | 2.4.1 | Fiche `Bank Account` : No. Series dédié, `Bank Acc. Posting Group`, devise, formats d'export et d'import. Ne poste aucune écriture. |
| `2.4.2-journal-templates-number-series.md` | 2.4.2 | `No. Series` vs `Posting No. Series`, `Source Code`, `Reason Code`, effet du `Type` du template. |
| `2.4.3-general-journal-batches.md` | 2.4.3 | Héritage template → batch, `Bal. Account Type`/`No.`, TVA au niveau batch. |
| `2.4.4-recurring-journals.md` | 2.4.4 | `Recurring Method`, `Recurring Frequency`, `Expiration Date`, allocations. |
| `2.5-payment-discounts.md` | 2.5.1, 2.5.2 | Escompte de règlement fournisseur. Ne couvre pas `2.5.4` ; `2.5.3 Set up payment journals` n'est vu que côté opérations dans `4.5-cash-management.md`. |
| `2.6-accounts-receivable-setup.md` | 2.6.1 à 2.6.4 | Ne couvre pas `2.6.5` (relation customer ledger entries / detailed / G/L). |
| `2.7-fixed-assets-setup.md` | 2.7.1 à 2.7.3 · 4.6.1 à 4.6.3 | Paramétrage **et** transactions d'immobilisations. |
| `4.5-cash-management.md` | 4.5.1, 4.5.6 · 2.4.1 en partie | Payment journals et rapprochement bancaire. Le paramétrage de la fiche `Bank Account` appartient désormais à `2.4.1-bank-account-setup.md` : ici il n'est qu'un pré-requis. |
| `hors-referentiel-vat-posting-setup.md` | **aucun** | La TVA n'est pas une compétence mesurée. Recoupe partiellement `2.3 Set up posting groups` par la mécanique des posting groups. À traiter en dernier, voire à ignorer. |

## Renommages du 2026-09-17

Les labs antérieurs au recalage du référentiel portaient l'ancienne numérotation. Table de
correspondance, utile si tu as des PDF déjà imprimés :

| Ancien nom | Nouveau nom | Pourquoi |
|---|---|---|
| `2.2-posting-groups.md` | `2.3-posting-groups.md` | Le groupe officiel des posting groups est `2.3`. |
| `2.3-currency-exchange-rates.md` | `2.1.8-currency-exchange-rates.md` | Objectif isolé du groupe `2.1`, dont `2.1-finance-setup.md` porte déjà le numéro. |
| `2.4-accounts-receivable-setup.md` | `2.6-accounts-receivable-setup.md` | Le groupe officiel des accounts receivables est `2.6`. |
| `2.6-vat-posting-setup.md` | `hors-referentiel-vat-posting-setup.md` | Aucun objectif mesuré, et `2.6` revient aux accounts receivables. |
| `2.7-cash-management.md` | `4.5-cash-management.md` | Son contenu dominant relève de `4.5 Process journals and payments`. |
| `2.8-fixed-assets-setup.md` | `2.7-fixed-assets-setup.md` | Le groupe officiel des fixed assets est `2.7`. |
| `2.9-financial-reports-analysis-views.md` | `2.2.2-financial-reports-analysis-views.md` | Objectif isolé du groupe `2.2`. |

Inchangés : `1.4-dimensions.md`, `2.1-finance-setup.md`, `2.5-payment-discounts.md` — leur
numéro correspondait déjà au groupe officiel.

`journal.csv` et `erreurs.csv` étaient vides au moment du renommage : aucune reprise d'historique
n'a été nécessaire. `tools/chemins-verifies.csv` et `lexique.csv` ont été remis à jour sur les
nouveaux noms.

## Objectifs sans lab, à fort rendement

Points du guide officiel qu'aucun lab ne couvre et qui ne relèvent pas de la pratique
quotidienne d'un référent ERP :

- `1.1.2` Create a configuration worksheet · `1.1.3` configuration package · `1.1.4` journal opening balances
- `1.2.4` Apply security filters · `1.2.5` security groups · `1.2.6` security auditing
- `1.3.4` **Enable Copilot and agent capabilities** — nouveauté de la version du 30/06/2026
- `2.1.1` native workflows · `2.1.2` notification system · `2.1.3` approval user groups · `2.1.12` manage approvals
- `2.1.7` Set up deferrals, et son pendant opérationnel `4.2.9` / `4.3.9`
- `2.2.3` general ledger allocations, et `4.5.8`
- `2.3.4` inventory posting setup · `2.3.5` allow multiple posting groups
- `2.5.4` / `2.6.5` relation ledger entries ↔ detailed ledger entries ↔ G/L entries
- `3.1.6` stockkeeping units · `3.1.2` item attributes et variants
- `4.4.10` prepayment invoices · `4.4.5` / `4.4.6` combinaison d'expéditions et de réceptions
- `4.5.10` **Dimension Correction Tool** · `4.5.11` revalue G/L account balances
- `4.7` Process inventory transactions — groupe entièrement **nouveau**
