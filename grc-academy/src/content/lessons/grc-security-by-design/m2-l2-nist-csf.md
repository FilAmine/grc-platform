# NIST CSF 2.0 : les six fonctions

## Un cadre, pas une norme certifiable

Le **NIST Cybersecurity Framework (CSF)** n'est pas une certification comme ISO 27001 — c'est un **cadre de référence volontaire**, conçu pour être utilisé quel que soit le secteur ou la taille de l'organisation, afin de structurer une conversation commune sur la maturité cybersécurité. Sa force est sa simplicité de communication : il donne un vocabulaire partagé entre équipes techniques, direction et régulateurs, sans imposer une méthodologie de risque unique.

La version 2.0 (publiée en 2024) a marqué une évolution majeure par rapport à la version 1.1 : l'ajout d'une sixième fonction, **Govern**, et l'élargissement du champ d'application au-delà des seules infrastructures critiques.

## Les six fonctions

### Govern (Gouverner) — nouvelle en 2.0

Placée délibérément en amont des cinq autres, cette fonction couvre la stratégie de gestion des risques, les rôles et responsabilités, la politique, la supervision et la gestion des risques liés à la chaîne d'approvisionnement (supply chain). Son introduction reconnaît explicitement que la sécurité technique sans gouvernance claire ne tient pas dans la durée — un écho direct au module 1 de cette formation.

### Identify (Identifier)

Comprendre le contexte : inventaire des actifs (données, systèmes, personnes), évaluation des risques, identification des vulnérabilités. On ne peut pas protéger ce qu'on n'a pas identifié — un principe qui paraît trivial mais qui reste, en pratique, l'angle mort numéro un des organisations (shadow IT, bases de données oubliées, comptes de service jamais désactivés).

### Protect (Protéger)

Les mesures de sauvegarde préventives : gestion des identités et des accès, formation, protection des données, sécurité des plateformes (durcissement des systèmes), résilience de l'infrastructure. C'est la fonction où se concentre la majorité des contrôles Security by Design "classiques" (chiffrement, moindre privilège, segmentation).

### Detect (Détecter)

Identifier en temps utile qu'un événement de sécurité est en train de se produire : surveillance continue, analyse d'anomalies, détection d'intrusion. Sans cette fonction, "Protect" seule crée une fausse impression de sécurité — aucun contrôle préventif n'est efficace à 100 %, et la vitesse de détection conditionne directement l'ampleur de l'impact d'un incident.

### Respond (Répondre)

Contenir l'impact d'un incident détecté : plan de réponse à incident, communication (y compris réglementaire — notification RGPD sous 72h par exemple), analyse et atténuation.

### Recover (Se rétablir)

Restaurer les capacités ou services affectés : plan de continuité et de reprise d'activité, communication de rétablissement, intégration des enseignements tirés de l'incident dans le dispositif (boucle avec Govern et Identify).

## Les "Tiers" de maturité

NIST CSF évalue la maturité de l'implémentation de chaque fonction sur 4 niveaux (Tiers), indépendamment du contenu :

1. **Partiel** — gestion des risques ad hoc, réactive.
2. **Informé sur les risques** — pratiques approuvées mais pas formalisées en politique organisationnelle.
3. **Répétable** — politiques formalisées, mises à jour régulièrement selon les changements du contexte.
4. **Adaptatif** — amélioration continue basée sur les enseignements et une anticipation active de l'évolution des menaces.

Ces Tiers ne sont pas hiérarchiques au sens "il faut viser Tier 4 partout" — une organisation peut légitimement viser Tier 2 sur une fonction à faible enjeu et Tier 4 sur une fonction critique, selon son appétence au risque (encore une fois, une décision de gouvernance).

## Pourquoi NIST CSF et ISO 27001 se complètent

NIST CSF est souvent utilisé en amont, comme outil de communication stratégique et de cartographie de maturité avec la direction, tandis qu'ISO 27001 structure la mise en œuvre certifiable et auditable des contrôles. De nombreuses organisations maintiennent une table de correspondance (mapping) entre les fonctions NIST CSF et les contrôles de l'Annexe A d'ISO 27001, pour éviter de dupliquer le travail d'évaluation entre les deux référentiels — un sujet approfondi dans la leçon "Comparatif" de ce module.
