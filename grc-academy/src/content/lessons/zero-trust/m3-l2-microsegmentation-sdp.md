# Les approches de déploiement (2/2) : micro-segmentation et périmètre défini par logiciel

## Pourquoi la segmentation réseau traditionnelle ne suffit jamais à elle seule

La segmentation réseau traditionnelle, déjà développée à travers plusieurs référentiels de cette plateforme — notamment pour l'Objectif 1 du CSCF de SWIFT CSP ou la réduction de périmètre de PCI DSS —, divise généralement un réseau en quelques grandes zones (réseau interne, zone démilitarisée, réseau externe). L'architecture Zero Trust pousse cette logique beaucoup plus loin à travers la **micro-segmentation** — diviser le réseau en zones beaucoup plus fines, potentiellement jusqu'au niveau d'une charge de travail individuelle, plutôt que de quelques grandes zones seulement.

## La micro-segmentation comme application directe des principes fondamentaux

Cette granularité extrême de segmentation constitue une traduction directe du premier principe déjà développé au module 1 de ce parcours — puisque toutes les ressources méritent une protection équivalente indépendamment de leur localisation, la segmentation ne peut jamais se limiter à distinguer un réseau interne globalement fiable d'un réseau externe hostile, mais doit isoler chaque ressource ou groupe restreint de ressources les unes des autres, y compris au sein même du réseau interne traditionnellement considéré comme fiable.

## Un exemple concret illustrant l'intérêt de cette granularité

Dans une architecture micro-segmentée, la compromission d'un poste de travail au sein du réseau interne ne permettrait jamais à un attaquant de se déplacer librement (mouvement latéral) vers l'ensemble des autres ressources du réseau, contrairement au modèle périmétrique traditionnel où la confiance implicite accordée au réseau interne facilite justement ce type de propagation — chaque tentative d'accès depuis le poste compromis vers une autre ressource ferait l'objet d'une nouvelle évaluation par le Policy Engine, développé au module 2 de ce parcours, limitant ainsi drastiquement l'ampleur potentielle d'un incident initial.

## Le périmètre défini par logiciel (Software-Defined Perimeter — SDP)

Le **périmètre défini par logiciel** constitue une technologie souvent associée au déploiement d'une architecture Zero Trust — plutôt que d'exposer des ressources sur un réseau où leur existence même est visible avant toute authentification, le SDP rend les ressources protégées **invisibles** par défaut, ne révélant leur existence et n'autorisant une connexion qu'après une authentification et une autorisation préalables réussies. Ce principe d'invisibilité par défaut avant authentification rappelle directement celui déjà développé pour les pratiques interdites de l'article 5 de l'AI Act, où certaines capacités ne doivent jamais être rendues accessibles sans un contrôle préalable strict, bien qu'appliqué ici à un contexte de connectivité réseau plutôt qu'à un usage d'intelligence artificielle.

## Comment ces deux techniques se combinent concrètement

Une micro-segmentation rigoureuse combinée à un périmètre défini par logiciel produit une architecture où chaque ressource demeure isolée et invisible jusqu'à ce qu'un demandeur légitime, correctement authentifié et autorisé par le Policy Engine, obtienne un accès strictement limité à cette ressource précise — une combinaison qui rappelle directement le principe de moindre privilège déjà développé à de multiples reprises dans cette plateforme, ici appliqué non seulement aux droits d'un utilisateur au sein d'un système, mais à la visibilité même de l'existence des ressources sur le réseau.

## Les défis pratiques de cette granularité extrême

Cette granularité de segmentation, aussi rigoureuse soit-elle sur le plan théorique, engendre des défis opérationnels réels — la gestion d'un nombre considérable de règles de segmentation fines exige des outils d'automatisation sophistiqués, sous peine de devenir rapidement ingérable manuellement ; et une segmentation excessivement rigide peut entraver la collaboration légitime entre équipes si elle n'est pas conçue avec suffisamment de souplesse contextuelle. Ce défi rappelle directement celui déjà signalé pour l'équilibre entre le coût du traitement et le bénéfice attendu au titre d'ISO 31000, développé dans le parcours dédié de cette plateforme — une segmentation disproportionnée par rapport au risque réel constitue un coût opérationnel évitable.

## Un tableau de synthèse

| Technique | Principe | Bénéfice principal |
|---|---|---|
| Micro-segmentation | Isolation fine, potentiellement jusqu'à la charge de travail individuelle | Limitation drastique du mouvement latéral en cas de compromission |
| Périmètre défini par logiciel (SDP) | Invisibilité des ressources avant authentification réussie | Réduction de la surface d'attaque directement exposée |

## Le lien avec le module suivant

Ces techniques de déploiement ne peuvent jamais être adoptées du jour au lendemain par une organisation disposant d'une infrastructure existante fondée sur un modèle périmétrique traditionnel — la migration progressive vers une architecture Zero Trust, développée au module suivant de ce parcours.
