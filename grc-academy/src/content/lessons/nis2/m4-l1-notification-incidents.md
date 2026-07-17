# La notification des incidents (article 23)

## Un processus en plusieurs étapes, plus détaillé que le simple délai unique du RGPD

Le parcours RGPD de cette plateforme a développé en détail la règle des 72 heures pour la notification d'une violation de données. L'article 23 de NIS2 organise un processus de notification **plus élaboré**, structuré en plusieurs étapes successives, pour les **incidents significatifs** affectant la fourniture des services des entités essentielles et importantes.

## Qu'est-ce qu'un "incident significatif"

L'article 23.3 définit un incident comme significatif s'il remplit au moins l'un des deux critères suivants :

- il a causé ou est susceptible de causer une **perturbation opérationnelle grave des services** ou des **pertes financières** pour l'entité concernée,
- il a affecté ou est susceptible d'affecter **d'autres personnes physiques ou morales** en causant des dommages matériels ou immatériels considérables.

Cette définition, volontairement large et fondée sur l'impact réel plutôt que sur une liste fermée de types d'événements, rappelle directement la définition d'une violation de données à caractère personnel du RGPD (article 4.12) développée dans le parcours dédié de cette plateforme — avec cette différence que le seuil de significativité de NIS2 s'apprécie du point de vue de la continuité et de l'intégrité du service fourni, plutôt que du seul point de vue de la protection des données personnelles.

## Les trois étapes de la notification

### L'alerte précoce (early warning) — dans les 24 heures

Dès que l'entité a connaissance d'un incident significatif, elle doit adresser, sans retard injustifié et **au plus tard dans les 24 heures**, une alerte précoce à son CSIRT (Computer Security Incident Response Team) ou à son autorité compétente, indiquant notamment si l'incident est présumé résulter d'actes illicites ou malveillants, et s'il est susceptible d'avoir un impact transfrontière. Ce délai de 24 heures, plus court que celui du RGPD, reflète l'urgence particulière attachée à des incidents pouvant affecter la continuité de services considérés comme critiques pour la société.

### La notification de l'incident — dans les 72 heures

Dans un délai de **72 heures** après avoir eu connaissance de l'incident significatif, l'entité doit transmettre une notification de l'incident, qui met à jour, le cas échéant, les informations de l'alerte précoce et fournit une première évaluation de l'incident, y compris sa gravité et son impact, ainsi que les indicateurs de compromission disponibles — ce deuxième palier de 72 heures rejoint, dans son délai, celui déjà rencontré pour la notification d'une violation de données à une autorité de contrôle sous le RGPD, développée dans le parcours dédié de cette plateforme, bien que les deux obligations restent juridiquement distinctes et puissent se déclencher simultanément pour un même incident affectant à la fois la continuité de service et des données personnelles.

### Le rapport final — dans un délai d'un mois

Au plus tard **un mois** après la transmission de la notification de l'incident, l'entité doit soumettre un rapport final, comprenant une description détaillée de l'incident (sa gravité et son impact), le type de menace ou de cause profonde ayant probablement déclenché l'incident, les mesures d'atténuation appliquées et en cours, et, le cas échéant, l'impact transfrontière de l'incident. Si l'incident est toujours en cours à cette échéance, l'entité doit alors fournir un **rapport intermédiaire** à la place, suivi d'un rapport final dans un délai d'un mois après le traitement de l'incident.

## Un mécanisme d'information réciproque : le CSIRT ou l'autorité peut répondre

L'article 23 prévoit également que le CSIRT ou l'autorité compétente destinataire fournisse, sans retard indu, une réponse à l'entité notifiante, incluant des retours initiaux sur l'incident significatif et, sur demande de l'entité, des conseils sur la mise en œuvre de mesures d'atténuation possibles — un mécanisme de coopération bidirectionnelle qui va au-delà d'une simple obligation déclarative à sens unique, et qui recoupe la mission de conseil et d'appui déjà rencontrée pour les CSIRT nationaux dans l'écosystème de coopération développé au module 6 de ce parcours.

## La notification aux destinataires des services, dans certains cas

Lorsqu'un incident significatif est susceptible d'affecter la fourniture de son service, l'entité doit également, sans retard indu, **informer les destinataires de ses services** de l'incident lui-même et, le cas échéant, des mesures ou des actions correctives que ces destinataires peuvent eux-mêmes prendre en réponse à la menace — un parallèle direct avec la notification aux personnes concernées de l'article 34 du RGPD (développée dans le parcours dédié de cette plateforme), mais appliquée ici à l'ensemble des destinataires d'un service, pas seulement aux personnes physiques dont les données seraient affectées.

## Comment cette procédure recoupe la gestion des incidents déjà étudiée dans cette plateforme

Ce processus en plusieurs étapes rejoint, dans son principe général, la logique déjà rencontrée pour la fonction Respond du NIST CSF, les contrôles 5.24-5.28 de l'Annexe A d'ISO 27001, et le contrôle 17 des CIS Controls, tous développés dans les parcours précédents de cette plateforme — avec cette spécificité propre à NIS2 : un calendrier de notification à plusieurs paliers (24h, 72h, un mois) explicitement fixé par la loi, plutôt qu'un simple principe général de notification "dans les meilleurs délais" laissé à l'appréciation de chaque organisation.
