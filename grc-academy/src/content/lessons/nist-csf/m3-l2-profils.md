# Les Profils : Current, Target, Community, et l'analyse d'écarts

## Un Profil, qu'est-ce que c'est concrètement ?

Un **Profil** est la sélection spécifique des résultats du Core (fonctions, catégories, sous-catégories) qu'une organisation a choisi de prioriser, avec le niveau atteint ou visé pour chacun. Contrairement aux Tiers (qui caractérisent la rigueur globale de la gestion des risques), un Profil descend au niveau granulaire de chaque sous-catégorie — c'est l'outil qui permet de répondre concrètement à "où en sommes-nous, sous-catégorie par sous-catégorie, et où voulons-nous aller".

## Current Profile : la photographie de l'existant

Le **Current Profile** documente l'état présent : pour chaque sous-catégorie retenue comme pertinente, quel est le niveau effectivement atteint aujourd'hui, avec les preuves à l'appui (pas une auto-évaluation déclarative sans vérification — le même principe de preuve que pour un audit ISO 27001 ou SOC 2). Construire un Current Profile honnête suppose souvent un travail d'audit interne préalable : interroger les équipes opérationnelles, vérifier les configurations réelles plutôt que les politiques déclarées.

## Target Profile : la destination

Le **Target Profile** documente le niveau visé pour chaque sous-catégorie retenue, déterminé à partir :

- de la stratégie de risque définie en Govern (GV.RM) — quel niveau de risque résiduel est acceptable,
- des exigences externes (obligations réglementaires, exigences contractuelles de clients),
- des résultats de l'évaluation des risques (ID.RA) — les sous-catégories protégeant les actifs les plus critiques justifient un Target Profile plus exigeant.

Un Target Profile n'est donc jamais "Tier 4 partout" — il reflète des priorités différenciées, cohérentes avec le principe fondamental du CSF selon lequel toutes les sous-catégories ne méritent pas le même niveau d'investissement.

## L'analyse d'écarts (gap analysis)

La comparaison systématique entre Current Profile et Target Profile, sous-catégorie par sous-catégorie, produit une liste d'écarts priorisée — c'est le livrable le plus directement actionnable du CSF pour construire un plan d'action (développé dans la leçon suivante sur la mise en œuvre). Une bonne pratique consiste à documenter, pour chaque écart :

- le résultat visé (la sous-catégorie du Target Profile),
- l'état actuel et la preuve documentée,
- l'effort estimé pour combler l'écart,
- le risque résiduel si l'écart n'est pas comblé dans l'immédiat, et qui (quel risk owner) accepte formellement ce risque résiduel temporaire.

## Community Profiles : des Target Profiles pré-mâchés par secteur

Introduits formellement en CSF 2.0, les **Community Profiles** sont des Target Profiles développés collectivement par un secteur, une communauté d'intérêt ou une technologie spécifique (le NIST a par exemple publié des Community Profiles pour le secteur manufacturier, ou pour l'intelligence artificielle générative). Ils offrent un point de départ déjà adapté au contexte sectoriel, évitant à chaque organisation de reconstruire un Target Profile entièrement de zéro — un peu comme un template de risques préconstruit pour un secteur donné.

Une organisation peut adopter un Community Profile tel quel, ou plus généralement l'ajuster à la marge en fonction de ses spécificités propres (taille, exposition particulière, exigences contractuelles additionnelles) — le Community Profile devient alors le point de départ du Target Profile plutôt que le Target Profile final.

## Organizational Profiles : la vue consolidée

Le CSF 2.0 introduit également la notion d'**Organizational Profile**, qui peut combiner plusieurs Profils correspondant à différentes parties de l'organisation (une filiale, une ligne de produit, un environnement cloud spécifique) en une vue consolidée — utile pour une direction générale qui a besoin d'une vision d'ensemble sans perdre la granularité nécessaire à l'action pour chaque équipe opérationnelle.

## Pourquoi les Profils sont l'outil le plus concrètement actionnable du CSF

Contrairement au Core (qui décrit *quoi* faire en général) et aux Tiers (qui caractérisent une posture globale), les Profils sont l'endroit où le CSF devient un document de travail opérationnel : une liste priorisée d'écarts, avec preuves, propriétaires et échéances — la matière première directe d'un plan d'action, sujet de la leçon suivante.
