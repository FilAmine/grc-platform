# Les plans de continuité et la structure de gestion de crise

## De la stratégie au plan : rendre la continuité exécutable dans l'urgence

La clause 8.4 d'ISO 22301 impose à l'organisation de traduire ses stratégies de continuité (développées à la leçon précédente) en **procédures documentées et exécutables** — des plans de continuité d'activité (Business Continuity Plans — BCP) suffisamment détaillés pour être suivis par du personnel sous tension, sans nécessiter d'improvisation ni de recherche d'information au moment critique. Un plan de continuité qui exigerait de son utilisateur de retrouver des informations dispersées, de contacter des personnes dont les coordonnées ne sont plus à jour, ou de prendre des décisions non anticipées, perd une grande partie de sa valeur précisément au moment où sa fiabilité importe le plus.

## Les trois niveaux de documents généralement distingués

La pratique de la continuité d'activité distingue généralement trois niveaux de documents complémentaires, chacun répondant à un besoin différent :

- **Le plan de gestion de crise (Crisis Management Plan)** — décrit la structure de gouvernance de la réponse à la crise (développée plus loin dans cette leçon), les critères de déclenchement, et les grandes lignes de la communication de crise.
- **Le plan de continuité d'activité (Business Continuity Plan)**, propre à chaque activité ou processus critique — décrit les actions précises à mener pour reprendre cette activité spécifique : qui contacter, quelles ressources mobiliser, dans quel ordre, avec quels critères de succès.
- **Le plan de reprise après sinistre (Disaster Recovery Plan)**, propre aux systèmes d'information — décrit les procédures techniques précises de basculement vers l'infrastructure de secours choisie comme stratégie (module précédent), généralement rédigé et testé par les équipes informatiques elles-mêmes.

## La structure de gestion de crise : qui décide, et selon quelle autorité

La gestion de crise repose typiquement sur une structure à plusieurs niveaux, comparable dans son principe hiérarchique aux architectures de gouvernance déjà rencontrées dans cette plateforme (les trois lignes de maîtrise du premier parcours, ou l'architecture à plusieurs acteurs de la conformité SOX) :

- **La cellule de crise stratégique**, généralement présidée par un dirigeant, qui prend les décisions les plus lourdes de conséquences (communication publique, arbitrages budgétaires majeurs, décision de basculement vers un site de secours coûteux).
- **La cellule de crise opérationnelle**, qui coordonne l'exécution effective des plans de continuité activité par activité.
- **Les équipes de terrain**, qui exécutent les actions précises documentées dans chaque plan de continuité.

## Les critères de déclenchement et d'escalade

Le plan de gestion de crise doit préciser des **critères de déclenchement objectifs** — par exemple, une indisponibilité de site dépassant un seuil de durée prédéfini, ou un incident affectant un nombre de clients au-delà d'un certain seuil — plutôt que de laisser cette décision à une appréciation purement subjective au moment de l'incident. Cette exigence de critères objectifs rappelle directement celle déjà développée pour la classification des incidents majeurs au titre de DORA, ou pour les critères de notification en plusieurs paliers de NIS2, développées dans les parcours dédiés de cette plateforme — un déclenchement trop tardif d'une cellule de crise, faute de critère clair, aggrave souvent inutilement l'impact d'une perturbation par ailleurs bien anticipée sur le papier.

## La communication de crise, un enjeu à part entière

Le plan de gestion de crise doit anticiper précisément la **communication** à destination de chaque partie intéressée pertinente — le personnel (instructions de sécurité, informations sur la reprise), les clients (transparence sur l'impact et les délais), les autorités de régulation le cas échéant (une obligation qui rejoint directement la notification des incidents majeurs déjà développée dans le parcours DORA de cette plateforme), et les médias pour les crises les plus visibles. Une communication de crise mal maîtrisée — tardive, contradictoire, ou trop optimiste au regard de la réalité — peut aggraver significativement l'impact réputationnel d'une perturbation, indépendamment même de sa gravité opérationnelle réelle.

## Pourquoi ces plans doivent rester vivants plutôt que figés

Un plan de continuité rédigé une fois puis jamais mis à jour perd rapidement sa valeur opérationnelle à mesure que l'organisation évolue — nouveaux systèmes, nouveaux locaux, changements de personnel clé, nouveaux fournisseurs critiques — un piège d'obsolescence silencieuse de la documentation déjà signalé à de multiples reprises dans cette plateforme, notamment pour l'actualisation annuelle du périmètre d'évaluation SOX ou pour les Significant Change Requests de FedRAMP. C'est précisément le programme d'exercices et de tests, développé au module suivant de ce parcours, qui permet de révéler ces décalages avant qu'une crise réelle ne les révèle de la pire des façons.

## Le lien avec le module suivant

Rédiger un plan de continuité, aussi soigné soit-il, ne garantit jamais qu'il fonctionnera effectivement le jour venu — seul un programme structuré d'exercices et de tests, développé au module suivant de ce parcours, permet de vérifier concrètement sa pertinence et de former les équipes à son exécution effective.
