# Atelier 1 (1/2) : cadrage, valeurs métier et événements redoutés

## Cinq ateliers, pas nécessairement séquentiels

EBIOS RM structure une étude de risque en **cinq ateliers**, dont les productions s'enrichissent mutuellement — l'ANSSI insiste explicitement sur le caractère itératif de la démarche : un enseignement tiré de l'atelier 3 ou 4 peut amener à revenir ajuster le cadrage de l'atelier 1, exactement comme un enseignement tiré de l'audit interne ISO 27001 peut amener à réviser l'appréciation des risques initiale, un principe d'itération déjà rencontré à de multiples reprises dans cette plateforme. Ce premier module de ce parcours développe l'Atelier 1, qui pose les fondations de toute la démarche.

## Définir le cadre et les objectifs de l'étude

L'Atelier 1 commence par la détermination du **cadre de l'étude** — le périmètre organisationnel, technique et temporel de l'analyse — et des objectifs qu'elle poursuit, en cohérence avec le contexte propre de l'organisation (missions, environnement réglementaire, contraintes stratégiques). Ce cadrage initial rejoint directement la détermination du domaine d'application d'un SMSI ISO 27001 ou du périmètre d'autorisation du NIST RMF, déjà développés dans les parcours précédents de cette plateforme — un périmètre mal calibré à cette étape compromet la pertinence de l'ensemble des ateliers suivants.

## Les valeurs métier : ce qui compte réellement pour l'organisation

Le concept le plus structurant et le plus distinctif d'EBIOS RM, introduit dès l'Atelier 1, est celui de **valeur métier (business value)** — ce qui a réellement de la valeur pour l'organisation et mérite d'être protégé : une donnée sensible, un processus métier critique, un savoir-faire, une réputation, une mission de service public. C'est un point de départ délibérément différent de la plupart des référentiels déjà étudiés dans cette plateforme, qui partent plus souvent d'un inventaire d'actifs techniques (le contrôle 1 des CIS Controls, par exemple) : EBIOS RM force à identifier **d'abord** ce qui compte vraiment pour l'organisation, **avant** de descendre vers les systèmes techniques qui le supportent.

## Les biens supports : ce qui porte techniquement la valeur métier

Une fois les valeurs métier identifiées, l'étude détermine les **biens supports (supporting assets)** — les éléments du système d'information (matériels, logiciels, réseaux, mais aussi organisations, locaux, personnes) sur lesquels reposent ces valeurs métier. Cette distinction en deux niveaux — valeur métier d'abord, bien support ensuite — rappelle directement la cascade des objectifs de COBIT, déjà développée dans le parcours dédié de cette plateforme, qui relie de la même manière un niveau stratégique (les objectifs d'entreprise) à un niveau technique concret (les biens supports, ici, plutôt que les objectifs de management de COBIT) — la logique de traçabilité verticale entre le concret et le stratégique, retrouvée ici sous une forme propre à EBIOS RM.

## Les événements redoutés : la matérialisation du risque sur une valeur métier

Pour chaque valeur métier, l'étude identifie les **événements redoutés (feared events)** — une atteinte à sa disponibilité, son intégrité, sa confidentialité, ou sa traçabilité (une déclinaison de la triade CID enrichie d'une quatrième propriété propre à la tradition française de sécurité des systèmes d'information), et évalue sa **gravité** si cet événement venait à se matérialiser, en tenant compte des impacts métier, humains, financiers, juridiques ou d'image.

Un exemple concret : pour la valeur métier "dossier patient" d'un établissement de santé, un événement redouté pourrait être "divulgation non autorisée du dossier patient", avec une gravité jugée critique compte tenu de la sensibilité des données de santé (un sujet déjà développé en détail dans le parcours HIPAA de cette plateforme, bien que dans un cadre juridique distinct) et de l'impact potentiel sur la confiance des patients.

## La cartographie de l'écosystème : une première esquisse

L'Atelier 1 amorce également, de façon encore générale, l'identification des **parties prenantes** de l'écosystème de l'organisation — fournisseurs, sous-traitants, partenaires, clients — dont la cartographie complète et le rôle dans les chemins d'attaque possibles seront développés en détail dans l'Atelier 3, objet du module 3 de ce parcours. Cette esquisse précoce permet de ne pas découvrir tardivement des dépendances critiques qui auraient dû être prises en compte dès le cadrage initial.

## Ce que cette première étape produit concrètement

À l'issue de cette première partie de l'Atelier 1, l'étude dispose d'une cartographie structurée : les valeurs métier de l'organisation, les biens supports qui les portent, les événements redoutés associés à chacune et leur gravité, et une première esquisse de l'écosystème — la matière première indispensable pour aborder, dans la seconde partie de l'Atelier 1 développée dans la leçon suivante, l'établissement du socle de sécurité de référence.
