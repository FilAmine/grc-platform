# Le catalogue VDA ISA et les niveaux de maturité (2/2) : l'échelle de maturité 0 à 5

## Un modèle hérité du monde de l'évaluation des processus logiciels

Le catalogue VDA ISA évalue chaque contrôle selon une échelle de **niveaux de maturité allant de 0 à 5**, un modèle directement inspiré de la norme ISO/IEC 33001 sur l'évaluation des processus (elle-même héritière du modèle SPICE), et de la même famille conceptuelle que le modèle CMMI déjà mobilisé par COBIT pour ses propres niveaux de capacité, développés dans le parcours dédié de cette plateforme. Ce choix méthodologique n'est pas anodin : l'industrie automobile utilise ce même modèle de maturité pour l'évaluation de ses processus de développement logiciel via **Automotive SPICE**, une proximité méthodologique qui facilite la diffusion d'une culture commune de l'évaluation par maturité au sein du secteur.

## Les six niveaux de l'échelle

- **Niveau 0 — Incomplet** : le processus n'est pas mis en œuvre, ou échoue à atteindre son objectif.
- **Niveau 1 — Réalisé** : le processus est mis en œuvre et atteint son objectif, mais de façon largement informelle ou ad hoc.
- **Niveau 2 — Géré** : le processus est planifié, surveillé et ajusté ; les responsabilités sont définies.
- **Niveau 3 — Établi** : le processus repose sur un processus type documenté et standardisé, appliqué de façon cohérente à travers l'organisation.
- **Niveau 4 — Prévisible** : le processus est mesuré quantitativement et ses performances sont prévisibles.
- **Niveau 5 — Optimisant** : le processus fait l'objet d'une amélioration continue fondée sur des objectifs quantitatifs.

## Le niveau 3 comme seuil de référence généralement attendu

Bien que l'échelle complète compte six niveaux, la très grande majorité des évaluations TISAX visent et attendent, pour l'essentiel des critères du catalogue, un niveau de maturité **3 (Établi)** — un seuil qui correspond à l'existence de processus formalisés, documentés et appliqués de façon cohérente, sans nécessairement exiger la mesure quantitative et l'optimisation continue des niveaux 4 et 5, réservés en pratique aux organisations les plus matures ou aux critères jugés les plus critiques. Ce seuil de référence rappelle, dans son principe de "niveau raisonnable plutôt qu'excellence maximale sur tous les critères", celui déjà rencontré pour la logique de proportionnalité de plusieurs référentiels étudiés dans cette plateforme.

## Comment ce modèle se distingue de la logique binaire d'ISO 27001 ou de PCI DSS

Le parcours ISO 27001 de cette plateforme a développé une logique de certification largement binaire : un contrôle de l'Annexe A est soit implémenté de façon satisfaisante, soit non conforme, avec une éventuelle non-conformité mineure ou majeure selon sa gravité. TISAX adopte une logique sensiblement plus nuancée : un même contrôle peut être jugé "réalisé" mais insuffisamment "géré" ou "établi", ce qui permet à l'évaluation de refléter une trajectoire de progression plutôt qu'un simple verdict de conformité — une granularité d'appréciation qui se rapproche davantage du modèle de niveaux de capacité de COBIT que de la logique de certification ISO 27001 ou SOC 2.

## Ce que ce modèle de maturité implique pour la préparation d'un fournisseur

Un fournisseur qui se prépare à une évaluation TISAX doit ainsi anticiper non seulement l'existence de ses contrôles de sécurité, mais également le niveau de formalisation et de documentation de ces contrôles — un contrôle technique par ailleurs solide mais insuffisamment documenté ou appliqué de façon incohérente à travers l'organisation peut se voir attribuer un niveau de maturité inférieur au seuil attendu, malgré une réalité opérationnelle acceptable. Ce piège rejoint directement celui déjà signalé pour la nécessité de documenter, et pas seulement d'implémenter, les contrôles ITGC dans le parcours SOX de cette plateforme.

## Un tableau de synthèse de l'échelle

| Niveau | Nom | Ce qu'il implique concrètement |
|---|---|---|
| 0 | Incomplet | Processus absent ou n'atteignant pas son objectif |
| 1 | Réalisé | Objectif atteint, mais de façon informelle |
| 2 | Géré | Planifié, surveillé, responsabilités définies |
| 3 | Établi | Standardisé et documenté, appliqué de façon cohérente — seuil généralement attendu |
| 4 | Prévisible | Mesuré quantitativement |
| 5 | Optimisant | Amélioration continue fondée sur des objectifs quantitatifs |

## Le lien avec le module suivant

Ce modèle de maturité s'applique de façon différenciée selon le niveau d'évaluation TISAX visé par le fournisseur (Assessment Level) et le niveau de protection requis pour les informations qu'il traite — une distinction développée au module suivant de ce parcours.
