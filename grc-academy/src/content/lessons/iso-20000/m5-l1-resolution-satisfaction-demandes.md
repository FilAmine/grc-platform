# La résolution des incidents et des problèmes, et la satisfaction des demandes

## Trois processus distincts, souvent confondus en pratique

ISO/IEC 20000 distingue trois processus complémentaires mais conceptuellement distincts, dont la confusion constitue l'une des erreurs les plus fréquentes chez les organisations découvrant la gestion des services : la **gestion des incidents**, la **gestion des problèmes**, et la **satisfaction des demandes de service** — chacun reprenant, sous une forme désormais certifiable, une pratique déjà développée en détail dans le parcours ITIL de cette plateforme.

## La gestion des incidents

Un **incident** désigne une interruption non planifiée d'un service ou une dégradation de sa qualité — la gestion des incidents vise à restaurer le service normal **le plus rapidement possible**, en priorisant les incidents selon leur impact et leur urgence, sans nécessairement rechercher, dans l'immédiat, la cause profonde de la défaillance constatée. Cette priorisation par l'impact et l'urgence rappelle directement celle déjà développée pour l'évaluation de la sévérité au titre de COSO ERM, ou pour la priorisation par la gravité déjà rencontrée à de multiples reprises dans cette plateforme, notamment pour la matérialité de SOX ou les échéances différenciées du POA&M de FedRAMP.

## La gestion des problèmes

Un **problème**, à la différence d'un incident, désigne la **cause sous-jacente** d'un ou plusieurs incidents, souvent récurrents — la gestion des problèmes vise à identifier et à traiter cette cause profonde, afin d'éviter la répétition future des incidents qu'elle engendre, plutôt que de se contenter de restaurer le service à chaque occurrence sans jamais en traiter l'origine. Cette distinction entre traitement immédiat de la conséquence (l'incident) et traitement de la cause profonde (le problème) rejoint directement celle déjà développée pour les actions correctives des clauses 10 d'ISO 27001, d'ISO 22301 et d'ISO/IEC 42001, toutes développées dans les parcours dédiés de cette plateforme — un incident résolu sans jamais traiter le problème sous-jacent reviendra presque inévitablement se reproduire.

## La satisfaction des demandes de service

Une **demande de service**, distincte d'un incident et d'un problème, désigne une requête légitime et anticipée d'un utilisateur — une demande d'accès à une nouvelle application, une demande d'information, ou une demande de modification standard préapprouvée. Ce processus rejoint directement la pratique de gestion des demandes de service déjà développée dans le parcours ITIL de cette plateforme, et se distingue nettement de la gestion des incidents par sa nature planifiée et non urgente — traiter une demande d'accès comme un incident, ou inversement traiter un incident critique selon le rythme habituel des demandes de service, engendrerait une gestion des priorités totalement inadaptée à la réalité de chaque situation.

## Un tableau de synthèse des trois processus

| Processus | Nature de la situation | Objectif |
|---|---|---|
| Gestion des incidents | Interruption ou dégradation non planifiée d'un service | Restaurer le service le plus rapidement possible |
| Gestion des problèmes | Cause profonde sous-jacente à un ou plusieurs incidents | Éliminer la cause pour prévenir la répétition future |
| Satisfaction des demandes de service | Requête légitime et anticipée d'un utilisateur | Traiter la demande selon un processus planifié et standardisé |

## Le rôle central du centre de services (service desk)

Ces trois processus convergent typiquement vers un **centre de services** unique, point de contact centralisé pour l'ensemble des utilisateurs, chargé de qualifier chaque sollicitation entrante (s'agit-il d'un incident, d'une demande de service, ou du signalement d'un problème potentiellement récurrent ?) avant de l'orienter vers le processus de traitement approprié. Ce rôle de centre de services rejoint directement celui déjà développé dans le parcours ITIL de cette plateforme parmi les pratiques opérationnelles centrales — un point d'entrée unique qui évite la confusion et la dispersion des sollicitations à travers de multiples canaux non coordonnés.

## Un exemple concret illustrant l'articulation des trois processus

Une panne récurrente d'un serveur applicatif, survenant plusieurs fois par mois, serait ainsi traitée à travers ces trois processus de façon coordonnée : chaque occurrence de la panne fait l'objet d'une résolution rapide au titre de la gestion des incidents (redémarrage du service affecté) ; la récurrence de ces incidents déclenche l'ouverture d'un problème, dont l'investigation révèle une fuite mémoire dans une version logicielle obsolète ; la résolution définitive de ce problème passe par une mise à jour logicielle planifiée, gérée à travers le processus de gestion des changements déjà développé au module 4 de ce parcours — tandis qu'une demande d'accès simultanée d'un nouvel employé à ce même serveur, sans lien avec la panne, suivrait un traitement entièrement distinct au titre de la satisfaction des demandes de service.

## Le lien avec le module suivant

Au-delà de cette réactivité au quotidien, ISO/IEC 20000 impose également des exigences plus larges d'assurance du service — disponibilité, continuité et sécurité de l'information — développées au module suivant de ce parcours.
