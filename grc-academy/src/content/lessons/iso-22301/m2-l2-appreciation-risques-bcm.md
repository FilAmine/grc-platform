# L'analyse d'impact sur l'activité (2/2) : l'appréciation des risques propre à la continuité

## Une seconde brique indispensable, complémentaire de la BIA

La clause 8.2.3 d'ISO 22301 exige, en complément de la BIA développée à la leçon précédente, une **appréciation des risques (risk assessment)** spécifiquement orientée vers l'identification des scénarios de perturbation susceptibles d'affecter les activités jugées critiques — une appréciation des risques qui se distingue de celle déjà développée dans le parcours ISO 27001 de cette plateforme par son objet : là où l'appréciation des risques d'ISO 27001 porte sur la confidentialité, l'intégrité et la disponibilité de l'information, celle d'ISO 22301 porte sur la capacité de l'organisation à maintenir la délivrance de ses produits et services essentiels, quelle que soit la cause de la perturbation.

## Une approche par scénarios plutôt que par actif

Contrairement à l'appréciation des risques d'ISO 27001, structurée autour des actifs informationnels, l'appréciation des risques d'ISO 22301 raisonne le plus souvent par **scénarios de perturbation** — la perte d'un site (incendie, inondation, indisponibilité d'accès), la perte de systèmes d'information critiques (panne majeure, cyberattaque), la perte de personnel clé (pandémie, mouvement social), ou la défaillance d'un fournisseur ou prestataire critique. Cette approche par scénarios rappelle directement celle déjà développée pour les scénarios stratégiques et opérationnels d'EBIOS RM dans le parcours dédié de cette plateforme, bien qu'appliquée ici à la seule question de la continuité d'activité plutôt qu'à l'ensemble du risque cyber.

## L'approche "tous risques" (all-hazards) comme principe directeur

ISO 22301 encourage explicitement une approche dite **"tous risques" (all-hazards)** : plutôt que de bâtir une stratégie de continuité distincte pour chaque cause possible de perturbation (un plan pour l'incendie, un autre pour la pandémie, un autre encore pour la cyberattaque), l'organisation se concentre prioritairement sur l'**impact** d'une indisponibilité de site, de système ou de personnel — quelle qu'en soit la cause — puisque les mesures de reprise à mettre en œuvre (basculement vers un site de secours, activation d'un système de repli, mobilisation de personnel de remplacement) sont souvent largement identiques, indépendamment de l'événement déclencheur. Cette approche "tous risques" illustre un principe de rationalisation méthodologique déjà rencontré à plusieurs reprises dans cette plateforme, notamment pour la priorisation par les conséquences plutôt que par la cause déjà développée dans le cadre de gestion des risques liés aux TIC de DORA.

## Comment la BIA et l'appréciation des risques se combinent concrètement

La BIA identifie les activités critiques et leurs délais de reprise attendus (RTO, RPO) ; l'appréciation des risques identifie les scénarios susceptibles de provoquer l'indisponibilité des ressources nécessaires à ces mêmes activités, et évalue leur probabilité et leur gravité selon une logique de priorisation déjà familière depuis les parcours EBIOS RM et NIST RMF de cette plateforme. La combinaison des deux permet à l'organisation d'identifier ses vulnérabilités les plus critiques — par exemple, une activité au RTO très court (quelques heures) qui dépend entièrement d'un unique site physique sans site de secours identifié constitue une vulnérabilité prioritaire, quelle que soit par ailleurs la probabilité précise de chaque scénario de sinistre susceptible d'affecter ce site.

## Ce que cette double analyse produit concrètement

À l'issue de la BIA et de l'appréciation des risques, l'organisation dispose d'une cartographie précise de ses activités critiques, de leurs délais de reprise attendus, de leurs ressources minimales nécessaires, et des scénarios de perturbation les plus probables et les plus graves susceptibles de les affecter — l'ensemble des données d'entrée indispensables pour élaborer des stratégies de continuité réalistes et proportionnées, développées au module suivant de ce parcours, plutôt que des mesures de continuité génériques et déconnectées des besoins réels de l'organisation.

## Le lien avec le module suivant

Une fois cette cartographie établie, l'organisation doit choisir, pour chaque activité critique, la ou les stratégies de continuité les plus adaptées à son RTO, son RPO et son budget disponible — un arbitrage qui fait l'objet du module suivant de ce parcours.
