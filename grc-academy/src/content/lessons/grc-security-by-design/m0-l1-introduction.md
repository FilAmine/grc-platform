# Bienvenue : pourquoi former GRC et Security by Design ensemble ?

## Deux mondes qui ont trop longtemps vécu séparés

Dans beaucoup d'organisations, deux équipes se croisent sans vraiment se parler :

- **L'équipe GRC** (Gouvernance, Risques, Conformité) produit des politiques, tient des registres de risques, prépare des audits ISO 27001 ou SOC 2, et répond aux questionnaires clients.
- **L'équipe technique** (développeurs, architectes cloud, ingénieurs sécurité) conçoit des systèmes, choisit des architectures cloud, écrit du code.

Le résultat classique : la politique de sécurité dit une chose, le système en production en fait une autre. Le registre de risques liste une "faiblesse de contrôle d'accès" en langage abstrait, pendant que l'architecte cloud configure — ou oublie de configurer — l'IAM sans jamais avoir lu ce registre.

**Security by Design** est le pont entre les deux : c'est la discipline qui consiste à traduire les exigences de gouvernance, de gestion des risques et de conformité en décisions d'architecture concrètes, prises dès la conception plutôt qu'ajoutées après coup.

Cette formation part du principe que vous ne pouvez pas être bon dans l'un sans comprendre l'autre :

- Un responsable conformité qui ne comprend pas ce qu'est un rôle IAM ou le modèle de responsabilité partagée du cloud va écrire des politiques inapplicables ou invérifiables.
- Un ingénieur cloud qui ignore pourquoi ISO 27001 exige une "revue des droits d'accès périodique" va considérer ça comme une contrainte bureaucratique plutôt que comme un contrôle qui réduit un risque réel.

## Ce que vous allez apprendre

Le parcours est structuré en sept modules progressifs :

1. **Gouvernance, Risque, Conformité** — les fondamentaux : qui décide, comment on évalue un risque, ce que "être conforme" veut vraiment dire.
2. **Les normes et référentiels clés** — ISO/IEC 27001 & 27002, NIST CSF 2.0, SOC 2, RGPD : ce qu'ils exigent réellement, et comment ils se recoupent.
3. **Security by Design** — les principes fondateurs (shift-left, defense in depth, moindre privilège, zero trust, threat modeling).
4. **Privacy by Design** — les 7 principes de Cavoukian et leur traduction opérationnelle dans le RGPD (minimisation, PIA/DPIA, pseudonymisation).
5. **Security by Design dans le Cloud** — modèle de responsabilité partagée, IAM, chiffrement, segmentation réseau, référentiels cloud (CSA CCM, CIS Benchmarks).
6. **Synthèse** — comment boucler la boucle : de la politique de gouvernance jusqu'à la configuration technique, et retour.

## Comment lire cette formation

Chaque leçon peut se lire seule, mais l'ordre est pensé pour construire une compréhension cumulative : les modules 2 à 5 s'appuient tous sur le vocabulaire posé au module 1. Si vous êtes déjà familier des fondamentaux du risque, vous pouvez avancer plus vite sur le module 1 — mais ne le sautez pas complètement : la façon dont *cette* formation définit risque, contrôle et conformité conditionne la compréhension de tout le reste.

Prenez votre temps sur les modules 4 et 5 : c'est là que la formation répond directement à la question posée dans son titre — "Security by Design", appliqué concrètement à la vie privée et au cloud, les deux terrains où la théorie de la conformité rencontre le plus durement la réalité de l'implémentation technique.
