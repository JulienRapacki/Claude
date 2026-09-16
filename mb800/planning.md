# Rétroplanning MB-800

Cible : examen **fin novembre 2026**, date exacte à figer (`README.md`).
Départ : semaine du lundi 2026-09-21. 10 semaines, pondérées par le poids des domaines.

> Ce séquencement est **provisoire**. Il sera réordonné après l'auto-évaluation de S1 :
> les objectifs à fort poids et faible confiance passent devant, quel que soit leur numéro.
> Réviser dans l'ordre du référentiel quand on pratique BC au quotidien, c'est payer
> plein tarif pour ce qu'on sait déjà.

| Semaine | Du | Contenu | Livrable attendu |
|---|---|---|---|
| S1 | 21/09 | Recalage du référentiel sur le study guide officiel + auto-évaluation des 25 objectifs | `referentiel.csv` : colonnes `confiance` et `date_evaluation` remplies, plus aucun `a_evaluer` |
| S2 | 28/09 | Set up Business Central — 1.1 à 1.3 | 2 labs exécutés, journalisés |
| S3 | 05/10 | Set up Business Central — 1.4 à 1.6 (dimensions et configuration packages : gros gisement de questions) | 2 labs exécutés |
| S4 | 12/10 | Configure financials — 2.1 à 2.5 | 2 labs exécutés |
| S5 | 19/10 | Configure financials — 2.6 à 2.9 (VAT, cash management, fixed assets, financial reporting) | 2 labs exécutés |
| S6 | 26/10 | Configure sales and purchasing — 3.1 à 3.3 | 1 lab exécuté |
| S7 | 02/11 | Perform operations — 4.1 à 4.4 | 2 labs exécutés |
| S8 | 09/11 | Perform operations — 4.5 à 4.7 | 2 labs exécutés |
| S9 | 16/11 | Examens blancs + reprise intégrale de `erreurs.csv` | Score de blanc ≥ 80 % |
| S10 | 23/11 | Reprise ciblée des objectifs `confiance <= 1` + révision du `lexique.csv` + examen | Certification |

## Règles de conduite

- Une semaine sans ligne dans `journal.csv` est une semaine perdue : elle décale tout le reste, elle ne se rattrape pas.
- Un objectif n'est `acquis` qu'après un lab exécuté **et** trois questions de contrôle réussies. La lecture seule ne fait jamais passer un objectif à `acquis`.
- Toute erreur de `erreurs.csv` non reprise sous 7 jours est traitée comme une erreur non corrigée : elle repasse en tête de la semaine suivante.
- S9 et S10 ne sont pas du rab. Si le contenu déborde, c'est S6 (10-15 % du barème) qui se compresse, jamais les semaines de blanc.
