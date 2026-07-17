# Construire un dossier d'autorisation et une feuille de route réaliste

## Le contenu complet d'un dossier d'autorisation

Au-delà des trois documents centraux déjà présentés au module 1 (SSP, SAR, POA&M), un dossier d'autorisation complet rassemble généralement des documents complémentaires produits au fil des sept étapes du processus :

- le **plan de catégorisation** (étape Categorize), documentant l'analyse FIPS 199 et les types d'information traités,
- le **plan de gestion de la configuration**, décrivant comment les changements apportés au système sont maîtrisés dans la durée (en lien avec la famille de contrôles CM, module 2),
- le **plan de continuité d'activité**, incluant les résultats des tests de reprise réalisés (famille CP),
- le **plan de gestion des risques de la chaîne d'approvisionnement**, propre au système (famille SR, module 5),
- l'**analyse d'impact sur la vie privée (PIA)**, lorsque le système traite des informations personnellement identifiables (module 5),
- la **stratégie de surveillance continue** propre au système, préparée dès l'étape Select et affinée à l'étape Monitor (module 1).

Un dossier d'autorisation qui rassemble une documentation cohérente et à jour de l'ensemble de ces éléments permet à l'Authorizing Official de fonder sa décision sur une vision complète du risque — un dossier incomplet ou dont certains éléments datent d'une version antérieure du système constitue un motif fréquent de report de la décision d'autorisation, voire de refus.

## Outillage : le rôle des systèmes de gestion de la conformité fédérale

Dans la pratique fédérale américaine, la gestion de ce dossier d'autorisation s'appuie généralement sur des plateformes dédiées — le ministère de la Défense utilise par exemple **eMASS (Enterprise Mission Assurance Support Service)** comme système de référence pour suivre l'état des contrôles, le POA&M et le statut d'autorisation de chaque système à travers l'ensemble de l'organisation. Ces plateformes jouent, pour le RMF, un rôle comparable à celui d'une plateforme GRC dédiée qui centraliserait la Déclaration d'Applicabilité et le suivi des non-conformités d'un SMSI ISO 27001, déjà évoqué dans le parcours dédié de cette plateforme — la centralisation outillée devient d'autant plus indispensable que le volume de contrôles à suivre (plus de mille pour SP 800-53) rend une gestion purement documentaire artisanale rapidement intenable à l'échelle d'une grande organisation.

## Une durée de premier processus généralement longue

Pour un système fédéral de complexité moyenne, catégorisé Modéré, le premier cycle complet du RMF — depuis l'étape Prepare jusqu'à l'obtention de l'autorisation d'exploitation — s'étend généralement sur **six à douze mois**, un ordre de grandeur comparable à celui déjà observé pour une première certification ISO 27001 ou un premier programme SOC 2 dans les parcours précédents de cette plateforme, avec une variable supplémentaire propre au RMF : la disponibilité d'un évaluateur indépendant qualifié et la charge de travail de l'Authorizing Official, qui peut être responsable de l'autorisation de plusieurs systèmes simultanément au sein d'une même organisation.

## Les pièges les plus fréquents

- **Sous-estimer l'étape Prepare au niveau organisationnel** — un système qui aborde le processus sans stratégie de gestion des risques organisationnelle déjà établie, ni rôles clairement désignés (module 3), se heurte à des blocages récurrents dès les premières étapes, faute de cadre de décision clair.
- **Une catégorisation de complaisance** — sous-évaluer délibérément l'impact potentiel d'un système (module 1) pour viser une base de référence de contrôles moins exigeante réduit la charge de travail à court terme, mais expose à un refus d'autorisation ou à une réévaluation forcée dès qu'un audit ou un incident révèle l'écart entre la catégorisation déclarée et la réalité du système.
- **Un POA&M qui devient un cimetière** — des faiblesses identifiées lors de l'évaluation, jamais réellement corrigées ni suivies avec des échéances crédibles, un piège déjà signalé pour le registre de non-conformités d'ISO 27001 dans le parcours dédié de cette plateforme, qui s'applique avec la même acuité au POA&M du RMF.
- **Négliger la préparation à la surveillance continue** — traiter l'obtention de l'autorisation initiale comme l'aboutissement du projet, plutôt que comme le point de départ d'un dispositif de surveillance continue (module 1, étape Monitor) qui doit fonctionner dans la durée, exactement le même piège de "projet qui s'arrête à la certification" déjà signalé pour ISO 27001 et SOC 2 dans les parcours précédents.

## Vers l'autorisation continue : une évolution à anticiper dès la conception

Comme développé au module 1, la tendance de fond du RMF va vers l'**autorisation continue**, portée par une surveillance automatisée et une maturité opérationnelle suffisante du système. Une organisation qui conçoit un nouveau système avec cet objectif en tête dès le départ — en investissant dans l'automatisation de la collecte de preuves de conformité, dans une intégration continue intégrant des contrôles de sécurité automatisés, dans une surveillance en temps réel de la posture de sécurité — se donne les moyens de réduire, dans la durée, la charge que représente un cycle de réautorisation périodique traditionnel, en cohérence directe avec les principes Security by Design et DevSecOps développés dans le premier parcours de cette plateforme.

## En clôture de ce parcours

Ce parcours a couvert le NIST RMF de bout en bout : ses origines dans la FISMA et son unification progressive des processus antérieurs, les sept étapes du processus (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor), le catalogue de contrôles SP 800-53 et ses familles les plus structurantes, les rôles nommément désignés qui portent la responsabilité de chaque décision, son application concrète au cloud via FedRAMP, l'intégration de la vie privée et de la gestion des risques de la chaîne d'approvisionnement, et enfin la construction d'un dossier d'autorisation et d'une feuille de route réaliste. Combiné aux cinq autres parcours de cette plateforme — les fondamentaux GRC et Security by Design, le NIST CSF 2.0, ISO 27001 en profondeur, SOC 2 en profondeur, et le RGPD en profondeur — vous disposez désormais d'une compréhension à la fois large et approfondie des principaux référentiels qui structurent une démarche GRC moderne, du cadre le plus volontaire et orienté résultat (NIST CSF) jusqu'au processus le plus prescriptif et formellement responsabilisé (NIST RMF).
