# CMMC face aux autres référentiels, et une feuille de route de mise en conformité

## CMMC comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | CMMC | FedRAMP | TISAX | SWIFT CSP |
|---|---|---|---|---|
| Marché visé | Base industrielle de défense américaine (DoD) | Agences civiles fédérales américaines | Industrie automobile européenne | Écosystème financier mondial (SWIFT) |
| Catalogue de contrôles | NIST SP 800-171 (et SP 800-172 pour le niveau 3) | SP 800-53 (bases de référence cloud) | VDA ISA | CSCF |
| Niveaux | 3 (Foundational, Advanced, Expert) | 3 + LI-SaaS (Faible, Modéré, Élevé) | 3 (AL1, AL2, AL3) | Non applicable (objectifs et contrôles) |
| Évaluateur indépendant | C3PAO (niveau 2), DIBCAC (niveau 3) | 3PAO | Audit Provider | Audit interne ou évaluateur externe |
| Registre centralisé | SPRS, accès restreint aux acteurs légitimes | FedRAMP Marketplace, public | Portail ENX, consentement bilatéral | KYC Registry, relation de correspondance |
| Gouvernance | Cyber-AB, sous supervision du DoD | FedRAMP PMO | ENX Association | SWIFT (coopérative) |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : la structure d'un dispositif de certification sectoriel — niveaux gradués, évaluateur tiers accrédité, registre centralisé de résultats — se retrouve, sous des formes adaptées à chaque contexte, à travers de nombreux écosystèmes distincts, qu'il s'agisse du gouvernement fédéral américain, de l'industrie automobile européenne, ou de la finance mondiale.

## Le mapping avec le NIST RMF comme socle méthodologique commun

Comme développé au module 2 de ce parcours, SP 800-171 constitue un sous-ensemble dérivé de SP 800-53, déjà développé en détail dans le parcours NIST RMF de cette plateforme — une organisation déjà familière du NIST RMF, ou disposant déjà d'un dispositif de sécurité aligné sur SP 800-53 pour d'autres besoins fédéraux, dispose ainsi d'une base méthodologique directement transposable pour satisfaire les exigences techniques de CMMC.

## Le mapping avec FedRAMP pour les fournisseurs servant simultanément les deux marchés fédéraux

Comme développé au module 0 de ce parcours, un fournisseur technologique d'envergure servant à la fois des agences civiles américaines et le Department of Defense doit fréquemment satisfaire simultanément FedRAMP et CMMC — les deux dispositifs partagent un socle technique largement commun (dérivé de SP 800-53), mais restent gouvernés par des organismes distincts (le FedRAMP PMO et le Cyber-AB) et répondent à des besoins contractuels différents, selon le même principe de mutualisation d'un socle technique commun plutôt que de construction de dispositifs entièrement cloisonnés déjà rencontré à de multiples reprises dans cette plateforme.

## Le mapping avec ISO 27001 pour les organisations déjà certifiées

Une organisation déjà certifiée ISO 27001, déjà développée dans le parcours dédié de cette plateforme, dispose d'un socle de contrôles techniques (gestion des accès, gestion des vulnérabilités, journalisation) directement réutilisable pour satisfaire une large part du catalogue SP 800-171 — bien que CMMC exige une documentation et une preuve spécifiques, propres à son propre processus d'évaluation, plutôt qu'une simple équivalence automatique entre les deux certifications.

## Les pièges les plus fréquents dans une démarche CMMC

- **Mal identifier le niveau de certification réellement requis** — un contractant qui sous-estimerait la sensibilité des informations qu'il traite pourrait se retrouver à devoir reprendre l'intégralité de son processus de certification à un niveau supérieur, un piège déjà signalé pour la catégorisation initiale à travers plusieurs parcours de cette plateforme.
- **Négliger la vérification du statut de ses propres sous-traitants** — en se concentrant uniquement sur sa propre certification, sans vérifier que le flow-down développé au module 5 de ce parcours est effectivement respecté par l'ensemble de sa chaîne d'approvisionnement.
- **Sous-estimer l'exigence de préservation des preuves après un incident** — en négligeant l'obligation de conservation de quatre-vingt-dix jours développée au module 6 de ce parcours, exposant l'organisation à un manquement distinct de l'incident lui-même.
- **Recourir excessivement au mécanisme de POA&M** — en tentant de différer la remédiation d'un trop grand nombre de lacunes plutôt que d'atteindre une conformité substantielle réelle avant l'évaluation, un piège déjà signalé au module 4 de ce parcours.

## Une feuille de route réaliste de première mise en conformité

1. **Déterminer précisément le niveau de certification requis**, en fonction de la nature des informations traitées (FCI ou CUI) et des exigences contractuelles spécifiques du client fédéral concerné (module 1).
2. **Réaliser une auto-évaluation préalable** au regard du catalogue applicable (les 15 exigences de base ou les 110 exigences de SP 800-171), en s'appuyant sur une certification ISO 27001 ou un alignement NIST RMF déjà existant (module 2).
3. **Combler les écarts identifiés**, en priorisant les pratiques jamais éligibles au POA&M (module 4).
4. **Choisir la voie d'évaluation appropriée** — auto-évaluation ou C3PAO selon la criticité du contrat concerné (module 3).
5. **Soumettre les résultats dans le SPRS** et vérifier le statut de conformité de ses propres sous-traitants (module 5).
6. **Mettre en place un dispositif de détection et de notification des incidents** conforme au délai de 72 heures de DFARS 252.204-7012 (module 6).
7. **Planifier le cycle de renouvellement triennal** (pour une certification C3PAO) ou annuel (pour une auto-évaluation), en anticipant l'évolution du catalogue SP 800-171 applicable.

## En clôture de ce parcours

Ce parcours a couvert CMMC de bout en bout : ses origines dans l'échec du modèle d'auto-attestation pure face aux pertes majeures d'informations sensibles de la base industrielle de défense, les trois niveaux de certification (Foundational, Advanced, Expert), le catalogue NIST SP 800-171 et les pratiques renforcées de SP 800-172, les voies d'évaluation (auto-évaluation, C3PAO, DIBCAC), le mécanisme du Plan of Action and Milestones et son encadrement strict, la cascade des exigences à travers la chaîne d'approvisionnement de la défense et le Supplier Performance Risk System, la clause DFARS 252.204-7012 et la notification des incidents, et enfin son articulation avec le NIST RMF, FedRAMP et ISO 27001 déjà étudiés dans cette plateforme. Combiné aux vingt-six autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — du gouvernement fédéral civil américain jusqu'à sa base industrielle de défense, en passant par l'ensemble des secteurs et des géographies déjà couverts par les parcours précédents.
