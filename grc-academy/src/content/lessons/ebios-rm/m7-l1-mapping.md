# EBIOS RM face aux autres méthodologies de gestion des risques

## Une comparaison qui referme la boucle ouverte dans le premier parcours

Le premier parcours de cette plateforme a présenté trois méthodologies de gestion des risques — ISO 31000, le NIST RMF, et EBIOS RM — sans les comparer en détail. Ce parcours ayant développé EBIOS RM en profondeur, le moment est venu d'établir cette comparaison précisément.

## EBIOS RM face à ISO 31000 et ISO 27005

**ISO 31000** pose des principes généraux de management du risque, applicables à tout type de risque (pas seulement numérique), sans imposer de méthode de cotation ou de structure d'atelier précise — une norme volontairement générique, comme déjà signalé dans le premier parcours de cette plateforme. **ISO 27005** décline ces principes spécifiquement à la sécurité de l'information, mais reste, elle aussi, formulée à un niveau de lignes directrices plutôt que de méthode opératoire détaillée.

EBIOS RM se positionne explicitement comme une **mise en œuvre concrète** de ces principes génériques, avec une méthode structurée en cinq ateliers précis (développés aux modules 1 à 5 de ce parcours), des concepts propres et bien définis (valeurs métier, biens supports, sources de risque, objectifs visés), et des livrables types. Une organisation qui doit démontrer une appréciation des risques conforme à la clause 6.1.2 d'ISO 27001 — déjà développée dans le parcours dédié de cette plateforme — peut directement s'appuyer sur les résultats d'une étude EBIOS RM pour la produire, sans avoir à construire une méthodologie de risque distincte à partir des seuls principes généraux d'ISO 31000.

## EBIOS RM face au NIST RMF

Le NIST RMF, développé en détail dans le parcours dédié de cette plateforme, partage avec EBIOS RM un même souci de structuration en étapes précises et de documentation rigoureuse — mais les deux méthodes divergent sensiblement dans leur philosophie. Le NIST RMF reste centré sur une logique de **catégorisation d'un système** (FIPS 199) puis de **sélection de contrôles** dans un catalogue détaillé (SP 800-53), une approche qui part davantage du système et de ses caractéristiques techniques. EBIOS RM part, à l'inverse, des **valeurs métier** et des **sources de risque** motivées, avec un accent particulier mis sur la construction de scénarios narratifs incluant explicitement l'écosystème — une différence de point de départ qui rejoint la distinction déjà établie dans le premier parcours de cette plateforme entre une approche "depuis la checklist" et une approche "depuis l'attaquant".

Ces deux méthodes ne sont cependant pas incompatibles : une organisation pourrait tout à fait utiliser EBIOS RM pour structurer son analyse de risque stratégique et l'identification des scénarios prioritaires, puis s'appuyer sur le catalogue SP 800-53 pour sélectionner les contrôles techniques précis qui traitent ces scénarios — un exemple de plus de la logique de mapping entre méthode de risque et catalogue de contrôles déjà observée à de multiples reprises dans cette plateforme.

## Un tableau de synthèse

| Aspect | EBIOS RM | ISO 31000/27005 | NIST RMF |
|---|---|---|---|
| Origine | ANSSI et Club EBIOS (France) | ISO (international) | NIST (fédéral américain) |
| Nature | Méthode structurée en 5 ateliers | Lignes directrices générales | Processus en 7 étapes lié à un catalogue de contrôles |
| Point de départ | Valeurs métier et sources de risque motivées | Contexte et critères de risque généraux | Catégorisation du système (FIPS 199) |
| Traitement de l'écosystème | Cartographie graphique explicite des parties prenantes comme vecteurs d'attaque (Atelier 3) | Traité de façon plus générale, sans méthode dédiée | Traité via la famille SR de SP 800-53 |
| Niveau de prescription | Modéré, méthode précise mais pas de catalogue de contrôles imposé | Faible, principes généraux | Élevé, catalogue de plus de 1000 contrôles |

## Ce que cette comparaison confirme sur la convergence des approches de gestion des risques

Cette comparaison confirme, une dernière fois pour ce qui concerne les méthodologies de gestion des risques, un principe déjà établi à de multiples reprises dans cette plateforme : les différentes méthodes convergent largement sur les grands principes de fond (identifier, analyser, évaluer, traiter, surveiller), tout en se distinguant par leur origine institutionnelle, leur degré de prescription, et surtout par l'angle privilégié pour aborder l'analyse — un système technique à catégoriser (NIST RMF), un principe général à décliner (ISO 31000/27005), ou une narration crédible centrée sur un attaquant motivé et son chemin d'attaque à travers l'écosystème (EBIOS RM). Le choix entre ces méthodes dépend moins de leur "supériorité" intrinsèque que du contexte réglementaire, culturel et organisationnel dans lequel l'analyse de risque doit être menée — un principe de contingence déjà rencontré à travers l'ensemble des douze parcours précédents de cette plateforme.
