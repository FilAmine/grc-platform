# FedRAMP face aux autres référentiels, et une feuille de route de mise en conformité

## FedRAMP comparé aux autres référentiels déjà étudiés dans cette plateforme

| Aspect | FedRAMP | ISO 27001 | SOC 2 | NIST RMF (générique) |
|---|---|---|---|---|
| Nature | Programme fédéral obligatoire pour vendre au gouvernement américain | Norme certifiable volontaire | Rapport d'attestation volontaire | Processus obligatoire (agences fédérales) |
| Catalogue de contrôles sous-jacent | SP 800-53 avec bases de référence cloud spécifiques | Annexe A (93 contrôles) | Common Criteria alignés COSO | SP 800-53 |
| Décision centrale | ATO (agence) ou P-ATO (FedRAMP Board) | Certification par organisme accrédité | Opinion d'audit par cabinet CPA | Autorisation par un AO |
| Évaluateur indépendant | 3PAO accrédité spécifiquement FedRAMP | Organisme de certification accrédité | Cabinet d'audit CPA | Évaluateur indépendant du RMF |
| Rythme de surveillance continue | Mensuel | Annuel (audit de surveillance) | Période d'observation de 6 à 12 mois | Continu, rythme variable selon le système |
| Marché visé | Gouvernement fédéral américain | International, tous secteurs | Principalement B2B nord-américain | Agences fédérales américaines |

Ce tableau confirme un principe déjà établi à travers l'ensemble des parcours précédents de cette plateforme : le niveau de prescription et la fréquence de surveillance d'un référentiel sont directement corrélés à la nature obligatoire ou volontaire de son origine — FedRAMP, né d'une politique puis d'une loi fédérale américaine destinée à protéger des systèmes gouvernementaux sensibles, impose logiquement le rythme de surveillance le plus soutenu et le catalogue de contrôles le plus volumineux parmi l'ensemble des référentiels étudiés dans cette plateforme.

## Le lien avec ISO 27001, SOC 2 et CIS Controls dans une stratégie de mapping

Un CSP qui vise simultanément FedRAMP, une certification ISO 27001 et un rapport SOC 2 Type II — une combinaison fréquente pour un fournisseur cloud d'envergure internationale, déjà signalée dans le parcours NIST RMF de cette plateforme — ne construit pas trois dispositifs de contrôles distincts : les contrôles techniques de base (gestion des accès, gestion des vulnérabilités, journalisation, chiffrement, réponse aux incidents), largement communs aux trois référentiels et également alignés sur les Safeguards des CIS Controls déjà développés dans le parcours dédié de cette plateforme, constituent un socle unique documenté différemment pour chaque processus d'évaluation — la stratégie de mapping plutôt que de duplication, un principe directeur constant de cette plateforme depuis ses tout premiers parcours.

## Le lien avec la gestion des risques de la chaîne d'approvisionnement

Une agence ou une organisation qui évalue un fournisseur cloud américain dans le cadre de sa propre gestion des risques de la chaîne d'approvisionnement — un exercice déjà développé dans le parcours DORA de cette plateforme pour les prestataires tiers critiques d'une entité financière, et dans la famille SR du RMF pour les agences fédérales elles-mêmes — peut directement s'appuyer sur le statut FedRAMP de ce fournisseur comme preuve substantielle de maturité de sécurité, réduisant d'autant l'effort de sa propre diligence raisonnable, selon le même principe de mutualisation de la preuve d'audit déjà rencontré à de multiples reprises dans cette plateforme.

## Les pièges les plus fréquents dans une démarche FedRAMP

- **Sous-estimer le volume de documentation du System Security Plan (SSP)** — un document qui peut atteindre plusieurs centaines de pages pour un système au niveau d'impact Élevé, et dont la rédaction initiale constitue souvent le poste de charge le plus sous-estimé par les CSP novices sur ce programme.
- **Ne pas anticiper la charge récurrente de la surveillance continue mensuelle** — un CSP qui dimensionne son équipe de conformité pour la seule phase d'autorisation initiale, sans anticiper l'effort continu développé au module 4 de ce parcours, se trouve rapidement dépassé une fois l'autorisation obtenue.
- **Choisir un niveau d'impact disproportionné par rapport au marché réellement visé** — viser d'emblée le niveau Élevé sans besoin client identifié à ce niveau immobilise des ressources considérables pour un bénéfice commercial incertain, un piège déjà signalé au module 1 de ce parcours.
- **Négliger la coordination entre les équipes techniques et l'ISSO lors des Significant Change Requests** — une évolution technique mise en œuvre sans notification préalable expose le CSP à une remise en cause de son autorisation, un piège rappelant celui déjà signalé pour les changements non maîtrisés dans le parcours SOX et le parcours ITIL de cette plateforme.

## Une feuille de route réaliste de première autorisation

1. **Choisir le niveau d'impact et la voie d'autorisation** en fonction du marché fédéral réellement ciblé (modules 1 et 2 de ce parcours), et identifier une agence sponsor ou candidater à la sélection du FedRAMP Board.
2. **Constituer une équipe de conformité dédiée**, incluant un ISSO et une coordination étroite avec les équipes d'ingénierie, avant même le lancement du processus d'évaluation.
3. **Rédiger le System Security Plan** en documentant précisément l'implémentation de chaque contrôle de la base de référence applicable.
4. **Sélectionner un 3PAO accrédité** et conduire l'évaluation indépendante (SAP puis SAR), en anticipant un délai réaliste souvent sous-estimé par les candidats novices.
5. **Établir le POA&M initial** pour toute faiblesse relevée, et engager la remédiation selon les échéances différenciées par gravité développées au module 4 de ce parcours.
6. **Obtenir la décision d'autorisation** (ATO ou P-ATO) et publier le statut au FedRAMP Marketplace développé au module 5.
7. **Dimensionner durablement l'équipe de conformité** pour le rythme de surveillance continue mensuel, condition de maintien de l'autorisation dans la durée.

## En clôture de ce parcours

Ce parcours a couvert FedRAMP de bout en bout : ses origines dans la politique "Cloud First" et le principe fondateur "do once, use many times", la catégorisation par niveaux d'impact et les bases de référence de contrôles adaptées au cloud, les deux voies d'autorisation (Agence et FedRAMP Board), les acteurs de l'écosystème et le rôle central du 3PAO, le dispositif de surveillance continue mensuelle et la gestion du POA&M, le FedRAMP Marketplace et le principe de réciprocité, les programmes apparentés (StateRAMP, les niveaux d'impact du DoD), et enfin son articulation avec les autres référentiels déjà étudiés dans cette plateforme. Combiné aux quinze autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — du contrôle interne financier le plus ancien étudié ici (SOX, 2002) jusqu'aux mécanismes d'autorisation cloud les plus contemporains du gouvernement fédéral américain.
