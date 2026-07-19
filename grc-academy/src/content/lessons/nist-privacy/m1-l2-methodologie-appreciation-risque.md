# Le modèle de risque vie privée (2/2) : méthodologie d'appréciation du risque

## Une chaîne causale à trois maillons

Le NIST Privacy Framework structure l'appréciation du risque vie privée autour d'une chaîne causale précise, développée à la leçon précédente : une **data action** peut engendrer un **problematic data action**, qui peut à son tour engendre un **préjudice (problem)** pour un individu — préjudice économique (perte financière directe), préjudice psychologique (anxiété liée à un sentiment de surveillance), préjudice de discrimination, ou préjudice d'atteinte à la dignité ou à l'autonomie. Cette chaîne causale rappelle, dans sa logique de propagation d'une cause vers une conséquence via un événement intermédiaire, celle déjà développée pour les scénarios stratégiques et opérationnels d'EBIOS RM dans le parcours dédié de cette plateforme, bien qu'appliquée ici à la vie privée plutôt qu'au risque cyber au sens large.

## Estimer la probabilité qu'une data action devienne problématique

Pour chaque data action identifiée, l'organisation évalue la **probabilité** qu'elle engendre effectivement un problematic data action, en tenant compte de facteurs tels que la nature des données traitées (des données de santé ou de localisation présentent un potentiel de préjudice plus élevé que des données déjà publiques), le contexte de la collecte (une collecte transparente et attendue par la personne concernée présente un risque moindre qu'une collecte opaque ou inattendue), et les contrôles déjà en place pour limiter les usages non anticipés.

## Estimer l'impact du préjudice sur les individus

En complément de la probabilité, l'organisation évalue l'**impact** du préjudice potentiel sur les individus concernés — un exercice qui rappelle directement celui déjà développé pour l'analyse d'impact relative à la protection des données (AIPD) dans le parcours RGPD de cette plateforme, ou pour l'appréciation des risques de sécurité dans ISO 27001, mais centré ici spécifiquement sur le préjudice pour la personne plutôt que sur l'impact pour l'organisation elle-même — une différence de perspective qui structure profondément la méthodologie du NIST Privacy Framework par rapport aux référentiels de sécurité plus classiques déjà étudiés dans cette plateforme.

## Une différence de perspective fondamentale : le risque pour l'individu, pas seulement pour l'organisation

Cette centration sur le préjudice pour la personne concernée, plutôt que sur le seul risque pour l'organisation (perte financière, atteinte réputationnelle, sanction réglementaire), constitue l'apport méthodologique le plus distinctif du NIST Privacy Framework parmi l'ensemble des référentiels déjà étudiés dans cette plateforme. La plupart des référentiels de sécurité — ISO 27001, NIST CSF, CIS Controls — structurent leur appréciation des risques autour de la question "quel est le risque pour mon organisation ?". Le NIST Privacy Framework pose une question complémentaire et distincte : "quel est le risque pour les personnes dont je traite les données ?" — une question qui rejoint directement l'esprit du RGPD, où les droits des personnes concernées occupent une place centrale, déjà développée dans le parcours dédié de cette plateforme.

## Comment cette double perspective se traduit dans la priorisation

Une organisation mature combine les deux perspectives pour prioriser ses actions : une data action à fort risque pour les individus mais à faible probabilité, et une data action à risque modéré pour les individus mais à forte probabilité et touchant un grand nombre de personnes, peuvent justifier un niveau de priorité comparable — un principe de priorisation par la combinaison de la probabilité et de la gravité déjà rencontré à de multiples reprises dans cette plateforme, notamment pour la matérialité de SOX ou la classification des risques d'EBIOS RM, ici appliqué à une échelle de préjudice centrée sur l'individu plutôt que sur l'organisation.

## Ce que cette méthodologie produit concrètement

À l'issue de cette appréciation, l'organisation dispose d'une cartographie de ses data actions les plus susceptibles d'engendrer un préjudice significatif pour les personnes concernées — une cartographie qui alimente directement le choix des activités du Core à prioriser, développées au module suivant de ce parcours, de la même façon que l'appréciation des risques de sécurité alimente la sélection des contrôles pertinents dans ISO 27001 ou le NIST CSF.

## Le lien avec le module suivant

Cette méthodologie de risque, aussi rigoureuse soit-elle, ne prend tout son sens qu'une fois articulée avec le Core du NIST Privacy Framework — le catalogue structuré de fonctions, catégories et sous-catégories qui traduit cette compréhension du risque en actions concrètes de gestion, développé au module suivant de ce parcours.
