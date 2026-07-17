# Rôles et responsabilités propres au RMF

## Une gouvernance nommément désignée, pas seulement fonctionnelle

Une caractéristique distinctive du RMF, par rapport aux référentiels plus génériques déjà étudiés dans cette plateforme, est le degré de précision avec lequel il définit des rôles individuels, nommément désignés pour un système donné — au-delà de la simple répartition fonctionnelle des responsabilités déjà rencontrée dans le modèle des trois lignes de maîtrise du premier parcours de cette plateforme.

## L'Authorizing Official (AO) — la décision de risque incarnée

L'**Authorizing Official** est un cadre supérieur, désigné par l'organisation, qui assume formellement la responsabilité d'accepter le risque résiduel d'un système et de décider de son autorisation d'exploitation (l'étape 6 du processus, développée au module 1). Il ne s'agit jamais d'une fonction purement technique — l'AO doit disposer d'une autorité et d'une vision suffisamment larges sur la mission de l'organisation pour arbitrer un niveau de risque acceptable au regard des enjeux métier, pas seulement des enjeux de sécurité isolés. Un AO peut, selon la taille de l'organisation, être responsable de l'autorisation de plusieurs systèmes ; certaines organisations désignent également un **AO Designated Representative (AODR)**, qui agit en son nom pour les aspects opérationnels du processus sans détenir lui-même le pouvoir final de décision d'autorisation.

## Le System Owner — le propriétaire opérationnel du système

Le **System Owner** est responsable du fonctionnement global du système tout au long de son cycle de vie : il pilote le développement du Plan de Sécurité du Système (SSP), coordonne la mise en œuvre des contrôles avec les équipes techniques, et reste l'interlocuteur principal pour les questions opérationnelles relatives au système. Ce rôle correspond, dans son esprit, au propriétaire de risque (risk owner) déjà développé dans le premier parcours de cette plateforme, mais appliqué spécifiquement au périmètre d'un système d'information précis plutôt qu'à un risque métier plus large.

## L'Information System Security Officer (ISSO) — le pilote quotidien de la sécurité

L'**ISSO** assure au quotidien la mise en œuvre et le maintien de la posture de sécurité du système : il coordonne le processus d'évaluation et d'autorisation avec l'évaluateur indépendant, maintient le SSP à jour, suit l'avancement du Plan d'Actions et d'Échéances (POA&M, module 1), et sert de point de contact pour les questions de sécurité quotidiennes relatives au système. Ce rôle est fonctionnellement proche d'un RSSI opérationnel appliqué à un système précis plutôt qu'à l'organisation entière — dans une grande organisation gérant de nombreux systèmes, plusieurs ISSO peuvent coexister, chacun rattaché à un ou plusieurs systèmes spécifiques.

## Le Senior Agency Information Security Officer (SAISO) — la vision organisationnelle

Le **SAISO** (parfois désigné Chief Information Security Officer selon les organisations) porte la responsabilité de sécurité de l'information à l'échelle de l'organisation entière, pas d'un seul système : il définit la stratégie de gestion des risques organisationnelle établie à l'étape Prepare (module 1), supervise le programme de sécurité dans son ensemble, et rend compte à la direction générale de l'organisation — un rôle directement comparable au RSSI d'une organisation au sens large, déjà évoqué dans le premier parcours de cette plateforme, mais formalisé ici avec un titre et des responsabilités précisément définis par le RMF.

## Le Common Control Provider — la mutualisation des contrôles

Développé au module 1 lors de la présentation des contrôles communs, le **Common Control Provider** est responsable du développement, de l'implémentation, de l'évaluation et de la surveillance continue d'un ou plusieurs contrôles fournis de façon centralisée et hérités par plusieurs systèmes — par exemple, l'équipe responsable d'un centre de données partagé qui fournit les contrôles physiques hérités par tous les systèmes qui y sont hébergés. Ce rôle évite qu'un même contrôle physique ou d'infrastructure ne soit documenté et évalué séparément par chaque System Owner dont le système utilise cette infrastructure commune.

## L'évaluateur indépendant (Independent Assessor)

Déjà présenté au module 1 lors du développement de l'étape Assess, l'évaluateur indépendant conduit l'évaluation des contrôles selon les procédures de SP 800-53A, et produit le Rapport d'Évaluation de Sécurité (SAR) qui alimente la décision de l'Authorizing Official. Son indépendance vis-à-vis du System Owner et de l'ISSO — qui ont, eux, un intérêt direct à ce que l'évaluation soit favorable — constitue une garantie structurelle comparable à celle exigée pour un auditeur SOC 2 ou un auditeur interne ISO 27001, déjà rencontrées dans les parcours précédents de cette plateforme.

## Comment ces rôles s'articulent en pratique

Un exemple concret permet de fixer l'articulation de ces rôles : pour un système hébergé dans un centre de données partagé d'une agence, le **System Owner** pilote le développement du système et de son SSP, s'appuyant sur les contrôles physiques déjà fournis par le **Common Control Provider** du centre de données ; l'**ISSO** coordonne au quotidien la mise en œuvre des contrôles spécifiques au système et le suivi du POA&M ; un **évaluateur indépendant**, sans lien hiérarchique avec l'équipe du système, conduit l'évaluation selon SP 800-53A et produit le SAR ; enfin, l'**Authorizing Official**, s'appuyant sur le paquet d'autorisation complet (SSP, SAR, POA&M), rend une décision formelle d'autorisation — le tout supervisé, au niveau de l'organisation entière, par le **SAISO**, garant de la cohérence de la stratégie de gestion des risques à travers l'ensemble des systèmes de l'organisation.

Cette granularité de rôles nommément définis, bien plus précise que ce qu'exigent explicitement ISO 27001, le NIST CSF ou SOC 2, reflète directement l'origine du RMF dans un contexte d'obligation légale stricte : en cas de manquement ou d'incident, la responsabilité de chaque décision doit pouvoir être attribuée à une personne identifiée précisément, pas seulement à une fonction ou une équipe diffuse.
