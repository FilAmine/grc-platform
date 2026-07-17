# La vie privée dans le RMF

## Une intégration tardive mais désormais structurelle

Historiquement, la protection de la vie privée n'occupait qu'une place secondaire dans les premières versions du RMF, largement centrées sur la sécurité de l'information au sens classique (confidentialité, intégrité, disponibilité). La révision Rev. 2 de SP 800-37 (2018) et la révision Rev. 5 de SP 800-53 (2020) ont profondément intégré la vie privée comme une dimension à part entière du processus, au même niveau que la sécurité — une évolution qui reflète, avec un vocabulaire distinct, la même prise de conscience déjà rencontrée dans le module Privacy by Design du premier parcours de cette plateforme et dans le parcours RGPD dédié.

## Le Senior Agency Official for Privacy (SAOP)

Chaque agence fédérale désigne un **Senior Agency Official for Privacy**, dont le rôle est directement comparable, dans son esprit, au Délégué à la Protection des Données (DPO) du RGPD développé dans le parcours dédié de cette plateforme : superviser les risques de vie privée à l'échelle de l'organisation, être consulté sur les traitements de données personnelles significatifs, et rendre compte à la direction de l'agence. Le SAOP est impliqué dès l'étape Prepare du RMF (module 1) pour la définition de la stratégie de gestion des risques de vie privée au niveau organisationnel.

## La famille de contrôles PT (PII Processing and Transparency)

Ajoutée dans SP 800-53 Rev. 5 (module 2), la famille **PT** regroupe les contrôles spécifiquement dédiés au traitement des informations personnellement identifiables (Personally Identifiable Information — PII) et à la transparence de ce traitement :

- **PT-1** — établissement d'une politique et de procédures de traitement des PII,
- **PT-2** — autorité de traitement des PII, exigeant de documenter la base légale ou réglementaire qui autorise chaque traitement — un parallèle direct avec les bases légales de l'article 6 du RGPD, développées en détail dans le parcours dédié de cette plateforme, bien que dans un contexte juridique américain distinct,
- **PT-3** — limitation des finalités du traitement des PII — l'équivalent direct du principe de limitation des finalités du RGPD,
- **PT-5** — notification de confidentialité (privacy notice), l'équivalent du droit à l'information du RGPD,
- **PT-6** — gestion du consentement au traitement des PII,
- **PT-7** — minimisation spécifique aux PII collectées — un rappel direct du principe de minimisation déjà développé dans le module Privacy by Design du premier parcours de cette plateforme.

## L'analyse d'impact sur la vie privée (Privacy Impact Assessment — PIA)

Le RMF intègre une évaluation d'impact sur la vie privée, la **Privacy Impact Assessment (PIA)**, exigée par l'E-Government Act de 2002 pour tout système fédéral traitant des informations personnellement identifiables. Sa logique est directement comparable à celle de l'analyse d'impact relative à la protection des données (AIPD/DPIA) du RGPD, développée en détail dans le parcours dédié de cette plateforme : documenter systématiquement quelles données personnelles sont collectées, pourquoi, comment elles sont protégées, et quels risques résiduels pèsent sur les personnes concernées — avec cette différence de contexte que la PIA s'inscrit dans le cadre légal américain (E-Government Act, Privacy Act de 1974) plutôt que dans le RGPD, et s'articule avec le processus RMF plutôt qu'être un exercice juridique autonome.

## Un exemple d'intégration entre catégorisation de sécurité et risque de vie privée

Un système de gestion des demandes de prestations sociales illustre bien cette intégration : sa catégorisation de sécurité (FIPS 199, module 1) évalue l'impact d'une atteinte à la confidentialité, l'intégrité et la disponibilité du système — mais l'évaluation du risque de vie privée, distincte et complémentaire, s'attache spécifiquement à l'impact sur les **personnes concernées** elles-mêmes en cas de traitement inapproprié de leurs données (un parallèle direct avec la distinction déjà soulignée pour la DPIA du RGPD, qui évalue le risque pour la personne et non pour l'organisation). Ces deux évaluations, bien que distinctes dans leur objet, s'articulent au sein d'un même processus RMF, avec le SAOP et l'Authorizing Official collaborant sur la décision finale d'autorisation lorsque des risques de vie privée significatifs sont identifiés.

## Ce que cette intégration révèle sur la convergence des référentiels

L'intégration de la vie privée comme dimension à part entière du RMF, avec ses propres rôles (SAOP), sa propre famille de contrôles (PT), et sa propre évaluation d'impact (PIA), suit une trajectoire remarquablement similaire à celle observée pour Privacy by Design et le RGPD dans les parcours précédents de cette plateforme — la sécurité de l'information et la protection de la vie privée, longtemps traitées comme des sujets disjoints portés par des équipes différentes, convergent aujourd'hui systématiquement vers un même processus intégré, quel que soit le référentiel considéré.
