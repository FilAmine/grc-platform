# La fonction Map (2/2) : catégoriser et documenter le système

## De la compréhension du contexte à la documentation structurée

La leçon précédente a développé comment Map établit le contexte d'usage, catégorise le niveau de risque, et identifie les parties prenantes et composants tiers d'un système d'IA. Cette seconde partie de la fonction Map se concentre sur la **documentation structurée** qui formalise cette compréhension, condition indispensable pour que les fonctions Measure et Manage, développées aux modules suivants de ce parcours, puissent s'appuyer sur une base commune et partagée entre l'ensemble des AI Actors impliqués.

## Les fiches de modèle (model cards) et la documentation de traçabilité

La pratique de gestion du risque IA a développé, en cohérence avec les exigences de Map, des outils de documentation structurée tels que les **fiches de modèle (model cards)** — des documents synthétiques décrivant l'objectif du modèle, ses performances mesurées sur différents sous-groupes de population, ses limites connues, et les conditions d'usage recommandées. Ces fiches jouent, pour un système d'IA, un rôle comparable à celui de la Déclaration d'Applicabilité pour ISO 27001 ou du System Security Plan pour FedRAMP, tous deux développés dans les parcours dédiés de cette plateforme — un document de référence structuré qui rend explicite ce qui, sans lui, resterait implicite ou dispersé entre plusieurs équipes.

## Les fiches de données (data sheets) pour les jeux de données d'entraînement

De façon similaire, Map encourage la documentation de l'origine, de la composition et des limites connues des jeux de données utilisés pour l'entraînement du modèle — une pratique qui répond directement au risque de biais systémique déjà développé au module 1 de ce parcours : une organisation qui ne documente jamais la composition démographique de ses données d'entraînement ne peut ensuite jamais vérifier, lors de la fonction Measure, si son modèle produit des résultats disproportionnellement défavorables pour certains groupes sous-représentés dans ces données.

## L'identification des risques ne se limite jamais à une liste générique

Map insiste sur le fait que l'identification des risques ne peut jamais se limiter à l'application mécanique d'une liste générique de risques préétablie — chaque système d'IA, déployé dans un contexte spécifique, présente une combinaison de risques propre qui doit être activement recherchée plutôt que simplement cochée sur une liste standard. Ce principe rejoint directement celui déjà développé pour l'approche par scénarios d'EBIOS RM dans le parcours dédié de cette plateforme, où l'identification de scénarios de risque pertinents exige une réflexion contextuelle active plutôt qu'une simple application mécanique d'un référentiel générique.

## La documentation comme condition de la transparence exigée par l'IA digne de confiance

Cette exigence de documentation structurée rejoint directement la caractéristique de transparence déjà développée au module 1 de ce parcours parmi les sept caractéristiques de l'IA digne de confiance — un système d'IA dont le contexte, les données d'entraînement et les limites connues ne sont documentés nulle part ne peut jamais satisfaire une exigence de transparence envers ses utilisateurs ou les personnes impactées par ses décisions, quelle que soit par ailleurs la qualité technique de sa conception.

## Un exemple concret d'application de la fonction Map

Une organisation développant un système d'aide à la décision pour l'octroi de crédit documenterait, au titre de Map, l'objectif métier (accélérer l'instruction des dossiers tout en maintenant un niveau de risque de défaut acceptable), le contexte d'usage prévu (un outil d'aide à la décision pour un conseiller humain, plutôt qu'une décision entièrement automatisée), la catégorisation du niveau de risque (élevé, compte tenu du domaine sensible du crédit et du risque de discrimination), les parties prenantes impactées (les demandeurs de crédit, y compris ceux qui n'ont aucune relation préexistante avec l'organisation), et la composition des données d'entraînement historiques utilisées, avec une attention particulière portée à leur représentativité démographique.

## Le lien avec le module suivant

Cette cartographie et cette documentation structurée établissent le terrain sur lequel l'organisation peut désormais mesurer concrètement les risques identifiés — l'objet de la fonction Measure, développée au module suivant de ce parcours.
