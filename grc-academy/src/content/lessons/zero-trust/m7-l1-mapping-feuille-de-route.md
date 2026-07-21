# L'architecture Zero Trust face aux autres référentiels, et une feuille de route de mise en œuvre

## Zero Trust comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | Zero Trust (SP 800-207) | NIST CSF | CIS Controls | ISO 27001 |
|---|---|---|---|---|
| Nature | Architecture technique de référence | Cadre volontaire de gouvernance | Catalogue de contrôles priorisés | Norme certifiable |
| Objet central | Comment structurer concrètement le contrôle d'accès et la segmentation | Gestion globale du risque de sécurité de l'information | Contrôles techniques priorisés par niveau de maturité | Système de management de la sécurité de l'information |
| Décision centrale | Aucune (architecture technique, non certifiable) | Aucune (outil de priorisation) | Aucune (catalogue de bonnes pratiques) | Certification par organisme accrédité |
| Niveau d'abstraction | Le plus concret et le plus technique | Généraliste, orienté gouvernance | Intermédiaire, contrôles techniques précis | Système de management, contrôles listés en Annexe A |

Ce tableau confirme un principe déjà établi à travers les parcours précédents de cette plateforme, sous un angle nouveau : Zero Trust ne concurrence jamais les référentiels de gouvernance déjà étudiés, il en constitue le prolongement technique le plus concret — répondant à la question "comment" là où le NIST CSF ou ISO 27001 répondent principalement à la question "quoi" et "pourquoi".

## Le mapping avec le NIST CSF

La fonction Protect du NIST CSF, déjà développée en détail dans le parcours dédié de cette plateforme, impose des résultats attendus en matière de gestion des identités et de contrôle d'accès, sans jamais prescrire une architecture technique précise pour les atteindre — Zero Trust fournit précisément cette réponse architecturale concrète, permettant à une organisation de satisfaire les objectifs de la fonction Protect à travers une implémentation cohérente et éprouvée plutôt que par des choix techniques ad hoc et potentiellement incohérents entre eux.

## Le mapping avec les CIS Controls

Plusieurs Safeguards des CIS Controls, déjà développés dans le parcours dédié de cette plateforme, notamment ceux relatifs à la gestion des accès et à la gestion de l'infrastructure réseau, trouvent une traduction architecturale directe dans les principes de Zero Trust développés au module 1 de ce parcours — une organisation ayant déjà priorisé ses investissements selon les Implementation Groups des CIS Controls dispose ainsi d'une feuille de route de contrôles techniques directement compatible avec une trajectoire de migration vers Zero Trust.

## Le mapping avec FedRAMP et CMMC pour le contexte fédéral américain

Les parcours FedRAMP et CMMC de cette plateforme ont développé des catalogues de contrôles (bases de référence cloud, SP 800-171) qui intègrent de plus en plus explicitement des exigences directement inspirées des principes Zero Trust, notamment sur l'authentification multifacteur systématique et la segmentation réseau rigoureuse — un fournisseur cloud ou un contractant de la défense engagé dans une trajectoire de migration Zero Trust dispose ainsi d'une base solide pour satisfaire ces exigences réglementaires, selon le principe de mapping plutôt que de duplication déjà rencontré à de multiples reprises dans cette plateforme.

## Le mapping avec DORA pour la résilience opérationnelle numérique

Une entité financière européenne soumise à DORA, déjà développé dans le parcours dédié de cette plateforme, peut directement intégrer une architecture Zero Trust au sein de son cadre de gestion des risques liés aux TIC — la réduction du mouvement latéral permise par la micro-segmentation, développée au module 3 de ce parcours, limite directement l'ampleur potentielle d'un incident majeur devant être notifié aux autorités de supervision au titre de DORA.

## Les pièges les plus fréquents dans une démarche Zero Trust

- **Considérer Zero Trust comme un produit à acheter plutôt qu'une architecture à concevoir** — un piège déjà signalé au module 0 de ce parcours, qui conduit à des déploiements technologiques disparates sans cohérence architecturale d'ensemble.
- **Négliger la cartographie préalable des flux de communication existants** — avant d'engager la micro-segmentation, un piège déjà signalé au module 4 de ce parcours, qui risque d'interrompre des flux légitimes essentiels.
- **Sous-estimer les menaces propres à l'architecture elle-même** — en négligeant la protection renforcée du Policy Engine et du Policy Administrator, un piège déjà signalé au module 5 de ce parcours.
- **Viser une migration uniforme plutôt que priorisée** — en tentant de faire progresser l'ensemble des cinq piliers du modèle CISA simultanément, plutôt que de concentrer l'effort sur les écarts les plus significatifs au regard du risque, un piège déjà signalé au module 6 de ce parcours.

## Une feuille de route réaliste de migration vers Zero Trust

1. **Cartographier le niveau de maturité actuel** selon les cinq piliers du modèle CISA (module 6).
2. **Renforcer la gestion des identités** — authentification multifacteur généralisée, centralisation des identités (module 4).
3. **Cartographier les flux de communication existants** pour les ressources les plus critiques (module 4).
4. **Concevoir l'architecture logique** — Policy Engine, Policy Administrator, Policy Enforcement Point — et l'algorithme de confiance approprié au contexte (module 2).
5. **Choisir la ou les approches de déploiement** adaptées à chaque catégorie de ressources et de demandeurs (module 3).
6. **Déployer une première micro-segmentation limitée** aux ressources prioritaires, puis étendre progressivement (module 3).
7. **Protéger spécifiquement les composants centraux** contre les menaces propres à l'architecture Zero Trust elle-même (module 5).

## En clôture de ce parcours

Ce parcours a couvert l'architecture Zero Trust de bout en bout : les sept principes fondamentaux qui rompent avec le modèle périmétrique traditionnel, l'architecture logique à trois composants (Policy Engine, Policy Administrator, Policy Enforcement Point) et l'algorithme de confiance qui oriente leurs décisions, les quatre approches de déploiement concrètes, la micro-segmentation et le périmètre défini par logiciel, la migration progressive depuis un modèle périmétrique existant, les menaces propres à l'architecture elle-même, le modèle de maturité de la CISA, et enfin son articulation avec le NIST CSF, les CIS Controls, FedRAMP, CMMC et DORA déjà étudiés dans cette plateforme. Combiné aux vingt-huit autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — de la gouvernance la plus généraliste jusqu'à l'architecture technique la plus concrète qui en traduit les objectifs en pratique quotidienne.
