# Scoping et segmentation réseau

## Pourquoi le scoping conditionne tout le reste de la démarche PCI DSS

Avant même de commencer à évaluer sa conformité aux douze exigences déjà développées au module 1, une entité doit déterminer précisément quels systèmes relèvent de son **environnement des données de titulaires de cartes (CDE)**, déjà défini au module 0 — cette étape de **scoping** conditionne directement l'ampleur de l'effort de mise en conformité : plus le périmètre est large, plus le nombre de systèmes soumis à l'intégralité des douze exigences est important.

## Les trois catégories de systèmes à considérer

Le scoping PCI DSS distingue, en pratique, trois catégories de systèmes :

- les systèmes qui **stockent, traitent ou transmettent directement** des données de titulaires de carte — indiscutablement dans le CDE,
- les systèmes **connectés au CDE ou susceptibles d'affecter sa sécurité** — par exemple, un serveur d'authentification centralisé utilisé aussi bien pour l'accès au CDE que pour d'autres systèmes de l'entreprise, ou un système de gestion à distance ayant un accès administratif au CDE — également dans le périmètre, même s'ils ne traitent aucune donnée de carte eux-mêmes,
- les systèmes **totalement isolés** du CDE, sans connexion ni influence possible sur sa sécurité — hors périmètre.

Cette deuxième catégorie est souvent sous-estimée par des organisations qui découvrent PCI DSS pour la première fois : un système qui ne traite jamais directement de données de cartes, mais qui dispose d'un accès réseau non contrôlé vers le CDE, reste pleinement soumis aux exigences du référentiel — un principe similaire, dans son esprit, à l'inclusion des contrôles communs et hérités déjà rencontrée dans le parcours NIST RMF de cette plateforme, mais appliqué ici dans le sens inverse : ce n'est pas un héritage de contrôle qui étend la couverture, mais une simple connectivité réseau non maîtrisée qui étend le périmètre d'audit.

## La segmentation réseau comme levier de réduction du périmètre

PCI DSS **n'exige pas formellement** la segmentation réseau — mais sans elle, l'intégralité du réseau de l'entité est considérée comme faisant partie du CDE, ce qui rend la démarche de conformité disproportionnellement lourde pour la plupart des organisations. La **segmentation** consiste à isoler physiquement ou logiquement le CDE du reste du réseau de l'entreprise, via des pare-feux, des VLAN dédiés, ou des contrôles d'accès réseau stricts, de sorte que seuls les systèmes réellement en contact avec les données de cartes se trouvent dans le périmètre d'évaluation.

Cette pratique recoupe directement le contrôle 8.22 de l'Annexe A d'ISO 27001 (cloisonnement des réseaux) et le contrôle SC-7 de SP 800-53, déjà développés dans les parcours précédents de cette plateforme — avec cette spécificité propre à PCI DSS : l'efficacité de cette segmentation doit être **testée régulièrement par un tiers indépendant** (exigence 11, déjà développée au module 1), et non simplement documentée sur un schéma d'architecture qui pourrait ne plus refléter la réalité opérationnelle.

## Un exemple concret d'impact du scoping sur l'effort de conformité

Un commerçant en ligne qui traite lui-même les paiements sur ses propres serveurs, sans aucune segmentation entre son infrastructure de paiement et le reste de son système d'information (site web, base de données clients, outils internes), se retrouve avec l'intégralité de son infrastructure dans le périmètre PCI DSS — chaque serveur, chaque poste de travail ayant un accès réseau non contrôlé vers les systèmes de paiement doit satisfaire aux douze exigences. Le même commerçant, qui isolerait strictement son infrastructure de paiement dans un segment réseau dédié, sans connexion directe avec le reste de son système d'information sauf à travers des points de contrôle précisément documentés et testés, réduit son périmètre d'évaluation à ce seul segment — une différence d'ampleur considérable dans l'effort de mise en conformité, pour un même volume d'activité de paiement.

## Le recours à l'externalisation comme stratégie de réduction du périmètre

Une stratégie fréquemment adoptée par les commerçants, en particulier les plus petits, consiste à **externaliser entièrement** le traitement des paiements à un prestataire tiers déjà validé PCI DSS (une passerelle de paiement hébergée, un widget de paiement intégré qui ne transite jamais par les serveurs du commerçant) — réduisant ainsi drastiquement, voire en théorie à néant, le périmètre CDE du commerçant lui-même. Cette stratégie détermine directement le type de questionnaire d'auto-évaluation applicable au commerçant, développé en détail au module 3 de ce parcours : un commerçant entièrement externalisé relève généralement du questionnaire le plus léger (SAQ A), tandis qu'un commerçant qui gère lui-même tout ou partie du traitement relève d'un questionnaire nettement plus exigeant.

## Ce que le scoping implique pour la suite de la démarche

Un scoping mal réalisé — trop optimiste, excluant à tort des systèmes qui devraient être inclus — expose l'entité à une évaluation de conformité invalide, potentiellement découverte seulement après un incident de sécurité impliquant un système qui aurait dû être couvert. À l'inverse, un scoping trop prudent, incluant par excès de précaution des systèmes qui pourraient légitimement être exclus par une segmentation appropriée, alourdit inutilement l'effort de conformité — un arbitrage qui rappelle directement celui déjà développé pour le domaine d'application d'un SMSI ISO 27001 dans le parcours dédié de cette plateforme, où un périmètre mal calibré, dans un sens comme dans l'autre, complique disproportionnellement la suite de la démarche.
