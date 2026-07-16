# Les fonctions Respond et Recover : contenir et rebondir

## Respond : agir une fois l'incident détecté

Respond couvre les actions prises concernant un incident de cybersécurité détecté. En CSF 2.0, cette fonction a été simplifiée en trois catégories, contre cinq auparavant.

### RS.MA — Gestion des incidents (Incident Management)

Les activités de réponse sont exécutées en cohérence avec le plan de réponse aux incidents, une fois qu'un incident est déclaré. Cela suppose qu'un tel plan existe, qu'il ait été testé (exercices de simulation — tabletop exercises), et que les rôles de chacun pendant un incident réel soient clairs, plutôt que découverts sous pression le jour même.

### RS.AN — Analyse (Analysis)

Une analyse est menée pour assurer une réponse efficace et pour appuyer les activités de récupération, y compris l'analyse forensique lorsque nécessaire pour comprendre la cause racine, l'étendue de la compromission et les données potentiellement affectées — une information indispensable, entre autres, pour déterminer si une notification réglementaire est requise (par exemple sous le RGPD, en cas de violation de données personnelles).

### RS.CO — Communication (Response Communication)

Les activités de réponse sont coordonnées avec les parties prenantes internes et externes, y compris :

- Communication interne (direction, équipes concernées).
- Communication réglementaire lorsqu'exigée (délai légal de notification, comme les 72 heures du RGPD).
- Communication vers les clients ou le public si nécessaire, gérée pour limiter l'impact réputationnel sans pour autant compromettre l'exactitude des informations communiquées.

## Recover : restaurer les capacités affectées

Recover couvre la restauration des actifs et des opérations affectés par un incident de cybersécurité, réduite en 2.0 à deux catégories.

### RC.RP — Exécution du plan de récupération (Incident Recovery Plan Execution)

Les activités de restauration sont exécutées en cohérence avec le plan de récupération, avec une priorisation claire (quels systèmes restaurer en premier, selon leur criticité métier) et une vérification que les systèmes restaurés ne réintroduisent pas la vulnérabilité qui a permis l'incident initial — un piège classique : restaurer une sauvegarde compromise ou remettre en production un système sans avoir corrigé la faille exploitée.

### RC.CO — Communication de récupération (Recovery Communication)

Les activités de restauration sont coordonnées avec les parties internes et externes, y compris la communication sur le rétablissement des services, et le partage des enseignements tirés une fois l'incident clos.

## Pourquoi Respond et Recover sont traités ensemble dans cette leçon

Bien qu'il s'agisse de deux fonctions distinctes dans le Core, elles forment un continuum opérationnel très lié dans la pratique : la frontière entre "répondre à un incident en cours" et "restaurer les capacités affectées" est souvent progressive plutôt que binaire (un système peut être partiellement restauré pendant que l'analyse forensique de l'incident se poursuit encore sur d'autres composants).

## La boucle vers Govern : l'étape la plus souvent négligée

Le CSF insiste, via la catégorie GV.OV (supervision) vue précédemment, sur le fait que les enseignements tirés d'un incident (Respond/Recover) doivent remonter formellement vers la gouvernance — pas seulement vers un compte-rendu technique archivé. Concrètement : un incident révélant qu'un risque avait été mal évalué (probabilité sous-estimée, impact plus large que prévu) devrait déclencher une révision explicite de la stratégie de gestion des risques en GV.RM, pas seulement une correction technique ponctuelle sur le système affecté. C'est cette boucle de rétroaction — du terrain vers la stratégie — qui distingue une organisation qui *apprend réellement* de ses incidents d'une organisation qui se contente de les "fermer" administrativement.
