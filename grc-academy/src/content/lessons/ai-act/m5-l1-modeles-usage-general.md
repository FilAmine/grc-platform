# Les modèles d'IA à usage général (GPAI)

## Pourquoi la pyramide des risques ne suffit pas pour ces modèles

La pyramide des risques développée au module 1 de ce parcours catégorise les systèmes d'IA selon leur **finalité d'usage** précise — recrutement, évaluation de solvabilité, identification biométrique. Cette approche se heurte cependant à une limite pour les **modèles d'IA à usage général (General-Purpose AI — GPAI)** — des modèles fondamentaux, souvent entraînés sur des volumes massifs de données, capables d'être adaptés à un très large éventail de tâches en aval, sans que leur fournisseur d'origine ne puisse toujours anticiper l'ensemble des usages finaux qui en seront faits par des tiers. L'AI Act consacre ainsi un régime spécifique à ces modèles, distinct de la logique de catégorisation par cas d'usage développée au module 1 de ce parcours.

## Les obligations générales applicables à tout modèle GPAI

Tout fournisseur d'un modèle d'IA à usage général doit établir et tenir à jour une **documentation technique** décrivant le processus d'entraînement et de test du modèle ainsi que ses résultats d'évaluation, mettre à disposition des fournisseurs en aval qui intègrent ce modèle dans leurs propres systèmes une information suffisante pour leur permettre de comprendre les capacités et limites du modèle, et établir une **politique de respect du droit d'auteur** de l'Union européenne, notamment concernant les données utilisées pour l'entraînement du modèle. Cette dernière obligation, sans équivalent direct dans les référentiels de sécurité déjà étudiés dans cette plateforme, répond à une préoccupation spécifique aux modèles génératifs entraînés sur de vastes corpus de contenus potentiellement protégés par le droit d'auteur.

## Un régime renforcé pour les modèles présentant un risque systémique

L'AI Act ajoute des obligations substantiellement renforcées pour les modèles GPAI présentant un **risque systémique** — déterminé notamment par un seuil de puissance de calcul utilisée pour leur entraînement (fixé à 10^25 FLOPs, une unité de mesure de la puissance de calcul), ou par une désignation explicite de la Commission européenne compte tenu de l'impact du modèle sur le marché intérieur. Ces modèles doivent procéder à une **évaluation contradictoire (adversarial testing)** de leurs capacités et limites, documenter et signaler les incidents graves à la Commission européenne, et assurer un niveau de cybersécurité approprié pour le modèle et son infrastructure physique.

## Un parallèle avec les catégories de risque systémique déjà rencontrées dans cette plateforme

Cette distinction entre obligations générales et obligations renforcées pour les acteurs présentant un risque systémique rappelle directement celle déjà développée pour la supervision directe des prestataires TIC critiques (Lead Overseer) dans le parcours DORA de cette plateforme, ou pour le niveau d'impact Élevé de FedRAMP — un principe déjà établi à travers cette plateforme : plus l'ampleur potentielle des conséquences d'une défaillance est importante, compte tenu de l'échelle de déploiement ou de l'influence de marché de l'acteur concerné, plus la supervision et les obligations imposées deviennent strictes.

## Le lien avec les caractéristiques de l'IA digne de confiance du NIST AI RMF

Les obligations imposées aux modèles GPAI à risque systémique — évaluation contradictoire, documentation des incidents, cybersécurité renforcée — recoupent directement plusieurs des sept caractéristiques de l'IA digne de confiance déjà développées dans le parcours NIST AI RMF de cette plateforme, notamment la robustesse face aux entrées adverses et la sécurité du modèle lui-même contre l'extraction ou la manipulation non autorisée — une nouvelle illustration du rôle de référence méthodologique du NIST AI RMF déjà signalé au module 0 de ce parcours.

## Les codes de bonnes pratiques comme mécanisme de mise en conformité facilité

L'AI Act encourage l'élaboration de **codes de bonnes pratiques**, développés en collaboration entre les fournisseurs de modèles GPAI, la Commission européenne et les parties prenantes concernées, permettant de démontrer une présomption de conformité aux obligations du règlement sans devoir en apporter une preuve entièrement distincte pour chaque fournisseur — un mécanisme de mutualisation méthodologique qui rappelle directement celui déjà développé pour les profils sectoriels du NIST CSF et du NIST AI RMF, tous deux développés dans les parcours dédiés de cette plateforme.

## Un tableau de synthèse du régime GPAI

| Catégorie | Obligations |
|---|---|
| Tout modèle GPAI | Documentation technique, information des fournisseurs en aval, politique de respect du droit d'auteur |
| Modèle GPAI à risque systémique (seuil de calcul ou désignation) | Évaluation contradictoire, signalement des incidents graves, cybersécurité renforcée |

## Le lien avec le module suivant

Ce régime spécifique aux modèles GPAI, comme l'ensemble des obligations développées tout au long de ce parcours, s'inscrit dans une architecture de gouvernance institutionnelle et un régime de sanctions précis, développés au module suivant de ce parcours.
