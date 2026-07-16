# La fonction Identify : savoir ce qu'on protège

## Le principe : on ne protège pas ce qu'on n'a pas identifié

Identify a pour objectif de développer une compréhension de l'organisation nécessaire pour gérer les risques de cybersécurité pesant sur les systèmes, les personnes, les actifs, les données et les capacités. En CSF 2.0, cette fonction a été recentrée (une partie de son contenu historique — le contexte organisationnel et la stratégie de risque — ayant été déplacée vers Govern) autour de trois catégories.

## Les catégories d'Identify

### ID.AM — Gestion des actifs (Asset Management)

Les actifs (matériels, logiciels, systèmes, services, données, et le **personnel**) sont identifiés et gérés en cohérence avec leur importance relative pour les objectifs de l'organisation et sa stratégie de risque. Concrètement :

- Inventaire des équipements physiques et des systèmes logiciels — y compris le **shadow IT** (systèmes déployés sans validation formelle, angle mort classique).
- Cartographie des flux de données et de communication.
- Catalogue des services externes (fournisseurs cloud, SaaS tiers) dont dépend l'organisation.
- Classification des actifs selon leur criticité et leur sensibilité — un serveur de test et une base de données de production contenant des données de santé ne portent évidemment pas le même niveau de risque.

Un inventaire d'actifs incomplet ou obsolète est la cause racine la plus fréquente d'incidents graves : un système qu'on ne sait pas exister ne reçoit ni correctif, ni surveillance, ni contrôle d'accès à jour.

### ID.RA — Évaluation des risques (Risk Assessment)

Le risque de cybersécurité pesant sur l'organisation, ses actifs et ses individus est compris. Cette catégorie couvre :

- L'identification des vulnérabilités (internes et via une veille sur les menaces externes).
- L'évaluation de la probabilité et de l'impact des scénarios de menace.
- La prise en compte des renseignements sur les menaces (threat intelligence) pertinents pour le secteur d'activité.
- L'évaluation des risques liés aux fournisseurs et prestataires spécifiques (en complément de la stratégie C-SCRM définie au niveau Govern).

C'est directement l'application, au niveau de chaque actif ou système, de la méthodologie générale de gestion des risques (ISO 31000, EBIOS RM, NIST RMF) : cette sous-catégorie ne réinvente pas la méthode de cotation du risque, elle en exige simplement l'application systématique et documentée.

### ID.IM — Amélioration (Improvement) — nouvelle en 2.0

Les améliorations aux processus de gestion des risques de cybersécurité de l'organisation sont identifiées à partir de toutes les sources pertinentes : évaluations, tests, exercices, opérations courantes, et enseignements tirés des incidents passés. Cette catégorie formalise ce qui était auparavant implicite : identifier ne se limite pas à un inventaire statique, mais inclut un processus continu de remise en question et d'amélioration de la manière dont on identifie les risques eux-mêmes.

## Un exemple concret d'articulation ID.AM → ID.RA

Une organisation qui découvre, via ID.AM, qu'elle héberge une base de données clients dans un environnement cloud avec un accès mal documenté, va naturellement alimenter ID.RA : ce système devient un candidat prioritaire pour une évaluation de risque approfondie — probabilité d'un accès non autorisé, impact d'une fuite de données, contrôles existants (ou absents). Sans l'inventaire précis d'ID.AM, cette évaluation de risque n'aurait tout simplement pas de point de départ concret.

## Pourquoi Identify reste sous-estimé en pratique

Beaucoup d'organisations investissent prioritairement dans Protect et Detect (perçus comme plus "actifs" et plus visibles : pare-feux, outils de détection) tout en négligeant Identify, perçu à tort comme une simple tâche administrative de documentation. C'est une erreur de priorisation fréquente : un excellent contrôle d'accès (Protect) déployé sur un inventaire d'actifs incomplet laisse nécessairement des angles morts — les systèmes non inventoriés ne bénéficient tout simplement pas du contrôle, aussi bon soit-il par ailleurs.
