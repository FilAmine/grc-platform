# La fonction Detect : identifier qu'un événement se produit

## Pourquoi Detect reste indispensable même avec un excellent Protect

Aucune mesure de protection n'est infaillible à 100 % — c'est un principe accepté dans toute discipline de gestion du risque mature. Detect part de ce postulat : l'objectif n'est pas seulement d'empêcher les incidents, mais de les **identifier le plus tôt possible** lorsqu'ils surviennent malgré tout, afin de limiter leur impact. Le temps moyen de détection d'une compromission reste, dans la plupart des études sectorielles, mesuré en semaines voire en mois lorsque cette fonction est faible — un délai qui multiplie directement le coût et l'ampleur d'un incident.

## Les catégories de Detect

### DE.CM — Surveillance continue (Continuous Monitoring)

Les actifs sont surveillés pour détecter des anomalies, des indicateurs de compromission et d'autres événements potentiellement adverses :

- Surveillance du trafic réseau pour détecter des schémas anormaux.
- Surveillance de l'activité des comptes à privilège (souvent la cible ou le vecteur d'une attaque avancée).
- Surveillance des environnements cloud, souvent négligée alors que les journaux d'activité cloud (CloudTrail, Activity Log, Cloud Audit Logs selon le fournisseur) sont une source de détection de premier plan pour des actions comme une modification de politique IAM inhabituelle.
- Surveillance de l'intégrité du code et des artefacts de déploiement (pertinent pour détecter une compromission de la chaîne d'approvisionnement logicielle, en écho direct à GV.SC).

### DE.AE — Analyse des événements adverses (Adverse Event Analysis)

Les événements anormaux sont analysés pour caractériser les incidents et déterminer une réponse adéquate :

- Corrélation d'événements provenant de sources multiples pour distinguer un faux positif d'un incident réel.
- Détermination de l'ampleur et de l'impact d'un événement détecté.
- Communication rapide des résultats de l'analyse aux parties prenantes pertinentes (préparant directement la transition vers Respond).

## Le piège du volume d'alertes sans capacité d'analyse

Un écueil très fréquent : déployer des outils de surveillance (DE.CM) produisant un volume d'alertes que l'équipe ne peut pas traiter (DE.AE insuffisant), ce qui aboutit paradoxalement à une **moins bonne** détection effective qu'un dispositif plus modeste mais correctement dimensionné pour être exploité. Le CSF, fidèle à sa philosophie basée sur le risque, n'impose pas un volume ou un type d'outil précis — il attend que l'organisation dimensionne DE.CM et DE.AE ensemble, en cohérence avec sa capacité réelle d'analyse, plutôt que d'accumuler des capteurs sans traitement en aval.

## Le lien avec Identify et Govern

L'efficacité de Detect dépend directement de la qualité d'Identify : on ne peut détecter une anomalie sur un actif que si l'on sait ce qu'est un comportement "normal" pour cet actif — ce qui suppose de l'avoir préalablement inventorié et classifié. De même, la stratégie de risque définie en Govern (GV.RM) devrait déterminer quels systèmes justifient une surveillance continue approfondie (systèmes critiques, données sensibles) et lesquels peuvent se contenter d'une surveillance plus légère — Detect n'est donc pas un chantier purement technique déconnecté des priorités de gouvernance.
