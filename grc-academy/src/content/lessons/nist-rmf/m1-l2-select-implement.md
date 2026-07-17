# Les sept étapes du RMF (2/4) : Select et Implement

## Étape 3 — Select (Sélectionner)

À partir de la catégorisation obtenue à l'étape précédente, cette étape consiste à sélectionner un ensemble initial de contrôles de sécurité et de vie privée pour le système, puis à l'adapter à son contexte réel.

### Le choix de la base de référence (baseline)

**SP 800-53B** définit trois bases de référence de contrôles, correspondant directement aux trois niveaux de catégorisation FIPS 199 : une base de référence **Faible**, une base de référence **Modérée** (la plus fréquemment utilisée en pratique, la majorité des systèmes fédéraux relevant de ce niveau), et une base de référence **Élevée**. Chaque base de référence supérieure inclut l'ensemble des contrôles de la base inférieure, en y ajoutant des contrôles supplémentaires et des exigences renforcées sur certains contrôles déjà présents — une architecture cumulative qui simplifie la transition d'un système d'un niveau de catégorisation à un niveau supérieur.

**FIPS 200** complète ce dispositif en fixant, indépendamment du choix précis des contrôles, des **exigences de sécurité minimales** organisées selon 17 domaines de sécurité (correspondant largement aux familles de contrôles de SP 800-53, développées au module 2) auxquelles toute organisation fédérale doit satisfaire, quel que soit le niveau de catégorisation retenu.

### L'adaptation (tailoring) : la nuance essentielle

Une base de référence n'est jamais appliquée telle quelle sans analyse — le processus de **tailoring** permet d'ajuster les contrôles sélectionnés au contexte réel du système :

- **l'attribution de valeurs aux paramètres** des contrôles (par exemple, un contrôle exigeant une revue des comptes "à une fréquence définie par l'organisation" doit voir cette fréquence précisée : trimestrielle, mensuelle, selon le contexte de risque),
- l'**identification et la justification des contrôles jugés non applicables**, dans une logique très proche de l'exclusion documentée dans la Déclaration d'Applicabilité d'ISO 27001, déjà développée dans le parcours dédié de cette plateforme,
- l'**ajout de contrôles compensatoires** lorsqu'un contrôle de la base de référence ne peut être implémenté tel quel, mais qu'une mesure alternative permet d'atteindre un objectif de sécurité équivalent,
- l'application d'**overlays** — des ensembles de contrôles spécialisés, prédéfinis pour un contexte particulier (systèmes en environnement infonuagique, systèmes classifiés, systèmes de contrôle industriel), qui se superposent à la base de référence générale sans la remplacer entièrement.

### Le plan de surveillance continue

Cette étape produit également une première version de la stratégie de surveillance continue propre au système — une préparation directe de l'étape 7 (Monitor), développée plus loin dans ce module.

## Étape 4 — Implement (Mettre en œuvre)

Cette étape consiste à mettre en œuvre effectivement les contrôles sélectionnés et adaptés à l'étape précédente, et à documenter précisément la manière dont chaque contrôle est implémenté dans le **Plan de Sécurité du Système (System Security Plan — SSP)**.

### Le Plan de Sécurité du Système (SSP)

Le SSP est le document central qui décrit, contrôle par contrôle, comment chacun est implémenté dans le système concerné — bien au-delà d'une simple case cochée : il précise l'implémentation technique ou organisationnelle réelle, les responsabilités associées, et, le cas échéant, si le contrôle est hérité d'un **contrôle commun** fourni par un Common Control Provider au niveau organisationnel plutôt que réimplémenté spécifiquement pour ce système. Ce document occupe, dans l'architecture documentaire du RMF, une fonction très proche de la Déclaration d'Applicabilité d'ISO 27001 ou de la matrice de contrôles SOC 2 déjà rencontrées dans les parcours précédents de cette plateforme — la trace écrite qui relie chaque exigence normative à sa mise en œuvre réelle et vérifiable.

### Les contrôles communs, hybrides et spécifiques au système

Le RMF distingue explicitement trois statuts d'implémentation pour un contrôle donné :

- **Contrôle commun (common control)** — implémenté une seule fois au niveau organisationnel (par exemple, la sécurité physique d'un centre de données partagé) et hérité par tous les systèmes hébergés dans ce périmètre, sans qu'aucun d'entre eux n'ait à le réimplémenter individuellement.
- **Contrôle hybride** — partiellement fourni au niveau organisationnel, partiellement complété au niveau du système lui-même.
- **Contrôle spécifique au système (system-specific)** — entièrement implémenté et documenté au niveau du système considéré, sans aucun héritage.

Cette distinction évite une duplication massive de l'effort de documentation et d'évaluation à travers un grand nombre de systèmes qui partagent une infrastructure commune — un principe d'efficacité qui rejoint, dans son esprit, la logique de mapping et de réutilisation des contrôles déjà rencontrée à plusieurs reprises dans les parcours précédents de cette plateforme, ici appliquée non pas entre référentiels différents mais entre systèmes d'une même organisation partageant une infrastructure commune.

## Le lien entre ces deux étapes et le reste du processus

Select fixe **quels** contrôles s'appliquent, ajustés au contexte réel du système ; Implement produit la **preuve documentée** de leur mise en œuvre effective dans le SSP. Ce couple d'étapes est directement analogue, dans sa logique, à la relation entre la Déclaration d'Applicabilité et sa mise en œuvre technique effective déjà développée pour ISO 27001 — la différence structurante étant que le RMF impose des bases de référence de contrôles bien plus prescriptives et détaillées (SP 800-53, développé au module 2) que l'Annexe A d'ISO 27001, reflet direct de son origine dans un contexte fédéral américain à obligation légale plutôt que dans un système de management volontairement plus générique.
