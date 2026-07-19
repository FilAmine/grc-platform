# Le modèle de risque vie privée (1/2) : distinguer le risque vie privée du risque de sécurité

## Deux catégories de risque trop souvent confondues

La distinction déjà esquissée au module 0 de ce parcours mérite d'être développée précisément, tant elle constitue le fondement conceptuel de l'ensemble du NIST Privacy Framework. Le **risque de sécurité**, au cœur du NIST CSF déjà développé dans le parcours dédié de cette plateforme, naît d'un événement indésirable — une perte de confidentialité, d'intégrité ou de disponibilité d'un actif informationnel, provoquée par une menace exploitant une vulnérabilité. Le **risque vie privée**, à l'inverse, peut naître d'un traitement de données parfaitement autorisé, sécurisé et conforme à son objectif déclaré — le simple fait de traiter des données personnelles, même dans les règles, peut engendrer des conséquences problématiques pour les personnes concernées.

## Le concept central de "data action"

Le NIST Privacy Framework introduit le concept de **data action** — toute opération technique effectuée sur des données, qu'il s'agisse de leur collecte, leur stockage, leur transformation, leur partage ou leur suppression. Une organisation qui collecte des données de géolocalisation pour améliorer un service de navigation réalise une data action parfaitement légitime au regard de son objectif déclaré. Mais cette même data action peut, dans certaines circonstances, devenir une **problematic data action** — une action de traitement des données qui engendre un effet indésirable pour un ou plusieurs individus, indépendamment de toute défaillance de sécurité.

## Des exemples concrets de "problematic data actions"

Le NIST identifie plusieurs catégories de problematic data actions, dont plusieurs exemples permettent d'illustrer la distinction avec le risque de sécurité :

- **La réidentification** — combiner des données prétendument anonymisées avec d'autres sources pour réidentifier un individu, sans qu'aucune faille de sécurité technique n'ait jamais eu lieu.
- **L'usage inattendu (unanticipated uses)** — utiliser des données collectées pour un objectif précis à des fins que la personne concernée n'aurait jamais anticipées ni acceptées, même si ce nouvel usage reste techniquement sécurisé.
- **La discrimination algorithmique** — un système de décision automatisée, entraîné sur des données par ailleurs correctement sécurisées, peut produire des résultats discriminatoires envers certains groupes de personnes.
- **La surveillance excessive (surveillance)** — une collecte de données par ailleurs autorisée et sécurisée peut, par son ampleur ou sa granularité, engendrer un sentiment de surveillance disproportionné chez les personnes concernées, avec un effet dissuasif sur leur comportement.

## Pourquoi cette distinction change fondamentalement l'approche de gestion du risque

Cette distinction implique qu'une organisation peut satisfaire l'intégralité des exigences de sécurité de l'information déjà développées dans les parcours ISO 27001, NIST CSF ou CIS Controls de cette plateforme — chiffrement rigoureux, contrôle d'accès strict, journalisation complète — tout en générant un risque vie privée significatif, simplement parce que la nature ou l'ampleur du traitement de données lui-même pose un problème indépendamment de sa sécurité technique. Réciproquement, un incident de sécurité (une fuite de données) peut ou non engendrer un préjudice réel pour les personnes concernées selon la nature des données exposées — une fuite de données déjà publiques n'engendre pas le même risque vie privée qu'une fuite de données de santé sensibles, bien que les deux puissent constituer un même type d'incident de sécurité au sens du NIST CSF.

## Un parallèle avec la distinction déjà développée dans le parcours RGPD

Cette distinction rejoint, sans s'y confondre exactement, celle déjà développée dans le parcours RGPD de cette plateforme entre la sécurité du traitement (article 32) et les principes plus larges de licéité, loyauté et transparence (article 5) — un traitement de données peut être parfaitement sécurisé au sens de l'article 32 tout en étant déloyal ou disproportionné au sens de l'article 5. Le NIST Privacy Framework formalise cette même intuition à travers un vocabulaire méthodologique propre (data actions, problematic data actions) que le RGPD n'articule jamais de façon aussi explicite et outillée.

## Le lien avec la leçon suivante

Une fois cette distinction fondamentale posée, il reste à déterminer comment une organisation évalue concrètement la probabilité et la gravité de ces problematic data actions pour prioriser ses efforts de gestion du risque vie privée — l'objet de la méthodologie d'appréciation du risque, développée à la leçon suivante de ce parcours.
