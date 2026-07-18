# TISAX face aux autres référentiels, et une feuille de route de mise en conformité

## TISAX comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | TISAX | ISO 27001 | PCI DSS | RGPD |
|---|---|---|---|---|
| Nature | Dispositif contractuel sectoriel (automobile) | Norme certifiable volontaire | Dispositif contractuel sectoriel (cartes de paiement) | Règlement européen |
| Évaluateur indépendant | Audit Provider accrédité par l'ENX Association | Organisme de certification accrédité | Qualified Security Assessor (QSA) | Aucun (autorités de contrôle a posteriori) |
| Méthode de notation | Niveaux de maturité 0 à 5 par critère | Conforme / non conforme, avec gravité de non-conformité | Conforme / non conforme par exigence | Sans notation formalisée |
| Mode de diffusion des résultats | Partage explicite par consentement, portail ENX | Certificat, souvent publié par l'organisme certificateur | Attestation de conformité (AOC), diffusion contractuelle | Non applicable |
| Durée de validité | Généralement 3 ans | 3 ans, avec audits de surveillance annuels | 1 an, avec scans trimestriels | Non applicable (obligation continue) |
| Sanction en cas de non-conformité | Perte d'accès au marché automobile | Perte de la certification | Amendes contractuelles, révocation du droit d'accepter les paiements | Amendes administratives plafonnées |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : la nature de l'origine d'un référentiel — ici, une initiative purement privée et sectorielle de l'industrie automobile européenne — détermine directement son mode de gouvernance, sa méthode de notation et son mécanisme de sanction, sans qu'un fondement légal soit nécessaire pour produire un dispositif rigoureux et à fort enjeu commercial.

## Le mapping avec ISO 27001 comme socle de réutilisation documentaire

Comme développé au module 1 de ce parcours, une organisation déjà certifiée ISO 27001 dispose d'un socle de documentation (politiques de sécurité, procédures de gestion des accès, plan de continuité d'activité) directement réutilisable pour une évaluation TISAX portant sur l'objectif Sécurité de l'information — une stratégie de mapping plutôt que de duplication déjà rencontrée à de multiples reprises dans cette plateforme, notamment pour la réutilisation des contrôles ISO 27001 dans le cadre des ITGC de SOX, ou du socle CIS Controls dans le cadre de FedRAMP.

## Le mapping avec le RGPD pour l'objectif Protection des données

L'objectif d'évaluation Protection des données de TISAX, développé au module 2 de ce parcours, s'appuie directement sur les concepts du RGPD déjà développés en détail dans le parcours dédié de cette plateforme — un fournisseur automobile déjà doté d'un registre des traitements, d'une analyse d'impact relative à la protection des données (AIPD) et d'un dispositif de notification des violations conforme au RGPD dispose ainsi d'une base solide et largement transférable pour cet objectif d'évaluation spécifique.

## Le mapping avec PCI DSS comme référentiel contractuel comparable

TISAX et PCI DSS, tous deux d'origine strictement contractuelle et sectorielle, partagent une logique de gouvernance comparable — un catalogue de contrôles précis, un évaluateur tiers accrédité par l'organisme gérant le programme, une sanction purement commerciale en cas de manquement — qui permet à une organisation ayant déjà développé une culture de conformité à l'un de ces deux référentiels d'appréhender plus aisément les exigences de l'autre, malgré des catalogues de contrôles substantiellement différents sur le fond.

## Les pièges les plus fréquents dans une démarche TISAX

- **Sous-estimer l'exigence de documentation et de formalisation liée au modèle de maturité** — un contrôle technique par ailleurs solide mais insuffisamment documenté peut se voir attribuer un niveau de maturité inférieur au seuil de 3 généralement attendu, un piège déjà signalé au module 1 de ce parcours.
- **Ne pas anticiper le module de protection des prototypes lorsqu'il est requis** — des exigences physiques et organisationnelles entièrement nouvelles, sans documentation préexistante réutilisable, contrairement au module de sécurité de l'information.
- **Négliger la gestion du partage des labels sur le portail ENX** — un label obtenu mais jamais partagé avec le partenaire commercial qui l'exige reste, en pratique, sans effet vis-à-vis de ce partenaire.
- **Considérer le renouvellement triennal comme une simple formalité administrative** — alors qu'il s'agit d'une réévaluation intégrale selon la version la plus récente du catalogue VDA ISA alors en vigueur, un piège de sous-estimation de l'effort de renouvellement déjà signalé pour d'autres référentiels de cette plateforme.

## Une feuille de route réaliste de première évaluation

1. **Identifier précisément l'exigence formulée par le partenaire commercial** — niveau d'évaluation (AL1/AL2/AL3) et objectifs d'évaluation (sécurité de l'information, prototypes, données) réellement requis.
2. **Réaliser une auto-évaluation préalable** au regard du catalogue VDA ISA, en s'appuyant sur la documentation ISO 27001 existante le cas échéant.
3. **Sélectionner un Audit Provider accrédité** par l'ENX Association et planifier l'évaluation.
4. **Conduire l'évaluation** (documentaire, puis entretiens et vérifications sur site pour le niveau AL3) et établir un plan d'action pour tout critère en deçà du niveau de maturité attendu.
5. **Publier et partager le label** avec chaque partenaire commercial concerné via le portail ENX.
6. **Planifier le renouvellement** bien avant l'échéance triennale, en tenant compte de l'évolution éventuelle du catalogue applicable.

## En clôture de ce parcours

Ce parcours a couvert TISAX de bout en bout : ses origines dans la volonté de l'industrie automobile européenne de mutualiser les audits de sécurité entre OEM et fournisseurs, le catalogue VDA ISA et son modèle de maturité à six niveaux, les niveaux d'évaluation (AL1/AL2/AL3) et les trois objectifs d'évaluation modulaires, le processus d'évaluation et le rôle central des Audit Providers accrédités par l'ENX Association, le mécanisme de partage des labels par consentement explicite et leur durée de validité triennale, le module unique de protection des prototypes, les enjeux contractuels et l'absence de sanction légale directe, et enfin son articulation avec les autres référentiels déjà étudiés dans cette plateforme. Combiné aux seize autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — des dispositifs les plus anciens et les plus légaux (SOX, 2002) jusqu'aux mécanismes les plus contemporains et les plus strictement sectoriels et contractuels, comme TISAX.
