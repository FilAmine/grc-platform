# Contrôles organisationnels (2/2) : incidents, continuité et conformité

## Gestion des incidents de sécurité de l'information (5.24 à 5.28)

- **5.24 — Planification et préparation de la gestion des incidents de sécurité de l'information** : l'organisme planifie et prépare la gestion des incidents en définissant, établissant et communiquant les processus, rôles et responsabilités de gestion des incidents.
- **5.25 — Appréciation des événements de sécurité de l'information et prise de décision** : l'organisme évalue les événements de sécurité de l'information et décide s'ils doivent être classés comme incidents de sécurité de l'information.
- **5.26 — Réponse aux incidents de sécurité de l'information** : les incidents de sécurité de l'information sont traités conformément aux procédures documentées.
- **5.27 — Tirer des enseignements des incidents de sécurité de l'information** : les connaissances acquises à partir des incidents sont utilisées pour renforcer et améliorer les contrôles de sécurité de l'information — le contrôle qui institutionnalise la boucle de rétroaction post-incident, déjà rencontrée sous la forme de la fonction Recover du NIST CSF.
- **5.28 — Collecte de preuves** : l'organisme établit et met en œuvre des procédures pour l'identification, la collecte, l'acquisition et la préservation des preuves relatives aux événements de sécurité de l'information — essentiel pour toute suite judiciaire ou disciplinaire éventuelle, et pour la robustesse d'une analyse forensique.

## Continuité d'activité (5.29 à 5.30)

- **5.29 — Sécurité de l'information en cas de perturbation** : l'organisme planifie comment maintenir la sécurité de l'information à un niveau approprié en cas de perturbation.
- **5.30 — Préparation des TIC pour la continuité d'activité** *(nouveau en 2022)* : la préparation des technologies de l'information et de la communication est planifiée, mise en œuvre, maintenue et testée sur la base des objectifs de continuité d'activité et des exigences de continuité des TIC — un contrôle qui comble un vide de l'édition 2013, où la continuité informatique restait sous-spécifiée par rapport à la continuité d'activité au sens large.

## Exigences légales, réglementaires et contractuelles (5.31 à 5.34)

- **5.31 — Exigences légales, statutaires, réglementaires et contractuelles** : les exigences légales, statutaires, réglementaires et contractuelles pertinentes pour la sécurité de l'information, et l'approche de l'organisme pour les respecter, sont identifiées, documentées et tenues à jour — le contrôle qui institutionnalise la cartographie réglementaire.
- **5.32 — Droits de propriété intellectuelle** : l'organisme met en œuvre des procédures appropriées pour protéger les droits de propriété intellectuelle.
- **5.33 — Protection des enregistrements** : les enregistrements sont protégés contre la perte, la destruction, la falsification, l'accès non autorisé et la divulgation non autorisée.
- **5.34 — Protection de la vie privée et protection des données à caractère personnel** : l'organisme identifie et satisfait les exigences relatives à la préservation de la vie privée et à la protection des données à caractère personnel conformément aux lois et réglementations applicables et aux exigences contractuelles — le point de jonction direct entre ISO 27001 et le RGPD, déjà développé en détail dans le premier parcours de cette plateforme (module Privacy by Design). ISO 27001 ne remplace jamais une conformité RGPD complète (le règlement impose des obligations, comme les droits des personnes, que l'Annexe A ne couvre pas en détail), mais un SMSI bien construit fournit une bonne partie des mesures techniques et organisationnelles exigées par l'article 32 du RGPD.

## Revue indépendante et conformité technique (5.35 à 5.36)

- **5.35 — Revue indépendante de la sécurité de l'information** : l'approche de l'organisme en matière de gestion de la sécurité de l'information et sa mise en œuvre, y compris les personnes, les processus et les technologies, sont revues de manière indépendante à intervalles planifiés ou en cas de changement significatif — une exigence distincte de l'audit interne (clause 9.2), typiquement réalisée par une fonction ou un tiers encore plus détaché du fonctionnement quotidien du SMSI (proche, dans l'esprit, de la troisième ligne de maîtrise vue dans le premier parcours de cette plateforme).
- **5.36 — Conformité avec les politiques, règles et normes en matière de sécurité de l'information** : la conformité avec la politique de sécurité de l'information de l'organisme, les thématiques spécifiques et les normes est régulièrement revue.

## Procédures d'exploitation documentées (5.37)

- **5.37 — Procédures d'exploitation documentées** : les procédures d'exploitation pour les installations de traitement de l'information sont documentées et mises à la disposition du personnel qui en a besoin — le contrôle qui clôt le thème organisationnel, souvent négligé alors qu'il conditionne directement la reproductibilité des opérations de sécurité (que se passe-t-il si la personne qui connaît "de mémoire" une procédure critique est absente ou quitte l'organisation).

## Ce que ce deuxième bloc de contrôles organisationnels révèle

Contrairement au premier bloc (largement centré sur la définition de règles et de rôles), ce second bloc de contrôles organisationnels est presque entièrement tourné vers la **réactivité et la vérification dans la durée** : gérer un incident quand il survient, assurer la continuité quand une perturbation frappe, vérifier régulièrement (revue indépendante, conformité aux politiques) que le dispositif fonctionne réellement. C'est la même logique de boucle de rétroaction que les clauses 9 et 10 de la norme elle-même, appliquée ici au niveau opérationnel des contrôles plutôt qu'au niveau du système de management dans son ensemble.
