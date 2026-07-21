# Les sept principes fondamentaux (1/2)

## Une architecture fondée sur des principes plutôt que sur des contrôles précis

NIST SP 800-207 énonce sept principes fondamentaux (tenets) qui définissent collectivement ce que signifie une architecture Zero Trust — des principes directeurs plutôt qu'une liste de contrôles techniques précis à implémenter mécaniquement, une approche qui rappelle celle déjà développée pour les huit principes d'ISO 31000 dans le parcours dédié de cette plateforme : des critères de qualité permettant d'évaluer une démarche, plutôt qu'une séquence d'étapes à exécuter.

## Premier principe : toutes les sources de données et tous les services informatiques sont considérés comme des ressources

Ce premier principe élargit délibérément la notion de "ressource" à protéger au-delà des seuls serveurs traditionnels — les appareils personnels connectés au réseau de l'organisation, les fonctions logicielles en tant que service, et même les capteurs envoyant des données constituent tous des ressources devant être protégées selon la même rigueur. Cette conception élargie rejoint directement celle déjà développée pour la notion de data action dans le parcours NIST Privacy Framework de cette plateforme, où toute opération sur des données mérite considération, aussi anodine paraisse-t-elle a priori.

## Deuxième principe : toute communication est sécurisée, quelle que soit la localisation réseau

Ce principe rompt directement avec le modèle périmétrique déjà critiqué au module 0 de ce parcours — le simple fait qu'une communication se déroule au sein du réseau interne de l'organisation, plutôt que sur l'internet public, ne justifie jamais une réduction du niveau de sécurité appliqué. Chaque flux de communication doit satisfaire les mêmes exigences de chiffrement et d'authentification, qu'il traverse un réseau interne réputé fiable ou un réseau externe non maîtrisé.

## Troisième principe : l'accès aux ressources est accordé sur une base sessionnelle

Une autorisation d'accès à une ressource ne doit jamais être accordée de façon permanente une fois pour toutes, mais **par session**, avec une confiance réévaluée à chaque nouvelle interaction — l'accès accordé pour une session donnée ne doit jamais impliquer automatiquement un accès équivalent pour une session ultérieure, même rapprochée dans le temps. Ce principe de réévaluation systématique rejoint directement celui déjà développé pour l'appréciation des risques spécifique à la vie privée d'ISO/IEC 27701, qui doit être réitérée plutôt que considérée comme figée, développée dans le parcours dédié de cette plateforme.

## Quatrième principe : l'accès est déterminé par une politique dynamique

L'autorisation d'accès à une ressource doit tenir compte d'un ensemble d'attributs dynamiques — le comportement observé de l'utilisateur ou de l'équipement, des attributs environnementaux (l'heure, la localisation géographique, le niveau de risque du réseau utilisé), et l'état de sécurité de l'équipement demandeur — plutôt que de reposer sur un ensemble figé et statique de règles d'accès définies une fois pour toutes. Cette exigence de dynamisme rejoint directement le principe déjà développé parmi les huit principes d'ISO 31000 de cette plateforme, où la gestion des risques doit demeurer dynamique face à un contexte en évolution constante.

## Un tableau de synthèse des quatre premiers principes

| Principe | Ce qu'il exige |
|---|---|
| 1. Toutes les ressources | Une protection uniforme, sans négliger les ressources périphériques |
| 2. Toute communication sécurisée | Aucune réduction de sécurité fondée sur la seule localisation réseau |
| 3. Accès sessionnel | Une réévaluation de la confiance à chaque nouvelle interaction |
| 4. Politique dynamique | Une décision d'accès fondée sur des attributs contextuels évolutifs, non figés |

## Le lien avec la leçon suivante

Ces quatre premiers principes posent le cadre conceptuel général de l'architecture Zero Trust — trois principes supplémentaires, portant plus directement sur les mécanismes opérationnels de surveillance et de vérification, complètent cette architecture à la leçon suivante de ce parcours.
