# Le NIST AI RMF face aux autres référentiels, et une feuille de route de mise en œuvre

## Le NIST AI RMF comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | NIST AI RMF | NIST CSF | NIST Privacy Framework | RGPD (article 22) |
|---|---|---|---|---|
| Nature | Cadre volontaire | Cadre volontaire | Cadre volontaire | Règlement européen obligatoire |
| Objet central | Risque sociotechnique des systèmes d'IA | Risque de sécurité de l'information | Risque vie privée pour les individus | Décision individuelle automatisée |
| Structure | Core (4 fonctions), Profils | Core (6 fonctions), Profils, Tiers | Core (5 fonctions), Profils, Tiers | Droit à l'intervention humaine, droit d'explication |
| Fonction transversale | Govern, explicitement transversal | Govern, ajouté en 2.0 | Govern-P | Non applicable |
| Sanction en cas de manquement | Aucune (outil volontaire) | Aucune (outil volontaire) | Aucune (outil volontaire) | Amendes administratives plafonnées |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : les cadres volontaires du NIST fournissent la méthodologie opérationnelle, tandis que les textes légaux comme le RGPD imposent les obligations contraignantes — l'un ne remplace jamais l'autre, mais l'articulation entre les deux permet à une organisation de structurer sa conformité légale sur une base méthodologique solide.

## Le mapping avec le NIST CSF et le NIST Privacy Framework

Comme développé tout au long de ce parcours, l'AI RMF partage avec ses deux prédécesseurs une même architecture générale (Core, Profils) et une même fonction transversale de gouvernance — une organisation ayant déjà déployé le NIST CSF et le NIST Privacy Framework, tous deux développés dans les parcours dédiés de cette plateforme, bénéficie ainsi d'une courbe d'apprentissage réduite pour adopter l'AI RMF, et peut directement réutiliser la caractéristique "sécurisé et résilient" de l'IA digne de confiance (développée au module 1 de ce parcours) en s'appuyant sur les contrôles déjà déployés au titre du CSF, ou la caractéristique "respectueux de la vie privée" en s'appuyant sur le Privacy Framework déjà déployé.

## Le mapping avec le règlement européen sur l'intelligence artificielle

Le règlement européen sur l'intelligence artificielle (AI Act), qui impose des obligations contraignantes de gestion des risques pour les systèmes d'IA classés à haut risque, s'inspire directement, dans sa structure méthodologique, de cadres de gestion du risque comparables à l'AI RMF — une organisation ayant déjà déployé l'AI RMF de façon rigoureuse dispose ainsi d'une base méthodologique substantielle pour satisfaire les exigences de gestion des risques de l'AI Act, sans que l'un ne se substitue jamais légalement à l'autre pour une organisation soumise au règlement européen — un rôle de référence méthodologique pour un texte légal ultérieur qui rappelle directement celui déjà observé pour le NIST CSF vis-à-vis de DORA, développé dans le parcours dédié de cette plateforme.

## Le mapping avec l'article 22 du RGPD sur la décision individuelle automatisée

Pour toute organisation européenne déployant un système de décision automatisée touchant des personnes physiques, l'article 22 du RGPD, déjà développé dans le parcours dédié de cette plateforme, impose un droit à l'intervention humaine et une forme de droit à l'explication pour les décisions produisant des effets juridiques ou significativement similaires. La fonction Map de l'AI RMF, en documentant précisément le degré d'autonomie d'un système et son contexte d'usage (module 3 de ce parcours), et la caractéristique d'explicabilité développée au module 1, fournissent directement les éléments méthodologiques nécessaires pour démontrer la conformité à cette exigence légale.

## Les pièges les plus fréquents dans une démarche AI RMF

- **Traiter Govern comme une étape préalable isolée plutôt que comme une fonction réellement transversale** — un piège déjà signalé au module 2 de ce parcours, qui prive l'organisation d'une vigilance continue face aux risques émergents.
- **Se limiter aux métriques de performance globale sans désagrégation par sous-groupe** — un piège déjà signalé au module 4 de ce parcours, qui dissimule des écarts de traitement discriminatoires derrière une performance moyenne satisfaisante.
- **Considérer une évaluation initiale comme suffisante sans surveillance post-déploiement** — en ignorant le phénomène de dérive de modèle déjà développé au module 4 de ce parcours.
- **Appliquer mécaniquement une liste générique de risques plutôt que de cartographier activement le contexte spécifique de chaque système** — un piège déjà signalé au module 3 de ce parcours.

## Une feuille de route réaliste de première mise en œuvre

1. **Établir la gouvernance transversale** au titre de Govern — désigner des responsabilités claires et associer une diversité de parties prenantes disciplinaires (module 2).
2. **Cartographier le contexte de chaque système d'IA** au titre de Map — objectif métier, contexte d'usage prévu, catégorisation du risque, parties prenantes impactées (module 3).
3. **Documenter structurellement le système et ses données d'entraînement**, à travers des fiches de modèle et de données (module 3).
4. **Mesurer les risques identifiés** à travers des métriques désagrégées, des tests d'équité et de robustesse, et des méthodes qualitatives impliquant des utilisateurs réels (module 4).
5. **Mettre en place une surveillance post-déploiement continue** et des mécanismes de signalement accessibles aux personnes impactées (module 4).
6. **Traiter les risques mesurés** selon les quatre options classiques (atténuer, transférer, éviter, accepter), en priorisant selon la gravité et la probabilité (module 5).
7. **Documenter un Profil par système ou cas d'usage**, et réitérer le cycle Map-Measure-Manage à mesure que le système évolue (module 6).

## En clôture de ce parcours

Ce parcours a couvert le NIST AI RMF de bout en bout : la nature sociotechnique et émergente du risque IA, le cycle de vie étendu des systèmes d'intelligence artificielle et les sept caractéristiques de l'IA digne de confiance, la fonction transversale Govern, la fonction Map et l'établissement du contexte, la fonction Measure et ses méthodes quantitatives et qualitatives, la fonction Manage et le traitement du risque, les Profils AI RMF et l'absence délibérée de Tiers, et enfin son articulation avec le NIST CSF, le NIST Privacy Framework et le règlement européen sur l'intelligence artificielle. Combiné aux vingt autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — de la gouvernance financière la plus ancienne étudiée ici jusqu'à la gestion du risque la plus contemporaine, celle des systèmes d'intelligence artificielle dont les conséquences, à la fois techniques et sociétales, continuent d'évoluer à mesure que ces systèmes se déploient à grande échelle.
