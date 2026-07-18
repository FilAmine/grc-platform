# Les niveaux d'évaluation et les objectifs (1/2) : Assessment Levels et besoins de protection

## Trois niveaux d'évaluation, proportionnés au besoin de protection

TISAX distingue trois **niveaux d'évaluation (Assessment Levels — AL)**, chacun correspondant à un besoin de protection croissant de l'information traitée par le fournisseur évalué — un principe de proportionnalité déjà rencontré à de multiples reprises dans cette plateforme, notamment pour les niveaux d'impact FedRAMP (Faible/Modéré/Élevé) développés dans le parcours dédié, ou pour les niveaux de validation PCI DSS gradués selon le volume de transactions traité.

## Assessment Level 1 : l'auto-évaluation

Le niveau **AL1** repose sur une simple **auto-évaluation (self-assessment)** réalisée par le fournisseur lui-même, sans intervention obligatoire d'un tiers indépendant — un niveau réservé aux besoins de protection les plus faibles, généralement utilisé en interne par un groupe pour évaluer ses propres filiales, ou dans des contextes où le partenaire commercial n'exige pas de preuve indépendante. Ce niveau rappelle, dans son principe d'auto-déclaration sans vérification externe systématique, celui déjà rencontré pour les Self-Assessment Questionnaires (SAQ) des niveaux de validation les plus bas de PCI DSS, développés dans le parcours dédié de cette plateforme.

## Assessment Level 2 : la vérification de plausibilité

Le niveau **AL2** ajoute à l'auto-évaluation du fournisseur un contrôle de **plausibilité (plausibility check)** réalisé à distance par un Audit Provider accrédité (développé au module 3 de ce parcours) — un examen documentaire des preuves fournies par le fournisseur, sans visite sur site ni test technique approfondi des contrôles. Ce niveau intermédiaire convient à des besoins de protection modérés, où une simple déclaration non vérifiée serait insuffisante, sans pour autant justifier l'effort d'une évaluation complète sur site.

## Assessment Level 3 : l'évaluation complète sur site

Le niveau **AL3**, le plus exigeant, impose une **évaluation complète réalisée sur site** par un Audit Provider accrédité, incluant l'examen documentaire, des entretiens avec les équipes du fournisseur, et la vérification technique effective de l'implémentation des contrôles — un niveau réservé aux besoins de protection les plus élevés, généralement exigé pour les fournisseurs traitant des informations stratégiques (données de développement de véhicules non dévoilés, systèmes critiques pour la sécurité fonctionnelle). Ce niveau rappelle directement, dans sa rigueur méthodologique, l'évaluation sur site du 3PAO pour une autorisation FedRAMP de niveau Élevé, ou l'audit complet d'un cabinet CPA pour un rapport SOC 2 Type II, déjà développés dans les parcours dédiés de cette plateforme.

## Qui détermine le niveau d'évaluation requis

Contrairement à FedRAMP, où le niveau d'impact est généralement choisi par le CSP lui-même en fonction de son marché cible, le niveau d'évaluation TISAX requis d'un fournisseur est le plus souvent **imposé par le partenaire commercial (l'OEM ou un fournisseur de rang supérieur)** dans le cadre de sa propre appréciation du besoin de protection des informations partagées avec ce fournisseur — un fournisseur ne choisit ainsi généralement pas librement son niveau d'évaluation, mais répond à une exigence contractuelle précise formulée par son client au sein de la chaîne d'approvisionnement automobile.

## Un tableau de synthèse des trois niveaux

| Niveau | Méthode d'évaluation | Besoin de protection typique |
|---|---|---|
| AL1 | Auto-évaluation, sans vérification externe systématique | Faible, contextes internes à un groupe |
| AL2 | Auto-évaluation + contrôle de plausibilité à distance | Modéré |
| AL3 | Évaluation complète sur site par un Audit Provider accrédité | Élevé, informations stratégiques ou critiques |

## Le lien avec les objectifs d'évaluation, développés à la leçon suivante

Le niveau d'évaluation (AL1, AL2 ou AL3) détermine la rigueur méthodologique de l'évaluation, mais ne précise pas encore quel périmètre de critères du catalogue VDA ISA sera effectivement évalué — cette seconde dimension, les objectifs d'évaluation (Assessment Objectives) et les trois modules possibles (sécurité de l'information, protection des prototypes, protection des données), fait l'objet de la leçon suivante de ce parcours.
