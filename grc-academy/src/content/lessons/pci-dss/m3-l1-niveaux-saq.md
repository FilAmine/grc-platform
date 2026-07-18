# Validation de conformité (1/2) : niveaux et questionnaires d'auto-évaluation

## Une gradation fixée par chaque marque de carte, pas par le PCI SSC lui-même

Un point souvent mal compris : ce n'est pas le PCI SSC qui fixe les niveaux de validation de conformité applicables à chaque entité, mais **chaque marque de carte séparément** (Visa, Mastercard, etc.), selon des critères globalement similaires mais pas strictement identiques d'une marque à l'autre. Cette leçon présente la structure générale, largement partagée entre les marques, sans prétendre à une exactitude universelle pour chaque marque prise individuellement.

## Les niveaux de validation pour les commerçants

Les commerçants sont généralement classés en quatre niveaux, fondés sur leur **volume annuel de transactions** :

- **Niveau 1** — plus de 6 millions de transactions par an (tous canaux confondus), ou tout commerçant ayant subi une compromission de données, ou désigné comme Niveau 1 par une marque de carte pour tout autre motif. Ce niveau exige un **Rapport de conformité (Report on Compliance — RoC)** annuel réalisé par un auditeur qualifié (QSA, développé dans la leçon suivante).
- **Niveau 2** — entre 1 et 6 millions de transactions par an. Ce niveau exige généralement un **questionnaire d'auto-évaluation (Self-Assessment Questionnaire — SAQ)** annuel, bien que certaines marques ou certains acquéreurs puissent exiger un RoC.
- **Niveau 3** — entre 20 000 et 1 million de transactions e-commerce par an. Un SAQ annuel est généralement requis.
- **Niveau 4** — moins de 20 000 transactions e-commerce, ou jusqu'à 1 million de transactions tous canaux confondus. Un SAQ est généralement requis, bien que les exigences précises varient selon l'acquéreur.

## Les niveaux de validation pour les prestataires de services

Les prestataires de services suivent une classification distincte, généralement à deux niveaux :

- **Niveau 1** — plus de 300 000 transactions par an. Un RoC annuel réalisé par un QSA est requis.
- **Niveau 2** — moins de 300 000 transactions par an. Un SAQ est en principe suffisant, bien qu'en pratique de nombreux acquéreurs et marques de cartes exigent malgré tout un RoC complet de la part des prestataires de services, quel que soit leur volume, compte tenu du risque agrégé qu'ils représentent pour l'ensemble de leurs clients — un principe de prudence qui rappelle, dans son esprit, la préoccupation de concentration de risque déjà développée pour les prestataires TIC critiques dans le parcours DORA de cette plateforme, bien que sans mécanisme de désignation formel comparable.

## Les principaux types de questionnaires d'auto-évaluation (SAQ)

Le SAQ applicable à un commerçant dépend directement de son architecture de traitement des paiements — pas seulement de son volume de transactions :

- **SAQ A** — commerçants n'acceptant que des paiements à distance (vente par correspondance/téléphone, ou e-commerce), entièrement externalisés vers un prestataire tiers validé PCI DSS, sans stockage, traitement ni transmission électronique de données de cartes sur les propres systèmes du commerçant. Le questionnaire le plus léger, réservé aux commerçants qui ont poussé la stratégie d'externalisation développée au module 2 à son maximum.
- **SAQ A-EP** — commerçants e-commerce partiellement externalisés, dont le site web ne reçoit pas directement les données de carte mais influence la sécurité de la transaction de paiement (par exemple, une redirection vers une page de paiement tierce contrôlée en partie par le code du commerçant).
- **SAQ B** — commerçants utilisant exclusivement des terminaux de paiement autonomes connectés par ligne téléphonique, sans stockage électronique de données de cartes.
- **SAQ B-IP** — commerçants utilisant des terminaux de paiement autonomes validés PTS (PIN Transaction Security) connectés par IP plutôt que par ligne téléphonique.
- **SAQ C** — commerçants disposant de systèmes de paiement connectés à internet, sans stockage électronique de données de cartes.
- **SAQ C-VT** — commerçants utilisant exclusivement un terminal de paiement virtuel basé sur navigateur web, sans stockage électronique de données de cartes.
- **SAQ P2PE** — commerçants utilisant une solution de chiffrement point à point validée (P2PE), qui protège les données de carte dès leur capture jusqu'à leur déchiffrement par le prestataire de solution P2PE.
- **SAQ D** — le questionnaire le plus complet, couvrant l'intégralité des douze exigences, applicable à tous les commerçants qui ne correspondent à aucun des scénarios simplifiés ci-dessus, et à **tous les prestataires de services** éligibles à l'auto-évaluation.

## Pourquoi le choix du bon SAQ est déterminant

Un commerçant qui utilise, à tort, un SAQ trop léger par rapport à son architecture réelle de traitement des paiements (par exemple, un SAQ A alors que son propre site web influence directement la sécurité de la transaction) produit une auto-évaluation invalide, susceptible d'être contestée en cas d'incident ultérieur ou de contrôle par l'acquéreur — un piège comparable, dans son principe, à une catégorisation de complaisance déjà signalée dans le parcours NIST RMF de cette plateforme, ou à un scoping ISO 27001 mal calibré. Déterminer précisément son architecture de traitement des paiements (module 2) est donc un préalable indispensable au choix du bon type de SAQ, avant même de commencer à répondre au questionnaire lui-même.
