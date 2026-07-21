# La migration depuis un modèle périmétrique traditionnel

## Un parcours plutôt qu'une destination, selon les termes mêmes de NIST SP 800-207

NIST SP 800-207 souligne explicitement qu'aucune organisation disposant d'une infrastructure existante ne peut basculer instantanément d'un modèle périmétrique traditionnel vers une architecture Zero Trust intégrale — la migration constitue un **parcours progressif**, s'étendant typiquement sur plusieurs années, plutôt qu'un projet ponctuel avec un aboutissement définitif. Cette reconnaissance explicite d'un cheminement graduel rappelle directement celle déjà développée pour le calendrier échelonné de l'AI Act, ou pour l'entrée en application progressive de PCI DSS et du CSCF de SWIFT CSP, tous développés dans les parcours dédiés de cette plateforme.

## Une coexistence nécessaire entre ancien et nouveau modèle

Pendant la durée de cette migration, une organisation doit nécessairement faire coexister des éléments de son ancien modèle périmétrique avec des composants Zero Trust déjà déployés — une réalité hybride qui exige une attention particulière aux **points de jonction** entre les deux modèles, où une ressource protégée selon les principes Zero Trust interagit avec un système hérité encore fondé sur une confiance implicite liée à sa localisation réseau. Cette coexistence temporaire rappelle directement celle déjà développée pour l'intégration progressive d'ISO/IEC 42001, d'ISO/IEC 27701 ou d'ISO/IEC 20000 au sein d'un système de management intégré construit autour d'une certification ISO 27001 préexistante, développée dans les parcours dédiés de cette plateforme.

## Prioriser les ressources les plus critiques ou les plus exposées

Une migration réaliste commence typiquement par les ressources jugées les plus critiques pour l'organisation, ou les plus directement exposées à un risque élevé — les systèmes traitant les données les plus sensibles, ou les accès les plus fréquemment ciblés par des tentatives d'intrusion. Cette priorisation rejoint directement le principe de priorisation par la gravité et la probabilité déjà rencontré à de multiples reprises dans cette plateforme, notamment pour la matérialité de SOX, la classification des risques d'EBIOS RM, ou l'évaluation de la sévérité au titre de COSO ERM.

## Cartographier les flux de communication existants avant toute migration

Une étape préalable indispensable consiste à cartographier précisément les flux de communication existants entre les utilisateurs, les équipements et les ressources de l'organisation — sans cette cartographie, il devient impossible de concevoir des règles de micro-segmentation pertinentes, développées au module 3 de ce parcours, sans risquer d'interrompre des flux légitimes essentiels au fonctionnement de l'organisation. Cette exigence de cartographie préalable rejoint directement celle déjà développée pour la gestion des actifs et de la configuration dans le parcours ISO/IEC 20000 de cette plateforme, condition indispensable pour évaluer correctement l'impact d'un changement avant sa mise en œuvre.

## Le rôle de l'identité comme point de départ fréquent de la migration

De nombreuses organisations engagent leur migration vers Zero Trust en commençant par renforcer leur gestion des identités et des accès — généraliser l'authentification multifacteur, centraliser la gestion des identités, et affiner progressivement les politiques d'accès — avant de s'attaquer à la micro-segmentation réseau plus complexe et plus coûteuse à mettre en œuvre. Cette séquence progressive, de l'identité vers le réseau, rejoint directement l'observation déjà faite pour le modèle de maturité de la CISA, développé au module 6 de ce parcours, qui identifie l'identité comme l'un des piliers fondateurs d'une architecture Zero Trust mature.

## Un exemple concret d'une feuille de route de migration progressive

Une organisation pourrait ainsi engager sa migration en généralisant d'abord l'authentification multifacteur pour l'ensemble de ses utilisateurs et en centralisant sa gestion des identités, puis en cartographiant ses flux de communication existants pour ses systèmes les plus critiques, avant de déployer une première micro-segmentation limitée à ces systèmes prioritaires selon l'une des approches déjà développées au module 3 de ce parcours, et enfin d'étendre progressivement cette approche à l'ensemble de son infrastructure sur plusieurs années, en traitant en priorité les points de jonction les plus sensibles entre ancien et nouveau modèle.

## Un tableau de synthèse des étapes typiques de migration

| Étape | Ce qu'elle accomplit |
|---|---|
| Renforcement de la gestion des identités | Authentification multifacteur généralisée, centralisation des identités |
| Cartographie des flux existants | Une base indispensable pour concevoir une micro-segmentation pertinente |
| Priorisation des ressources critiques | Un déploiement initial concentré sur les systèmes les plus sensibles |
| Extension progressive | Une généralisation sur plusieurs années, en gérant la coexistence hybride |

## Le lien avec le module suivant

Cette architecture, aussi rigoureuse soit-elle une fois pleinement déployée, n'est jamais elle-même à l'abri de menaces spécifiques qui la ciblent directement — développées au module suivant de ce parcours.
