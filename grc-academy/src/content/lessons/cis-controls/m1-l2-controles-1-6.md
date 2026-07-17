# Les 18 contrôles (1/3) : contrôles 1 à 6 — les fondations

## Pourquoi ces six contrôles ouvrent systématiquement le référentiel

Les six premiers contrôles couvrent les fondations sans lesquelles aucun autre contrôle du référentiel ne peut réellement porter ses fruits — un principe déjà rencontré dans le premier parcours de cette plateforme à propos de la fonction Identify du NIST CSF : on ne protège pas ce qu'on n'a pas inventorié. Ce n'est pas un hasard si la quasi-totalité des Safeguards de ces six contrôles relèvent du niveau de priorisation le plus basique, l'**Implementation Group 1**, développé en détail au module 2.

## Contrôle 1 — Inventaire et contrôle des actifs de l'entreprise

Établir et maintenir activement un inventaire précis de tous les actifs matériels de l'entreprise (postes de travail, serveurs, équipements mobiles, objets connectés), y compris ceux gérés par des tiers, connectés au réseau physiquement, virtuellement, à distance, ou hébergés dans des environnements cloud. Ce contrôle recoupe directement la catégorie ID.AM du NIST CSF et le contrôle 5.9 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme.

## Contrôle 2 — Inventaire et contrôle des actifs logiciels

Établir et maintenir activement un inventaire précis de l'ensemble des logiciels autorisés et installés, afin que seuls les logiciels autorisés puissent être installés et exécutés, et que les logiciels non autorisés soient détectés et supprimés. Un point de vigilance directement lié à la gestion des risques de la chaîne d'approvisionnement logicielle déjà développée dans les parcours NIST CSF et NIST RMF de cette plateforme : un inventaire logiciel précis est le préalable indispensable pour identifier rapidement l'exposition à une vulnérabilité découverte dans un composant tiers largement utilisé.

## Contrôle 3 — Protection des données

Développer des processus et des contrôles techniques pour identifier, classifier, gérer en sécurité, conserver et éliminer les données — un contrôle qui recoupe directement la classification de l'information (contrôle 5.12 d'ISO 27001) et la minimisation des données déjà développée dans le module Privacy by Design du premier parcours de cette plateforme, ainsi que les principes de limitation de la conservation du RGPD, développés dans le parcours dédié. Les Safeguards de ce contrôle couvrent notamment le chiffrement des données au repos et en transit, la classification selon la sensibilité, et l'élimination sécurisée des données obsolètes.

## Contrôle 4 — Configuration sécurisée des actifs de l'entreprise et des logiciels

Établir et maintenir la configuration sécurisée des actifs de l'entreprise (postes de travail, serveurs, équipements mobiles) et des logiciels (systèmes d'exploitation et applications) — c'est ici que les **CIS Benchmarks** (développés en détail au module 3) trouvent leur point d'ancrage naturel dans les CIS Controls : ce contrôle 4 exige des configurations durcies, tandis que les Benchmarks fournissent le détail technique précis, plateforme par plateforme, pour y parvenir. Ce contrôle recoupe directement le contrôle 8.9 (gestion de la configuration) de l'Annexe A d'ISO 27001, déjà développé dans le parcours dédié de cette plateforme.

## Contrôle 5 — Gestion des comptes

Utiliser des processus et des outils pour attribuer et gérer l'autorisation des identifiants pour les comptes utilisateurs, y compris les comptes d'administration ainsi que les comptes de service, sur les actifs et logiciels de l'entreprise. Les Safeguards couvrent notamment la tenue d'un inventaire des comptes, l'utilisation de mots de passe uniques, la désactivation des comptes dormants, et la restriction des privilèges des comptes d'administration à leur seul usage — l'application directe du principe de moindre privilège développé dans le module Security by Design du premier parcours de cette plateforme.

## Contrôle 6 — Gestion du contrôle d'accès

Utiliser des processus et des outils pour créer, attribuer, gérer et révoquer les identifiants et privilèges d'accès pour les comptes utilisateurs, administrateurs et services, pour les actifs et logiciels de l'entreprise. Un contrôle distinct mais complémentaire du contrôle 5 : là où le contrôle 5 porte sur le **cycle de vie du compte lui-même**, le contrôle 6 porte sur le **cycle de vie des droits d'accès** que ce compte détient — une distinction qui recoupe la différence, déjà rencontrée dans le parcours ISO 27001 de cette plateforme, entre le contrôle 5.16 (gestion des identités) et le contrôle 5.18 (droits d'accès) de l'Annexe A. Les Safeguards de ce contrôle incluent notamment l'authentification multifacteur, généralisée à l'ensemble des accès à privilège et aux applications exposées à l'extérieur du réseau de l'entreprise.

## Un socle qui recoupe très directement l'inventaire ID.AM et le contrôle d'accès PR.AA déjà étudiés

Ces six premiers contrôles ne sont pas propres au référentiel CIS — ils traduisent, avec un vocabulaire orienté action et un degré de granularité technique généralement plus fin, les mêmes fondations déjà rencontrées sous d'autres formulations dans le NIST CSF (Identify, Protect) et ISO 27001 (contrôles organisationnels et technologiques 5.9 à 5.18) dans les parcours précédents de cette plateforme. Ce qui distingue les CIS Controls à ce stade n'est pas le fond des exigences, mais leur formulation systématiquement orientée vers une action vérifiable et mesurable — une caractéristique qui se confirme et s'accentue dans les contrôles suivants, développés dans la leçon suivante.
