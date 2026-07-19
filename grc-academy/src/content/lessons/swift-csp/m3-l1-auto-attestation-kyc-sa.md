# L'auto-attestation et l'évaluation indépendante (1/2) : le processus KYC-SA

## Une obligation annuelle pour tout utilisateur du réseau

Chaque utilisateur SWIFT doit soumettre, une fois par an, une **attestation de conformité (Know Your Customer Security Attestation — KYC-SA)** au regard du CSCF applicable à son type d'architecture (module 1 de ce parcours), via une application dédiée hébergée sur le **KYC Registry** de SWIFT, développé plus en détail au module 4 de ce parcours. Cette obligation annuelle rappelle directement, dans son principe de renouvellement récurrent plutôt que ponctuel, celle déjà développée pour le cycle annuel de conformité SOX ou pour le renouvellement des labels TISAX dans les parcours dédiés de cette plateforme.

## Le contenu de l'attestation

L'attestation KYC-SA couvre, contrôle par contrôle, l'état d'implémentation de chacun des contrôles obligatoires du CSCF applicables au type d'architecture de l'utilisateur (module 1 de ce parcours) — pour chaque contrôle, l'utilisateur déclare s'il est pleinement implémenté, partiellement implémenté avec un plan de remédiation, ou non implémenté. Un utilisateur peut également déclarer l'implémentation des contrôles consultatifs, bien que cette déclaration reste facultative — une gradation qui rappelle celle déjà développée pour les niveaux de maturité 0 à 5 de TISAX, bien que structurée ici de façon plus binaire (implémenté / en remédiation / non implémenté) que l'échelle continue de maturité de TISAX.

## Le plan de remédiation pour les contrôles non pleinement implémentés

Pour tout contrôle obligatoire non pleinement implémenté, l'utilisateur doit documenter un **plan de remédiation** précisant les actions engagées et l'échéance visée pour parvenir à une conformité complète — un mécanisme qui rappelle directement celui du Plan of Action and Milestones (POA&M) déjà développé dans le parcours FedRAMP de cette plateforme, bien qu'à une échelle et avec un formalisme sensiblement plus légers, cohérents avec la nature d'auto-attestation plutôt que d'évaluation intégralement pilotée par un tiers.

## L'auto-évaluation comme point de départ, mais rarement suffisante seule

Contrairement à une simple déclaration sur l'honneur sans aucune vérification, l'attestation KYC-SA doit désormais être **corroborée** par l'une des deux voies développées à la leçon suivante de ce parcours — un audit interne indépendant de la fonction informatique, ou une évaluation par un assesseur externe qualifié — une exigence de vérification qui distingue le dispositif actuel de sa version initiale de 2016, où la simple auto-déclaration sans vérification tierce constituait le socle unique du dispositif, avant que SWIFT ne renforce progressivement l'exigence de corroboration à mesure que la maturité du programme progressait.

## Pourquoi cette évolution vers davantage de vérification était nécessaire

Cette évolution progressive, d'une simple auto-déclaration vers une attestation corroborée par une vérification indépendante, rappelle directement celle déjà rencontrée pour le renforcement des exigences de PCI DSS au fil de ses versions successives, ou pour l'ajout de l'évaluation indépendante 3PAO dans l'écosystème FedRAMP — une auto-déclaration non vérifiée, aussi bien intentionnée soit-elle, reste structurellement vulnérable au biais d'auto-évaluation optimiste, un phénomène déjà signalé à plusieurs reprises dans cette plateforme, notamment pour la distinction entre une Déclaration d'Applicabilité rédigée sérieusement et une SoA "de façade" dans le parcours ISO 27001.

## Le lien avec la leçon suivante

Cette exigence de corroboration par un audit interne indépendant ou par un assesseur externe qualifié constitue précisément l'objet de la leçon suivante de ce parcours, qui développe les deux voies possibles et leurs critères respectifs de qualification.
