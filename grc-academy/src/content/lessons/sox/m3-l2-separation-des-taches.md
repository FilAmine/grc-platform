# Les contrôles généraux informatiques (2/2) : la séparation des tâches

## Un principe déjà rencontré, ici appliqué aux systèmes financiers

Le premier parcours de cette plateforme a déjà mentionné la séparation des tâches (segregation of duties) comme principe général de gouvernance, et le parcours ISO 27001 a développé le contrôle 5.3 de l'Annexe A dans le même sens : séparer les tâches et domaines de responsabilité conflictuels pour réduire le risque de modification ou d'utilisation abusive non autorisée des actifs. Dans le contexte spécifique de SOX et des systèmes financiers, ce principe prend une importance particulièrement structurante — au point de constituer, en pratique, l'un des chantiers ITGC les plus lourds pour la plupart des organisations.

## Le risque au cœur de la séparation des tâches financières

Le risque que ce principe cherche à prévenir est direct : une personne disposant, au sein d'un système financier (typiquement un ERP), de **droits d'accès combinés incompatibles** pourrait commettre une fraude sans qu'aucun contrôle croisé ne l'en empêche — par exemple, une personne capable à la fois de **créer un fournisseur** dans le système et d'**approuver un paiement** vers ce même fournisseur pourrait créer un fournisseur fictif et s'approuver elle-même un paiement frauduleux, sans qu'aucune autre personne n'intervienne dans le processus pour détecter cette manipulation.

## Les combinaisons de droits classiquement surveillées

Les combinaisons de droits d'accès considérées comme incompatibles varient selon les processus métier, mais suivent des schémas récurrents largement documentés par la pratique d'audit :

- créer un fournisseur **et** approuver une facture ou un paiement vers ce fournisseur,
- créer un client **et** approuver un avoir ou une remise accordée à ce client,
- initier une transaction **et** l'approuver soi-même, sans intervention d'une seconde personne,
- modifier les paramètres de paie **et** approuver le traitement de la paie,
- avoir un accès administrateur système étendu **et** un accès fonctionnel aux modules financiers eux-mêmes, permettant de contourner les contrôles applicatifs par un accès technique de plus haut niveau.

Ce dernier cas de figure — un accès administrateur système cumulé à un accès fonctionnel financier — recoupe directement le principe de moindre privilège et la restriction des accès privilégiés déjà développés dans le contrôle 8.2 de l'Annexe A d'ISO 27001 et la famille IA de SP 800-53, tous deux développés dans les parcours précédents de cette plateforme, appliqués ici spécifiquement au risque de fraude financière plutôt qu'au seul risque de sécurité de l'information.

## Les matrices de séparation des tâches et les outils de surveillance automatisée

Compte tenu du volume de rôles et de combinaisons de droits possibles dans un ERP moderne (souvent plusieurs centaines de rôles fonctionnels distincts), une évaluation manuelle exhaustive des combinaisons incompatibles devient rapidement impraticable pour une organisation de taille significative. La pratique de référence consiste à construire une **matrice de séparation des tâches (SoD matrix)**, qui documente formellement l'ensemble des combinaisons de droits jugées incompatibles pour l'organisation, puis à s'appuyer sur des **outils de surveillance automatisée** (souvent intégrés directement à l'ERP ou proposés par des éditeurs spécialisés en gouvernance des accès) qui analysent en continu les droits effectivement attribués et alertent sur toute combinaison incompatible détectée.

Ce mécanisme de surveillance continue automatisée rappelle directement, dans son principe, les outils de Cloud Security Posture Management déjà évoqués dans le premier parcours de cette plateforme, ou le CIS Controls Self Assessment Tool développé dans le parcours dédié aux CIS Controls — une même logique de vérification continue par un outil automatisé, plutôt qu'un contrôle ponctuel et manuel réalisé une seule fois par an.

## Les mesures compensatoires quand la séparation des tâches n'est pas réalisable

Dans certaines organisations, en particulier les structures de taille modeste avec des équipes financières restreintes, une séparation des tâches complète peut s'avérer matériellement impossible — trop peu de personnes disponibles pour répartir des fonctions incompatibles entre des individus distincts. Dans ce cas, l'organisation doit mettre en œuvre des **contrôles compensatoires** : par exemple, une revue périodique et documentée, par une troisième personne indépendante, des transactions réalisées par une personne cumulant des droits incompatibles — un principe de compensation déjà rencontré sous des formes comparables à travers plusieurs référentiels de cette plateforme (les mesures compensatoires d'ISO 27001, l'approche personnalisée de PCI DSS, ou le mécanisme Required/Addressable de HIPAA), appliqué ici spécifiquement au risque de séparation des tâches financières.

## Ce que cette pratique révèle sur la centralité des ITGC dans un audit SOX

La séparation des tâches au sein des systèmes financiers constitue, en pratique, l'un des sujets les plus fréquemment cités dans les déficiences de contrôle relevées lors des audits SOX — un rappel que la fiabilité du reporting financier d'une organisation moderne ne peut jamais être dissociée de la rigueur de la gestion de ses accès informatiques, un principe qui referme la boucle ouverte au module précédent : les quatre domaines des ITGC ne sont jamais un sujet périphérique de la conformité SOX, ils en constituent une composante aussi structurante que les contrôles financiers eux-mêmes.
