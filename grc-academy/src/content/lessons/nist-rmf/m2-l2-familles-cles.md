# Le catalogue SP 800-53 (2/2) : zoom sur les familles les plus structurantes

## Access Control (AC) — la famille la plus volumineuse

La famille AC couvre l'ensemble du cycle de vie des comptes et des permissions : gestion des comptes (**AC-2**, avec des améliorations couvrant l'automatisation de la création/désactivation et la revue périodique), application du moindre privilège (**AC-6**), limitation des tentatives de connexion infructueuses (**AC-7**), contrôle d'accès à distance (**AC-17**), et restriction de l'utilisation des dispositifs mobiles (**AC-19**). Cette famille recoupe directement le contrôle d'accès déjà rencontré sous des formulations différentes dans les parcours ISO 27001 (contrôles 5.15 à 5.18), SOC 2 (Common Criterion CC6), et Security by Design (principe de moindre privilège) de cette plateforme — un nouvel exemple concret de la convergence des référentiels matures sur un socle de bonnes pratiques largement commun.

## Audit and Accountability (AU) — la journalisation au service de l'imputabilité

Au-delà de la simple production de journaux, cette famille insiste sur l'**imputabilité (accountability)** : le contrôle **AU-2** exige de déterminer précisément quels événements doivent être journalisés au regard des besoins d'investigation de l'organisation, **AU-3** exige que chaque enregistrement contienne un contenu suffisant (identité, horodatage, résultat de l'événement) pour permettre une reconstitution fiable des faits, et **AU-6** exige une revue et une analyse régulières des journaux — pas seulement leur collecte passive. C'est ce dernier point qui distingue une famille AU correctement implémentée d'une simple accumulation de journaux jamais exploités, un piège déjà signalé pour le contrôle 8.16 (activités de surveillance) d'ISO 27001 dans le parcours dédié de cette plateforme.

## Configuration Management (CM) — la maîtrise du changement

La famille CM couvre l'établissement de configurations de référence durcies (**CM-2**, un équivalent direct du contrôle 8.9 d'ISO 27001 déjà rencontré dans le parcours dédié), le contrôle des changements (**CM-3**), l'analyse d'impact de sécurité avant tout changement (**CM-4**), et la restriction des privilèges d'accès nécessaires pour effectuer un changement (**CM-5**). Cette famille recoupe directement la gestion des changements déjà développée comme Common Criterion CC8 dans le parcours SOC 2 de cette plateforme.

## Contingency Planning (CP) — au-delà de la simple sauvegarde

Cette famille dépasse largement la seule sauvegarde de données : elle couvre l'élaboration d'un plan de continuité (**CP-2**), la formation du personnel à ce plan (**CP-3**), le **test régulier du plan de continuité** (**CP-4** — un rappel direct de l'exigence de test de restauration déjà rencontrée pour le contrôle A1.3 de SOC 2 et le contrôle 8.13 d'ISO 27001 dans les parcours précédents), et la définition de sites de repli alternatifs pour le traitement (**CP-7**) et le stockage (**CP-6**) en cas d'indisponibilité du site principal.

## Identification and Authentication (IA) — au-delà du simple mot de passe

Cette famille couvre l'identification et l'authentification des utilisateurs organisationnels (**IA-2**, avec des améliorations imposant l'authentification multifacteur pour les accès à privilège ou les accès réseau), mais aussi, distinction souvent négligée, l'identification et l'authentification des **utilisateurs non organisationnels** (**IA-8** — partenaires, prestataires, citoyens accédant à un service public) et des **dispositifs** eux-mêmes (**IA-3** — authentification machine à machine), un périmètre plus large que le simple contrôle d'accès humain déjà couvert par la famille AC.

## System and Communications Protection (SC) — l'architecture technique de sécurité

Cette famille couvre la séparation des fonctions utilisateur et des fonctions de gestion du système (**SC-2**), le cloisonnement des applications (**SC-3**), la protection des limites du système et sa segmentation réseau (**SC-7** — un équivalent direct du contrôle 8.22 d'ISO 27001 déjà rencontré dans le parcours dédié), la protection de la confidentialité et de l'intégrité des transmissions (**SC-8**), et l'utilisation de mécanismes cryptographiques (**SC-13**). C'est la famille la plus directement alignée avec les principes de défense en profondeur et de segmentation réseau développés dans le module Security by Design du premier parcours de cette plateforme.

## System and Information Integrity (SI) — la vigilance opérationnelle continue

Cette famille couvre la correction des défauts logiciels et la gestion des correctifs (**SI-2**), la protection contre les logiciels malveillants (**SI-3**), la surveillance du système pour détecter des attaques et des indicateurs de compromission potentielle (**SI-4** — directement lié à la fonction Detect du NIST CSF 2.0 déjà étudiée dans le deuxième parcours de cette plateforme), et la validation des entrées pour prévenir les attaques par injection (**SI-10**).

## Risk Assessment (RA) — au-delà de l'évaluation ponctuelle

Cette famille inclut désormais, depuis la révision 5, un contrôle dédié au **scan de vulnérabilités** (**RA-5**) avec des exigences précises de fréquence et de remédiation, ainsi qu'un contrôle de **renseignement sur les menaces (threat intelligence, RA-10)** — un ajout de la révision 5 qui fait directement écho au contrôle 5.7 d'ISO 27001 (également nouveau en 2022) et à la catégorie ID.RA du NIST CSF, déjà rencontrés dans les parcours précédents de cette plateforme : plusieurs référentiels majeurs ont, indépendamment et presque simultanément, formalisé l'exigence de threat intelligence comme un contrôle à part entière plutôt qu'une pratique informelle laissée à l'initiative de chaque organisation.

## Ce que ce panorama révèle sur la maturité mutuelle des référentiels

Ce parcours à travers quelques familles clés de SP 800-53 confirme un constat déjà établi à plusieurs reprises dans cette plateforme : au niveau des pratiques techniques concrètes, les référentiels majeurs (ISO 27001, NIST CSF, SOC 2, RMF) convergent largement sur un socle commun de bonnes pratiques — ce qui distingue surtout le RMF, c'est le niveau de détail prescriptif de son catalogue et la rigueur du processus formel qui encadre sa sélection, son implémentation et son évaluation, plutôt qu'un contenu technique fondamentalement différent des autres référentiels étudiés.
