# Le déroulement de l'audit : méthodes de test et types d'opinion

## Type I et Type II : au-delà de la définition de base

Le premier parcours de cette plateforme a déjà posé la distinction essentielle : Type I évalue la conception des contrôles à un instant donné, Type II évalue leur fonctionnement effectif sur une période d'observation. Cette leçon détaille comment un auditeur SOC 2 construit réellement cette évaluation.

## Les méthodes de test utilisées par l'auditeur

Pour évaluer si un contrôle fonctionne effectivement (pertinent surtout en Type II), un auditeur SOC 2 combine plusieurs méthodes, empruntées aux normes d'audit générales :

- **Enquête (inquiry)** — interroger le personnel responsable du contrôle sur son fonctionnement. La méthode la plus faible en valeur probante si utilisée seule : une déclaration verbale n'est jamais une preuve suffisante.
- **Observation** — observer directement le contrôle en cours d'exécution (par exemple, assister à une revue d'accès en direct). Fournit une assurance ponctuelle, mais ne garantit rien sur la constance du contrôle en dehors du moment observé.
- **Inspection** — examiner la documentation ou les preuves produites par le contrôle (tickets, journaux, captures d'écran de configuration, comptes rendus). La méthode la plus fréquemment utilisée en pratique.
- **Réexécution (reperformance)** — l'auditeur exécute lui-même à nouveau le contrôle pour vérifier qu'il produit le résultat attendu (par exemple, tenter de se connecter avec un compte désactivé pour vérifier que l'accès est effectivement bloqué). La méthode la plus rigoureuse, mais aussi la plus coûteuse en temps d'audit — réservée aux contrôles les plus critiques.

Un auditeur combine généralement plusieurs de ces méthodes pour un même contrôle, la robustesse de la conclusion augmentant avec le nombre et la diversité des méthodes utilisées.

## L'échantillonnage en Type II

Pour un contrôle récurrent sur toute la période d'audit (par exemple, "les nouveaux comptes sont approuvés avant activation"), l'auditeur ne vérifie presque jamais l'intégralité des occurrences — il prélève un **échantillon** représentatif, dont la taille dépend de la fréquence du contrôle (mensuelle, hebdomadaire, quotidienne) et du niveau de risque associé. Un contrôle exécuté quotidiennement sur une période de douze mois pourra ainsi être testé sur un échantillon de 25 à 45 occurrences selon les méthodologies statistiques d'audit couramment utilisées, plutôt que sur les centaines d'occurrences réelles — une pratique standard en audit financier, transposée telle quelle à SOC 2.

Ce principe d'échantillonnage a une conséquence pratique directe pour l'organisation auditée : la **qualité et la disponibilité de la documentation** de chaque occurrence du contrôle (et pas seulement son exécution réelle) conditionne directement la capacité à démontrer sa conformité lors de l'échantillonnage — un contrôle bien exécuté mais mal documenté produira une exception d'audit, presque aussi sûrement qu'un contrôle réellement défaillant.

## Les exceptions : ce qu'elles signifient réellement

Une **exception** est une occurrence, dans l'échantillon testé, où le contrôle n'a pas fonctionné comme attendu (par exemple, un compte désactivé trois jours après le départ effectif d'un salarié au lieu du jour même prévu par la procédure). Une exception n'invalide pas nécessairement l'ensemble du rapport — elle est documentée dans le rapport lui-même (développé au module 4), avec, le cas échéant, la réponse de la direction expliquant la cause et la mesure corrective prise. Un rapport SOC 2 contenant quelques exceptions ponctuelles et correctement traitées reste souvent perçu plus favorablement par un client averti qu'un rapport prétendant une conformité parfaite sans la moindre exception — signe, pour un lecteur expérimenté, d'un audit potentiellement peu approfondi plutôt que d'un dispositif réellement irréprochable.

## Les types d'opinion d'audit

À l'issue de l'examen, l'auditeur émet une opinion, selon une échelle standard aux normes d'attestation :

- **Opinion sans réserve (unqualified/unmodified)** — les contrôles décrits sont présentés fidèlement et, en Type II, ont fonctionné efficacement sur la période. L'opinion la plus favorable, la plus fréquente pour un rapport bien préparé.
- **Opinion avec réserve (qualified)** — une ou plusieurs exceptions ou déficiences significatives, mais limitées à un périmètre identifié, empêchent une opinion sans réserve sur ce périmètre précis, sans pour autant invalider l'ensemble du rapport.
- **Opinion défavorable (adverse)** — les contrôles décrits ne sont pas présentés fidèlement ou n'ont pas atteint leurs objectifs de manière significative et généralisée. Rare en pratique, car une organisation qui anticipe un tel résultat retarde généralement l'audit plutôt que de le laisser aboutir à cette conclusion.
- **Impossibilité de formuler une opinion (disclaimer)** — l'auditeur n'a pas pu obtenir suffisamment d'éléments probants pour fonder une opinion, par exemple si l'organisation ne parvient pas à produire les preuves nécessaires pendant l'audit.

## Ce que cette mécanique implique pour la préparation d'un audit

Comprendre cette mécanique de test — échantillonnage, méthodes de preuve, exceptions documentées plutôt qu'un jugement binaire pass/fail — change directement la manière de se préparer à un audit SOC 2 : l'enjeu n'est pas seulement d'avoir de bons contrôles, mais de savoir en produire la preuve, de façon cohérente, sur l'intégralité de la période couverte par l'audit — un sujet développé en détail au module 5 (préparation de l'audit) et directement lié à l'anatomie du rapport, objet de la leçon suivante.
