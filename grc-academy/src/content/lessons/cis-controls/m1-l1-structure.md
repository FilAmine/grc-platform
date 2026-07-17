# La structure des CIS Controls v8 : contrôles, Safeguards et attributs

## Deux niveaux, comme dans les autres catalogues déjà étudiés

À l'image de SP 800-53 (contrôles et améliorations, parcours NIST RMF de cette plateforme) ou de l'Annexe A d'ISO 27001 (thèmes et contrôles, parcours dédié), les CIS Controls s'organisent en deux niveaux :

- **18 Contrôles (Controls)** — des domaines d'action de haut niveau (par exemple, "Gestion des comptes"), qui ne sont jamais directement "implémentés" tels quels.
- **153 Safeguards** — les actions concrètes et mesurables qui composent chaque contrôle (par exemple, "utiliser des mots de passe uniques" au sein du contrôle Gestion des comptes) — l'équivalent fonctionnel des sous-catégories du NIST CSF ou des contrôles individuels de l'Annexe A d'ISO 27001, déjà rencontrés dans les parcours précédents de cette plateforme.

## Les attributs qui accompagnent chaque Safeguard

Ce qui distingue la version 8 des versions antérieures, c'est l'enrichissement de chaque Safeguard par un ensemble d'**attributs** structurés, qui permettent de filtrer et de recomposer le référentiel selon différents angles d'analyse :

### Le type d'actif (Asset Type)

Chaque Safeguard est rattaché à un type d'actif concerné : **Devices** (équipements), **Applications**, **Network** (réseau), **Data** (données), ou **Users** (utilisateurs) — une classification qui permet, par exemple, à une équipe responsable spécifiquement de la sécurité réseau d'extraire rapidement l'ensemble des Safeguards qui la concernent, sans devoir parcourir l'intégralité du référentiel.

### La fonction de sécurité (Security Function)

Chaque Safeguard est également rattaché à l'une des cinq fonctions historiques du NIST CSF (Identify, Protect, Detect, Respond, Recover, déjà développées en détail dans le deuxième parcours de cette plateforme) — un choix de conception qui n'est pas anodin : il permet une correspondance directe et systématique entre les CIS Controls et le NIST CSF, facilitant grandement le mapping entre les deux référentiels (développé au module 4).

### Le groupe de mise en œuvre (Implementation Group)

Chaque Safeguard est enfin associé à un ou plusieurs des trois **Implementation Groups (IG1, IG2, IG3)** — le système de priorisation le plus distinctif du référentiel, développé en détail au module 2.

## L'organisation par activité plutôt que par acteur

La révision v8 a introduit un changement de principe important par rapport aux versions antérieures : les contrôles ne sont plus organisés selon **qui** gère l'actif concerné (une distinction héritée d'une époque où les équipements étaient majoritairement gérés directement par l'organisation elle-même), mais selon le **type d'activité de sécurité** en jeu — gestion d'inventaire, gestion des comptes, gestion des vulnérabilités, etc. Ce choix reconnaît explicitement la généralisation du cloud, des équipements personnels utilisés à des fins professionnelles (BYOD), et du travail à distance, qui rendent de plus en plus artificielle une distinction fondée sur la propriété ou la gestion directe de l'équipement — un constat similaire à celui qui a motivé, dans ISO 27001:2022, l'ajout du contrôle 5.23 sur les services cloud déjà développé dans le parcours dédié de cette plateforme.

## La liste des 18 contrôles

1. Inventaire et contrôle des actifs de l'entreprise (Enterprise Assets)
2. Inventaire et contrôle des actifs logiciels (Software Assets)
3. Protection des données (Data Protection)
4. Configuration sécurisée des actifs de l'entreprise et des logiciels
5. Gestion des comptes (Account Management)
6. Gestion du contrôle d'accès (Access Control Management)
7. Gestion continue des vulnérabilités (Continuous Vulnerability Management)
8. Gestion des journaux d'audit (Audit Log Management)
9. Protections de la messagerie et du navigateur web
10. Défenses contre les logiciels malveillants (Malware Defenses)
11. Récupération des données (Data Recovery)
12. Gestion de l'infrastructure réseau
13. Surveillance et défense du réseau
14. Sensibilisation à la sécurité et formation des compétences
15. Gestion des prestataires de services (Service Provider Management)
16. Sécurité des logiciels applicatifs (Application Software Security)
17. Gestion de la réponse aux incidents
18. Tests d'intrusion (Penetration Testing)

Les trois leçons suivantes détaillent ces 18 contrôles par groupes de six, en soulignant à chaque fois les recoupements les plus directs avec les référentiels déjà étudiés dans cette plateforme.

## Pourquoi ce niveau de granularité en deux temps facilite l'appropriation

Cette architecture à deux niveaux — 18 domaines faciles à mémoriser et à présenter à une direction, 153 Safeguards concrets pour l'implémentation technique — répond à un besoin de communication similaire à celui des six fonctions du NIST CSF (faciles à retenir) complétées par leurs catégories et sous-catégories plus détaillées, déjà observé dans le deuxième parcours de cette plateforme. C'est un choix de conception récurrent chez les référentiels matures : offrir un niveau de lecture stratégique compact, tout en conservant, en dessous, la précision opérationnelle nécessaire à une mise en œuvre réelle et vérifiable.
