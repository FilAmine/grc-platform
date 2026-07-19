# Les trois niveaux de CMMC 2.0 (2/2) : les niveaux Advanced et Expert

## Le niveau 2 — Advanced : la protection des informations non classifiées contrôlées

Le **niveau 2 (Advanced)** s'applique aux contractants qui traitent des **informations non classifiées contrôlées (Controlled Unclassified Information — CUI)** — des informations qui, sans être classifiées au sens du secret défense, nécessitent néanmoins une protection particulière en vertu d'une loi, d'un règlement ou d'une politique fédérale : spécifications techniques d'équipements militaires, données de recherche et développement sensibles, ou informations logistiques critiques. Ce niveau constitue, pour l'écosystème CMMC, l'équivalent fonctionnel du niveau d'impact Modéré de FedRAMP développé dans le parcours dédié de cette plateforme — le niveau le plus fréquemment visé par la majorité des contractants manipulant des informations réellement sensibles.

## Le catalogue des 110 exigences de sécurité

Le niveau 2 repose sur l'intégralité des **110 exigences de sécurité** du catalogue NIST SP 800-171, développé en détail au module 2 de ce parcours — un catalogue substantiellement plus exigeant que les quinze exigences de base du niveau 1, couvrant quatorze familles de contrôles allant du contrôle d'accès à la protection des systèmes et des communications.

## Une méthode d'évaluation qui varie selon la criticité du programme

Contrairement au niveau 1, entièrement fondé sur l'auto-évaluation, le niveau 2 impose une méthode d'évaluation variable selon la criticité des informations concernées : pour la majorité des contrats impliquant des informations non classifiées contrôlées, une **évaluation par un organisme tiers accrédité (C3PAO)**, développée au module 3 de ce parcours, est exigée tous les trois ans ; pour un sous-ensemble plus restreint de programmes jugés moins critiques par le Department of Defense, une simple auto-évaluation annuelle demeure suffisante. Cette gradation de la rigueur d'évaluation selon la criticité du programme concerné rappelle directement celle déjà développée pour les voies d'évaluation de SWIFT CSP (audit interne ou évaluateur externe selon la taille et la maturité de l'organisation), développée dans le parcours dédié de cette plateforme.

## Le niveau 3 — Expert : les programmes les plus critiques de la défense

Le **niveau 3 (Expert)**, réservé aux contractants impliqués dans les programmes de défense les plus prioritaires et les plus exposés aux menaces les plus sophistiquées, ajoute aux 110 exigences du niveau 2 un ensemble de **pratiques renforcées supplémentaires** issues du catalogue NIST SP 800-172 — des exigences avancées de détection des menaces persistantes, de durcissement technique et de résilience face à des adversaires disposant de capacités étatiques, développées plus en détail au module 2 de ce parcours.

## Une évaluation exclusivement gouvernementale pour le niveau le plus élevé

Le niveau 3 impose une évaluation menée directement par le gouvernement fédéral lui-même, à travers le **Defense Industrial Base Cybersecurity Assessment Center (DIBCAC)**, plutôt que par un organisme tiers accrédité — une différence notable par rapport au niveau 2, qui rappelle celle déjà développée pour la voie du FedRAMP Board dans le parcours dédié de cette plateforme, réservée aux CSP à plus fort enjeu et jugée suffisamment stratégique pour justifier l'implication directe d'un organe centralisé plutôt que d'un évaluateur tiers classique — le niveau 3 de CMMC pousse cette logique à son terme en confiant l'évaluation elle-même à une entité gouvernementale plutôt qu'à un organisme accrédité privé.

## Un tableau de synthèse des trois niveaux

| Niveau | Public visé | Catalogue de référence | Méthode d'évaluation |
|---|---|---|---|
| 1 — Foundational | Informations contractuelles fédérales (FCI) | 15 exigences du FAR 52.204-21 | Auto-évaluation annuelle |
| 2 — Advanced | Informations non classifiées contrôlées (CUI) | 110 exigences de NIST SP 800-171 | C3PAO tous les 3 ans, ou auto-évaluation annuelle selon la criticité |
| 3 — Expert | Programmes de défense les plus critiques | NIST SP 800-171 + pratiques renforcées de NIST SP 800-172 | Évaluation gouvernementale par le DIBCAC |

## Pourquoi cette gradation à trois niveaux plutôt que cinq, comme dans la version initiale du programme

Cette simplification vers trois niveaux, plutôt que les cinq niveaux de la version initiale de CMMC, répond directement à une critique récurrente formulée par les acteurs de la base industrielle de défense — un dispositif trop complexe et trop coûteux risquait de décourager la participation des plus petites entreprises sous-traitantes, essentielles à la chaîne d'approvisionnement de la défense, au profit des seuls grands industriels disposant des ressources nécessaires pour absorber ce coût de conformité. Cette préoccupation de proportionnalité et d'accessibilité rappelle directement celle déjà développée pour les initiatives de simplification de PCI DSS ou pour la base de référence LI-SaaS de FedRAMP, développées dans les parcours dédiés de cette plateforme.

## Le lien avec le module suivant

Le catalogue NIST SP 800-171, socle technique du niveau 2 et fondation du niveau 3, mérite un développement méthodologique dédié — l'objet du module suivant de ce parcours.
