# SOC 2 en profondeur : introduction et repères

## Pourquoi un parcours entier dédié à une seule attestation

Le premier parcours de cette plateforme traite SOC 2 en une seule leçon, au même niveau que ISO 27001, NIST CSF ou le RGPD. Ce parcours va beaucoup plus loin : il détaille la structure des Common Criteria, les cinq catégories de critères de confiance, le déroulement réel d'un audit, l'anatomie complète d'un rapport, et la manière de préparer et maintenir une démarche SOC 2 dans la durée — le niveau de détail nécessaire à quelqu'un qui doit réellement piloter un programme SOC 2, pas seulement en comprendre les grandes lignes.

## Une origine comptable, pas une origine "sécurité"

SOC 2 descend d'une lignée de normes d'audit américaines centrées, à l'origine, sur le contrôle interne comptable :

- **SAS 70** (Statement on Auditing Standards No. 70), norme historique utilisée dès les années 1990 pour auditer les contrôles des prestataires de services affectant les états financiers de leurs clients — mais fréquemment détournée à l'époque pour servir de preuve générale de sécurité, un usage pour lequel elle n'était pas conçue.
- **SSAE 16** (2011), puis **SSAE 18** (2017, norme actuellement en vigueur, codifiée dans les sections **AT-C 105 et AT-C 205** des normes d'attestation de l'AICPA) — ont clarifié et séparé les usages : SOC 1 pour le contrôle interne relatif au reporting financier, **SOC 2** spécifiquement pour les critères de confiance (Trust Services Criteria) que sont la sécurité, la disponibilité, l'intégrité de traitement, la confidentialité et la protection de la vie privée.

Cette origine comptable explique une différence structurante par rapport à ISO 27001 ou au CSF : SOC 2 reste, par construction, un exercice d'**audit financier appliqué à la sécurité**, mené selon des normes d'attestation professionnelles strictes, pas un référentiel de gestion des risques au sens d'ISO 31000 ou du NIST.

## Qui a le droit de réaliser un audit SOC 2

Un point structurant, souvent ignoré : un rapport SOC 2 ne peut être émis que par un **cabinet d'expertise comptable habilité (CPA firm)**, soumis aux règles d'indépendance du Code de déontologie professionnelle de l'AICPA. Contrairement à ISO 27001 (où l'organisme de certification est accrédité par un organisme national d'accréditation comme le COFRAC ou l'UKAS, vu dans le parcours ISO 27001 de cette plateforme), un cabinet SOC 2 est avant tout un cabinet d'audit financier, dont l'expertise en sécurité de l'information s'ajoute aux compétences comptables de base — une différence qui explique en partie pourquoi la qualité et la rigueur des audits SOC 2 peuvent varier sensiblement d'un cabinet à l'autre.

## Une attestation, pas une certification : une distinction qui a des conséquences concrètes

Répétée dans le premier parcours, cette distinction mérite d'être développée ici :

- Il n'existe **pas de certificat SOC 2** à afficher publiquement, ni de logo à apposer sur un site web (à la différence de SOC 3, développé au module 6).
- Le rapport est un document **à usage restreint (restricted use)** : il est destiné à la direction de l'organisation, à ses clients existants ou prospects informés (souvent sous accord de confidentialité), et aux régulateurs — pas au grand public.
- Le rapport contient une **opinion d'audit** (développée au module 3) qui peut être qualifiée, voire défavorable — contrairement à une certification ISO 27001 qui est binaire (certifié ou non certifié), un rapport SOC 2 peut documenter des exceptions tout en restant un rapport valide et utile.

## SOC 1, SOC 2, SOC 3 : une famille, pas un seul document

Le sigle SOC (System and Organization Controls) recouvre en réalité trois types de rapports bien distincts, dont seul le deuxième fait l'objet de ce parcours en détail (le module 6 y reviendra pour les distinguer précisément) :

- **SOC 1** — centré sur le contrôle interne relatif au reporting financier (ICFR) d'un prestataire de services, pertinent par exemple pour un prestataire de paie ou un administrateur de fonds.
- **SOC 2** — centré sur les Trust Services Criteria (sécurité, disponibilité, intégrité de traitement, confidentialité, vie privée), le sujet de ce parcours.
- **SOC 3** — un rapport dérivé de SOC 2, à diffusion publique, sans le détail des tests réalisés.

## Comment ce parcours est organisé

Huit modules structurent ce parcours : la structure des Common Criteria alignée sur le référentiel COSO (module 1), les cinq catégories de critères de confiance en détail (module 2), le déroulement de l'audit et les types d'opinion (module 3), l'anatomie complète d'un rapport SOC 2 (module 4), la préparation pratique d'un audit (module 5), la distinction avec SOC 1/SOC 3 et le mapping avec d'autres référentiels (module 6), et une feuille de route réaliste pour un premier programme SOC 2 (module 7).
