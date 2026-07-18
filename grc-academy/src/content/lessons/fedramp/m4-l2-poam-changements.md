# La surveillance continue (2/2) : le POA&M et les changements significatifs

## Le Plan of Action and Milestones, document vivant de la conformité FedRAMP

Le **Plan of Action and Milestones (POA&M)** recense chaque faiblesse identifiée — que ce soit lors de l'évaluation initiale par le 3PAO, d'un scan de vulnérabilités mensuel, ou de toute autre activité de surveillance continue —, avec pour chacune une description du risque résiduel, un plan de remédiation, un responsable désigné et une échéance cible. Ce document n'est jamais figé : il évolue en continu au rythme des trois livrables mensuels déjà développés à la leçon précédente, et son examen régulier constitue l'un des principaux points d'attention de l'agence sponsor ou du FedRAMP Board dans le maintien de la confiance accordée au CSP autorisé.

## Des échéances de remédiation différenciées par niveau de gravité

FedRAMP impose des échéances de remédiation cibles différenciées selon la gravité de la faiblesse identifiée, généralement classée selon une échelle Élevée/Modérée/Faible directement héritée de la terminologie du Common Vulnerability Scoring System (CVSS) : les faiblesses de gravité Élevée doivent typiquement être corrigées dans un délai de 30 jours, celles de gravité Modérée dans un délai de 90 jours, et celles de gravité Faible dans un délai de 180 jours. Cette logique de priorisation par la gravité et de délai différencié rappelle directement celle déjà développée pour la classification des déficiences de contrôle interne dans le parcours SOX de cette plateforme (déficience, déficience significative, faiblesse matérielle), bien qu'appliquée ici à des vulnérabilités techniques plutôt qu'à des déficiences de contrôle interne financier.

## Que se passe-t-il en cas de dépassement d'échéance

Un dépassement répété ou non justifié des échéances de remédiation fixées dans le POA&M peut conduire l'agence sponsor ou le FedRAMP Board à réévaluer la confiance accordée au CSP, voire, dans les cas les plus graves ou répétés, à suspendre ou révoquer l'autorisation — une conséquence potentiellement lourde qui rappelle, dans son principe de sanction graduée fondée sur le comportement réel plutôt que sur le seul constat initial, celle déjà développée pour les sanctions PCI DSS pouvant aller jusqu'à la révocation du droit d'accepter les paiements, dans le parcours dédié de cette plateforme.

## Les Significant Change Requests (SCR)

Au-delà de la remédiation des faiblesses, tout CSP autorisé doit notifier à l'avance toute **modification substantielle** de son environnement technique via une **Significant Change Request** — l'ajout d'un nouveau composant d'infrastructure critique, un changement de sous-traitant impliqué dans l'hébergement, une modification de l'architecture réseau, ou l'ajout d'une nouvelle région géographique d'hébergement en constituent des exemples typiques. L'agence sponsor ou le FedRAMP Board examine la SCR avant sa mise en œuvre effective, et peut exiger une évaluation complémentaire du 3PAO si l'ampleur du changement le justifie — un mécanisme qui rappelle directement la gestion des changements significatifs déjà développée dans le parcours ITIL de cette plateforme (la pratique de facilitation des changements et le rôle du Change Advisory Board), ici appliquée spécifiquement au maintien de la validité d'une autorisation de sécurité plutôt qu'à la stabilité opérationnelle générale des services.

## Pourquoi ce mécanisme évite l'obsolescence silencieuse de l'autorisation

Sans un mécanisme de notification préalable des changements significatifs, une autorisation FedRAMP obtenue à un instant donné pourrait progressivement ne plus refléter la réalité de l'environnement technique effectivement exploité par le CSP, à mesure que celui-ci fait évoluer son architecture pour des raisons commerciales ou techniques sans lien avec la conformité — un piège d'obsolescence silencieuse de la documentation de sécurité déjà signalé à plusieurs reprises dans cette plateforme, notamment pour la nécessité d'actualiser le périmètre d'évaluation SOX d'une année sur l'autre, développée dans le parcours dédié.

## Un tableau de synthèse des délais de remédiation typiques

| Gravité de la faiblesse | Délai de remédiation cible | Comparaison avec un référentiel déjà étudié |
|---|---|---|
| Élevée | 30 jours | Comparable en urgence à une faiblesse matérielle SOX exigeant une action immédiate |
| Modérée | 90 jours | Comparable à une déficience significative SOX |
| Faible | 180 jours | Comparable à une déficience simple SOX, sans urgence immédiate |

## Le lien avec la suite de ce parcours

Ce dispositif de surveillance continue, aussi exigeant soit-il, constitue précisément la contrepartie qui permet au principe de réciprocité — développé à la leçon suivante à travers le FedRAMP Marketplace — de fonctionner en confiance : une agence qui adopte l'ATO d'un CSP déjà autorisé par une autre agence s'appuie non seulement sur l'évaluation initiale, mais également sur la garantie que ce dispositif de surveillance mensuelle continue de s'appliquer dans la durée.
