# Acteurs et écosystème : le rôle central du 3PAO

## Une architecture à cinq types d'acteurs

L'écosystème FedRAMP repose sur une répartition claire des responsabilités entre plusieurs acteurs distincts, dont l'articulation rappelle, dans son principe général, celle déjà développée pour les rôles nommément désignés du RMF dans le parcours dédié de cette plateforme (Authorizing Official, System Owner, ISSO, SAISO), tout en y ajoutant des acteurs propres au caractère centralisé et mutualisé du programme FedRAMP.

## Le Cloud Service Provider (CSP)

Le **CSP** est le fournisseur du service cloud candidat à l'autorisation — il porte la responsabilité première de l'implémentation des contrôles de la base de référence applicable (module 1 de ce parcours), de la rédaction du System Security Plan (SSP), et du maintien de la conformité dans la durée via la surveillance continue développée au module 4. Le CSP joue, dans l'écosystème FedRAMP, un rôle directement comparable à celui de l'organisation certifiée dans le parcours ISO 27001 ou de l'entité auditée dans le parcours SOC 2 de cette plateforme — à la différence près que la relation contractuelle et la décision finale d'autorisation impliquent ici une agence fédérale ou un organe collégial plutôt qu'un client privé.

## L'agence sponsor et le FedRAMP Board comme Authorizing Officials

Selon la voie d'autorisation empruntée (module 2 de ce parcours), c'est soit une **agence sponsor** spécifique, soit le **FedRAMP Board**, qui exerce la fonction d'Authorizing Official déjà développée dans le parcours NIST RMF — la décision formelle d'accepter le niveau de risque résiduel documenté dans le dossier de sécurité et d'accorder l'autorisation d'exploitation.

## Le Third-Party Assessment Organization (3PAO)

Le **3PAO** constitue l'acteur le plus spécifique à l'écosystème FedRAMP, et le plus structurant pour la crédibilité de l'ensemble du programme. Il s'agit d'un organisme d'évaluation indépendant, **accrédité spécifiquement pour FedRAMP** par un processus géré conjointement par le programme FedRAMP et un organisme d'accréditation dédié (le A2LA, American Association for Laboratory Accreditation, pour la compétence technique des évaluateurs) — une architecture d'accréditation à deux niveaux qui rappelle, par son principe de contrôle du contrôleur, celle déjà développée pour le PCAOB supervisant les cabinets d'audit dans le parcours SOX de cette plateforme, ou pour l'accréditation des organismes de certification ISO 27001 par un organisme national d'accréditation.

Le 3PAO réalise l'évaluation indépendante des contrôles implémentés par le CSP, produit le **Security Assessment Plan (SAP)** décrivant la méthodologie de test avant de commencer, puis le **Security Assessment Report (SAR)** documentant les résultats effectifs et toute faiblesse relevée — un rôle qui rappelle directement celui du Qualified Security Assessor (QSA) dans le parcours PCI DSS de cette plateforme, ou celui de l'auditeur SOC 2, à la différence que l'accréditation FedRAMP du 3PAO est gérée par un programme fédéral dédié plutôt que par une marque de cartes de paiement ou un institut national de comptables.

## Le rôle de l'ISSO côté CSP

À l'instar de l'Information System Security Officer déjà développé dans le parcours NIST RMF de cette plateforme, un CSP candidat à FedRAMP désigne généralement un **ISSO** chargé, au quotidien, de la mise en œuvre opérationnelle des contrôles, de la coordination avec le 3PAO lors des évaluations, et du suivi du POA&M — un rôle qui devient particulièrement chargé une fois l'autorisation obtenue, compte tenu du rythme de surveillance continue mensuel exigé par le programme (module 4 de ce parcours), sensiblement plus soutenu que le rythme annuel typique d'un audit de surveillance ISO 27001.

## Le FedRAMP Program Management Office (PMO)

Le **FedRAMP PMO**, hébergé au sein de la General Services Administration (GSA), joue un rôle de coordination d'ensemble du programme : il maintient le catalogue des bases de référence de contrôles, gère le processus d'accréditation des 3PAO, administre le FedRAMP Marketplace (module 5 de ce parcours), et publie les orientations méthodologiques applicables à l'ensemble de l'écosystème — un rôle de gouvernance centrale qui n'a pas d'équivalent exact parmi les référentiels de certification volontaire déjà étudiés dans cette plateforme, la plupart d'entre eux (ISO 27001, SOC 2) reposant sur un écosystème plus décentralisé d'organismes de certification ou de cabinets d'audit indépendants les uns des autres.

## Un tableau de synthèse des rôles

| Acteur | Rôle principal | Équivalent déjà rencontré dans cette plateforme |
|---|---|---|
| CSP | Implémente les contrôles, rédige le SSP | Organisation certifiée ISO 27001, entité auditée SOC 2 |
| Agence sponsor / FedRAMP Board | Décision d'autorisation (ATO / P-ATO) | Authorizing Official du RMF |
| 3PAO | Évaluation indépendante, SAP et SAR | QSA de PCI DSS, auditeur SOC 2, organisme de certification ISO 27001 |
| ISSO (côté CSP) | Mise en œuvre opérationnelle et suivi du POA&M | ISSO du RMF |
| FedRAMP PMO | Gouvernance et coordination du programme | Sans équivalent direct — rôle centralisé propre à FedRAMP |
