# Les trois objectifs de sécurité (2/2) : détecter et réagir

## Objectif 3 — Détecter et réagir : accepter que la prévention seule ne suffit jamais

Le troisième objectif du CSCF part d'un principe déjà rencontré à de multiples reprises dans cette plateforme — la clause 9 et 10 d'ISO 27001, la fonction Detect du NIST CSF, ou les contrôles de détection déjà développés dans les CIS Controls — la prévention, aussi rigoureuse soit-elle, ne suffit jamais à elle seule à garantir l'absence totale d'incident : un dispositif mature doit également être capable de détecter rapidement une activité anormale et d'y réagir efficacement avant que ses conséquences ne deviennent irréversibles.

## Les contrôles clés de cet objectif

- **La journalisation et la surveillance (logging and monitoring)** des accès et des activités sur les systèmes SWIFT, avec une conservation suffisante des journaux pour permettre une investigation a posteriori en cas d'incident suspecté.
- **La détection d'anomalies dans les schémas de transaction habituels** — un utilisateur SWIFT type présente un profil de transactions relativement stable (montants typiques, destinataires habituels, plages horaires d'activité) ; un écart significatif par rapport à ce profil constitue un signal d'alerte précoce directement inspiré de l'enseignement de l'incident de la banque centrale du Bangladesh, où des transferts inhabituels par leur montant et leur destination auraient pu être détectés plus rapidement avec une surveillance adaptée.
- **La planification de la réponse aux incidents (cyber incident response planning)** — l'existence d'un plan documenté et testé de réponse à un incident affectant les systèmes SWIFT, avec des procédures précises de confinement, de notification et de coordination, y compris avec SWIFT elle-même et les contreparties bancaires potentiellement affectées par une transaction frauduleuse déjà émise.
- **Les scans de sécurité et tests de pénétration périodiques**, vérifiant que les contrôles des deux premiers objectifs restent effectivement opérants dans la durée plutôt que de rester une simple déclaration documentaire.

## Un parallèle direct avec la planification de crise déjà développée dans cette plateforme

Cette exigence de planification de la réponse aux incidents rejoint directement celle développée pour les plans de continuité et la structure de gestion de crise dans le parcours ISO 22301 de cette plateforme, ou pour la classification et la notification des incidents majeurs de DORA — un incident affectant les systèmes SWIFT présente cependant une urgence particulière et immédiate : une instruction de paiement frauduleuse, une fois émise et exécutée par la contrepartie destinataire, peut devenir extrêmement difficile, voire impossible, à récupérer au-delà d'une fenêtre de quelques heures — ce qui justifie une exigence de détection et de réaction en temps quasi réel, plus stricte que le rythme de détection généralement suffisant pour d'autres catégories d'incidents de sécurité de l'information.

## Pourquoi cet objectif ferme la boucle du dispositif CSCF

Les trois objectifs du CSCF, pris ensemble, couvrent ainsi l'intégralité du cycle de vie d'un incident potentiel : l'Objectif 1 réduit la probabilité qu'un attaquant parvienne à s'introduire dans l'environnement local ; l'Objectif 2 limite ce qu'un attaquant, même parvenu à s'introduire, pourrait accomplir avec des accès insuffisamment maîtrisés ; l'Objectif 3 garantit qu'une activité malveillante, si elle survient malgré tout, soit détectée et traitée avant que ses conséquences ne deviennent irréversibles — une architecture en profondeur (defense in depth) qui rappelle directement celle déjà développée pour la structure du NIST CSF 2.0 dans le parcours dédié de cette plateforme.

## Ce que révèle, une fois de plus, l'origine de ce référentiel

Chacun des trois objectifs du CSCF peut être directement rattaché à un enseignement précis de l'incident de la banque centrale du Bangladesh développé au module 0 de ce parcours — une segmentation réseau insuffisante (Objectif 1), des identifiants dérobés et des accès insuffisamment surveillés (Objectif 2), et l'absence de détection rapide de transactions manifestement anormales par leur montant et leur destination (Objectif 3). Ce constat confirme, une fois de plus, un principe déjà établi à travers cette plateforme : un référentiel sectoriel né d'un incident précis porte souvent, dans sa structure même, les traces directes de cet incident fondateur.

## Le lien avec le module suivant

Une fois ces contrôles implémentés selon le type d'architecture retenu (module 1 de ce parcours), l'utilisateur SWIFT doit encore attester formellement de sa conformité — un processus d'auto-attestation et d'évaluation indépendante développé au module suivant de ce parcours.
