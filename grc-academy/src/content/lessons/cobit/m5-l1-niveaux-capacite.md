# Niveaux de capacité et gestion de la performance

## Un changement de référence entre COBIT 5 et COBIT 2019

COBIT 5 évaluait la maturité de chaque processus selon un modèle propre, fondé sur la norme ISO/IEC 15504 (évaluation des processus logiciels). COBIT 2019 a remplacé ce modèle par une échelle de **niveaux de capacité alignée sur le référentiel CMMI** (Capability Maturity Model Integration), un choix qui facilite la comparaison et l'intégration avec d'autres démarches d'évaluation de maturité déjà largement répandues dans l'industrie du développement logiciel.

## Les six niveaux de capacité

- **Niveau 0 — Incomplet** — le processus n'est pas mis en œuvre, ou échoue à atteindre son objectif.
- **Niveau 1 — Initial** — le processus est mis en œuvre et atteint globalement son objectif, mais de manière non systématique.
- **Niveau 2 — Géré (Managed)** — le processus est désormais planifié, surveillé et ajusté, et ses produits de travail sont correctement établis, contrôlés et maintenus.
- **Niveau 3 — Défini (Defined)** — le processus est mis en œuvre selon un processus défini, capable d'atteindre ses résultats.
- **Niveau 4 — Géré quantitativement** — le processus est mesuré et contrôlé à l'aide de techniques quantitatives.
- **Niveau 5 — Optimisant** — le processus est amélioré en continu pour répondre aux objectifs actuels et futurs pertinents de l'entreprise.

Cette échelle rappelle directement, dans sa structure, les quatre Tiers du NIST CSF déjà développés dans le parcours dédié de cette plateforme (Partiel, Informé sur les risques, Répétable, Adaptatif) — les deux modèles caractérisent la rigueur d'un processus ou d'une pratique plutôt qu'un simple état binaire de conformité, avec une progression similaire d'une exécution ad hoc vers une amélioration continue pilotée par la donnée.

## Une nuance essentielle : la capacité n'est pas la performance

Un point souvent mal compris : le niveau de capacité d'un objectif COBIT mesure la **rigueur** avec laquelle le processus est exécuté — pas directement s'il produit les résultats attendus pour l'entreprise. Une organisation pourrait, en théorie, exécuter un processus de manière très rigoureuse (niveau de capacité élevé) tout en poursuivant des objectifs mal alignés avec les besoins réels de l'entreprise. C'est précisément pour combler cette distinction que COBIT 2019 introduit, en complément du modèle de capacité, une approche de **gestion de la performance (Performance Management)**.

## L'approche de gestion de la performance

Au-delà du seul niveau de capacité d'un processus, COBIT 2019 encourage l'évaluation de la performance de chaque composant (pas seulement le composant "processus", mais l'ensemble des sept composants déjà développés au module 3) au regard des objectifs propres de l'entreprise, tels que définis par la cascade des objectifs (module 1). Cette double perspective — capacité (la rigueur d'exécution) et performance (l'atteinte effective des résultats attendus) — permet d'éviter un piège déjà signalé à plusieurs reprises dans cette plateforme : confondre la conformité formelle à un processus documenté avec l'efficacité réelle de ce processus au service des objectifs qui le justifient.

## Comment déterminer un niveau de capacité cible

Comme pour les autres mécanismes de gradation déjà rencontrés dans cette plateforme (les bases de référence de contrôles du NIST RMF, les Implementation Groups des CIS Controls), COBIT ne recommande jamais de viser le niveau de capacité maximal pour l'ensemble des quarante objectifs indépendamment de leur importance relative. Le niveau cible pour chaque objectif découle directement de sa priorité déterminée par les facteurs de conception (module 4) et sa position dans la cascade des objectifs (module 1) : un objectif jugé peu prioritaire pour le contexte propre de l'entreprise peut légitimement rester à un niveau de capacité 2 ou 3, tandis qu'un objectif jugé critique (par exemple, APO13 ou DSS05 pour une entreprise fortement exposée aux risques de cybersécurité) justifiera un investissement pour atteindre un niveau 4 ou 5.

## Ce que ce modèle apporte de spécifique par rapport aux modèles de maturité déjà rencontrés

Bien que la structure générale (une échelle progressive de rigueur) rappelle les Tiers du NIST CSF et, dans une moindre mesure, le cycle PDCA d'ISO 27001 déjà développés dans les parcours précédents de cette plateforme, le modèle COBIT se distingue par son ancrage explicite sur **CMMI**, un référentiel largement utilisé au-delà du seul domaine de la sécurité (dans l'ingénierie logicielle, la gestion de projet, l'assurance qualité) — ce qui facilite, pour une organisation qui utilise déjà CMMI dans un autre contexte (par exemple, pour évaluer la maturité de ses pratiques de développement logiciel), une cohérence méthodologique directe avec l'évaluation de sa gouvernance IT au sens de COBIT, sans avoir à jongler entre deux échelles de maturité incompatibles.
