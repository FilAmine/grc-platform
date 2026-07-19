# Le catalogue NIST SP 800-171 (1/2) : structure et quatorze familles

## Un catalogue conçu spécifiquement pour les systèmes non fédéraux

Le parcours NIST RMF de cette plateforme a déjà développé en détail le catalogue **SP 800-53**, applicable aux systèmes d'information des agences fédérales américaines elles-mêmes. **SP 800-171**, socle technique du niveau 2 de CMMC développé au module 1 de ce parcours, répond à un besoin distinct : protéger les informations non classifiées contrôlées lorsqu'elles sont traitées par des **organisations non fédérales** — les contractants de la base industrielle de défense, qui ne sont jamais directement soumis au RMF applicable aux agences elles-mêmes, mais qui manipulent néanmoins des informations sensibles pour leur compte.

## Une dérivation directe de SP 800-53, adaptée au contexte non fédéral

SP 800-171 n'a jamais été conçu de façon entièrement indépendante : il constitue un **sous-ensemble adapté** des contrôles de sécurité et de vie privée modérés de SP 800-53, déjà développé dans le parcours NIST RMF de cette plateforme, épuré des exigences propres à la gouvernance fédérale elle-même (accréditation gouvernementale, rôles administratifs fédéraux) pour ne conserver que les exigences directement pertinentes pour la protection technique et organisationnelle des informations chez un contractant privé. Cette relation de dérivation rappelle directement celle déjà développée entre ISO 27002 et ISO 27001, ou entre le CSCF de SWIFT CSP et les référentiels de sécurité généralistes, toutes deux développées dans les parcours dédiés de cette plateforme — un principe de réutilisation d'un socle existant plutôt que de construction d'un catalogue entièrement nouveau.

## Les quatorze familles de contrôles

SP 800-171 organise ses 110 exigences en quatorze familles, largement comparables dans leur intitulé aux familles de contrôles de SP 800-53 déjà développées dans le parcours NIST RMF de cette plateforme : contrôle d'accès, sensibilisation et formation, audit et responsabilisation, gestion de la configuration, identification et authentification, réponse aux incidents, maintenance, protection des supports, sécurité du personnel, protection physique, évaluation des risques, évaluation de la sécurité, protection des systèmes et des communications, et intégrité des systèmes et de l'information.

## Un exemple concret d'exigence, pour illustrer le niveau de détail du catalogue

Une exigence typique de la famille contrôle d'accès impose de limiter l'accès aux systèmes d'information aux seuls types de transactions et fonctions que les utilisateurs autorisés sont habilités à exécuter — une exigence qui rejoint directement le principe du moindre privilège déjà développé à de multiples reprises dans cette plateforme, notamment pour l'Objectif 2 du CSCF de SWIFT CSP ou pour la séparation des tâches du parcours SOX. Une exigence typique de la famille protection des systèmes et des communications impose de surveiller, contrôler et protéger les communications aux frontières externes et aux frontières internes clés des systèmes d'information — une exigence qui rejoint directement la segmentation réseau déjà développée pour l'Objectif 1 du CSCF de SWIFT CSP ou pour la réduction de périmètre de PCI DSS.

## Pourquoi ce catalogue reste plus resserré que SP 800-53

Bien que dérivé de SP 800-53, SP 800-171 reste sensiblement plus resserré — 110 exigences contre plus d'un millier de contrôles potentiels dans le catalogue complet de SP 800-53 développé dans le parcours NIST RMF de cette plateforme — une réduction de volume qui reflète directement le périmètre plus restreint de SP 800-171, concentré sur la seule protection de la confidentialité des informations non classifiées contrôlées, plutôt que sur l'ensemble des objectifs de sécurité, de vie privée et de gestion des risques de la chaîne d'approvisionnement couverts par SP 800-53 pour un système fédéral complet.

## Un tableau de synthèse comparant les deux catalogues NIST

| Aspect | SP 800-53 | SP 800-171 |
|---|---|---|
| Public visé | Systèmes d'information des agences fédérales elles-mêmes | Organisations non fédérales traitant des CUI pour le compte du gouvernement |
| Volume de contrôles | Plus d'un millier, selon la base de référence retenue | 110 exigences |
| Relation entre les deux | Catalogue source | Sous-ensemble dérivé et adapté |
| Cadre d'application développé dans cette plateforme | NIST RMF | CMMC (niveau 2) |

## Le lien avec la leçon suivante

Ce catalogue, une fois maîtrisé dans sa structure générale, doit encore être complété, pour le niveau 3 de CMMC, par les pratiques renforcées de SP 800-172 — un développement complémentaire présenté à la leçon suivante de ce parcours, à travers un exemple concret d'application du catalogue complet.
