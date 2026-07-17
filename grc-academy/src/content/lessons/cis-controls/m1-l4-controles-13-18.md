# Les 18 contrôles (3/3) : contrôles 13 à 18 — détection, réponse et maturité

## Contrôle 13 — Surveillance et défense du réseau

Opérer des processus et des outils pour établir et maintenir une surveillance complète du réseau contre les menaces de sécurité à travers l'infrastructure et la base d'utilisateurs de l'entreprise. Ce contrôle prolonge directement le contrôle 12 (gestion de l'infrastructure réseau) vers une posture active de **détection** — recoupant la fonction Detect du NIST CSF et le Common Criterion CC7 de SOC 2, déjà développés dans les parcours précédents de cette plateforme.

## Contrôle 14 — Sensibilisation à la sécurité et formation des compétences

Établir et maintenir un programme de sensibilisation à la sécurité pour influencer le comportement de la main-d'œuvre afin qu'elle soit consciente de la sécurité et correctement formée pour réduire les risques de cybersécurité pour l'entreprise. Ce contrôle recoupe directement le contrôle 6.3 de l'Annexe A d'ISO 27001 et la catégorie PR.AT du NIST CSF, déjà développés dans les parcours précédents de cette plateforme — les Safeguards de ce contrôle précisent des thématiques concrètes de formation (reconnaissance du hameçonnage, gestion sécurisée des mots de passe, reconnaissance et signalement d'un incident) plutôt qu'une exigence générique de "sensibilisation".

## Contrôle 15 — Gestion des prestataires de services

Développer un processus pour évaluer les prestataires de services qui détiennent des données sensibles, ou sont responsables de la disponibilité de plateformes ou processus critiques pour l'entreprise, afin de s'assurer que ces prestataires protègent ces plateformes et ces données de manière appropriée. Ce contrôle, introduit comme domaine à part entière dans la révision v8, recoupe directement les contrôles 5.19 à 5.23 de l'Annexe A d'ISO 27001, la catégorie GV.SC du NIST CSF, le Common Criterion CC9.2 de SOC 2, et la famille SR de SP 800-53, déjà développés dans les parcours précédents de cette plateforme — une nouvelle confirmation de la convergence des référentiels majeurs sur l'importance croissante de la gestion des risques fournisseurs.

## Contrôle 16 — Sécurité des logiciels applicatifs

Gérer le cycle de vie de sécurité des logiciels développés, hébergés ou acquis en interne afin de prévenir, détecter et remédier aux faiblesses de sécurité avant qu'elles n'aient un impact sur l'entreprise. Ce contrôle recoupe directement le bloc de contrôles 8.25 à 8.34 de l'Annexe A d'ISO 27001 (développement sécurisé) et les principes Security by Design développés dans le premier parcours de cette plateforme (secure SDLC, threat modeling, tests de sécurité). Les Safeguards couvrent notamment l'inventaire des applications développées en interne, la formation des développeurs aux pratiques de codage sécurisé, et l'utilisation d'outils d'analyse statique et dynamique de sécurité applicative.

## Contrôle 17 — Gestion de la réponse aux incidents

Établir un programme pour développer et maintenir une capacité de réponse aux incidents (politiques, plans, procédures, rôles définis, formation, communications) pour se préparer, détecter et se remettre rapidement d'une attaque. Ce contrôle recoupe directement les contrôles 5.24 à 5.28 de l'Annexe A d'ISO 27001, les fonctions Respond et Recover du NIST CSF, et le Common Criterion CC7 de SOC 2, déjà développés dans les parcours précédents de cette plateforme — avec, comme pour ces référentiels, une insistance des Safeguards sur les **exercices réguliers** (simulations de crise) plutôt qu'un plan qui resterait uniquement théorique jusqu'à un incident réel.

## Contrôle 18 — Tests d'intrusion

Tester l'efficacité et la résilience des actifs de l'entreprise en identifiant et en exploitant les faiblesses des contrôles (personnes, processus, technologie), et en simulant les objectifs et les actions d'un attaquant. C'est le seul contrôle du référentiel entièrement consacré à une démarche de **vérification offensive** plutôt que défensive — un test d'intrusion cherche activement à contourner les dix-sept autres contrôles pour démontrer, de façon empirique, si les défenses mises en place résistent réellement à un attaquant motivé, plutôt que de se fier uniquement à leur conformité déclarative. Ce contrôle recoupe le contrôle 8.29 (tests de sécurité) et le contrôle 8.34 (protection des systèmes pendant les tests d'audit) de l'Annexe A d'ISO 27001, déjà développés dans le parcours dédié de cette plateforme.

## Ce que ce dernier bloc révèle sur la maturité croissante attendue

Ce troisième bloc de contrôles (13 à 18) se distingue par un degré de maturité organisationnelle généralement plus élevé que les deux blocs précédents : la surveillance active du réseau, la gestion structurée des prestataires, la sécurité applicative tout au long du cycle de développement, un programme de réponse aux incidents réellement exercé, et des tests d'intrusion réguliers supposent tous une organisation ayant déjà consolidé les fondations des contrôles 1 à 12. Ce n'est pas un hasard si la répartition des Safeguards de ces six derniers contrôles entre les Implementation Groups, développée dans la leçon suivante, penche nettement plus vers les niveaux IG2 et IG3 que vers le niveau IG1 — une confirmation supplémentaire de la logique de priorisation progressive qui structure l'ensemble du référentiel.
