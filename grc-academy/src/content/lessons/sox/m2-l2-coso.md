# La section 404 (2/2) : le référentiel COSO comme colonne vertébrale

## Un référentiel déjà rencontré, ici à sa source

Le parcours SOC 2 de cette plateforme a déjà développé en détail le référentiel **COSO** (Committee of Sponsoring Organizations of the Treadway Commission) comme fondement des Common Criteria — les cinq composantes et dix-sept principes qui structurent l'environnement de contrôle, l'appréciation des risques, les activités de contrôle, l'information et la communication, et les activités de surveillance. Ce même référentiel COSO, dans son document phare "Internal Control – Integrated Framework" (publié initialement en 1992, révisé en 2013), constitue la **base méthodologique la plus largement utilisée** par les sociétés américaines pour structurer leur évaluation de la section 404 — un lien direct entre les deux parcours qui n'est pas fortuit : SOX a été l'un des principaux moteurs de l'adoption massive de COSO comme référentiel de contrôle interne aux États-Unis, avant que ce même référentiel ne soit repris pour d'autres usages, dont celui des Trust Services Criteria de SOC 2.

## Rappel des cinq composantes, appliquées ici au reporting financier

Les cinq composantes de COSO, déjà développées en détail dans le parcours SOC 2 de cette plateforme, s'appliquent à l'évaluation ICFR de la façon suivante :

- l'**environnement de contrôle** — la culture d'intégrité et d'éthique de l'organisation, l'indépendance du conseil d'administration, les structures organisationnelles et les responsabilités en matière de reporting financier,
- l'**appréciation des risques** — l'identification des risques d'anomalies significatives dans les états financiers, en cohérence avec l'approche descendante et fondée sur le risque déjà développée dans la leçon précédente,
- les **activités de contrôle** — les contrôles proprement dits, manuels ou automatisés, qui préviennent ou détectent les anomalies dans le processus de reporting financier,
- l'**information et la communication** — la qualité et la circulation de l'information financière pertinente au sein de l'organisation,
- les **activités de surveillance** — l'évaluation continue ou ponctuelle de l'efficacité du dispositif de contrôle interne, notamment via l'audit interne développé au module 5 de ce parcours.

## Les dix-sept principes comme grille d'évaluation

La révision de 2013 du référentiel COSO a explicitement décliné ces cinq composantes en **dix-sept principes**, chacun associé à des points d'attention (points of focus) qui aident à démontrer la présence et le fonctionnement effectif de chaque composante. Cette structuration plus fine, déjà évoquée dans le parcours SOC 2 de cette plateforme, permet à une équipe d'évaluation SOX de documenter précisément, principe par principe, comment le dispositif de contrôle interne de l'organisation satisfait chacune des exigences du référentiel — plutôt que de se contenter d'une évaluation globale et peu étayée des cinq composantes prises isolément.

## La distinction entre contrôles au niveau de l'entité et contrôles au niveau des processus

L'application de COSO à la section 404 distingue deux niveaux de contrôle, une distinction déjà amorcée dans la leçon précédente :

- les **contrôles au niveau de l'entité (entity-level controls)** — des contrôles transversaux qui influencent l'ensemble de l'organisation (le ton donné par la direction, les politiques de recrutement du personnel comptable, la supervision exercée par le comité d'audit),
- les **contrôles au niveau des processus (process-level controls ou transaction-level controls)** — des contrôles spécifiques à un cycle métier précis (le cycle des achats et des dépenses, le cycle des ventes et des créances, le cycle de la paie), qui traitent directement les assertions financières pertinentes développées dans la leçon précédente.

Un contrôle au niveau de l'entité robuste (par exemple, une forte culture d'intégrité et une supervision active du comité d'audit) peut réduire la profondeur de test nécessaire sur certains contrôles au niveau des processus — une logique d'interdépendance entre les niveaux de contrôle qui rappelle, dans son principe, celle déjà rencontrée pour les contrôles hérités et communs du NIST RMF, développée dans le parcours dédié de cette plateforme.

## Pourquoi COSO plutôt qu'un autre référentiel de contrôle interne

L'adoption quasi universelle de COSO pour la section 404, plutôt qu'un autre référentiel de gestion des risques ou de contrôle interne, s'explique par sa reconnaissance explicite par la SEC et le PCAOB comme référentiel adapté — les orientations réglementaires américaines citent directement COSO comme un exemple de référentiel convenant à l'évaluation ICFR, sans pour autant l'imposer légalement de façon exclusive. Cette reconnaissance quasi officielle explique pourquoi la quasi-totalité des sociétés cotées américaines, plutôt que de développer une méthodologie propre, s'appuient sur ce référentiel déjà éprouvé et largement documenté — un choix de proportionnalité et d'efficacité qui rappelle la logique de réutilisation de référentiels reconnus déjà observée à de multiples reprises dans cette plateforme (le recours à ISO 27005 pour EBIOS RM, ou à SP 800-53 pour le NIST RMF, tous deux développés dans les parcours précédents).

## Le lien avec les contrôles informatiques

Les activités de contrôle de COSO, déjà mentionnées plus haut dans cette leçon, incluent explicitement les contrôles technologiques généraux qui soutiennent le fonctionnement fiable des contrôles automatisés du processus de reporting financier — un sujet suffisamment structurant pour mériter un développement dédié dans le module suivant de ce parcours : les contrôles généraux informatiques (ITGC), sans lesquels la fiabilité de l'ensemble des contrôles automatisés reposant sur les systèmes d'information de l'organisation ne pourrait être valablement démontrée.
