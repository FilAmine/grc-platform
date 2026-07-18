# Les tests de résilience opérationnelle numérique : le programme de base

## Un régime de tests gradué, à l'image des Implementation Groups des CIS Controls

Le chapitre IV de DORA organise un régime de tests de résilience opérationnelle numérique à deux niveaux : un **programme de tests de base**, proportionné et applicable à toute entité financière, développé dans cette leçon, et un régime de **tests de pénétration fondés sur la menace (TLPT)**, réservé aux entités les plus systémiques, développé dans la leçon suivante — une gradation qui rappelle, dans son principe, la logique des Implementation Groups des CIS Controls déjà développée dans le parcours dédié de cette plateforme : tout le monde applique un socle, seule une partie applique le niveau le plus avancé.

## Le programme de tests de base

Toute entité financière doit établir, maintenir et réviser un **programme de tests de résilience opérationnelle numérique**, dans le cadre du cadre de gestion des risques liés aux TIC déjà développé au module 1. Ce programme doit inclure un éventail de tests, notamment :

- des **évaluations et analyses de vulnérabilités**,
- des **analyses de sécurité des réseaux ouverts**,
- des **analyses des écarts** par rapport aux normes de sécurité de référence,
- des **revues de sécurité physique**,
- des **questionnaires et solutions d'analyse de la sécurité des logiciels**, y compris, le cas échéant, des **revues du code source**,
- des **tests fondés sur des scénarios**, simulant des situations de crise réalistes,
- des **tests de compatibilité**,
- des **tests de performance**,
- des **tests de bout en bout**,
- des **tests de pénétration**, y compris, lorsque cela est justifié, des tests fondés sur la menace pour les entités identifiées comme telles.

Cette liste recoupe très largement les pratiques déjà développées dans les référentiels techniques étudiés dans cette plateforme — les scans de vulnérabilités du contrôle 7 des CIS Controls, les tests d'intrusion du contrôle 18 des CIS Controls et du contrôle 8.34 de l'Annexe A d'ISO 27001, les tests de sécurité applicative du contrôle 8.29 d'ISO 27001 — appliqués ici sous une obligation réglementaire directe pour le secteur financier.

## La fréquence et la proportionnalité des tests

Toutes les mesures de sécurité TIC critiques doivent être testées **au moins une fois par an**, selon un principe de proportionnalité qui tient compte de la taille, du profil d'activité et du profil de risque global de l'entité financière — un principe similaire, dans son esprit, à celui déjà rencontré pour l'article 21 de NIS2 dans le parcours dédié de cette plateforme.

## Qui réalise ces tests

Contrairement au régime de TLPT développé dans la leçon suivante (qui impose des testeurs externes indépendants sous conditions strictes), les tests du programme de base peuvent être réalisés par des **testeurs internes** de l'entité financière, à condition qu'aucun conflit d'intérêts ne compromette l'indépendance et l'objectivité du test — un principe de séparation des tâches directement comparable à celui déjà rencontré pour l'audit interne d'ISO 27001 (clause 9.2) et l'évaluation indépendante du NIST RMF, développés dans les parcours précédents de cette plateforme.

## Le lien avec le cadre de gestion des risques liés aux TIC

Ce programme de tests ne fonctionne jamais isolément — il constitue la fonction "Apprendre et évoluer" du cadre de gestion des risques liés aux TIC déjà développée au module 1 : les résultats des tests doivent alimenter une amélioration continue documentée du dispositif de sécurité, pas seulement produire un rapport archivé sans suite. Cette boucle de rétroaction entre test et amélioration rejoint directement le cycle PDCA d'ISO 27001 et la boucle de surveillance continue du NIST RMF, déjà développés dans les parcours précédents de cette plateforme — une nouvelle confirmation que, malgré des vocabulaires distincts, les référentiels matures convergent systématiquement vers le même principe de vérification et d'amélioration continues.

## Pourquoi ce socle de tests ne suffit pas pour les entités les plus systémiques

Ce programme de base, bien que substantiel, reste dimensionné pour couvrir les risques les plus courants et les vulnérabilités les plus fréquemment exploitées — il ne simule pas nécessairement un adversaire sophistiqué et déterminé, capable de mener une attaque ciblée et multi-vecteurs contre une institution financière systémique. C'est précisément la lacune que le régime de tests de pénétration fondés sur la menace, développé dans la leçon suivante, vient combler pour les entités dont la défaillance présenterait un risque disproportionné pour la stabilité du système financier.
