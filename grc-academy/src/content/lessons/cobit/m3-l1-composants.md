# Les composants d'un système de gouvernance

## Comment un objectif COBIT se réalise concrètement

Les quarante objectifs de gouvernance et de management déjà développés au module 2 décrivent **quoi** atteindre — mais chacun d'entre eux se réalise concrètement à travers une combinaison de **sept composants génériques**, que COBIT 2019 définit une fois pour toutes et qui s'appliquent, dans des proportions variables, à chacun des quarante objectifs. Ces composants portaient le nom d'**enablers** (facilitateurs) dans COBIT 5, et ont été renommés en **composants** dans COBIT 2019, sans changement de fond majeur dans leur définition.

## Les sept composants

### Processus

Un ensemble structuré de pratiques et d'activités pour atteindre certains objectifs et produire un ensemble de résultats en soutien à la réalisation des objectifs globaux liés à l'IT — le composant le plus immédiatement visible, souvent le seul auquel on pense spontanément en évoquant un "objectif COBIT".

### Structures organisationnelles

Les entités clés de prise de décision au sein d'une entreprise — comités de direction, comités de gestion des risques, fonctions de gouvernance IT — dont la composition, les modes de fonctionnement et le niveau d'autorité déterminent la capacité réelle de l'organisation à atteindre un objectif donné.

### Principes, politiques et cadres

Les moyens de traduire le comportement souhaité en lignes directrices pratiques pour la gestion quotidienne — un composant qui recoupe directement la distinction déjà développée entre politique, standard et procédure dans le premier parcours de cette plateforme.

### Information

L'information nécessaire pour maintenir une organisation fonctionnant efficacement, incluant toute l'information produite et utilisée par l'entreprise — un composant qui recoupe la famille PT de SP 800-53 (traitement des données personnelles) et l'objectif APO14 (gestion des données) déjà développé au module 2, mais appliqué ici plus largement à toute information nécessaire à la gouvernance, pas seulement aux données personnelles.

### Culture, éthique et comportement

Des individus et de l'entreprise, souvent sous-estimés comme facteur de succès des activités de gouvernance et de management — un composant qui rappelle directement la culture de sécurité et la sensibilisation déjà développées à travers de multiples référentiels de cette plateforme, mais élevée ici au rang de composant à part entière de tout objectif de gouvernance, pas seulement des objectifs de sécurité.

### Personnes, compétences et aptitudes

Nécessaires à l'aboutissement satisfaisant de toutes les activités, et à la prise de décisions correctes et à l'entreprise d'actions correctives.

### Services, infrastructures et applications

L'infrastructure, la technologie et les applications qui fournissent à l'entreprise le traitement et les services de technologie de l'information — le composant le plus proche, dans son contenu, de ce que les référentiels de sécurité spécialisés (ISO 27001, NIST CSF, CIS Controls) traitent en détail.

## Pourquoi ces sept composants doivent être considérés ensemble

Le principe central de ce modèle : un objectif de gouvernance ou de management ne peut jamais être atteint efficacement en n'agissant que sur un seul de ces sept composants. Un objectif comme APO13 (gérer la sécurité, déjà développé au module 2) suppose simultanément des **processus** de gestion de la sécurité, des **structures organisationnelles** (un comité de sécurité, un RSSI), des **politiques** documentées, une gestion appropriée de l'**information** sensible, une **culture** de sécurité diffusée dans l'organisation, des **personnes** compétentes, et des **infrastructures** techniques adéquates.

Ce principe rejoint directement une observation déjà faite à plusieurs reprises dans cette plateforme : un excellent contrôle technique isolé (une infrastructure bien configurée) ne suffit jamais si les structures organisationnelles, les compétences humaines ou la culture ne suivent pas — un constat déjà rencontré, sous une formulation différente, dans le premier parcours de cette plateforme à propos de l'articulation entre gouvernance et Security by Design.

## Un exemple concret d'application des sept composants à un même objectif

Reprenons DSS04 (gérer la continuité, déjà développé au module 2). Sa réalisation effective suppose : des **processus** documentés de continuité et de reprise, une **structure organisationnelle** de gestion de crise clairement identifiée, une **politique** de continuité approuvée par la direction, une **information** précise sur les systèmes et données critiques à restaurer en priorité, une **culture** qui prend au sérieux les exercices de simulation plutôt que de les traiter comme une formalité, des **personnes** formées à leur rôle en cas de crise, et une **infrastructure** technique de sauvegarde et de reprise réellement fonctionnelle. L'absence d'un seul de ces sept composants — par exemple, une infrastructure de sauvegarde excellente mais des personnes jamais formées à l'utiliser en situation de crise réelle — compromet l'efficacité de l'ensemble, quelle que soit la qualité des six autres composants.

## Le lien avec les facteurs de conception développés dans la leçon suivante

Ces sept composants sont génériques — identiques pour les quarante objectifs du référentiel. Ce qui varie, en revanche, c'est la **proportion et l'intensité** avec lesquelles chaque composant doit être développé pour un objectif donné, dans le contexte propre d'une entreprise précise — un ajustement piloté par les facteurs de conception, développés dans la leçon suivante de ce parcours.
