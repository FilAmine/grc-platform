# Le catalogue SP 800-53 (1/2) : structure et familles de contrôles

## Le catalogue de contrôles le plus détaillé parmi les référentiels étudiés dans cette plateforme

**SP 800-53 Rev. 5** (publiée en 2020, avec des mises à jour ultérieures) organise plus d'un millier de contrôles et d'améliorations de contrôles (control enhancements) en **20 familles**, identifiées par un préfixe à deux lettres. C'est, de très loin, le catalogue le plus volumineux et le plus prescriptif rencontré dans cette plateforme — nettement plus détaillé que les 93 contrôles de l'Annexe A d'ISO 27001 ou les neuf Common Criteria de SOC 2, déjà étudiés dans les parcours dédiés.

## Les 20 familles de contrôles

| Préfixe | Famille |
|---|---|
| AC | Access Control (Contrôle d'accès) |
| AT | Awareness and Training (Sensibilisation et formation) |
| AU | Audit and Accountability (Audit et imputabilité) |
| CA | Assessment, Authorization, and Monitoring (Évaluation, autorisation et surveillance) |
| CM | Configuration Management (Gestion de la configuration) |
| CP | Contingency Planning (Planification de la continuité) |
| IA | Identification and Authentication (Identification et authentification) |
| IR | Incident Response (Réponse aux incidents) |
| MA | Maintenance (Maintenance) |
| MP | Media Protection (Protection des supports) |
| PE | Physical and Environmental Protection (Protection physique et environnementale) |
| PL | Planning (Planification) |
| PM | Program Management (Gestion du programme) |
| PS | Personnel Security (Sécurité du personnel) |
| PT | PII Processing and Transparency (Traitement des données personnelles et transparence) |
| RA | Risk Assessment (Appréciation des risques) |
| SA | System and Services Acquisition (Acquisition de systèmes et de services) |
| SC | System and Communications Protection (Protection des systèmes et des communications) |
| SI | System and Information Integrity (Intégrité des systèmes et de l'information) |
| SR | Supply Chain Risk Management (Gestion des risques de la chaîne d'approvisionnement) |

Deux familles ont été ajoutées lors de la révision majeure de 2020 (Rev. 5) : **PT** (traitement des données personnelles et transparence, développée au module 5) et **SR** (gestion des risques de la chaîne d'approvisionnement, également développée au module 5) — une évolution qui reflète, avec quelques années d'écart, les mêmes priorités montantes déjà observées pour l'ajout du contrôle 5.23 (services cloud) et du bloc fournisseurs de l'Annexe A d'ISO 27001, ou de la catégorie GV.SC du NIST CSF 2.0, étudiés dans les parcours précédents de cette plateforme.

## La structure d'un contrôle

Chaque contrôle de SP 800-53 suit une structure normalisée :

- un **identifiant** (par exemple, **AC-2**),
- un **énoncé du contrôle**, décrivant l'exigence de sécurité ou de vie privée à satisfaire,
- des **discussions complémentaires**, qui précisent l'intention et le contexte du contrôle,
- des **références informatives** vers d'autres publications ou normes pertinentes,
- des **améliorations de contrôle (control enhancements)**, numérotées entre parenthèses — par exemple, **AC-2(1)** (gestion automatisée des comptes), **AC-2(3)** (désactivation automatique des comptes inactifs) — qui renforcent ou étendent le contrôle de base, et ne sont mobilisées que si la base de référence retenue (module 1) les exige.

Cette architecture à deux niveaux (contrôle de base, puis améliorations optionnelles) permet à SP 800-53 de couvrir un spectre de rigueur très large avec un même catalogue : un système à catégorisation Faible n'implémente que le contrôle de base d'AC-2, tandis qu'un système à catégorisation Élevée devra en implémenter plusieurs améliorations, selon ce qu'exige la base de référence Élevée de SP 800-53B.

## Une famille à part : PM (Program Management)

Contrairement aux dix-neuf autres familles, dont les contrôles s'appliquent à un système d'information précis, la famille **PM** rassemble des contrôles qui s'appliquent au **niveau de l'organisation entière**, indépendamment de tout système particulier — par exemple, l'existence d'un plan de sécurité de l'information à l'échelle de l'organisation, ou d'une stratégie de gestion des risques organisationnelle. Ces contrôles PM sont directement rattachés à l'étape "Prepare" du processus RMF au niveau organisationnel, développée au module 1 — la traduction, dans le catalogue de contrôles, de la distinction entre niveau organisationnel et niveau système déjà posée dès la première étape du RMF.

## Comparer cette structure avec les référentiels déjà étudiés

| Aspect | SP 800-53 | Annexe A ISO 27001 | Common Criteria SOC 2 |
|---|---|---|---|
| Nombre de contrôles | Plus de 1000 (contrôles + améliorations) | 93 | 9 (Common Criteria) + critères additionnels |
| Structure | 20 familles, contrôles + améliorations optionnelles | 4 thèmes | Alignés sur les 5 composantes COSO |
| Sélection | Bases de référence par niveau de catégorisation (SP 800-53B) | Déclaration d'Applicabilité, fondée sur l'analyse de risque | Choix des catégories TSC selon les engagements clients |
| Niveau de prescription | Très détaillé et prescriptif | Modéré, orienté résultat | Orienté résultat, contrôles définis par l'organisation |

Cette comparaison confirme une tendance déjà observée à plusieurs reprises dans cette plateforme : plus un référentiel est né dans un contexte d'obligation légale stricte (le RMF pour les agences fédérales américaines), plus il tend vers la prescription détaillée ; plus un référentiel reste volontaire ou orienté résultat (NIST CSF, SOC 2), plus il laisse de latitude à l'organisation dans le choix précis des contrôles à mettre en œuvre.
