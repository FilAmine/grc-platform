# La Security Rule (1/3) : les sauvegardes administratives et l'analyse de risque

## Un champ d'application limité aux seules ePHI

Contrairement à la Privacy Rule, qui couvre l'ensemble des informations de santé protégées quel que soit leur support, la **Security Rule** ne s'applique qu'aux informations de santé protégées sous forme **électronique (ePHI)**, déjà définies au module 0 de ce parcours. Elle structure ses exigences en trois catégories de sauvegardes (safeguards) : administratives (développées dans cette leçon), physiques et techniques (développées dans la leçon suivante).

## L'analyse de risque : l'exigence la plus fréquemment citée dans les sanctions de l'OCR

Avant de détailler l'ensemble des sauvegardes administratives, une exigence mérite d'être isolée tant elle domine, dans la pratique, les actions d'exécution de l'OCR développées au module 5 de ce parcours : la conduite d'une **évaluation précise et approfondie des risques et vulnérabilités potentiels** pesant sur la confidentialité, l'intégrité et la disponibilité des ePHI détenues par l'entité. Cette analyse de risque, exigée dès l'ouverture du processus de gestion de la sécurité, n'est pas une simple formalité ponctuelle — elle doit être **menée à l'échelle de l'ensemble de l'organisation** (enterprise-wide), couvrant tous les systèmes et emplacements où des ePHI sont créées, reçues, conservées ou transmises.

Dans la quasi-totalité des accords de résolution et sanctions financières prononcés par l'OCR (développés au module 5), le premier manquement cité est l'**absence ou l'insuffisance de cette analyse de risque** — un constat qui rappelle directement l'importance déjà accordée à l'analyse de risque initiale dans les parcours ISO 27001 (clause 6.1.2) et NIST RMF (l'étape Categorize) de cette plateforme : sans cette analyse fondatrice, l'ensemble des contrôles mis en œuvre par la suite reposent sur une base non démontrée et difficilement défendable devant un régulateur.

## Les autres sauvegardes administratives

### La responsabilité de sécurité désignée (Assigned Security Responsibility)

L'entité doit désigner un **responsable de la sécurité (Security Official)**, chargé du développement et de la mise en œuvre des politiques et procédures de sécurité requises — un rôle directement comparable au Délégué à la Protection des Données du RGPD ou au RSSI déjà développés dans les parcours précédents de cette plateforme, bien que HIPAA impose ce rôle sous un nom différent et avec un périmètre centré spécifiquement sur les ePHI plutôt que sur l'ensemble de la protection des données personnelles.

### La sécurité de la main-d'œuvre (Workforce Security)

Des politiques et procédures garantissant que l'ensemble du personnel dispose d'un accès approprié aux ePHI, et empêchant l'accès de ceux qui n'y sont pas autorisés — incluant des procédures d'autorisation et de supervision, des procédures de vérification préalable à l'embauche, et des procédures de suppression d'accès à la fin d'un contrat de travail.

### La gestion des accès à l'information (Information Access Management)

Des politiques et procédures pour autoriser l'accès aux ePHI en cohérence avec la Privacy Rule déjà développée au module 1 — l'application directe du principe de moindre privilège déjà développé dans le module Security by Design du premier parcours de cette plateforme.

### La sensibilisation et la formation à la sécurité (Security Awareness and Training)

Un programme de sensibilisation à la sécurité pour l'ensemble du personnel, incluant des rappels périodiques, une protection contre les logiciels malveillants, une surveillance des connexions, et des procédures de gestion des mots de passe.

### Les procédures d'incident de sécurité (Security Incident Procedures)

Des politiques et procédures pour identifier et répondre aux incidents de sécurité suspectés ou avérés, atténuer leurs effets néfastes connus, et documenter les incidents et leurs suites — un point directement rattaché à la règle de notification des violations développée au module 4 de ce parcours.

### Le plan de contingence (Contingency Plan)

Des politiques et procédures de réponse à un événement d'urgence (panne système, catastrophe naturelle) endommageant des systèmes contenant des ePHI, incluant un plan de sauvegarde des données, un plan de reprise après sinistre, et un plan d'exploitation en mode dégradé — un ensemble qui recoupe directement le contrôle 8.13 de l'Annexe A d'ISO 27001 et la famille CP de SP 800-53, tous deux développés dans les parcours précédents de cette plateforme.

### L'évaluation (Evaluation)

Une évaluation périodique, technique et non technique, du respect des exigences de la Security Rule, en réponse à des changements affectant la sécurité des ePHI.

## Le lien avec la leçon suivante

Ces sauvegardes administratives posent le cadre organisationnel et documentaire de la sécurité des ePHI — la leçon suivante développe les sauvegardes physiques et techniques, qui traduisent ce cadre en contrôles concrets sur les locaux, les équipements et les systèmes eux-mêmes.
