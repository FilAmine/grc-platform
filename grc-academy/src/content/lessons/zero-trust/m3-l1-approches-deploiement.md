# Les approches de déploiement (1/2) : quatre variantes concrètes

## Une architecture logique, plusieurs implémentations possibles

Déjà annoncé au module 2 de ce parcours, l'architecture Zero Trust ne prescrit jamais une implémentation technique unique — NIST SP 800-207 décrit plusieurs approches de déploiement concrètes, chacune adaptée à des contextes techniques différents, permettant à une organisation de choisir la variante la plus cohérente avec son infrastructure existante plutôt que de devoir reconstruire l'intégralité de son système d'information.

## L'approche par agent et passerelle (device agent/gateway-based)

Cette approche installe un **agent logiciel** sur chaque équipement demandeur, qui communique avec une **passerelle** placée en amont de chaque ressource protégée — l'agent authentifie l'équipement et l'utilisateur, tandis que la passerelle applique les décisions du Policy Engine avant de laisser transiter la communication vers la ressource. Cette approche convient particulièrement aux environnements où l'organisation maîtrise directement les équipements de ses utilisateurs, permettant l'installation d'un agent dédié — une configuration qui rappelle celle déjà développée pour l'Architecture Type A1 de SWIFT CSP, où l'utilisateur héberge et maîtrise l'intégralité de son infrastructure de connexion.

## L'approche par enclave (enclave-based)

Cette approche regroupe plusieurs ressources partageant des exigences de protection similaires au sein d'une **enclave** protégée par une passerelle commune, plutôt que de déployer une passerelle dédiée à chaque ressource individuelle — une approche particulièrement pertinente lorsque de nombreuses ressources anciennes ou difficiles à modifier individuellement doivent néanmoins bénéficier d'une protection Zero Trust cohérente. Cette approche par regroupement rappelle directement celle déjà développée pour la vue de portefeuille des risques de COSO ERM, où une vision consolidée plutôt que cloisonnée permet une gestion plus cohérente de risques comparables, développée dans le parcours dédié de cette plateforme.

## L'approche par portail de ressources (resource portal-based)

Cette approche place un **portail unique** devant l'ensemble des ressources protégées, à travers lequel chaque demandeur doit transiter pour accéder à n'importe laquelle d'entre elles — une approche qui ne nécessite aucune installation d'agent sur l'équipement du demandeur, ce qui la rend particulièrement adaptée aux contextes où l'organisation ne maîtrise pas directement les équipements utilisés (équipements personnels des employés, ou accès de partenaires externes). Cette approche rappelle directement celle déjà développée pour l'Architecture Type A3 de SWIFT CSP, où l'utilisateur n'exploite qu'une interface d'accès légère plutôt que l'intégralité de l'infrastructure de connexion, développée dans le parcours dédié de cette plateforme.

## L'isolation applicative sur l'équipement (device application sandboxing)

Cette dernière approche isole l'application accédant à une ressource protégée au sein d'un environnement d'exécution cloisonné (un sandbox) sur l'équipement du demandeur, limitant ainsi les conséquences potentielles d'une compromission de cet équipement sur l'ensemble du reste du système — une approche qui rappelle directement celle déjà développée pour la sécurité applicative propre à l'apprentissage automatique dans le parcours NIST AI RMF de cette plateforme, où l'isolation d'un composant limite la propagation d'une éventuelle compromission.

## Un tableau de synthèse des quatre approches de déploiement

| Approche | Principe | Contexte le plus adapté |
|---|---|---|
| Agent et passerelle | Un agent sur l'équipement, une passerelle par ressource | Équipements directement maîtrisés par l'organisation |
| Enclave | Une passerelle commune pour un groupe de ressources similaires | Ressources anciennes ou difficiles à modifier individuellement |
| Portail de ressources | Un point d'accès unique, sans agent installé | Équipements personnels ou partenaires externes |
| Isolation applicative | Cloisonnement de l'application accédant à la ressource | Limitation de la propagation d'une compromission de l'équipement |

## Pourquoi une organisation combine souvent plusieurs approches simultanément

En pratique, une organisation d'une certaine taille combine fréquemment plusieurs de ces approches selon le contexte de chaque catégorie de ressources et de demandeurs — l'approche par agent et passerelle pour les équipements professionnels directement maîtrisés, l'approche par portail pour les accès occasionnels de partenaires externes, et l'approche par enclave pour un groupe de systèmes hérités difficiles à moderniser individuellement. Cette combinaison de plusieurs approches plutôt qu'un choix unique et uniforme rappelle directement celle déjà développée pour la combinaison de plusieurs options de traitement du risque au titre d'ISO 31000 et de COSO ERM, développées dans les parcours dédiés de cette plateforme.

## Le lien avec la leçon suivante

Ces approches de déploiement s'appuient directement sur une capacité de segmentation réseau précise, condition indispensable pour isoler effectivement les ressources protégées — la micro-segmentation et le périmètre défini par logiciel, développés à la leçon suivante de ce parcours.
