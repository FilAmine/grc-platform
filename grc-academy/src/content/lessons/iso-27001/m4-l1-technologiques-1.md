# Contrôles technologiques (1/2) : accès, cryptographie, terminaux et réseau

## Le thème technologique : 34 contrôles, préfixe 8.x

Ce thème regroupe les contrôles les plus proches du travail quotidien d'un ingénieur ou d'un architecte. Cette leçon couvre le contrôle d'accès technique, la cryptographie, la sécurité des terminaux et la sécurité réseau ; la leçon suivante couvre le développement sécurisé, la journalisation et la gestion des vulnérabilités.

## Terminaux utilisateurs et accès privilégié

- **8.1 — Terminaux finaux des utilisateurs** : l'information stockée sur, traitée par ou accessible via les terminaux des utilisateurs est protégée.
- **8.2 — Droits d'accès privilégiés** : l'attribution et l'utilisation des droits d'accès privilégiés sont restreintes et gérées — l'application technique directe du principe de moindre privilège aux comptes à haut risque (administrateurs systèmes, comptes root cloud).
- **8.3 — Restriction d'accès à l'information** : l'accès à l'information et aux autres actifs associés est restreint conformément à la politique de contrôle d'accès applicable.
- **8.4 — Accès au code source** : l'accès en lecture et en écriture au code source, aux outils de développement et aux bibliothèques logicielles est géré de manière appropriée.
- **8.5 — Authentification sécurisée** : des technologies et procédures d'authentification sécurisées sont mises en œuvre en fonction des restrictions d'accès à l'information et de la politique de contrôle d'accès — le contrôle qui couvre notamment l'authentification multifacteur pour les accès à privilège.

## Gestion des capacités et séparation des environnements

- **8.6 — Gestion de la capacité** : l'utilisation des ressources est surveillée et ajustée conformément aux besoins de capacité actuels et attendus — un contrôle qui recoupe la disponibilité (au sens de la triade CID) autant que la sécurité pure : un système à court de capacité devient vulnérable à un déni de service même sans intention malveillante.
- **8.7 — Protection contre les logiciels malveillants** : une protection contre les logiciels malveillants est mise en œuvre et complétée par une sensibilisation appropriée des utilisateurs.
- **8.8 — Gestion des vulnérabilités techniques** : l'information sur les vulnérabilités techniques des systèmes d'information utilisés est obtenue, l'exposition de l'organisme à ces vulnérabilités est évaluée, et des mesures appropriées sont prises.
- **8.9 — Gestion de la configuration** *(nouveau en 2022)* : les configurations, y compris les configurations de sécurité, du matériel, des logiciels, des services et des réseaux sont établies, documentées, mises en œuvre, surveillées et revues — le contrôle qui formalise la notion de configuration de référence durcie (hardening baseline), très proche dans l'esprit des CIS Benchmarks étudiés dans le premier parcours de cette plateforme.

## Cycle de vie et protection des données

- **8.10 — Suppression des informations** *(nouveau en 2022)* : l'information stockée dans les systèmes d'information, les appareils ou dans tout autre support de stockage est supprimée lorsqu'elle n'est plus nécessaire — l'application technique directe du principe de minimisation et de limitation de la conservation du RGPD, développés dans le premier parcours.
- **8.11 — Masquage des données** *(nouveau en 2022)* : le masquage des données est utilisé conformément à la politique de contrôle d'accès de l'organisme et aux autres exigences thématiques associées, en tenant compte de la législation applicable — recoupe directement la pseudonymisation détaillée dans le module Privacy by Design du premier parcours.
- **8.12 — Prévention de la fuite de données** *(nouveau en 2022)* : des mesures de prévention de la fuite de données sont appliquées aux systèmes, réseaux et tout autre appareil traitant, stockant ou transmettant des informations sensibles.
- **8.13 — Sauvegarde de l'information** : des copies de sauvegarde de l'information, des logiciels et des systèmes sont conservées et testées régulièrement conformément à une politique de sauvegarde convenue — un contrôle qui va au-delà de la simple existence d'une sauvegarde : le **test** régulier de restauration est explicitement exigé, sans quoi une sauvegarde jamais testée ne constitue qu'une garantie théorique.
- **8.14 — Redondance des moyens de traitement de l'information** : les moyens de traitement de l'information sont mis en œuvre avec une redondance suffisante pour répondre aux exigences de disponibilité.

## Cryptographie

- **8.24 — Utilisation de la cryptographie** : des règles d'utilisation efficace de la cryptographie, y compris la gestion des clés cryptographiques, sont définies et mises en œuvre. C'est le contrôle qui couvre le chiffrement au repos et en transit développé en détail dans le module Cloud Security by Design du premier parcours, ainsi que les questions de gestion des clés (rotation, révocation, séparation des rôles entre celui qui gère les clés et celui qui accède aux données chiffrées).

## Sécurité réseau

- **8.15 — Journalisation** : des journaux enregistrant les activités, exceptions, défaillances et autres événements pertinents sont produits, stockés, protégés et analysés — traité plus en détail dans la leçon suivante avec la surveillance.
- **8.20 — Sécurité des réseaux** : les réseaux et dispositifs réseau sont sécurisés, gérés et contrôlés pour protéger l'information dans les systèmes et applications.
- **8.21 — Sécurité des services réseau** : les mécanismes de sécurité, les niveaux de service et les exigences de service des services réseau sont identifiés, mis en œuvre et surveillés.
- **8.22 — Cloisonnement des réseaux** : des groupes de services d'information, d'utilisateurs et de systèmes d'information sont cloisonnés au sein des réseaux de l'organisme — l'application technique directe de la segmentation réseau et de la micro-segmentation Zero Trust développées dans le premier parcours de cette plateforme.
- **8.23 — Filtrage web** *(nouveau en 2022)* : l'accès aux sites web externes est géré pour réduire l'exposition à des contenus malveillants.

## Le fil conducteur de ce premier bloc

Ce premier bloc de contrôles technologiques suit approximativement le cycle de vie d'un système : qui peut y accéder (8.1 à 8.5), comment sa capacité et sa configuration sont maîtrisées (8.6 à 8.9), comment les données qu'il traite sont protégées tout au long de leur cycle de vie (8.10 à 8.14, 8.24), et comment le réseau qui le connecte au reste de l'organisme est sécurisé (8.15, 8.20 à 8.23). La leçon suivante complète ce panorama avec le développement logiciel et la surveillance active.
