# Le programme d'exercices et de tests

## Une exigence explicite de la clause 8.5

La clause 8.5 d'ISO 22301 impose à l'organisation d'établir un **programme d'exercices (exercise programme)**, testant régulièrement les plans de continuité développés au module précédent de ce parcours — une exigence qui rejoint directement, dans son principe de vérification empirique plutôt que de simple confiance documentaire, celle déjà développée pour les tests de résilience opérationnelle numérique de DORA, ou pour le programme d'audit interne d'ISO 27001, tous deux développés dans les parcours dédiés de cette plateforme. Un plan de continuité jamais testé reste, par nature, une hypothèse non vérifiée sur la capacité réelle de l'organisation à reprendre son activité.

## Une gradation d'exercices, du plus simple au plus exigeant

La pratique de la continuité d'activité distingue généralement plusieurs types d'exercices, d'une complexité et d'un réalisme croissants :

- **L'exercice sur table (tabletop exercise)** — les participants discutent, autour d'une table, de leur réaction face à un scénario de crise hypothétique présenté par un animateur, sans mobiliser aucune ressource réelle ni interrompre l'activité normale. Un exercice peu coûteux et facile à organiser fréquemment, particulièrement adapté pour familiariser les nouveaux membres d'une cellule de crise avec leur rôle.
- **Le test technique isolé** — la vérification technique d'un composant spécifique du dispositif de continuité, par exemple la restauration effective d'une sauvegarde de données ou le basculement d'un système vers son infrastructure de secours, sans mobiliser l'ensemble de la structure de gestion de crise.
- **L'exercice de simulation** — un scénario plus réaliste, souvent conduit en temps réel ou accéléré, mobilisant effectivement la cellule de crise et une partie des équipes opérationnelles, sans toutefois interrompre réellement l'activité de production.
- **L'exercice grandeur nature (full-scale exercise)** — le test le plus exigeant et le plus réaliste, impliquant un basculement effectif vers les ressources de secours (site alternatif, infrastructure de repli) avec interruption contrôlée de tout ou partie de l'activité réelle — un exercice coûteux et risqué, réservé aux activités les plus critiques et généralement mené à une fréquence bien plus faible que les exercices sur table.

## Le rôle central du retour d'expérience (lessons learned)

Chaque exercice, quel que soit son niveau de complexité, doit systématiquement donner lieu à un **retour d'expérience formalisé** — les écarts constatés entre le déroulement réel de l'exercice et les prévisions documentées dans les plans, les délais effectivement observés comparés aux RTO visés, et les actions correctives nécessaires pour combler ces écarts. Ce retour d'expérience alimente directement le processus d'amélioration continue de la clause 10, développé au module suivant de ce parcours — un exercice qui ne débouche sur aucune action corrective documentée n'a, en pratique, qu'une valeur pédagogique limitée pour la maturité réelle du SMCA.

## Un programme pluriannuel plutôt qu'un exercice isolé

ISO 22301 exige un **programme** d'exercices, c'est-à-dire une planification pluriannuelle couvrant progressivement l'ensemble des plans de continuité critiques, plutôt qu'un unique exercice ponctuel réalisé une fois pour satisfaire une exigence d'audit puis jamais reconduit — une exigence de récurrence qui rappelle directement celle déjà développée pour le programme d'audit interne pluriannuel d'ISO 27001, ou pour le cycle annuel de conformité SOX, développés dans les parcours dédiés de cette plateforme. Un programme mature alterne généralement des exercices sur table fréquents (annuels, voire plus rapprochés pour les équipes de crise) avec des exercices grandeur nature plus rares mais plus révélateurs, réservés aux scénarios et activités jugés les plus critiques lors de la BIA.

## Ce que les exercices révèlent le plus fréquemment

L'expérience accumulée par la pratique de la continuité d'activité montre que les exercices révèlent le plus souvent des lacunes similaires d'une organisation à l'autre : des coordonnées de contact obsolètes dans les plans, une confusion sur les rôles précis en situation de crise malgré une documentation par ailleurs correcte, une sous-estimation systématique des délais réels de reprise par rapport aux RTO théoriquement visés, ou une dépendance non anticipée envers une ressource ou une personne clé absente le jour de l'exercice — des constats qui rappellent, par leur caractère récurrent d'une organisation à l'autre, ceux déjà signalés pour les pièges les plus fréquents de plusieurs référentiels étudiés dans cette plateforme.

## Un tableau de synthèse des types d'exercices

| Type d'exercice | Réalisme | Coût et fréquence typique |
|---|---|---|
| Exercice sur table | Discussion, sans mobilisation de ressources réelles | Faible coût, fréquence annuelle ou plus |
| Test technique isolé | Vérification d'un composant technique précis | Coût modéré, fréquence régulière |
| Exercice de simulation | Mobilisation de la cellule de crise en conditions proches du réel | Coût plus élevé, fréquence annuelle ou biennale |
| Exercice grandeur nature | Basculement effectif, interruption contrôlée de l'activité réelle | Coût élevé, fréquence rare, réservé aux activités les plus critiques |

## Le lien avec le module suivant

Les résultats de ce programme d'exercices constituent l'une des sources d'information les plus importantes pour l'évaluation des performances du SMCA — une évaluation structurée par les clauses 9 et 10 d'ISO 22301, développées au module suivant de ce parcours.
