# La fonction Measure (2/2) : surveillance continue et suivi post-déploiement

## Pourquoi une mesure ponctuelle avant déploiement ne suffit jamais

La leçon précédente a développé les méthodes de mesure du risque IA, mais une mesure réalisée une seule fois avant le déploiement d'un système d'IA, aussi rigoureuse soit-elle, ne suffit jamais à garantir sa fiabilité dans la durée — un phénomène connu sous le nom de **dérive de modèle (model drift)**, par lequel les performances d'un modèle se dégradent progressivement à mesure que le contexte réel dans lequel il opère s'écarte des conditions présentes dans ses données d'entraînement d'origine. Ce phénomène rappelle directement le principe déjà développé pour la surveillance continue mensuelle de FedRAMP ou pour le programme d'exercices récurrent d'ISO 22301, développés dans les parcours dédiés de cette plateforme : un dispositif validé à un instant donné n'offre aucune garantie de rester pertinent indéfiniment sans surveillance continue.

## La surveillance post-déploiement comme extension de Measure

L'AI RMF impose ainsi que la fonction Measure se prolonge bien au-delà du déploiement initial d'un système d'IA, à travers une **surveillance continue** de ses performances réelles en production — comparer régulièrement les métriques désagréguées par sous-groupe, développées à la leçon précédente, à leurs valeurs de référence établies avant déploiement, afin de détecter toute dégradation ou tout écart émergent qui n'aurait pas été anticipé lors de l'évaluation initiale.

## Le rôle des retours d'utilisateurs et des mécanismes de signalement

Au-delà des seules métriques automatisées, Measure encourage la mise en place de mécanismes structurés permettant aux utilisateurs et aux personnes impactées de signaler des résultats jugés incorrects, injustes ou préjudiciables — un canal de remontée qui rejoint directement celui déjà développé pour la fonction Govern au module 2 de ce parcours, et qui constitue souvent la source de détection la plus précoce et la plus riche d'enseignements pour des risques que les métriques statistiques seules n'auraient jamais révélés, précisément parce que ces risques sociotechniques touchent des dimensions d'expérience humaine difficiles à quantifier a priori.

## Comparer ses performances à des références externes (benchmarking)

Measure encourage également le recours à des jeux de données et des protocoles d'évaluation standardisés, reconnus par la communauté de recherche en intelligence artificielle, permettant de comparer les performances d'un système donné à celles d'autres systèmes similaires ou à des seuils de référence sectoriels — une pratique de benchmarking qui rappelle, dans son principe de comparaison à une référence externe partagée, celle déjà développée pour les profils sectoriels du NIST CSF ou du NIST Privacy Framework, développés dans les parcours dédiés de cette plateforme.

## Ce que la fonction Measure ne peut jamais garantir à elle seule

Il est utile de rappeler, comme cela a déjà été fait pour la certification ISO 27001 ou ISO 22301 dans les parcours dédiés de cette plateforme, que la fonction Measure, aussi rigoureuse soit-elle, ne garantit jamais l'absence totale de préjudice futur — elle permet de détecter et de quantifier les risques connus et mesurables, mais la nature émergente du risque sociotechnique développée au module 1 de ce parcours implique qu'un système d'IA peut toujours révéler, en conditions réelles d'usage à grande échelle, des risques qu'aucune méthode de mesure, aussi sophistiquée soit-elle, n'aurait pu anticiper avec certitude absolue.

## Un tableau de synthèse des méthodes de mesure

| Méthode | Ce qu'elle révèle |
|---|---|
| Métriques désagrégées par sous-groupe | Écarts de performance dissimulés par une métrique globale agrégée |
| Tests d'équité et de robustesse | Vulnérabilité aux biais et aux entrées adverses |
| Méthodes qualitatives (entretiens, groupes de discussion) | Risques sociotechniques non capturés par les seules statistiques |
| Surveillance post-déploiement continue | Dérive de modèle et risques émergents en conditions réelles |
| Mécanismes de signalement des utilisateurs | Détection précoce de préjudices non anticipés |
| Benchmarking externe | Comparaison à des références sectorielles partagées |

## Le lien avec le module suivant

Une fois les risques mesurés, qu'ils soient anticipés ou révélés en cours d'exploitation, l'organisation doit encore décider comment les traiter concrètement — l'objet de la fonction Manage, développée au module suivant de ce parcours.
