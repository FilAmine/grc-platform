# Préparer un audit SOC 2 (1/2) : cadrage et évaluation de préparation

## Choisir les catégories de critères de confiance

Le premier arbitrage d'un programme SOC 2, déjà évoqué au module 2, consiste à déterminer les catégories additionnelles à retenir au-delà de la Sécurité obligatoire. Cet arbitrage doit se fonder sur des éléments concrets, pas sur une ambition générale de complétude :

- consulter les demandes contractuelles réelles ou anticipées des clients (relire les clauses de sécurité des contrats en cours et des appels d'offres perdus faute de rapport disponible),
- évaluer si les engagements de disponibilité, d'intégrité de traitement ou de vie privée pris auprès des clients sont déjà formalisés (SLA, politique de confidentialité publiée) — car ces engagements deviendront directement les critères que l'auditeur testera,
- éviter d'ajouter une catégorie "par précaution" : chaque catégorie additionnelle alourdit le programme de preuves à maintenir en continu, bien au-delà du seul jour de l'audit.

## Définir le périmètre technique et organisationnel

Le périmètre (scope) d'un audit SOC 2 — quels systèmes, quelles équipes, quels sites sont couverts — doit être défini avec la même rigueur que le domaine d'application d'un SMSI ISO 27001 (développé dans le parcours dédié de cette plateforme). Un périmètre mal calibré produit les mêmes déséquilibres observés pour ISO 27001 : trop large, il complique disproportionnellement la collecte de preuves sur des systèmes annexes peu maîtrisés ; trop étroit, il risque de ne pas répondre aux attentes réelles des clients qui demandent le rapport (un client peut légitimement s'interroger si le périmètre exclut le système qui traite précisément ses propres données).

## L'évaluation de préparation (readiness assessment)

Avant de s'engager auprès d'un cabinet d'audit pour un audit formel (Type I ou Type II), la quasi-totalité des organisations réalisent une **évaluation de préparation** — souvent menée en interne, ou avec l'appui d'un consultant spécialisé, parfois par le cabinet d'audit lui-même dans une mission distincte de l'audit formel (pour préserver l'indépendance requise lors de l'audit proprement dit). Cette évaluation vise à :

- cartographier, Common Criteria par Common Criteria (module 1) et critère additionnel par critère additionnel (module 2), l'état actuel des contrôles existants,
- identifier les écarts par rapport aux critères retenus — l'équivalent direct de l'analyse d'écarts entre Current Profile et Target Profile du NIST CSF, ou de la comparaison entre contrôles existants et Annexe A d'ISO 27001, développées dans les parcours précédents,
- estimer le temps nécessaire pour combler chaque écart avant de pouvoir raisonnablement viser un audit Type I, puis, après une période d'observation suffisante, un audit Type II.

## Construire une matrice de contrôles

Le livrable central de cette phase de préparation est une **matrice de contrôles**, qui relie pour chaque Common Criterion et critère additionnel retenu :

- le contrôle interne réel mis en œuvre par l'organisation pour y répondre,
- le propriétaire de ce contrôle (la personne ou l'équipe responsable de son exécution),
- la fréquence d'exécution attendue (continue, quotidienne, hebdomadaire, trimestrielle, annuelle),
- la nature de la preuve que ce contrôle produit (ticket, journal système, capture d'écran, export de configuration) et où cette preuve est archivée.

Cette matrice n'est pas un document ponctuel produit uniquement pour l'audit — c'est le même type d'artefact vivant que la Déclaration d'Applicabilité d'ISO 27001, qui doit continuer à être maintenu et mis à jour bien après l'audit initial (développé à la fin de la leçon suivante).

## Anticiper la durée nécessaire avant un Type II

Un point de planification souvent sous-estimé par les organisations découvrant SOC 2 pour la première fois : un rapport **Type II** exige une **période d'observation minimale**, généralement au moins trois mois pour une première mission, plus fréquemment six à douze mois pour un rapport pleinement crédible aux yeux d'acheteurs exigeants. Il est donc impossible d'obtenir un Type II robuste immédiatement après avoir comblé les écarts identifiés lors de l'évaluation de préparation — contrairement à une idée reçue fréquente, un programme SOC 2 ne peut pas être "accéléré" au-delà de cette contrainte structurelle de durée d'observation, quel que soit le budget consacré à sa préparation. C'est pourquoi la trajectoire réaliste, développée dans la leçon suivante, passe presque toujours par un premier rapport Type I, suivi d'un Type II après une période d'observation suffisante.
