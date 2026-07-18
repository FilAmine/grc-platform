# Les douze exigences (3/3) : surveillance, tests et politique de sécurité

## Objectif 5 — Surveiller et tester régulièrement les réseaux

### Exigence 10 — Journaliser et surveiller tous les accès aux composants du système et aux données de titulaires de carte

Cette exigence impose une journalisation exhaustive de tous les accès aux composants du CDE, avec des enregistrements incluant l'identité de l'utilisateur, le type d'événement, l'horodatage, le succès ou l'échec, et l'origine de l'événement — recoupant directement la famille AU de SP 800-53 et le contrôle 8.15 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme. La v4.0 impose une exigence de **détection automatisée des défaillances des contrôles de sécurité critiques** (par exemple, un système anti-malware désactivé ou un pare-feu mal configuré), avec une alerte générée en temps quasi réel — une exigence plus prescriptive que la simple journalisation passive, dans l'esprit du contrôle 8.16 d'ISO 27001 (activités de surveillance) déjà développé dans le parcours dédié de cette plateforme.

### Exigence 11 — Tester régulièrement la sécurité des systèmes et des réseaux

Cette exigence structure un programme de tests à plusieurs niveaux :

- des **scans de vulnérabilités internes et externes**, trimestriels au minimum, les scans externes devant être réalisés par un **Approved Scanning Vendor (ASV)** — un prestataire spécifiquement accrédité par le PCI SSC (développé au module 3),
- des **tests d'intrusion internes et externes**, au moins annuels et après tout changement significatif de l'infrastructure ou des applications,
- des **tests de segmentation**, propres à PCI DSS et sans équivalent aussi formalisé dans les autres référentiels déjà étudiés dans cette plateforme : si l'entité s'appuie sur la segmentation réseau pour réduire le périmètre de son CDE (développée au module 2), elle doit tester régulièrement, par un tiers indépendant, que cette segmentation reste effective et n'a pas été compromise par un changement d'architecture non maîtrisé,
- une **détection des points d'accès sans fil non autorisés**, à un rythme trimestriel.

## Objectif 6 — Maintenir une politique de sécurité de l'information

### Exigence 12 — Soutenir la sécurité de l'information par des politiques et des programmes organisationnels

Cette dernière exigence regroupe les obligations de gouvernance du référentiel : une politique de sécurité de l'information formalisée et diffusée, une évaluation des risques annuelle documentée, un plan de réponse aux incidents testé régulièrement, un programme de sensibilisation à la sécurité pour le personnel, et une exigence spécifique aux prestataires de services développée plus loin dans cette leçon.

### L'obligation contractuelle envers les prestataires de services

L'exigence 12 impose qu'une entité conserve une liste documentée de tous ses prestataires de services ayant accès aux données de titulaires de carte, avec un **accord écrit** reconnaissant explicitement la responsabilité du prestataire pour la sécurité des données de titulaires de carte qu'il traite pour le compte de l'entité — une exigence directement comparable au contrat de sous-traitance de l'article 28 du RGPD et aux clauses contractuelles minimales de DORA, déjà développées dans les parcours dédiés de cette plateforme. PCI DSS impose en outre à l'entité de surveiller périodiquement le statut de conformité PCI DSS de chacun de ces prestataires — une vigilance qui recoupe directement le contrôle 5.22 de l'Annexe A d'ISO 27001 (surveillance des services fournisseurs), déjà développé dans le parcours dédié de cette plateforme.

## Comment ce dernier bloc referme la boucle du référentiel

Ces quatre dernières exigences (9 à 12) suivent, une fois de plus, la même logique de boucle de rétroaction déjà observée à travers de multiples référentiels de cette plateforme : la surveillance (exigence 10) et les tests réguliers (exigence 11) permettent de vérifier que les exigences précédentes (1 à 9) restent réellement effectives dans le temps, tandis que la gouvernance et la gestion documentée des risques (exigence 12) referment le cycle en s'assurant que les enseignements de cette surveillance alimentent une amélioration continue du dispositif — le même principe déjà rencontré sous la forme du cycle PDCA d'ISO 27001, de la fonction Monitor du NIST RMF, ou de la fonction "Apprendre et évoluer" du cadre de gestion des risques liés aux TIC de DORA, tous développés dans les parcours précédents de cette plateforme.
