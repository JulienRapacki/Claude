# Index des labs

Correspondance entre les labs produits et les objectifs du study guide officiel
(compétences mesurées au 30 juin 2026).

Les labs ont été rédigés **avant** le recalage du référentiel sur le guide officiel.
Leur numéro de fichier suit l'ancienne numérotation ; la colonne « Objectifs officiels »
fait foi. Les fichiers ne sont pas renommés : leur nom est cité dans `journal.csv`.

| Lab | Objectifs officiels couverts | Remarque |
|---|---|---|
| `1.4-dimensions.md` | 1.4.1 à 1.4.6 | Couvre le groupe `1.4 Set up dimensions` en entier. Numérotation inchangée par chance. |
| `2.1-finance-setup.md` | 2.1.4, 2.1.5, 2.1.10 · 2.2.1 · 2.4.2, 2.4.3 | À cheval sur trois groupes : general ledger setup, accounting periods, account categories, journal templates et batches. |
| `2.2-posting-groups.md` | 2.3.1 à 2.3.3 | Ne couvre pas `2.3.4 Configure inventory posting setup` ni `2.3.5 Allow multiple posting groups`. |
| `2.3-currency-exchange-rates.md` | 2.1.8 · 4.5.9 | Paramétrage des devises, et ajustement des taux côté opérations. |
| `2.4-accounts-receivable-setup.md` | 2.6.1 à 2.6.4 | Ne couvre pas `2.6.5` (relation customer ledger entries / detailed / G/L). |
| `2.5-payment-discounts.md` | 2.5.1, 2.5.2 | Escompte de règlement fournisseur. Ne couvre pas `2.5.3` ni `2.5.4`. |
| `2.6-vat-posting-setup.md` | **aucun** | La TVA n'est pas une compétence mesurée. Recoupe partiellement `2.3 Set up posting groups` par la mécanique des posting groups. À traiter en dernier, voire à ignorer. |
| `2.7-cash-management.md` | 2.4.1 · 4.5.1, 4.5.6 | Comptes bancaires, payment journals, rapprochement bancaire. |
| `2.8-fixed-assets-setup.md` | 2.7.1 à 2.7.3 · 4.6.1 à 4.6.3 | Couvre le paramétrage et les transactions d'immobilisations. |

## Objectifs sans lab, à fort rendement

Points du guide officiel qu'aucun lab ne couvre et qui ne relèvent pas de la pratique
quotidienne d'un référent ERP :

- `1.1.2` Create a configuration worksheet · `1.1.3` configuration package · `1.1.4` journal opening balances
- `1.2.4` Apply security filters · `1.2.5` security groups · `1.2.6` security auditing
- `1.3.4` **Enable Copilot and agent capabilities** — nouveauté de la version du 30/06/2026
- `2.1.1` native workflows · `2.1.2` notification system · `2.1.3` approval user groups · `2.1.12` manage approvals
- `2.1.7` Set up deferrals, et son pendant opérationnel `4.2.9` / `4.3.9`
- `2.2.3` general ledger allocations, et `4.5.8`
- `3.1.6` stockkeeping units · `3.1.2` item attributes et variants
- `4.4.10` prepayment invoices · `4.4.5` / `4.4.6` combinaison d'expéditions et de réceptions
- `4.5.10` **Dimension Correction Tool** · `4.5.11` revalue G/L account balances
- `4.7` Process inventory transactions — groupe entièrement **nouveau**
