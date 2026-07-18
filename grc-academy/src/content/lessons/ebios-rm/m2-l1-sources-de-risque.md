# Atelier 2 : les sources de risque et leurs objectifs visés

## Un raisonnement centré sur des acteurs réels, pas des catégories abstraites de menaces

L'Atelier 2 constitue le cœur de la spécificité méthodologique d'EBIOS RM : plutôt que de partir d'une taxonomie générique de menaces (comme la triade STRIDE déjà développée dans le premier parcours de cette plateforme, qui catégorise des types d'attaque sans nécessairement les rattacher à un acteur précis), EBIOS RM identifie des **sources de risque (SR)** — des acteurs réels et identifiables, avec leurs propres motivations, ressources et modes d'action — et leurs **objectifs visés (OV)**, c'est-à-dire ce que chaque source de risque cherche concrètement à obtenir en s'attaquant à l'organisation.

## Les catégories typiques de sources de risque

Bien qu'EBIOS RM n'impose pas de liste fermée, les catégories de sources de risque les plus fréquemment mobilisées dans une étude incluent :

- les **États et acteurs étatiques**, motivés par l'espionnage, le sabotage ou l'influence géopolitique,
- les **cybercriminels organisés**, motivés par le gain financier direct (rançongiciel, fraude, revente de données),
- les **concurrents économiques**, motivés par l'espionnage industriel ou l'avantage concurrentiel,
- les **activistes (hacktivistes)**, motivés par une cause idéologique ou politique,
- les **acteurs internes malveillants ou négligents**, motivés par la vengeance, le gain personnel, ou simplement par une erreur non intentionnelle,
- les **prestataires ou sous-traitants compromis**, qui deviennent eux-mêmes un vecteur d'attaque sans en être nécessairement l'origine première — un point qui prépare directement le développement de l'écosystème comme vecteur d'attaque, objet du module 3 de ce parcours.

## Les objectifs visés : ce que chaque source de risque cherche à obtenir

Pour chaque source de risque retenue, l'étude détermine son ou ses **objectifs visés** — par exemple, pour un acteur étatique : l'accès à des informations stratégiques classifiées ; pour un cybercriminel organisé : l'extorsion financière via un rançongiciel ; pour un concurrent : l'accès à un savoir-faire industriel protégé. Cette association systématique entre une source de risque et son objectif propre — le couple **SR/OV** — devient l'unité de base de toute l'analyse qui suit dans les ateliers suivants.

## L'évaluation et la priorisation des couples SR/OV

Toutes les sources de risque envisageables ne présentent pas le même niveau de pertinence pour une organisation donnée — EBIOS RM propose d'évaluer chaque couple SR/OV selon plusieurs critères :

- la **motivation** de la source de risque à l'égard de cet objectif précis, compte tenu du contexte de l'organisation,
- les **ressources et capacités techniques** dont elle dispose réellement,
- son **activité connue ou observée**, notamment via des retours d'expérience sectoriels ou des renseignements sur les menaces — un point qui recoupe directement la threat intelligence déjà développée à travers de multiples référentiels de cette plateforme (contrôle 5.7 d'ISO 27001, catégorie ID.RA du NIST CSF, contrôle RA-10 de SP 800-53).

Cette évaluation permet de **prioriser** un nombre restreint de couples SR/OV — ceux jugés les plus pertinents et les plus susceptibles de se matérialiser — plutôt que de tenter de traiter exhaustivement l'ensemble des sources de risque théoriquement imaginables, un principe de priorisation qui rappelle directement celui déjà développé pour les Implementation Groups des CIS Controls ou le mécanisme de désignation des entités essentielles de NIS2, tous deux développés dans les parcours précédents de cette plateforme : concentrer l'effort d'analyse fine sur ce qui est réellement pertinent pour l'organisation, plutôt que de le disperser uniformément.

## Un exemple concret d'évaluation d'un couple SR/OV

Pour un éditeur de logiciel de santé numérique, le couple "cybercriminel organisé / extorsion par rançongiciel sur les données de santé hébergées" serait probablement évalué comme hautement pertinent : la motivation financière est forte (les données de santé se monnayent bien sur les marchés clandestins), les capacités techniques nécessaires sont largement accessibles (les rançongiciels en tant que service sont un marché criminel mature), et l'activité de ce type d'acteur contre le secteur de la santé est largement documentée par les retours d'expérience sectoriels — ce couple SR/OV serait donc retenu en priorité pour une analyse approfondie dans les ateliers suivants, plutôt qu'un couple plus théorique comme "acteur étatique isolé / sabotage physique d'infrastructure", nettement moins pertinent pour ce profil d'organisation précis.

## Comment cet atelier prépare la suite de la méthode

Les couples SR/OV priorisés à l'issue de l'Atelier 2 deviennent le point de départ direct de l'Atelier 3, développé dans le module suivant de ce parcours : pour chaque couple retenu, l'étude construit un **scénario stratégique** décrivant le chemin plausible par lequel cette source de risque, poursuivant cet objectif précis, pourrait atteindre les valeurs métier de l'organisation identifiées à l'Atelier 1 — souvent en passant, comme on le verra, par l'écosystème de partenaires et de fournisseurs plutôt que par une attaque directe et frontale.
