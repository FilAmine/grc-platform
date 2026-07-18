# Les voies d'autorisation (2/2) : le FedRAMP Board et l'autorisation provisoire

## Une voie réservée aux CSP à forte demande potentielle

La seconde voie d'autorisation FedRAMP était historiquement pilotée par le **Joint Authorization Board (JAB)**, un conseil conjoint réunissant des représentants du Department of Defense, du Department of Homeland Security et de la General Services Administration — les trois agences fondatrices du programme FedRAMP. Depuis la consolidation légale du programme par la FedRAMP Authorization Act (développée au module 0 de ce parcours), cette fonction collégiale a évolué vers le **FedRAMP Board**, un organe de gouvernance élargi qui conserve néanmoins le même principe de fonctionnement : concentrer l'effort d'évaluation le plus rigoureux sur un nombre restreint de CSP jugés stratégiques pour l'ensemble de l'écosystème fédéral, plutôt que de laisser chaque agence répéter individuellement ce même travail.

## Le mécanisme de sélection et de priorisation

Contrairement à la voie Agence, où tout CSP disposant d'une agence sponsor peut engager le processus, l'accès à la voie du FedRAMP Board repose sur un mécanisme de **priorisation** : un CSP candidat soumet son dossier de candidature, et le FedRAMP Board sélectionne les CSP à accompagner en priorité selon des critères tels que la demande potentielle inter-agences déjà identifiée, la maturité de sécurité démontrée du CSP, et l'alignement avec les priorités technologiques du gouvernement fédéral du moment — un mécanisme de sélection qui n'a pas d'équivalent direct parmi les référentiels de certification volontaire déjà étudiés dans cette plateforme, la plupart d'entre eux (ISO 27001, SOC 2) restant ouverts à toute organisation qui en fait la demande à un organisme de certification ou un cabinet d'audit.

## L'autorisation provisoire (P-ATO) et sa nature juridique propre

À l'issue d'un processus d'évaluation rigoureux, comparable dans sa structure à celui de la voie Agence (SSP, évaluation 3PAO, SAR, POA&M), le FedRAMP Board délivre, en cas de conclusion favorable, une **Provisional Authorization to Operate (P-ATO)**. Le terme "provisoire" mérite d'être précisé : une P-ATO ne constitue pas, à elle seule, une autorisation opérationnelle définitive pour une agence donnée — elle représente une **déclaration de confiance collective** de la part du FedRAMP Board, que chaque agence fédérale intéressée peut ensuite adopter par réciprocité pour émettre sa propre ATO, sur la base du même dossier de sécurité, sans reconduire intégralement le processus d'évaluation déjà validé par le Board.

## Pourquoi cette distinction P-ATO / ATO structure tout l'écosystème FedRAMP

Cette distinction entre une évaluation centralisée rigoureuse (P-ATO du FedRAMP Board) et une décision d'autorisation propre à chaque agence utilisatrice (ATO) illustre le principe de réciprocité dans sa forme la plus institutionnalisée parmi l'ensemble des mécanismes de reconnaissance mutuelle déjà étudiés dans cette plateforme — comparable, dans son intention de mutualiser un audit coûteux entre de multiples parties prenantes, au principe des rapports SOC 1/SOC 2 réutilisés par de nombreux clients d'un même prestataire, déjà développé dans le parcours SOX de cette plateforme, mais porté ici à l'échelle de l'ensemble du gouvernement fédéral américain plutôt qu'à celle des clients d'un prestataire donné.

## Un tableau comparatif des deux voies

| Aspect | Voie Agence | Voie FedRAMP Board |
|---|---|---|
| Qui sponsorise le processus | Une agence fédérale spécifique | Le FedRAMP Board (sélection par priorisation) |
| Décision d'autorisation | ATO propre à l'agence sponsor | P-ATO collective, adoptée ensuite par chaque agence via une ATO propre |
| Accessibilité | Ouverte à tout CSP disposant d'une agence sponsor | Réservée aux CSP sélectionnés selon la demande potentielle et la maturité |
| Public visé typiquement | CSP à marché initial ciblé sur une ou quelques agences | CSP à fort potentiel de demande inter-agences |
| Reconnaissance perçue sur le marché fédéral | Solide mais parfois perçue comme moins immédiatement transférable | Considérée comme la référence de confiance la plus large du programme |

## Le lien avec le rôle du 3PAO, développé à la leçon suivante

Dans les deux voies d'autorisation, l'évaluation indépendante des contrôles reste confiée à un même type d'acteur accrédité — la Third-Party Assessment Organization (3PAO) — dont le rôle central dans l'ensemble de l'écosystème FedRAMP est développé au module suivant de ce parcours.
