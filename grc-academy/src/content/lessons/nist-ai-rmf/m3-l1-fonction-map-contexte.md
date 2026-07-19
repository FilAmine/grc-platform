# La fonction Map (1/2) : établir le contexte

## Le point de départ de chaque cycle Map-Measure-Manage

La fonction **Map** ouvre le cycle opérationnel proprement dit de l'AI RMF, appliqué à un système d'IA précis — elle consiste à établir le contexte dans lequel ce système sera conçu, déployé et utilisé, avant même de pouvoir mesurer (Measure) ou traiter (Manage) les risques qu'il pourrait engendrer. Cette fonction rejoint directement, dans son rôle de cartographie préalable, la fonction Identify du NIST CSF ou la fonction Identify-P du NIST Privacy Framework, toutes deux déjà développées dans les parcours dédiés de cette plateforme — mais Map s'attache spécifiquement au contexte d'usage d'un système d'IA plutôt qu'aux actifs informationnels ou aux flux de données personnelles.

## Comprendre l'objectif métier et le contexte d'usage prévu

Map commence par documenter précisément l'objectif métier du système d'IA — quel problème il est censé résoudre, quels bénéfices attendus justifient son développement — ainsi que le **contexte d'usage prévu**, incluant les utilisateurs visés, l'environnement d'exploitation, et les décisions ou actions que le système est censé influencer. Cette documentation préalable permet ensuite d'identifier les usages qui s'écarteraient de ce contexte prévu — un système de reconnaissance faciale conçu pour un usage de sécurité aéroportuaire, mais utilisé par un tiers pour un usage de surveillance généralisée non anticipé, illustre directement ce risque de dérive de contexte.

## Catégoriser le système selon son niveau de risque

Map impose de catégoriser le système d'IA selon son niveau de risque potentiel, en tenant compte de facteurs tels que le degré d'autonomie de ses décisions (un système purement consultatif qui n'assiste qu'un décideur humain présente un profil de risque différent d'un système entièrement automatisé), la réversibilité de ses décisions, et la sensibilité du domaine d'application (santé, justice, emploi, crédit) — une catégorisation qui rappelle directement, dans son principe, celle déjà développée pour la catégorisation FIPS 199 du NIST RMF ou pour les niveaux d'impact de FedRAMP, tous deux développés dans les parcours dédiés de cette plateforme, ici appliquée à un système d'IA plutôt qu'à un système d'information classique.

## Identifier les bénéfices et les risques pour l'ensemble des parties prenantes

Map exige d'identifier explicitement les bénéfices attendus du système, mais également les risques potentiels pour l'ensemble des AI Actors déjà développés au module 1 de ce parcours — pas seulement les risques pour l'organisation elle-même (réputationnels, juridiques, financiers), mais également les risques pour les utilisateurs directs et pour les personnes impactées sans lien contractuel avec l'organisation. Cette double perspective — bénéfice pour l'organisation, risque pour les personnes concernées — rejoint directement celle déjà développée pour la méthodologie d'appréciation du risque vie privée dans le parcours NIST Privacy Framework de cette plateforme, où l'appréciation du préjudice pour l'individu constitue une dimension distincte du seul risque pour l'organisation.

## Documenter les composants tiers et les données d'entraînement

Map impose également de documenter précisément l'origine et la nature des composants tiers intégrés au système — modèles pré-entraînés obtenus auprès d'un fournisseur externe, jeux de données d'entraînement acquis auprès de tiers — une exigence qui rejoint directement la gestion des risques de la chaîne d'approvisionnement déjà développée dans les parcours NIST RMF, DORA et NIST CSF de cette plateforme, mais appliquée ici spécifiquement aux composants et données propres à l'apprentissage automatique.

## Pourquoi cette cartographie initiale conditionne tout le reste du cycle

Une cartographie Map insuffisamment rigoureuse — un contexte d'usage mal documenté, des parties prenantes impactées non identifiées, des composants tiers non recensés — expose l'ensemble du cycle Measure et Manage à passer à côté de risques significatifs, faute d'avoir même identifié qu'ils existaient. Ce principe rejoint directement celui déjà développé pour l'importance de la catégorisation initiale dans le NIST RMF ou pour l'analyse d'impact sur l'activité dans ISO 22301, tous deux développés dans les parcours dédiés de cette plateforme : une étape de cartographie bâclée compromet la pertinence de tout le travail d'appréciation du risque qui en découle.

## Le lien avec la leçon suivante

Cette compréhension du contexte, une fois établie, doit encore être traduite en une catégorisation précise et documentée du système — l'objet de la leçon suivante de ce parcours.
