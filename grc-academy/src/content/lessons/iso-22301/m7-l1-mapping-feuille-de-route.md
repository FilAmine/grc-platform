# ISO 22301 face aux autres référentiels, et une feuille de route de mise en œuvre

## ISO 22301 comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | ISO 22301 | ISO 27001 | DORA | ITIL (continuité des services) |
|---|---|---|---|---|
| Nature | Norme certifiable, système de management dédié | Norme certifiable, système de management dédié | Règlement européen obligatoire | Cadre de bonnes pratiques, non certifiable en tant que tel |
| Objet central | Continuité des activités essentielles, quelle qu'en soit la cause | Confidentialité, intégrité, disponibilité de l'information | Résilience opérationnelle numérique du secteur financier | Continuité opérationnelle des services informatiques |
| Outil méthodologique central | Analyse d'impact sur l'activité (BIA), RTO/RPO | Appréciation des risques, Annexe A | Cadre de gestion des risques liés aux TIC, TLPT | Pratique intégrée au Service Value System |
| Vérification de l'efficacité | Programme d'exercices (tabletop à grandeur nature) | Audit interne et de certification | Tests de résilience, dont les TLPT | Amélioration continue via le modèle ITIL |
| Sanction en cas de défaillance | Perte de certification, ou perte de marché contractuel | Perte de certification | Sanctions administratives, supervision directe des prestataires critiques | Sans sanction directe (bonnes pratiques) |

Ce tableau confirme un principe déjà établi à travers les parcours précédents de cette plateforme : quatre approches complémentaires plutôt que concurrentes de la résilience organisationnelle — une norme certifiable généraliste (ISO 22301), un règlement sectoriel obligatoire (DORA), et un cadre de bonnes pratiques opérationnelles (ITIL) peuvent coexister au sein d'une même organisation, chacun répondant à un besoin et un public différents.

## Le mapping avec ISO 27001 comme socle de gouvernance partagé

Comme développé au module 0 et au module 6 de ce parcours, la High Level Structure commune à ISO 22301 et ISO 27001 permet une intégration profonde entre les deux systèmes de management — une organisation déjà certifiée ISO 27001 réutilise directement sa structure de gouvernance (clauses 4 à 7), sa revue de direction et son programme d'audit interne, en y ajoutant les éléments spécifiques à la continuité (BIA, stratégies, plans, exercices) développés tout au long de ce parcours. Cette intégration rejoint directement le principe de mapping plutôt que de duplication déjà rencontré à de multiples reprises dans cette plateforme.

## Le mapping avec DORA pour le secteur financier

Une entité financière européenne soumise à DORA, déjà développé en détail dans le parcours dédié de cette plateforme, retrouve dans ISO 22301 une structure méthodologique directement transposable à ses propres obligations de résilience opérationnelle numérique — le cadre de gestion des risques liés aux TIC de DORA recoupe largement l'appréciation des risques d'ISO 22301, et les tests de résilience de DORA (dont les TLPT) recoupent le programme d'exercices développé au module 4 de ce parcours. Une certification ISO 22301 ne dispense jamais une entité financière de ses obligations légales directes au titre de DORA, mais constitue une base méthodologique solide et largement reconnue pour les construire.

## Le mapping avec ITIL pour la dimension opérationnelle informatique

Le parcours ITIL de cette plateforme a mentionné la pratique de gestion de la continuité des services parmi ses 34 pratiques — une pratique qui, dans une organisation mature, s'articule directement avec le volet systèmes d'information des stratégies et plans de continuité d'ISO 22301 développés aux modules 3 et 4 de ce parcours : les équipes ITIL portent l'exécution technique des plans de reprise après sinistre, tandis que le SMCA porte la gouvernance d'ensemble, la BIA et la coordination avec les activités métier non informatiques.

## Les pièges les plus fréquents dans une démarche ISO 22301

- **Réaliser une BIA superficielle ou purement théorique** — sans entretiens réels avec les responsables d'activité, aboutissant à des RTO irréalistes ou à une hiérarchisation des activités critiques déconnectée de la réalité opérationnelle.
- **Choisir des stratégies de continuité disproportionnées par rapport aux RTO réellement nécessaires** — un piège de sur-investissement déjà signalé au module 3 de ce parcours, ou à l'inverse un sous-investissement dangereux pour les activités réellement vitales.
- **Ne jamais tester au-delà de l'exercice sur table** — un SMCA qui ne pratique que des exercices de discussion, sans jamais vérifier techniquement une restauration de sauvegarde ou un basculement réel, prend un risque de désillusion majeure le jour d'un incident véritable.
- **Laisser les plans de continuité devenir obsolètes** — un piège déjà signalé à de multiples reprises dans cette plateforme, particulièrement critique ici compte tenu du rôle des plans au moment précis où l'urgence ne laisse aucune place à l'improvisation.

## Une feuille de route réaliste de première certification

1. **Définir le domaine d'application** et obtenir l'engagement formel de la direction (module 1 de ce parcours).
2. **Conduire la BIA et l'appréciation des risques** à travers des entretiens réels avec les responsables de chaque activité (module 2).
3. **Choisir des stratégies de continuité proportionnées** aux RTO et RPO réellement nécessaires (module 3).
4. **Rédiger les plans de continuité et la structure de gestion de crise**, en veillant à leur caractère directement exécutable (module 3).
5. **Lancer un programme d'exercices progressif**, des exercices sur table vers des exercices plus réalistes à mesure que la maturité progresse (module 4).
6. **Mettre en place le dispositif de surveillance, d'audit interne et de revue de direction** (module 5).
7. **Engager l'audit de certification** (Stage 1 puis Stage 2) auprès d'un organisme accrédité (module 6).

## En clôture de ce parcours

Ce parcours a couvert ISO 22301 de bout en bout : ses origines dans BS 25999 et la High Level Structure partagée avec ISO 27001, les clauses 4 à 7 du système de management de la continuité d'activité, l'analyse d'impact sur l'activité et ses métriques clés (MTPD, RTO, RPO), l'appréciation des risques propre à la continuité, les stratégies de continuité et les plans opérationnels associés, la structure de gestion de crise, le programme d'exercices et de tests, les clauses 9 et 10 relatives à l'évaluation des performances et à l'amélioration continue, le processus de certification, et enfin son articulation avec ISO 27001, DORA et ITIL déjà étudiés dans cette plateforme. Combiné aux dix-sept autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — de la sécurité de l'information et de la conformité financière jusqu'à la capacité d'une organisation à traverser, et à apprendre de, ses crises les plus difficiles.
