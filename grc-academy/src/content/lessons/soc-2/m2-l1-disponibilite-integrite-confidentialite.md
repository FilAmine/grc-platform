# Les critères additionnels : Disponibilité, Intégrité de traitement, Confidentialité

## Le principe des critères additionnels

Chacune des quatre catégories optionnelles ajoute un jeu de **critères additionnels**, numérotés indépendamment des Common Criteria (préfixe distinct par catégorie). Une mission SOC 2 qui retient, par exemple, Sécurité + Disponibilité doit satisfaire l'intégralité des Common Criteria (CC1 à CC9) **et** les critères additionnels de la catégorie Disponibilité — les deux jeux de critères s'additionnent, ils ne se substituent jamais l'un à l'autre.

## Disponibilité (Availability) — trois critères (A1.1 à A1.3)

### A1.1 — Capacité

L'entité maintient, surveille et évalue la capacité actuelle de traitement et l'utilisation des ressources de l'infrastructure, des données et des logiciels, pour gérer la capacité future et aider à atteindre ses objectifs de disponibilité — recoupe directement la gestion de la capacité (CC6 déjà couverte, mais spécifiquement approfondie ici sous l'angle de la disponibilité future, pas seulement de la sécurité présente).

### A1.2 — Protections environnementales, sauvegarde et récupération

L'entité met en œuvre des protections environnementales, des procédures de sauvegarde des données et de récupération de l'infrastructure conçues pour répondre à ses objectifs de disponibilité.

### A1.3 — Test de récupération

L'entité teste les procédures de récupération soutenant la reprise du système pour répondre à ses objectifs de disponibilité — un critère qui rejoint directement l'exigence de test régulier des sauvegardes déjà rencontrée dans le contrôle 8.13 de l'Annexe A d'ISO 27001 : une sauvegarde jamais testée en restauration réelle ne constitue qu'une garantie théorique, un point que les auditeurs SOC 2 vérifient systématiquement via des preuves de tests de restauration effectivement réalisés pendant la période d'audit.

## Intégrité de traitement (Processing Integrity) — cinq critères (PI1.1 à PI1.5)

Cette catégorie est pertinente lorsque l'exactitude, l'exhaustivité, la validité et l'autorisation du traitement des données constituent un engagement explicite envers les clients — typiquement pour des systèmes de traitement de transactions financières, de facturation, ou tout système où une erreur de traitement (pas seulement une atteinte à la confidentialité) aurait un impact direct pour le client.

- **PI1.1** — l'entité obtient ou génère, utilise et communique des spécifications pertinentes, exactes et complètes concernant les objectifs de qualité de traitement des produits ou services, pour soutenir l'utilisation des produits ou services.
- **PI1.2** — l'entité conçoit et implémente des contrôles sur les entrées (inputs) pour répondre à ses objectifs de qualité de traitement.
- **PI1.3** — l'entité conçoit et implémente des contrôles sur le traitement du système pour répondre à ses objectifs de qualité de traitement.
- **PI1.4** — l'entité conçoit et implémente des contrôles sur les sorties (outputs) pour répondre uniquement à ses objectifs de qualité de traitement.
- **PI1.5** — l'entité conçoit et implémente des contrôles sur le stockage des entrées, éléments de traitement et sorties pour répondre à ses objectifs de qualité de traitement.

C'est la catégorie la moins fréquemment retenue en pratique (comparée à Sécurité, Disponibilité ou Confidentialité) — beaucoup d'éditeurs SaaS B2B n'en ont pas un besoin contractuel explicite, sauf lorsque leur produit traite directement des transactions financières ou des calculs dont l'exactitude est elle-même l'objet du service vendu (un logiciel de paie, un outil de réconciliation comptable).

## Confidentialité (Confidentiality) — deux critères (C1.1 à C1.2)

### C1.1 — Identification et maintien des informations confidentielles

L'entité identifie et maintient les informations confidentielles pour répondre aux objectifs de l'entité liés à la confidentialité.

### C1.2 — Élimination des informations confidentielles

L'entité élimine les informations confidentielles pour répondre aux objectifs de l'entité liés à la confidentialité.

Bien que ne comptant que deux critères (la plus courte des catégories additionnelles), Confidentialité recoupe directement la classification de l'information (contrôle 5.12 de l'Annexe A d'ISO 27001) et la protection des enregistrements — la brièveté du jeu de critères ne signifie pas une faible exigence de preuve : un auditeur vérifiera concrètement comment l'information désignée comme confidentielle par contrat (souvent définie dans l'accord de confidentialité signé avec chaque client) est identifiée, marquée, et effectivement protégée tout au long de son cycle de vie, y compris à sa suppression.

## Comment choisir les catégories additionnelles pertinentes

Le choix des catégories additionnelles à retenir dans le périmètre d'un audit SOC 2 dépend directement des engagements contractuels pris auprès des clients, pas d'une ambition générale de "faire le plus complet possible" :

- un éditeur SaaS B2B classique retient typiquement **Sécurité + Disponibilité + Confidentialité**,
- un prestataire dont le produit implique un calcul ou un traitement financier critique ajoutera **Intégrité de traitement**,
- un prestataire traitant des données personnelles à grande échelle, en particulier pour des clients américains soumis à des obligations spécifiques, pourra ajouter **Vie privée** — la catégorie la plus substantielle des quatre, développée en détail dans la leçon suivante.

Ajouter une catégorie non pertinente pour l'activité réelle de l'organisation alourdit inutilement l'audit (preuves supplémentaires à collecter, tests supplémentaires à documenter) sans bénéfice commercial correspondant — un des premiers arbitrages de la phase de cadrage d'un programme SOC 2, développée au module 5.
