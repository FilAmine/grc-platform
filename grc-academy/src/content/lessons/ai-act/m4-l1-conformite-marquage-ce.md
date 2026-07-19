# L'évaluation de conformité et le marquage CE

## Un mécanisme hérité du droit européen de la sécurité des produits

L'AI Act s'inscrit directement dans la tradition du droit européen de la sécurité des produits — le Nouveau cadre législatif déjà évoqué au module 3 de ce parcours —, qui impose depuis des décennies un mécanisme d'évaluation de conformité et de marquage CE pour de nombreuses catégories de produits (jouets, machines, dispositifs médicaux) avant leur mise sur le marché européen. Un système à haut risque, développé au module 1 de ce parcours, doit ainsi faire l'objet d'une **évaluation de conformité** avant sa mise sur le marché, débouchant, en cas de résultat favorable, sur l'apposition du **marquage CE** et l'établissement d'une déclaration de conformité UE.

## Deux voies d'évaluation, selon la catégorie de système concernée

L'AI Act distingue deux voies d'évaluation de conformité, selon la nature du système à haut risque concerné :

- **Le contrôle interne (Annexe VI)** — pour la majorité des catégories de systèmes à haut risque de l'Annexe III déjà développée au module 1 de ce parcours, le fournisseur peut réaliser lui-même l'évaluation de conformité, en vérifiant que son système respecte les obligations substantielles développées au module 2, sans intervention obligatoire d'un tiers indépendant.
- **L'évaluation par un organisme notifié (Annexe VII)** — pour certaines catégories jugées particulièrement sensibles, notamment les systèmes d'identification biométrique, l'évaluation de conformité doit être réalisée par un **organisme notifié** — un tiers indépendant accrédité par un État membre, comparable dans sa fonction au 3PAO de FedRAMP ou à l'Audit Provider de TISAX, tous deux développés dans les parcours dédiés de cette plateforme.

## Pourquoi cette distinction rappelle une logique de proportionnalité déjà rencontrée dans cette plateforme

Cette gradation entre auto-évaluation et évaluation tierce obligatoire rappelle directement celle déjà développée pour les niveaux d'évaluation TISAX (auto-évaluation AL1, évaluation sur site AL3) ou pour les voies de corroboration du SWIFT CSP (audit interne ou évaluateur externe), toutes deux développées dans les parcours dédiés de cette plateforme — plus le risque intrinsèque d'une catégorie de système est jugé élevé par le législateur, plus l'intervention d'un tiers indépendant devient incontournable plutôt que simplement recommandée.

## Le rôle des organismes notifiés

Les **organismes notifiés**, accrédités par les autorités nationales compétentes de chaque État membre développées au module 6 de ce parcours, vérifient concrètement la conformité d'un système à haut risque aux exigences substantielles du règlement — examen de la documentation technique, vérification des méthodes de test, et pour certaines catégories, examen direct du système lui-même. Cette architecture d'accréditation nationale, reconnue à travers l'ensemble de l'Union européenne, rappelle directement celle déjà développée pour les organismes de certification accrédités d'ISO 27001 ou d'ISO 22301, développés dans les parcours dédiés de cette plateforme.

## Le marquage CE et la déclaration de conformité UE

À l'issue d'une évaluation de conformité favorable, le fournisseur appose le **marquage CE** sur le système ou sa documentation, et établit une **déclaration de conformité UE** attestant, sous sa propre responsabilité, du respect de l'ensemble des exigences applicables. Ce marquage joue, pour un système d'IA à haut risque, un rôle comparable à celui du label TISAX ou de l'attestation de conformité PCI DSS, développés dans les parcours dédiés de cette plateforme — une preuve reconnue et standardisée, permettant à un déployeur ou un distributeur de vérifier rapidement la conformité d'un système sans devoir reconduire lui-même l'intégralité de l'évaluation.

## L'enregistrement dans la base de données européenne

Avant sa mise sur le marché, un système à haut risque (à l'exception de certaines catégories utilisées à des fins répressives) doit être **enregistré dans une base de données publique européenne**, gérée par la Commission européenne, recensant l'ensemble des systèmes à haut risque déployés au sein de l'Union — un registre public qui rappelle, dans son principe de transparence centralisée, le FedRAMP Marketplace déjà développé dans le parcours dédié de cette plateforme, bien qu'appliqué ici à l'échelle de l'ensemble du marché européen plutôt qu'au seul gouvernement fédéral américain.

## Un tableau de synthèse du mécanisme de conformité

| Élément | Fonction |
|---|---|
| Contrôle interne (Annexe VI) | Auto-évaluation par le fournisseur pour la majorité des catégories à haut risque |
| Organisme notifié (Annexe VII) | Évaluation tierce obligatoire pour les catégories les plus sensibles (biométrie) |
| Marquage CE | Preuve standardisée de conformité, reconnue dans toute l'Union européenne |
| Base de données européenne | Registre public centralisé des systèmes à haut risque déployés |

## Le lien avec le module suivant

Ce mécanisme de conformité s'applique aux systèmes d'IA à haut risque destinés à un usage spécifique — mais l'AI Act consacre un régime distinct aux modèles d'IA à usage général, dont la polyvalence rend inadaptée l'approche par catégorie fixe de l'Annexe III — un régime développé au module suivant de ce parcours.
