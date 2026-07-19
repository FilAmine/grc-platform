# Les obligations des systèmes à haut risque (2/2) : documentation, transparence et contrôle humain

## L'article 11 : la documentation technique

L'**article 11** impose l'élaboration d'une documentation technique complète avant la mise sur le marché d'un système à haut risque, décrivant son objectif, son architecture, les algorithmes utilisés, les données d'entraînement, les résultats des tests de performance, et les mesures de gestion des risques mises en œuvre au titre de l'article 9 développé à la leçon précédente de ce parcours. Cette documentation technique joue, pour l'AI Act, un rôle comparable à celui du System Security Plan de FedRAMP ou de la fiche de modèle (model card) déjà développée dans le parcours NIST AI RMF de cette plateforme — un document de référence structuré, condition indispensable pour toute évaluation de conformité ultérieure, développée au module 4 de ce parcours.

## L'article 12 : la journalisation automatique

L'**article 12** impose que les systèmes à haut risque permettent l'enregistrement automatique d'événements (journaux) tout au long de leur durée de fonctionnement, garantissant un niveau de traçabilité approprié pour identifier des situations susceptibles de présenter un risque ou de conduire à une modification substantielle du système. Cette exigence de journalisation rejoint directement celle déjà développée pour la surveillance continue de FedRAMP ou pour la journalisation exigée par l'Objectif 3 du CSCF de SWIFT CSP, tous deux développés dans les parcours dédiés de cette plateforme, ici appliquée spécifiquement à la traçabilité du fonctionnement d'un système d'IA plutôt qu'à la détection d'incidents de sécurité.

## L'article 13 : la transparence et les informations destinées aux déployeurs

L'**article 13** impose que les systèmes à haut risque soient accompagnés d'une notice d'utilisation complète et transparente, destinée aux déployeurs développés au module 3 de ce parcours, précisant l'identité du fournisseur, les caractéristiques et limites de performance du système, les circonstances susceptibles d'engendrer un risque, et le niveau de contrôle humain nécessaire pour son utilisation appropriée. Cette exigence de transparence envers le déployeur, distincte de la transparence envers l'utilisateur final développée pour les systèmes à risque limité au module 1 de ce parcours, rappelle la distinction déjà développée entre CUEC (contrôles complémentaires attendus de l'entité utilisatrice) des rapports SOC 1 et l'information du client final, dans le parcours SOX de cette plateforme — l'organisation qui déploie le système doit disposer d'une information suffisante pour assumer sa propre part de responsabilité.

## L'article 14 : le contrôle humain effectif

L'**article 14** impose qu'un système à haut risque soit conçu pour permettre un **contrôle humain effectif** pendant sa période d'utilisation — la capacité pour une personne physique de comprendre les capacités et limites du système, de surveiller correctement son fonctionnement, de décider de ne pas utiliser le système ou d'ignorer, annuler ou inverser sa sortie, et d'interrompre son fonctionnement par un dispositif d'arrêt. Cette exigence rejoint directement le droit à l'intervention humaine déjà développé pour l'article 22 du RGPD dans le parcours dédié de cette plateforme, mais l'étend à l'ensemble des systèmes à haut risque plutôt qu'aux seules décisions individuelles entièrement automatisées produisant des effets juridiques.

## L'article 15 : exactitude, robustesse et cybersécurité

L'**article 15** impose un niveau approprié d'exactitude, de robustesse et de cybersécurité, incluant une résilience face aux erreurs, aux défaillances ou aux incohérences pouvant survenir dans l'environnement d'exploitation, ainsi qu'une protection contre les tentatives de manipulation par des tiers exploitant les vulnérabilités propres à l'apprentissage automatique — les attaques par empoisonnement des données d'entraînement ou les entrées adverses déjà développées dans le parcours NIST AI RMF de cette plateforme. Cette exigence de cybersécurité recoupe directement les référentiels de sécurité de l'information déjà étudiés dans cette plateforme (ISO 27001, NIST CSF, CIS Controls), qu'un fournisseur peut directement mobiliser pour satisfaire cette obligation spécifique.

## Un tableau de synthèse des six obligations substantielles

| Article | Obligation | Parallèle déjà développé dans cette plateforme |
|---|---|---|
| 9 | Système de gestion des risques continu | Le cycle Map-Measure-Manage du NIST AI RMF |
| 10 | Gouvernance des données d'entraînement | Le risque de biais systémique du NIST AI RMF |
| 11 | Documentation technique complète | Le System Security Plan de FedRAMP, les fiches de modèle |
| 12 | Journalisation automatique | La surveillance continue de FedRAMP |
| 13 | Transparence envers les déployeurs | Les CUEC des rapports SOC 1 |
| 14 | Contrôle humain effectif | L'article 22 du RGPD |
| 15 | Exactitude, robustesse et cybersécurité | Les référentiels de sécurité de l'information déjà étudiés |

## Le lien avec le module suivant

Ces six obligations pèsent en premier lieu sur le fournisseur, mais l'AI Act répartit également des responsabilités précises sur d'autres acteurs de la chaîne — le déployeur, l'importateur, le distributeur — développés au module suivant de ce parcours.
