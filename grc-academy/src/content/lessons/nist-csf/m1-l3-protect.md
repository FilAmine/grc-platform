# La fonction Protect : les mesures de sauvegarde

## Une fonction restructurée et simplifiée en 2.0

Protect couvre la mise en œuvre de mesures de sauvegarde pour gérer les risques de cybersécurité de l'organisation. La version 2.0 a consolidé les six catégories historiques de la 1.1 en cinq catégories plus larges, en fusionnant notamment plusieurs catégories techniques dispersées (protection des données, maintenance, technologies de protection) sous des regroupements plus cohérents.

## Les catégories de Protect

### PR.AA — Gestion des identités, authentification et contrôle d'accès

Regroupe ce qui était auparavant séparé entre "Identity Management and Access Control" — l'accès physique et logique aux actifs est limité aux utilisateurs, services et matériels autorisés, et géré en cohérence avec le risque associé à un accès non autorisé :

- Gestion du cycle de vie des identités (création, modification, désactivation à la fin d'un contrat).
- Authentification, y compris l'authentification multifacteur pour les accès à privilège.
- Application du principe de moindre privilège dans l'attribution des permissions.
- Gestion des accès à distance et des accès des tiers.

### PR.AT — Sensibilisation et formation (Awareness and Training)

Le personnel de l'organisation reçoit une formation à la cybersécurité et est sensibilisé de manière à pouvoir exercer ses responsabilités en cohérence avec les politiques, procédures et accords en vigueur. Souvent sous-estimée face aux contrôles techniques, cette catégorie reste pertinente parce qu'une part significative des incidents commence par une erreur humaine (hameçonnage réussi, mauvaise configuration par méconnaissance).

### PR.DS — Sécurité des données (Data Security)

Les données sont gérées en cohérence avec la stratégie de risque de l'organisation pour protéger leur confidentialité, intégrité et disponibilité :

- Chiffrement des données au repos et en transit.
- Gestion du cycle de vie des données, y compris leur suppression sécurisée en fin de vie.
- Protection contre la fuite de données (data loss prevention).
- Intégrité des données vérifiée via des mécanismes appropriés (signatures, contrôles d'intégrité).

### PR.PS — Sécurité des plateformes (Platform Security) — consolidée en 2.0

Cette catégorie regroupe la sécurité du matériel, des logiciels (systèmes d'exploitation, applications, micrologiciels) et des services :

- Gestion des configurations et durcissement des systèmes (hardening) selon des bases de référence documentées.
- Gestion des correctifs (patch management) selon un calendrier proportionné à la criticité des vulnérabilités.
- Sécurité du cycle de développement logiciel — c'est ici que le CSF rejoint directement les pratiques Security by Design (secure SDLC, revue de code, gestion des dépendances).
- Sécurité de la configuration des environnements cloud et des conteneurs.

### PR.IR — Résilience de l'infrastructure technologique (Technology Infrastructure Resilience) — nouvelle en 2.0

Les architectures de sécurité sont gérées en cohérence avec la stratégie de risque pour protéger la confidentialité, l'intégrité et la disponibilité des actifs, et pour atteindre la résilience visée par l'organisation :

- Segmentation réseau, adaptée à la criticité des systèmes.
- Redondance des composants critiques.
- Capacité de l'infrastructure à supporter les pics de charge légitimes sans dégradation qui faciliterait une attaque par déni de service.

L'introduction de cette catégorie en 2.0 reconnaît explicitement que la résilience technique (pas seulement la prévention d'une compromission) fait partie intégrante d'une posture de protection — un écho direct au principe de défense en profondeur.

## Où se loge Security by Design dans Protect

PR.PS et PR.IR sont les deux catégories qui recoupent le plus directement les pratiques développées en profondeur ailleurs dans cette plateforme de formation (shift-left, secure SDLC, defense in depth, zero trust, sécurité cloud) : le CSF énonce l'exigence de résultat ("l'architecture est sécurisée et résiliente"), tandis que ces pratiques constituent le **comment** technique concret pour l'atteindre. C'est un exemple typique de la logique de mapping évoquée dans la leçon sur la philosophie du CSF : le cadre décrit le *quoi*, les référentiels et pratiques plus techniques (CIS Benchmarks, Well-Architected Frameworks, principes Security by Design) fournissent le *comment*.
