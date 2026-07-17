# Construire une feuille de route réaliste vers la certification

## Une durée de projet typique, et pourquoi elle varie autant

Pour une organisation de taille moyenne qui n'a aucun dispositif de sécurité formalisé au départ, un projet de première certification ISO 27001 dure généralement entre **six et douze mois** entre le lancement effectif et l'audit Stage 2, hors délai administratif de programmation avec l'organisme de certification. Cette durée varie fortement selon :

- la maturité de sécurité déjà existante (une organisation qui applique déjà informellement une bonne partie des contrôles technologiques ira plus vite qu'une organisation qui part de zéro),
- la taille et la complexité du domaine d'application choisi (module 1) — un périmètre large et hétérogène allonge mécaniquement le projet,
- la disponibilité réelle des ressources internes dédiées, souvent sous-estimée en phase de cadrage.

## Les phases typiques d'un projet de première certification

### Phase 1 — Cadrage (4 à 6 semaines)

Définition du domaine d'application (clause 4.3), désignation d'un porteur de projet et d'un sponsor exécutif (donnant corps à la clause 5.1), premier état des lieux des pratiques existantes par rapport aux contrôles de l'Annexe A.

### Phase 2 — Appréciation des risques et SoA initiale (6 à 10 semaines)

Réalisation de la première appréciation des risques (clause 6.1.2), construction de la Déclaration d'Applicabilité initiale (module 5), identification des écarts par rapport aux contrôles retenus.

### Phase 3 — Mise en œuvre des contrôles manquants (variable, souvent la phase la plus longue)

Déploiement ou formalisation des contrôles identifiés comme manquants — cette phase varie le plus en durée, car elle dépend directement du nombre et de la nature des écarts identifiés en phase 2 : un écart purement documentaire (rédiger une politique déjà appliquée en pratique) se comble en jours, un écart technique structurant (déployer un dispositif de journalisation centralisée là où il n'existait pas) peut prendre plusieurs mois.

### Phase 4 — Rodage du système de management (2 à 3 mois minimum)

Cette phase est souvent sous-estimée voire oubliée dans la planification initiale : un auditeur de certification veut voir des **preuves d'application dans la durée**, pas seulement l'existence de procédures fraîchement rédigées. Un premier cycle d'audit interne (clause 9.2), une première revue de direction (clause 9.3) documentée avec de vraies décisions, quelques mois de tickets de revue d'accès ou de journaux d'incidents à présenter en échantillon lors du Stage 2 — rien de tout cela ne peut être produit convenablement en quelques semaines avant l'audit.

### Phase 5 — Audit de certification (Stage 1 puis Stage 2)

Généralement espacés de quelques semaines à quelques mois, selon le calendrier convenu avec l'organisme de certification et le temps nécessaire pour traiter d'éventuelles non-conformités relevées au Stage 1 avant le Stage 2.

## Les pièges de planification les plus fréquents

- **Sous-estimer la phase de rodage (Phase 4)** — c'est, de loin, l'erreur de planification la plus fréquente : une organisation qui enchaîne directement de la mise en œuvre des contrôles au Stage 2, sans laisser au système de management le temps de produire de vraies preuves de fonctionnement récurrent, s'expose à des non-conformités majeures évitables.
- **Choisir un domaine d'application trop large pour la première itération** — une bonne pratique consiste à certifier d'abord un périmètre resserré mais réellement maîtrisé (par exemple, la plateforme SaaS principale plutôt que l'ensemble des systèmes internes de l'entreprise), puis à étendre le domaine d'application lors d'un cycle ultérieur plutôt que de retarder indéfiniment la première certification en cherchant l'exhaustivité dès le départ.
- **Ne pas impliquer le sponsor exécutif au-delà du lancement** — un projet ISO 27001 qui perd le soutien actif de la direction en cours de route (clause 5.1) peine ensuite à obtenir les ressources nécessaires pour la phase de mise en œuvre, souvent la plus consommatrice de temps et de budget.
- **Traiter la Déclaration d'Applicabilité comme un livrable ponctuel** plutôt que comme un document vivant (module 5) — une SoA figée après le Stage 2 devient rapidement obsolète face à l'évolution normale du système d'information.

## Le rôle des ressources externes

Beaucoup d'organisations, en particulier pour une première certification, s'appuient sur un consultant ou un cabinet spécialisé pour accélérer le cadrage et éviter les erreurs de méthode les plus fréquentes (notamment la SoA "à l'envers" du module 5). Ce recours externe reste utile principalement pour la méthode et l'accélération initiale — il ne dispense jamais l'organisation de construire en interne la capacité à faire vivre le SMSI dans la durée (module 7), un consultant externe ne pouvant pas se substituer indéfiniment aux rôles internes (propriétaires de risques, auditeurs internes, sponsor exécutif) que la norme elle-même exige.

## En clôture de ce parcours

Ce parcours a couvert ISO 27001 de bout en bout : la structure des clauses 4 à 10, l'intégralité des 93 contrôles de l'Annexe A organisés par thème, la Déclaration d'Applicabilité qui relie risque et contrôles, le processus de certification et son cycle triennal, et enfin comment planifier et maintenir un tel dispositif dans la durée. Combiné aux deux autres parcours de cette plateforme — les fondamentaux GRC et Security by Design, et le NIST CSF 2.0 — vous disposez désormais d'une compréhension à la fois large (comment les référentiels s'articulent) et profonde (comment un référentiel majeur se met en œuvre concrètement, clause par clause et contrôle par contrôle).
