# Le catalogue NIST SP 800-171 (2/2) : un exemple concret et les pratiques renforcées de SP 800-172

## Un exemple concret d'application à travers plusieurs familles de contrôles

Pour illustrer concrètement comment un contractant de la défense traduit le catalogue SP 800-171 en pratique opérationnelle, considérons une PME sous-traitante fabriquant des composants pour un programme d'aviation militaire, recevant des spécifications techniques classées comme informations non classifiées contrôlées. Cette entreprise devrait, au titre de la famille contrôle d'accès, mettre en œuvre une authentification multifacteur pour tout accès aux systèmes hébergeant ces spécifications ; au titre de la famille protection des supports, chiffrer les supports amovibles contenant ces données et en tracer précisément la circulation ; au titre de la famille réponse aux incidents, disposer d'une procédure documentée de détection et de signalement de tout incident affectant ces informations, développée plus en détail au module 6 de ce parcours ; et au titre de la famille évaluation des risques, conduire une appréciation périodique des risques pesant sur les systèmes hébergeant ces spécifications, selon une méthodologie qui peut directement s'appuyer sur le processus générique déjà développé dans le parcours ISO 31000 de cette plateforme.

## Pourquoi cet exemple illustre la nature interconnectée du catalogue

Cet exemple révèle un principe déjà rencontré à de multiples reprises dans cette plateforme, notamment pour le CSCF de SWIFT CSP ou l'Annexe A d'ISO 27001 : les quatorze familles de SP 800-171 ne fonctionnent jamais isolément les unes des autres — une authentification robuste (contrôle d'accès) reste insuffisante sans une détection effective des tentatives d'accès anormales (audit et responsabilisation), elle-même insuffisante sans une capacité de réponse rapide en cas d'incident avéré (réponse aux incidents). Un contractant qui implémenterait une seule famille de contrôles de façon exemplaire, en négligeant les autres, resterait exposé à des risques que le catalogue, pris dans son ensemble, cherche précisément à couvrir de façon cohérente.

## Les pratiques renforcées de SP 800-172, socle du niveau 3

Au-delà des 110 exigences de base de SP 800-171, la norme complémentaire **SP 800-172** ajoute des pratiques renforcées, réservées au niveau 3 de CMMC déjà développé au module 1 de ce parcours — des exigences avancées de détection des menaces persistantes sophistiquées (advanced persistent threats), de leurre et de déception technique pour ralentir un attaquant déjà infiltré, de durcissement renforcé de la configuration des systèmes, et de résilience accrue face à des adversaires disposant de capacités de niveau étatique. Ces pratiques renforcées répondent directement à un profil de menace distinct de celui visé par le socle de SP 800-171 — non plus la cybercriminalité opportuniste ou les tentatives d'intrusion classiques, mais des acteurs étatiques hautement sophistiqués et déterminés, ciblant spécifiquement les programmes de défense les plus stratégiques.

## Pourquoi ce niveau de sophistication supplémentaire se justifie

Cette gradation supplémentaire pour le niveau 3 rappelle directement celle déjà développée pour le niveau d'impact Élevé de FedRAMP, réservé aux systèmes traitant les données les plus sensibles avec les exigences de contrôle les plus strictes — un principe déjà établi à travers cette plateforme : plus l'enjeu stratégique et la sophistication de la menace ciblant une information sont élevés, plus le catalogue de contrôles applicable doit intégrer des pratiques spécifiquement conçues pour ce profil de menace, plutôt que de se contenter d'une application plus rigoureuse d'un socle générique.

## Un tableau de synthèse illustrant la progression entre les deux catalogues

| Catalogue | Niveau CMMC correspondant | Profil de menace visé |
|---|---|---|
| SP 800-171 (110 exigences) | Niveau 2 — Advanced | Cybercriminalité, intrusions opportunistes ou ciblées classiques |
| SP 800-171 + SP 800-172 | Niveau 3 — Expert | Menaces persistantes sophistiquées, acteurs de niveau étatique |

## Le lien avec le module suivant

Ce catalogue, une fois implémenté, doit encore être vérifié selon une méthode d'évaluation appropriée au niveau de certification visé — les voies d'évaluation de CMMC, développées en détail au module suivant de ce parcours.
