# Les sept étapes du RMF (3/4) : Assess et Authorize

## Étape 5 — Assess (Évaluer)

Cette étape consiste à faire évaluer, par un **évaluateur indépendant**, si les contrôles documentés dans le Plan de Sécurité du Système sont correctement implémentés, fonctionnent comme prévu, et produisent le résultat de sécurité attendu.

### L'indépendance de l'évaluateur

Le RMF exige une indépendance de l'évaluateur vis-à-vis de l'équipe qui a développé et implémenté le système — un principe directement comparable à l'indépendance de l'auditeur interne exigée par la clause 9.2 d'ISO 27001, ou à l'indépendance du cabinet d'audit SOC 2, déjà rencontrées dans les parcours précédents de cette plateforme. Le degré d'indépendance requis varie selon le niveau de catégorisation du système (module 1) : un système à impact Élevé exige un degré d'indépendance plus strict qu'un système à impact Faible.

### La méthode d'évaluation : SP 800-53A

**SP 800-53A** fournit, pour chaque contrôle du catalogue SP 800-53, des **procédures d'évaluation détaillées**, structurées autour de trois méthodes — un parallèle direct avec les méthodes de test déjà rencontrées dans le parcours SOC 2 de cette plateforme :

- **Examine** — examiner la documentation, les politiques, les configurations, les enregistrements (l'équivalent de la méthode d'inspection en SOC 2),
- **Interview** — interroger le personnel responsable de l'implémentation ou de la gestion du contrôle (l'équivalent de l'enquête en SOC 2),
- **Test** — exécuter ou observer l'exécution d'un mécanisme technique pour vérifier son comportement réel (l'équivalent de la réexécution en SOC 2).

### Le Rapport d'Évaluation de Sécurité (Security Assessment Report — SAR)

À l'issue de l'évaluation, l'évaluateur indépendant produit un **SAR**, qui documente les résultats de chaque procédure d'évaluation, et identifie les **faiblesses ou déficiences** constatées, classées selon leur sévérité. Ce document joue, dans l'architecture du RMF, un rôle analogue à la section IV d'un rapport SOC 2 (description des tests et de leurs résultats) déjà développée dans le parcours dédié de cette plateforme.

### Le Plan d'Actions et d'Échéances (Plan of Action and Milestones — POA&M)

Les faiblesses identifiées dans le SAR qui ne sont pas corrigées avant la décision d'autorisation (étape suivante) sont consignées dans un **POA&M** — un document vivant qui liste, pour chaque faiblesse résiduelle, l'action corrective prévue, les ressources nécessaires, le calendrier de remédiation, et le suivi de son avancement. Un POA&M qui grossit sans jamais se réduire, ou dont les échéances glissent indéfiniment sans justification documentée, constitue un signal d'alerte immédiatement identifié par l'Authorizing Official au moment de la décision d'autorisation — la même dynamique déjà observée pour le registre de non-conformités d'un SMSI ISO 27001 dans le parcours dédié de cette plateforme.

## Étape 6 — Authorize (Autoriser)

Cette étape est propre au RMF et n'a pas d'équivalent direct dans ISO 27001, le NIST CSF ou SOC 2 : elle consiste en une **décision formelle explicite**, prise par une personne nommément désignée et habilitée — l'**Authorizing Official (AO)**, développé en détail au module 3 — d'accepter le risque résiduel du système et d'autoriser (ou non) son exploitation.

### Le paquet d'autorisation (authorization package)

L'AO fonde sa décision sur un **paquet d'autorisation**, qui rassemble a minima le Plan de Sécurité du Système (SSP), le Rapport d'Évaluation de Sécurité (SAR), et le Plan d'Actions et d'Échéances (POA&M) — la matière documentaire complète produite par les étapes précédentes, condensée pour permettre une décision de risque éclairée par une personne qui n'a généralement pas participé directement à l'implémentation technique du système.

### Les types de décision d'autorisation

- **Autorisation d'exploitation (Authorization to Operate — ATO)** — le système est autorisé à fonctionner, généralement pour une durée déterminée ou sous réserve d'une surveillance continue satisfaisante (développée à l'étape 7).
- **Autorisation provisoire de test (Interim Authorization to Test — IATT)** — une autorisation limitée, permettant de tester le système dans un environnement opérationnel sans pour autant l'autoriser à traiter des données réelles en production.
- **Refus d'autorisation (Denial of Authorization to Operate)** — l'AO estime que le risque résiduel documenté dans le paquet d'autorisation est inacceptable ; le système ne peut pas être mis en exploitation tant que les déficiences majeures n'ont pas été corrigées et réévaluées.

### La réciprocité entre autorisations

Le RMF encourage un principe de **réciprocité** : une agence fédérale peut, sous certaines conditions, s'appuyer sur une autorisation déjà accordée par une autre agence pour un même système ou service, plutôt que de reconduire intégralement le processus d'évaluation — un principe d'efficacité comparable, dans son intention, à la logique de mapping entre référentiels déjà développée à plusieurs reprises dans cette plateforme, ici appliqué à la réutilisation d'une autorisation entre organisations plutôt qu'entre référentiels distincts. C'est ce principe de réciprocité, largement formalisé, qui sous-tend le fonctionnement du programme FedRAMP développé au module 4.

## Ce que cette paire d'étapes révèle sur la philosophie du RMF

L'existence d'une étape d'autorisation formelle, distincte de l'évaluation technique elle-même, matérialise un principe central du RMF : la décision d'accepter un risque résiduel de sécurité est une **décision de gestion**, pas une conclusion technique automatique — une personne nommément responsable doit l'assumer explicitement, avec son nom associé à cette décision dans le dossier d'autorisation, plutôt que de laisser cette responsabilité diluée entre plusieurs équipes techniques. C'est un parallèle direct avec le principe du "risk owner" qui accepte formellement un risque résiduel, déjà développé dans le premier parcours de cette plateforme — le RMF en fait une étape distincte et formalisée du processus, plutôt qu'une simple bonne pratique de gouvernance.
