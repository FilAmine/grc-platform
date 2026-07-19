# La conception, la construction et la transition des services (1/2) : la gestion des changements

## Un processus central, déjà esquissé dans le parcours ITIL

ISO/IEC 20000 impose un **processus de gestion des changements** structuré, qui contrôle l'ensemble des modifications apportées aux services et à l'infrastructure qui les sous-tend — un processus qui reprend directement, sous une forme désormais certifiable, la pratique de facilitation des changements (Change Enablement) déjà développée en détail dans le parcours ITIL de cette plateforme, avec ses trois catégories de changements (standard, normal, urgence) et le rôle du Change Advisory Board dans l'évaluation des changements les plus significatifs.

## Pourquoi ce processus s'appuie directement sur la gestion de la configuration développée au module 1

La gestion des changements ne peut jamais fonctionner efficacement sans s'appuyer sur la gestion des actifs et de la configuration déjà développée au module 1 de ce parcours — évaluer correctement l'impact potentiel d'un changement envisagé exige de connaître précisément les dépendances entre les composants d'infrastructure concernés et l'ensemble des services qui en découlent. Un changement mis en œuvre sans cette connaissance précise des dépendances s'expose à des interruptions de service en cascade, touchant des services que personne n'avait anticipé comme potentiellement affectés par la modification envisagée.

## L'évaluation préalable et l'autorisation des changements

ISO/IEC 20000 impose que tout changement fasse l'objet d'une évaluation préalable de son risque et de son impact potentiel, avant d'être autorisé par une autorité appropriée à son niveau de criticité — un changement mineur pouvant être autorisé par un responsable opérationnel, tandis qu'un changement majeur affectant des services critiques exige l'implication d'un organe de gouvernance plus large, à l'image du Change Advisory Board déjà développé dans le parcours ITIL de cette plateforme. Cette gradation de l'autorité d'approbation en fonction de la criticité rejoint directement celle déjà développée pour les seuils de délégation d'ISO 31000 et de COSO ERM, tous deux développés dans les parcours dédiés de cette plateforme.

## La planification du retour arrière (rollback)

ISO/IEC 20000 impose que tout changement significatif soit accompagné d'un **plan de retour arrière** documenté, permettant de restaurer rapidement l'état antérieur du service en cas de défaillance imprévue lors de sa mise en œuvre — une exigence de prudence qui rappelle directement celle déjà développée pour le dispositif d'arrêt exigé par l'article 14 de l'AI Act (le contrôle humain effectif permettant d'interrompre le fonctionnement d'un système d'IA), développé dans le parcours dédié de cette plateforme, bien qu'appliquée ici à un changement de service plutôt qu'à un système de décision automatisée.

## La revue post-implémentation

ISO/IEC 20000 impose une revue post-implémentation pour les changements les plus significatifs, vérifiant que le changement a effectivement atteint ses objectifs sans engendrer de conséquences imprévues sur d'autres services — une exigence de vérification a posteriori qui rejoint directement le principe d'amélioration continue déjà rencontré à de multiples reprises dans cette plateforme, notamment pour les clauses 9 et 10 d'ISO 27001, d'ISO 22301 et d'ISO/IEC 42001.

## Un exemple concret illustrant l'ensemble de ce processus

Une mise à jour majeure d'un système de messagerie électronique interne, susceptible d'affecter plusieurs autres services dépendants (annuaire d'entreprise, systèmes d'authentification unique), serait ainsi évaluée par le Change Advisory Board au regard de son impact potentiel identifié grâce à la base de données de configuration, planifiée avec un plan de retour arrière précis en cas de défaillance, mise en œuvre pendant une fenêtre de changement appropriée, puis revue après implémentation pour vérifier que l'ensemble des objectifs visés (amélioration de la sécurité, ajout de fonctionnalités) ont été atteints sans dégradation constatée des services dépendants.

## Un tableau de synthèse du processus de gestion des changements

| Étape | Ce qu'elle vérifie |
|---|---|
| Évaluation préalable | Le risque et l'impact potentiel du changement, en s'appuyant sur la CMDB |
| Autorisation | Approbation par une autorité proportionnée à la criticité du changement |
| Plan de retour arrière | La capacité à restaurer rapidement l'état antérieur en cas d'échec |
| Revue post-implémentation | La vérification que les objectifs ont été atteints sans conséquence imprévue |

## Le lien avec la leçon suivante

Cette gestion des changements s'inscrit dans un processus plus large de conception, de construction et de transition de nouveaux services ou de modifications substantielles de services existants — développé à la leçon suivante de ce parcours.
