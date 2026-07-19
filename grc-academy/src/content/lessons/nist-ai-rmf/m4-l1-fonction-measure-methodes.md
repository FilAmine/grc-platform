# La fonction Measure (1/2) : méthodes quantitatives et qualitatives

## Transformer les risques cartographiés en mesures concrètes

La fonction **Measure** consiste à employer des méthodes quantitatives, qualitatives, ou mixtes pour analyser, évaluer, comparer (benchmarker) et surveiller le risque IA et les impacts associés, identifiés lors de la fonction Map développée au module précédent de ce parcours. Là où Map répond à la question "quels risques ce système pourrait-il engendrer ?", Measure répond à la question bien plus opérationnelle "dans quelle mesure ces risques se matérialisent-ils réellement, et avec quelle ampleur ?" — une transition de l'identification vers la quantification déjà rencontrée, sous des formes variées, dans la plupart des référentiels de gestion des risques déjà étudiés dans cette plateforme.

## Les métriques de performance technique classiques

Measure couvre en premier lieu les métriques de performance technique traditionnelles de l'apprentissage automatique — précision, rappel, taux de faux positifs et de faux négatifs — mais insiste sur la nécessité de **désagréger ces métriques par sous-groupe démographique ou contextuel** plutôt que de se satisfaire d'une performance globale agrégée. Un modèle affichant une précision globale excellente peut dissimuler une performance nettement dégradée pour un sous-groupe spécifique de la population — un écart qui ne serait jamais détecté sans cette désagrégation systématique, et qui constitue précisément le mécanisme technique par lequel un biais systémique déjà évoqué au module 1 de ce parcours se traduit en préjudice concret pour les personnes concernées.

## Les métriques propres au risque sociotechnique

Au-delà des métriques de performance technique, Measure encourage le recours à des méthodes propres à l'évaluation du risque sociotechnique développé au module 1 de ce parcours — des tests d'équité (fairness testing) mesurant les écarts de traitement entre groupes démographiques selon différentes définitions statistiques de l'équité (parité démographique, égalité des chances, calibration), des évaluations de robustesse face à des entrées adverses délibérément conçues pour tromper le modèle, et des études qualitatives impliquant directement des utilisateurs réels ou des représentants des communautés potentiellement impactées, plutôt que de se limiter à des mesures purement statistiques déconnectées de l'expérience humaine réelle.

## Pourquoi les méthodes qualitatives restent indispensables

L'AI RMF insiste explicitement sur le fait que les méthodes purement quantitatives, aussi sophistiquées soient-elles, ne suffisent jamais à elles seules à capturer l'intégralité du risque sociotechnique d'un système d'IA — des entretiens structurés avec des utilisateurs réels, des groupes de discussion avec des représentants de communautés impactées, ou des évaluations par des experts du domaine d'application concerné permettent de détecter des risques que les seules métriques statistiques ne révèlent jamais, notamment les risques d'usage détourné ou de perte de confiance des utilisateurs envers le système. Cette insistance sur la complémentarité entre méthodes quantitatives et qualitatives rappelle, sans s'y confondre, celle déjà développée pour la combinaison de critères quantitatifs et qualitatifs dans l'appréciation de la matérialité au titre de SOX, développée dans le parcours dédié de cette plateforme.

## Le rôle des équipes TEVV (Test, Evaluation, Verification, Validation)

L'AI RMF désigne les équipes chargées de conduire ces activités de mesure sous l'acronyme **TEVV** — Test, Evaluation, Verification, Validation —, un rôle qui rejoint, dans sa fonction d'évaluation indépendante, celui déjà développé pour l'audit interne dans le parcours SOX, ou pour le 3PAO dans le parcours FedRAMP de cette plateforme, tous deux développés dans des parcours dédiés de cette plateforme. Une exigence d'indépendance de ces équipes TEVV vis-à-vis des équipes ayant conçu le modèle constitue une bonne pratique fortement recommandée par l'AI RMF, selon le même principe de séparation des rôles déjà rencontré à de multiples reprises dans cette plateforme.

## Le lien avec la leçon suivante

Ces méthodes de mesure, qu'elles soient quantitatives ou qualitatives, doivent encore être organisées en un dispositif structuré et récurrent plutôt qu'appliquées de façon ponctuelle — un dispositif de surveillance continue développé à la leçon suivante de ce parcours.
