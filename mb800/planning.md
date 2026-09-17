# Rétroplanning MB-800

Cible : examen **fin novembre 2026**, date exacte à figer (`README.md`).
Départ : semaine du lundi 2026-09-21. 10 semaines.

Structure et pondérations conformes au study guide officiel, compétences mesurées
**au 30 juin 2026** (page datée du 30/05/2026).

| Domaine | Poids | Groupes | Objectifs |
|---|---|---|---|
| Set up Business Central | 20-25 % | 4 | 21 |
| Configure financials | **30-35 %** | 7 | 36 |
| Configure sales and purchasing | 10-15 % | 3 | 12 |
| Perform Business Central operations | 30-35 % | 7 | 56 |

> Ce séquencement est **provisoire**. Il sera réordonné après l'auto-évaluation de S1 :
> les groupes à fort poids et faible confiance passent devant, quel que soit leur numéro.
> Réviser dans l'ordre du référentiel quand on pratique BC au quotidien, c'est payer
> plein tarif pour ce qu'on sait déjà.

| Semaine | Du | Contenu | Livrable attendu |
|---|---|---|---|
| S1 | 21/09 | Auto-évaluation des 21 groupes, puis des objectifs des groupes faibles | Plus aucun groupe à `a_evaluer` |
| S2 | 28/09 | 1.1 Create and configure a company · 1.2 Manage security | 2 labs exécutés, journalisés |
| S3 | 05/10 | 1.3 Set up core functionality · 1.4 Set up dimensions | 2 labs exécutés |
| S4 | 12/10 | 2.1 Set up financial management · 2.2 Manage the chart of accounts | 2 labs exécutés |
| S5 | 19/10 | 2.3 Set up posting groups · 2.4 Set up journals and bank accounts · 2.5 Set up accounts payables | 2 labs exécutés |
| S6 | 26/10 | 2.6 Set up accounts receivables · 2.7 Configure fixed assets · 3.1 Set up inventory | 2 labs exécutés |
| S7 | 02/11 | 3.2 Master data sales/purchasing · 3.3 Pricing and discounts · 4.1 Perform basic tasks | 2 labs exécutés |
| S8 | 09/11 | 4.2 Process purchases · 4.3 Process sales · 4.4 Process financial documents | 2 labs exécutés |
| S9 | 16/11 | 4.5 Process journals and payments · 4.6 Fixed asset transactions · 4.7 Inventory transactions | 2 labs exécutés |
| S10 | 23/11 | Examens blancs, reprise intégrale de `erreurs.csv`, révision du `lexique.csv`, examen | Certification |

## Points d'attention issus du guide officiel

- `Configure financials` pèse **30-35 %**, à égalité avec les opérations. C'est le domaine le plus lourd.
- **Copilot et agents** (`1.3 Enable Copilot and agent capabilities`) sont une nouveauté de la version
  du 30/06/2026. Rien dans l'expérience terrain ne couvre ce point : il se révise de zéro.
- Le groupe `4.1 Perform basic tasks` est marqué « Major change » au change log : personalization,
  data analysis mode, Edit in Excel, inspect pages. Ne pas le traiter comme de la figuration.
- `4.7 Process inventory transactions` est un groupe **nouveau**.
- La TVA n'apparaît nulle part dans les compétences mesurées. Elle n'est pas un objectif d'examen.

## Règles de conduite

- Une semaine sans ligne dans `journal.csv` est une semaine perdue : elle décale tout le reste.
- Un objectif n'est `acquis` qu'après un lab exécuté **et** trois questions de contrôle réussies.
- Toute erreur de `erreurs.csv` non reprise sous 7 jours repasse en tête de la semaine suivante.
- S10 n'est pas du rab. Si le contenu déborde, c'est S7 (10-15 % du barème) qui se compresse.
