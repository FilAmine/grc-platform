# Les pratiques d'ITIL 4 (2/2) : les pratiques opérationnelles centrales

## Les pratiques les plus quotidiennement mobilisées

Parmi les trente-quatre pratiques déjà présentées dans la leçon précédente, quatre occupent une place particulièrement centrale dans l'activité quotidienne d'une organisation IT — au point d'être, pour beaucoup de professionnels, ce qu'ITIL évoque en premier lieu, bien avant le Service Value System ou la chaîne de valeur développés aux modules 1 et 2 de ce parcours.

## Le centre de services (Service Desk)

Le **Service Desk** constitue le point de contact unique entre le fournisseur de services et l'ensemble de ses utilisateurs, pour la remontée des demandes, incidents et questions courantes. Sa valeur ne réside pas seulement dans sa fonction technique de premier support, mais dans le rôle humain qu'il joue souvent en situation de stress pour l'utilisateur (un incident bloquant, une demande urgente) — ITIL 4 insiste explicitement sur l'importance des compétences relationnelles du personnel de Service Desk, une dimension qui recoupe directement la dimension "Organisations et personnes" déjà développée au module 1 de ce parcours.

## La gestion des incidents (Incident Management)

Objectif : minimiser l'impact négatif des incidents en restaurant le fonctionnement normal du service aussi rapidement que possible. Un **incident** est défini comme une interruption non planifiée d'un service, ou une réduction de sa qualité. Cette pratique recoupe directement la fonction Respond du NIST CSF et les contrôles 5.24-5.28 de l'Annexe A d'ISO 27001, tous deux développés dans les parcours précédents de cette plateforme — avec une nuance de vocabulaire : ITIL distingue la restauration rapide du service normal (l'objectif immédiat de la gestion des incidents) de la recherche de la cause profonde (l'objectif distinct de la gestion des problèmes, développée plus loin dans cette leçon), une distinction déjà rencontrée sous une forme comparable dans le domaine DSS de COBIT (DSS02 gestion des demandes et incidents, DSS03 gestion des problèmes), développé dans le parcours dédié de cette plateforme.

Une notion propre à ITIL mérite d'être signalée : la **priorisation des incidents**, généralement fondée sur le croisement de deux critères — l'**impact** (l'ampleur des utilisateurs ou processus métier affectés) et l'**urgence** (la vitesse à laquelle une résolution est nécessaire) — un principe de priorisation qui rappelle, dans sa logique de croisement à deux facteurs, l'évaluation combinée de la gravité et de la vraisemblance déjà rencontrée pour les scénarios opérationnels d'EBIOS RM, développée dans le parcours dédié de cette plateforme.

## La gestion des problèmes (Problem Management)

Objectif : réduire la probabilité et l'impact des incidents en identifiant leurs causes profondes réelles ou potentielles, et en gérant les solutions de contournement et les erreurs connues. Cette pratique se décline en trois activités : l'**identification des problèmes** (souvent à partir de l'analyse de tendances dans les incidents récurrents), l'**analyse des problèmes** (recherche de la cause racine), et le **contrôle des erreurs** (gestion des erreurs connues et de leurs solutions de contournement documentées).

La **base de données des erreurs connues (Known Error Database — KEDB)** constitue un livrable central de cette pratique : un référentiel documentant chaque erreur connue, sa cause identifiée, et la solution de contournement disponible en attendant une résolution définitive — un outil qui permet au Service Desk et à la gestion des incidents de résoudre rapidement un incident récurrent en s'appuyant sur une solution déjà documentée, plutôt que de repartir de zéro à chaque occurrence. Cette distinction entre correction immédiate (gestion des incidents) et traitement de la cause racine (gestion des problèmes) rejoint directement celle déjà développée entre correction et action corrective dans le parcours ISO 27001 de cette plateforme.

## La gestion des demandes de service (Service Request Management)

Objectif : traiter l'ensemble des demandes de service initiées par les utilisateurs, de manière efficace et conviviale — une demande d'accès à une application, une demande d'équipement, une demande d'information. Contrairement à un incident (qui traite une défaillance non planifiée), une demande de service porte sur un besoin normal et attendu, généralement traité selon un processus standardisé et pré-approuvé — un parallèle direct avec la notion de **changement standard** développée dans la pratique de facilitation des changements, objet du module 4 de ce parcours.

## Ce que cette distinction entre incident, problème et demande révèle

La séparation nette entre ces trois pratiques — un incident restauré rapidement, un problème dont la cause profonde est traitée séparément et potentiellement plus lentement, une demande traitée selon un processus prévisible et standardisé — illustre bien la philosophie d'ensemble d'ITIL 4 : ne pas traiter tous les événements remontés par les utilisateurs de la même façon, mais reconnaître que chacun appelle une réponse de nature différente, avec des objectifs de délai et des ressources mobilisées distincts. Un Service Desk qui confondrait systématiquement ces trois catégories — en traitant, par exemple, chaque demande de service comme un incident à résoudre en urgence — produirait une allocation de ressources inefficace, exactement le type de dispersion de l'effort déjà signalée à travers de multiples référentiels de cette plateforme (la priorisation des Implementation Groups des CIS Controls, ou celle des couples source de risque/objectif visé d'EBIOS RM).
