# Les processus de relation : fournisseurs et parties prenantes métier

## Deux relations distinctes à gérer simultanément

ISO/IEC 20000 impose de structurer deux catégories de relations distinctes, chacune essentielle au bon fonctionnement du SMS : la **gestion de la relation métier (business relationship management)**, tournée vers les clients et bénéficiaires des services, et la **gestion des fournisseurs (supplier management)**, tournée vers les tiers qui contribuent à leur délivrance, déjà esquissée au module 1 de ce parcours à travers l'exigence d'inclure les services fournis par des tiers dans le périmètre du SMS.

## La gestion de la relation métier

Cette exigence impose d'établir un dialogue structuré et régulier avec les clients et bénéficiaires des services — comprendre leurs besoins actuels et futurs, recueillir leur satisfaction, et anticiper les évolutions de leurs attentes avant qu'elles ne se traduisent en insatisfaction ouverte. Cette exigence rejoint directement la fonction Communicate-P déjà développée dans le parcours NIST Privacy Framework de cette plateforme, ou la communication et la consultation déjà développées dans le parcours ISO 31000 — un dialogue bidirectionnel plutôt qu'une simple communication descendante, permettant à l'organisation de détecter précocement les signaux d'insatisfaction ou d'évolution des besoins.

## La gestion des fournisseurs

Cette exigence impose de sélectionner, contractualiser et superviser dans la durée l'ensemble des fournisseurs contribuant à la délivrance des services couverts par le SMS — des accords contractuels précisant les niveaux de service attendus de chaque fournisseur, une supervision régulière de leur performance effective, et des mécanismes d'escalade en cas de manquement constaté. Cette exigence rejoint directement celle déjà développée pour la gestion des risques de la chaîne d'approvisionnement dans les parcours NIST RMF, DORA et NIST AI RMF de cette plateforme — la responsabilité de la qualité du service rendu au client final ne se délègue jamais entièrement à un fournisseur sous-jacent, même contractuellement engagé sur des niveaux de service précis.

## Le Service Integration and Management (SIAM) dans les environnements multi-fournisseurs

Pour les organisations dont la délivrance de services repose sur de multiples fournisseurs simultanés — une réalité de plus en plus fréquente à mesure que les organisations externalisent des composants spécialisés de leur infrastructure —, ISO/IEC 20000 encourage l'adoption d'une approche de **Service Integration and Management (SIAM)**, qui coordonne l'ensemble de ces fournisseurs sous un unique système de management des services plutôt que de laisser chaque relation fournisseur gérée de façon cloisonnée et incohérente. Cette approche d'intégration multi-fournisseurs rappelle directement celle déjà développée pour la vue de portefeuille des risques de COSO ERM, développée dans le parcours dédié de cette plateforme — une vision consolidée plutôt qu'une appréciation cloisonnée révèle des interactions et des risques que chaque relation prise isolément ne permettrait jamais de détecter.

## Les accords de niveau de service comme instrument commun aux deux relations

Les **accords de niveau de service (Service Level Agreements — SLA)**, conclus avec les clients, et les **accords de niveau opérationnel (Operational Level Agreements — OLA)** ou contrats de soutien (Underpinning Contracts) conclus avec les fournisseurs internes ou externes, constituent l'instrument commun qui relie ces deux catégories de relations — un engagement de niveau de service pris envers un client ne peut jamais être tenu de façon fiable sans des engagements cohérents et alignés pris en amont auprès de chacun des fournisseurs contribuant à sa délivrance. Cette cohérence en cascade rappelle directement celle déjà développée pour la propagation des exigences à travers la chaîne d'approvisionnement dans les parcours TISAX et CMMC de cette plateforme.

## Un exemple concret d'articulation entre ces deux relations

Une organisation ayant pris l'engagement contractuel, envers ses clients, d'une disponibilité de 99,9 % pour un service critique doit ainsi s'assurer que chacun de ses fournisseurs contribuant à ce service (hébergement cloud, connectivité réseau, support applicatif tiers) est lui-même engagé sur des niveaux de disponibilité au moins équivalents, voire supérieurs pour compenser les marges d'incertitude propres à chaque maillon de la chaîne — un déséquilibre entre l'engagement pris envers le client et les engagements obtenus des fournisseurs sous-jacents expose directement l'organisation à un manquement qu'elle ne pourra jamais corriger unilatéralement une fois le service en production.

## Un tableau de synthèse de ces deux processus de relation

| Processus | Direction | Instrument |
|---|---|---|
| Gestion de la relation métier | Vers les clients et bénéficiaires | Accords de niveau de service (SLA) |
| Gestion des fournisseurs | Vers les tiers contribuant à la délivrance | Accords de niveau opérationnel (OLA), contrats de soutien |
| SIAM | Coordination transversale multi-fournisseurs | Système de management des services intégré |

## Le lien avec le module suivant

Ces relations établies, l'organisation doit encore structurer la façon dont ses services évoluent dans le temps — la conception, la construction et la transition des services, ainsi que la gestion des changements qui les accompagne, développées au module suivant de ce parcours.
