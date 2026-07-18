# Facteurs de conception et Focus Areas

## Pourquoi un référentiel générique ne peut pas s'appliquer identiquement partout

Les quarante objectifs et les sept composants déjà développés aux modules 2 et 3 constituent le **noyau** de COBIT — mais aucune entreprise n'a besoin d'atteindre le même niveau d'exigence sur chacun des quarante objectifs, ni de développer les sept composants avec la même intensité pour chacun d'eux. COBIT 2019 introduit, pour répondre à ce constat, la notion de **facteurs de conception (design factors)** — un mécanisme d'adaptation qui rappelle, dans son principe, la proportionnalité déjà rencontrée dans les parcours NIS2 et DORA de cette plateforme, ou les Implementation Groups des CIS Controls.

## Les facteurs de conception

Le guide de conception de COBIT 2019 identifie une dizaine de facteurs de conception, parmi lesquels :

- la **stratégie d'entreprise** — une entreprise orientée innovation n'a pas les mêmes priorités de gouvernance IT qu'une entreprise orientée stabilité opérationnelle,
- les **objectifs d'entreprise** — directement issus du deuxième niveau de la cascade des objectifs déjà développée au module 1,
- le **profil de risque** de l'entreprise,
- les **problématiques IT actuelles** rencontrées par l'entreprise,
- le **paysage des menaces** auquel l'entreprise est exposée,
- les **exigences de conformité** applicables — un point de jonction direct avec l'ensemble des textes légaux et contractuels déjà développés dans cette plateforme (RGPD, NIS2, DORA, PCI DSS),
- le **rôle de l'IT** dans l'entreprise — un simple centre de coût support, ou un levier stratégique de différenciation concurrentielle,
- le **modèle de sourcing** de l'IT — internalisé, externalisé, ou hybride,
- les **méthodes de mise en œuvre IT** — traditionnelles (cycle en cascade) ou agiles/DevOps,
- la **stratégie d'adoption technologique** de l'entreprise,
- la **taille de l'entreprise**.

## Comment ces facteurs influencent concrètement le système de gouvernance

Chaque facteur de conception oriente, pour chacun des quarante objectifs, la priorité relative à lui accorder et l'intensité de développement attendue pour chacun des sept composants. Une entreprise dont le modèle de sourcing IT est fortement externalisé accordera, par exemple, une importance accrue à APO10 (gérer les fournisseurs, déjà développé au module 2) par rapport à une entreprise qui internalise l'essentiel de sa fonction IT. Une entreprise dont les méthodes de mise en œuvre sont largement agiles/DevOps ajustera la formulation de ses processus (l'un des sept composants) pour refléter des cycles de livraison continue plutôt qu'un cycle en cascade traditionnel — un ajustement qui rappelle directement les principes DevSecOps déjà développés dans le module Security by Design du premier parcours de cette plateforme.

## Le processus de conception d'un système de gouvernance sur mesure

COBIT 2019 propose un processus en plusieurs étapes pour construire un système de gouvernance adapté :

1. **Comprendre le contexte de l'entreprise** à travers l'ensemble des facteurs de conception.
2. **Déterminer la portée initiale** du système de gouvernance, en identifiant les objectifs et composants les plus pertinents au regard de ce contexte.
3. **Affiner la portée**, en tenant compte d'éventuels facteurs de conception spécifiques supplémentaires (comme un Focus Area précis, développé plus bas).
4. **Conclure la conception du système de gouvernance**, en documentant la priorité relative accordée à chaque objectif et la manière dont chaque composant doit être développé pour l'atteindre.

Ce processus rappelle directement la logique du tailoring des bases de référence de contrôles du NIST RMF, déjà développée dans le parcours dédié de cette plateforme — sauf que COBIT applique ce même principe d'adaptation à l'ensemble de la gouvernance IT, pas seulement à un catalogue de contrôles de sécurité.

## Les Focus Areas : traiter un sujet transversal précis

Au-delà des facteurs de conception généraux, COBIT 2019 introduit la notion de **Focus Area** — un sujet de gouvernance spécifique (une technologie particulière, une méthodologie comme DevOps, ou un risque précis comme la cybersécurité) traité par une combinaison ciblée d'objectifs et de composants, sans nécessiter de reconstruire l'ensemble du référentiel. L'ISACA publie des guides de Focus Area dédiés à des sujets précis, permettant à une organisation de zoomer sur une préoccupation particulière (par exemple, la gouvernance spécifique d'un projet de transformation cloud) sans perdre de vue la cohérence d'ensemble du système de gouvernance COBIT dans lequel ce Focus Area s'insère.

## Ce que ce mécanisme confirme sur la maturité croissante des référentiels

L'introduction des facteurs de conception et des Focus Areas dans COBIT 2019, quelques années après les Implementation Groups des CIS Controls (2019) et l'approche personnalisée de PCI DSS v4.0 (2022), confirme une fois de plus une tendance de fond déjà observée à de multiples reprises dans cette plateforme : les référentiels les plus établis évoluent systématiquement vers davantage de flexibilité et de proportionnalité au contexte réel de chaque organisation, sans abandonner le socle structurant qui a fait leur crédibilité initiale.
