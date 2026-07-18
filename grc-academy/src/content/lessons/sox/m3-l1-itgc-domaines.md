# Les contrôles généraux informatiques (1/2) : les quatre domaines

## Pourquoi la fiabilité du reporting financier dépend des systèmes d'information

Dans toute organisation moderne, une part croissante des contrôles de reporting financier repose sur des systèmes automatisés — un progiciel de gestion intégré (ERP) qui calcule automatiquement des provisions, un système de facturation qui applique automatiquement des règles de reconnaissance du chiffre d'affaires, une interface qui transfère automatiquement des écritures comptables entre systèmes. Ce constat, déjà amorcé au module 0 de ce parcours, fonde le concept central des **contrôles généraux informatiques (IT General Controls — ITGC)** : un contrôle automatisé de reporting financier ne peut être considéré comme fiable que si l'environnement informatique qui le supporte est lui-même correctement maîtrisé — un principe que les praticiens SOX résument par l'expression de **"dépendance IT" (IT dependency)** des contrôles métier.

Concrètement, si un contrôle métier de reconnaissance du chiffre d'affaires repose sur une règle automatisée dans l'ERP, mais que n'importe quel développeur peut modifier cette règle sans processus de validation (une déficience du domaine "modifications de programmes", développé plus loin dans cette leçon), la fiabilité de ce contrôle automatisé devient impossible à garantir dans la durée — quelle que soit la qualité apparente du contrôle métier lui-même au moment où il a été testé.

## Les quatre domaines classiques des ITGC

### L'accès aux programmes et aux données

Ce domaine couvre le contrôle des accès logiques aux applications et aux données financières — qui peut consulter, modifier ou supprimer une donnée comptable, selon quel processus d'attribution et de révocation des droits. Ce domaine recoupe très directement le contrôle d'accès déjà développé à travers de nombreux référentiels de cette plateforme (les contrôles 5.15-5.18 de l'Annexe A d'ISO 27001, la famille AC de SP 800-53, le contrôle 6 des CIS Controls, le contrôle 7-8 de la Security Rule de HIPAA), avec une spécificité propre au contexte SOX développée dans la leçon suivante : la **séparation des tâches (segregation of duties)** au sein des systèmes financiers.

### Les modifications de programmes (Program Changes)

Ce domaine couvre la gestion des modifications apportées aux applications et aux configurations qui soutiennent le reporting financier — un processus de gestion des changements qui garantit qu'aucune modification n'est déployée en production sans évaluation préalable, tests et autorisation appropriés. Ce domaine recoupe directement le Common Criterion CC8 de SOC 2, le contrôle 8.32 de l'Annexe A d'ISO 27001, l'objectif BAI06 de COBIT, et la pratique Change Enablement d'ITIL 4, tous développés dans les parcours précédents de cette plateforme — le même piège déjà signalé à travers ces référentiels (des changements urgents contournant le processus formel sans documentation rétroactive) constitue, dans le contexte SOX, une des causes les plus fréquentes de déficiences de contrôle constatées lors des audits.

### Le développement de programmes (Program Development)

Ce domaine couvre les contrôles applicables au développement ou à l'acquisition de nouveaux systèmes ou de mises à niveau majeures ayant un impact sur le reporting financier — s'assurer que les exigences fonctionnelles et de contrôle sont correctement définies dès la conception, que des tests appropriés sont réalisés avant la mise en production, et que la migration des données historiques vers un nouveau système préserve leur intégrité. Ce domaine recoupe directement le cycle de développement sécurisé déjà développé dans le module Security by Design du premier parcours de cette plateforme, et l'objectif BAI03 de COBIT (gérer l'identification et la construction de solutions), développé dans le parcours dédié.

### Les opérations informatiques (Computer Operations)

Ce domaine couvre le bon déroulement des traitements informatiques courants qui soutiennent le reporting financier — l'exécution correcte et dans les délais des traitements par lots (batch processing) qui alimentent les états financiers, la gestion des sauvegardes et de la continuité, la supervision et la résolution des incidents affectant les systèmes financiers. Ce domaine recoupe directement le contrôle 8.13 de l'Annexe A d'ISO 27001 et la famille CP de SP 800-53, développées dans les parcours précédents de cette plateforme, ainsi que la pratique de gestion des opérations d'ITIL 4 (DSS01), également développée dans le parcours dédié.

## Pourquoi ces quatre domaines forment un tout indissociable

Un dispositif ITGC n'est jamais évalué domaine par domaine de façon cloisonnée — une faiblesse dans un seul de ces quatre domaines peut compromettre la fiabilité de l'ensemble des contrôles automatisés qui en dépendent, quelle que soit la robustesse apparente des trois autres domaines. Un accès aux données correctement restreint (premier domaine) ne protège en rien contre une modification de programme non maîtrisée qui altérerait la logique de calcul elle-même (deuxième domaine) — les deux domaines traitent des risques complémentaires, pas substituables l'un à l'autre, un principe de défense en profondeur déjà développé dans le module Security by Design du premier parcours de cette plateforme.

## Le lien avec la leçon suivante

Parmi ces quatre domaines, le contrôle d'accès occupe une place particulièrement centrale dans le contexte spécifique du reporting financier, en raison d'un enjeu propre développé dans la leçon suivante : la séparation des tâches au sein des systèmes financiers, un sujet qui structure une part importante de l'effort de conformité ITGC dans la pratique.
