# NIST CSF : origines et philosophie

## Une origine réglementaire américaine, un usage devenu mondial

Le **NIST Cybersecurity Framework** trouve son origine dans l'**Executive Order 13636** signé par le président Obama en février 2013, "Improving Critical Infrastructure Cybersecurity". Le NIST (National Institute of Standards and Technology) a été chargé de développer, en collaboration avec le secteur privé, un cadre volontaire pour aider les opérateurs d'infrastructures critiques (énergie, finance, santé, transport) à gérer le risque cybersécurité.

La première version (**CSF 1.0**) a été publiée en 2014. Contrairement à beaucoup de cadres gouvernementaux, elle n'a pas été rédigée uniquement par des fonctionnaires : le NIST a organisé des ateliers ouverts avec des centaines d'organisations privées, ce qui explique en grande partie pourquoi le framework a été massivement adopté bien au-delà de son périmètre initial (infrastructures critiques américaines) — aujourd'hui utilisé par des organisations de toute taille et de tout secteur, dans le monde entier.

## L'évolution des versions

- **CSF 1.0 (2014)** — cinq fonctions (Identify, Protect, Detect, Respond, Recover), orienté infrastructures critiques.
- **CSF 1.1 (2018)** — ajout de contenu sur la gestion des risques de la chaîne d'approvisionnement (supply chain), clarification de l'usage des Tiers et des mesures de performance (self-assessment).
- **CSF 2.0 (février 2024)** — évolution majeure : ajout d'une sixième fonction (**Govern**), élargissement explicite du champ d'application à **toute organisation**, quel que soit le secteur ou la taille (le nom complet officiel a même retiré la référence spécifique aux infrastructures critiques), et introduction des **Community Profiles** et des **Quick Start Guides** pour différentes audiences.

Cette trajectoire n'est pas anecdotique : elle reflète un constat du NIST lui-même — la gouvernance (qui n'existait pas comme fonction dédiée dans les versions précédentes) est la condition sans laquelle les cinq autres fonctions restent des pratiques techniques déconnectées de la stratégie et des responsabilités de l'organisation.

## La philosophie du cadre : trois partis pris

### 1. Basé sur les résultats (outcome-based), pas prescriptif

Le CSF ne dit jamais "installez cet outil" ou "configurez ce paramètre précis" — il énonce des résultats attendus ("les identités et les accréditations sont gérées pour les utilisateurs, services et matériels autorisés"). Charge à chaque organisation de choisir *comment* atteindre ce résultat, selon son contexte, sa taille, ses moyens et son secteur. C'est ce qui permet au même cadre de s'appliquer aussi bien à une startup de cinq personnes qu'à un opérateur d'infrastructure critique.

### 2. Basé sur le risque, pas sur une checklist universelle

Le CSF ne prétend pas qu'une organisation doit atteindre le même niveau sur chaque résultat. C'est la fonction des **Tiers** et des **Profils** (modules suivants) : prioriser les résultats et le niveau de rigueur en fonction de l'appétence au risque et du contexte propre à l'organisation — exactement l'esprit de la gestion des risques déjà vue pour ISO 31000 ou EBIOS RM.

### 3. Un langage commun, pas une nouvelle taxonomie concurrente

Le CSF est explicitement conçu pour être **mappé** vers d'autres référentiels (ISO 27001, NIST SP 800-53, COBIT, PCI DSS...) plutôt que pour les remplacer. Chaque sous-catégorie du Core est accompagnée de **références informatives** vers ces référentiels — une organisation déjà engagée dans une démarche ISO 27001 peut utiliser le CSF comme couche de communication stratégique par-dessus son dispositif existant, sans dupliquer le travail.

## Les trois composants du cadre

Le CSF s'articule autour de trois éléments, développés dans les leçons suivantes de ce parcours :

1. **Le Core (Noyau)** — les fonctions, catégories et sous-catégories : *quoi* faire (module suivant, en détail fonction par fonction).
2. **Les Tiers** — *avec quelle rigueur* les pratiques de gestion des risques sont mises en œuvre.
3. **Les Profils** — *où en est* l'organisation aujourd'hui (Current Profile) et *où elle veut aller* (Target Profile), permettant une analyse d'écarts priorisée.

## Ce que le CSF n'est pas

- **Ce n'est pas une certification** — il n'existe pas d'audit officiel "certifié CSF 2.0" délivré par le NIST ou un organisme accrédité, contrairement à ISO 27001.
- **Ce n'est pas une loi** — son usage reste volontaire, sauf lorsqu'un contrat, un régulateur sectoriel ou une politique interne le rend obligatoire.
- **Ce n'est pas un remplaçant des référentiels techniques détaillés** — pour une configuration précise (durcissement d'un serveur, paramétrage IAM cloud), le CSF renvoie vers des références informatives plus prescriptives (NIST SP 800-53, CIS Benchmarks).

Comprendre cette philosophie avant d'étudier les fonctions elles-mêmes évite l'erreur la plus fréquente chez ceux qui découvrent le CSF : le lire comme une checklist de contrôles à cocher, alors qu'il a été conçu comme un outil de conversation stratégique sur le risque.
