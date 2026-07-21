# L'architecture logique (1/2) : Policy Engine, Policy Administrator, Policy Enforcement Point

## Trois composants logiques, jamais nécessairement trois produits distincts

NIST SP 800-207 décrit l'architecture Zero Trust à travers trois composants logiques qui orchestrent ensemble chaque décision d'accès — une distinction **logique** plutôt que nécessairement physique : ces trois composants peuvent être implémentés par un unique produit commercial intégré, ou par plusieurs systèmes distincts interconnectés, selon le contexte technique de l'organisation. Cette distinction entre architecture logique et implémentation technique concrète rappelle directement celle déjà développée pour la distinction entre gouvernance et management dans le parcours COBIT de cette plateforme.

## Le Policy Engine (PE) : le cerveau décisionnel

Le **Policy Engine** constitue le composant central chargé de décider, pour chaque demande d'accès à une ressource, si celle-ci doit être accordée, refusée, ou révoquée si elle avait déjà été accordée — une décision qui s'appuie sur un **algorithme de confiance**, développé en détail à la leçon suivante de ce parcours, alimenté par de multiples sources d'information. Ce rôle décisionnel central rappelle directement celui déjà développé pour le Policy Decision Point de nombreuses architectures de contrôle d'accès classiques, mais NIST SP 800-207 en formalise ici précisément les sources de données et la logique d'évaluation.

## Le Policy Administrator (PA) : l'exécutant des décisions

Le **Policy Administrator** reçoit les décisions du Policy Engine et les traduit en actions concrètes — établir ou interrompre le chemin de communication entre le demandeur et la ressource, générer les identifiants ou jetons d'authentification propres à la session accordée. Le Policy Administrator ne prend ainsi jamais lui-même de décision d'accès de façon autonome : il exécute fidèlement les décisions du Policy Engine, une séparation des rôles entre décision et exécution qui rappelle directement celle déjà développée pour la séparation des tâches dans le parcours SOX de cette plateforme, ou pour la distinction entre gouvernance et exécution opérationnelle à travers de nombreux référentiels déjà étudiés.

## Le Policy Enforcement Point (PEP) : la porte d'accès effective

Le **Policy Enforcement Point** constitue le point de contrôle effectif à travers lequel transite toute communication entre le demandeur et la ressource protégée — il active, surveille et peut interrompre à tout moment la connexion, conformément aux instructions reçues du Policy Administrator. NIST SP 800-207 précise que ce composant logique peut lui-même se décomposer en deux éléments distincts, l'un du côté du demandeur (par exemple, un agent installé sur son équipement) et l'autre du côté de la ressource protégée (par exemple, une passerelle placée en amont du serveur hébergeant la ressource) — une architecture à deux points de contrôle qui rappelle celle déjà développée pour la segmentation réseau isolant l'environnement SWIFT dans le parcours CSCF de SWIFT CSP, développé dans le parcours dédié de cette plateforme.

## La séparation entre plan de contrôle et plan de données

Cette architecture à trois composants illustre une distinction fondamentale entre le **plan de contrôle**, où le Policy Engine et le Policy Administrator décident et orchestrent les accès, et le **plan de données**, où le Policy Enforcement Point fait effectivement transiter les communications autorisées — une séparation qui garantit que la logique décisionnelle la plus sensible (le Policy Engine) reste isolée des flux de données eux-mêmes, réduisant la surface d'attaque directement exposée à un éventuel intercepteur malveillant.

## Un exemple concret illustrant l'interaction des trois composants

Un employé souhaitant accéder à une application métier sensible depuis son ordinateur portable verrait sa demande initialement interceptée par le Policy Enforcement Point du côté du demandeur, transmise pour décision au Policy Engine (qui évalue le contexte : l'employé est-il correctement authentifié, son équipement présente-t-il une posture de sécurité satisfaisante, l'heure et la localisation de la demande sont-elles cohérentes avec son comportement habituel ?), puis, en cas de décision favorable, le Policy Administrator établirait le chemin de communication autorisé et générerait les identifiants de session propres à cet accès précis, avant que le Policy Enforcement Point du côté de la ressource ne laisse effectivement transiter la communication.

## Un tableau de synthèse des trois composants

| Composant | Rôle | Plan concerné |
|---|---|---|
| Policy Engine (PE) | Décide d'accorder, refuser ou révoquer l'accès | Plan de contrôle |
| Policy Administrator (PA) | Exécute la décision, établit ou interrompt la communication | Plan de contrôle |
| Policy Enforcement Point (PEP) | Point de contrôle effectif du transit des communications | Plan de données |

## Un exemple concret : à quoi ces trois composants correspondent chez AWS et Microsoft Azure

Ces composants logiques restent abstraits tant qu'ils ne sont pas rattachés à des services réellement disponibles chez les grands fournisseurs cloud. Chez **Microsoft Azure**, **Microsoft Entra ID** (anciennement Azure AD) joue directement le rôle de Policy Engine et de Policy Administrator à travers sa fonctionnalité de **Conditional Access** : pour chaque tentative de connexion, un moteur de décision évalue en temps réel des signaux tels que la conformité de l'équipement (via Intune), le niveau de risque du compte (via Entra ID Protection) et la localisation de la connexion, puis autorise, bloque, ou exige une authentification multifacteur supplémentaire — la décision étant ensuite appliquée par les applications et services Azure eux-mêmes, qui jouent le rôle de Policy Enforcement Point.

Chez **AWS**, **AWS Verified Access** (disponible depuis 2023) applique une logique directement comparable : chaque requête vers une application interne est évaluée en continu par un moteur de politiques s'appuyant sur des signaux provenant d'AWS IAM Identity Center pour l'identité et d'outils de gestion d'appareils tiers pour la posture de sécurité de l'équipement, sans jamais exposer l'application elle-même sur un réseau accessible sans cette vérification préalable — une implémentation concrète du principe d'invisibilité par défaut déjà développé au module 3 de ce parcours à travers le périmètre défini par logiciel. Dans les deux cas, aucune confiance n'est jamais accordée du seul fait qu'une requête provient d'un réseau d'entreprise ou d'un VPN déjà établi, conformément au deuxième principe fondamental développé au module 1 de ce parcours.

## Le lien avec la leçon suivante

La décision prise par le Policy Engine s'appuie sur un algorithme de confiance précis, alimenté par de multiples sources d'information — développé en détail à la leçon suivante de ce parcours.
