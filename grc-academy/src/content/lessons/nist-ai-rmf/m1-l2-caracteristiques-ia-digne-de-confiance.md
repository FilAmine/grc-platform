# Le risque de l'IA (2/2) : les caractéristiques de l'IA digne de confiance

## Sept caractéristiques comme boussole commune

L'AI RMF définit sept caractéristiques d'une intelligence artificielle **digne de confiance (trustworthy)**, qui servent de boussole commune pour l'ensemble des quatre fonctions du Core développées aux modules 2 à 5 de ce parcours — un système d'IA valide et fiable, sûr, sécurisé et résilient, responsable et transparent, explicable et interprétable, respectueux de la vie privée, et équitable avec une gestion active des biais préjudiciables.

## Valide et fiable (valid and reliable)

Un système d'IA doit démontrer, par des méthodes de validation rigoureuses, qu'il produit des résultats corrects et cohérents dans les conditions réelles de son usage prévu — une exigence qui rejoint directement la fonction Measure développée au module 4 de ce parcours, et qui distingue une simple performance mesurée en laboratoire d'une fiabilité démontrée en conditions opérationnelles réelles.

## Sûr (safe)

La sûreté couvre l'absence de conséquences dommageables pour la santé, la sécurité ou les biens des personnes et de l'environnement — une préoccupation particulièrement critique pour les systèmes d'IA intégrés à des dispositifs physiques (véhicules autonomes, dispositifs médicaux) mais également pertinente pour des systèmes purement logiciels dont les décisions peuvent avoir des conséquences réelles significatives sur la vie des personnes.

## Sécurisé et résilient (secure and resilient)

Cette caractéristique rejoint directement les préoccupations de sécurité de l'information déjà développées dans les parcours ISO 27001, NIST CSF et CIS Controls de cette plateforme, tout en y ajoutant des menaces spécifiques à l'apprentissage automatique — les attaques par empoisonnement des données d'entraînement (data poisoning), les attaques adverses visant à tromper un modèle par des entrées spécialement conçues, ou l'extraction non autorisée du modèle lui-même par un tiers.

## Responsable et transparent (accountable and transparent)

Cette caractéristique exige qu'une organisation puisse rendre compte des décisions prises par ses systèmes d'IA et de leur fonctionnement général, sans nécessairement révéler l'intégralité des détails techniques propriétaires — une transparence qui rejoint directement celle déjà développée pour la fonction Communicate-P dans le parcours NIST Privacy Framework de cette plateforme, ici appliquée spécifiquement aux systèmes de décision automatisée.

## Explicable et interprétable (explainable and interpretable)

Distincte de la transparence générale, cette caractéristique porte spécifiquement sur la capacité à expliquer **pourquoi** un système d'IA a produit une décision ou un résultat précis dans un cas donné — une capacité particulièrement critique pour les décisions automatisées à fort impact sur les individus (refus de crédit, décision de recrutement), où la personne concernée doit pouvoir comprendre les motifs d'une décision qui l'affecte directement, un enjeu qui rejoint directement l'article 22 du RGPD sur la décision individuelle automatisée, déjà développé dans le parcours dédié de cette plateforme.

## Respectueux de la vie privée (privacy-enhanced)

Cette caractéristique s'appuie directement sur le NIST Privacy Framework, déjà développé en détail dans le parcours dédié de cette plateforme — un système d'IA entraîné sur des données personnelles doit intégrer les mêmes principes de gestion du risque vie privée déjà développés (minimisation des données, limitation des usages non anticipés, capacité de contrôle par les personnes concernées), avec une acuité particulière compte tenu de la capacité des modèles d'apprentissage automatique à révéler ou inférer des informations personnelles au-delà de ce qui a été explicitement fourni.

## Équitable, avec une gestion active des biais préjudiciables (fair, with harmful bias managed)

Cette dernière caractéristique traite directement du risque de discrimination algorithmique déjà évoqué à la leçon précédente de ce parcours — l'AI RMF distingue plusieurs sources de biais préjudiciables : les **biais systémiques**, hérités de données d'entraînement reflétant des inégalités historiques ; les **biais statistiques et computationnels**, résultant de choix méthodologiques dans la conception du modèle ; et les **biais humains**, introduits par les personnes impliquées dans la conception, l'annotation des données ou l'interprétation des résultats.

## Un tableau de synthèse des sept caractéristiques

| Caractéristique | Préoccupation centrale |
|---|---|
| Valide et fiable | Exactitude et cohérence des résultats en conditions réelles |
| Sûr | Absence de préjudice pour les personnes, les biens et l'environnement |
| Sécurisé et résilient | Résistance aux menaces classiques et propres à l'IA (empoisonnement, attaques adverses) |
| Responsable et transparent | Capacité à rendre compte du fonctionnement général du système |
| Explicable et interprétable | Capacité à expliquer une décision précise dans un cas donné |
| Respectueux de la vie privée | Application des principes du NIST Privacy Framework aux données d'entraînement et d'usage |
| Équitable | Gestion active des biais systémiques, statistiques et humains |

## Le lien avec le module suivant

Ces sept caractéristiques ne constituent jamais une simple liste de vœux : elles structurent concrètement le travail attendu de chacune des quatre fonctions du Core, à commencer par la fonction transversale Govern, développée au module suivant de ce parcours.
