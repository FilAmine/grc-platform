# Contrôles technologiques (2/2) : développement sécurisé et surveillance

## Journalisation et surveillance approfondies

- **8.16 — Activités de surveillance** *(nouveau en 2022)* : les réseaux, systèmes et applications sont surveillés pour détecter tout comportement anormal, et des mesures appropriées sont prises pour évaluer les incidents de sécurité de l'information potentiels — le contrôle qui institutionnalise ce que le NIST CSF appelle DE.CM (surveillance continue), étudié dans le deuxième parcours de cette plateforme. Son introduction en 2022 comble un vide notable de l'édition 2013 : la journalisation seule (8.15) ne suffit pas sans une activité de surveillance active exploitant ces journaux.
- **8.17 — Synchronisation des horloges** : les horloges des systèmes de traitement de l'information utilisés par l'organisme sont synchronisées sur des sources de référence temporelle approuvées — un contrôle en apparence anodin mais déterminant : sans horodatage cohérent entre systèmes, corréler des événements de sécurité provenant de sources différentes pendant une analyse d'incident devient nettement plus difficile, voire impossible.
- **8.18 — Utilisation de programmes utilitaires à privilèges** : l'utilisation de programmes utilitaires susceptibles de contourner les contrôles du système et de l'application est restreinte et étroitement contrôlée.
- **8.19 — Installation de logiciels sur des systèmes en exploitation** : des procédures et des mesures sont mises en œuvre pour gérer en toute sécurité l'installation de logiciels sur des systèmes en exploitation.

## Développement sécurisé (8.25 à 8.34)

Ce bloc de dix contrôles est le plus directement aligné avec les pratiques Security by Design développées en profondeur dans le premier parcours de cette plateforme.

- **8.25 — Cycle de vie de développement sécurisé** : des règles pour le développement sécurisé de logiciels et de systèmes sont établies et appliquées — le contrôle qui exige formellement un secure SDLC.
- **8.26 — Exigences de sécurité des applications** : les exigences de sécurité de l'information sont identifiées, spécifiées et approuvées lors du développement ou de l'acquisition d'applications.
- **8.27 — Principes d'architecture et d'ingénierie sécurisées** : des principes d'ingénierie de systèmes sécurisés sont établis, documentés, maintenus et appliqués à toute activité de développement de systèmes d'information — le point d'entrée normatif pour des principes comme la défense en profondeur, le moindre privilège ou le fail secure, développés en détail dans le premier parcours.
- **8.28 — Codage sécurisé** *(nouveau en 2022)* : des principes de codage sécurisé sont appliqués au développement logiciel — l'introduction de ce contrôle en 2022 reconnaît formellement que la sécurité du code source lui-même (pas seulement de l'architecture globale) mérite une exigence dédiée.
- **8.29 — Tests de sécurité dans le développement et la recette** : des processus de test de sécurité sont définis et mis en œuvre dans le cycle de vie de développement — couvrant SAST, DAST et les tests de recette de sécurité fonctionnelle.
- **8.30 — Développement externalisé** : l'organisme dirige, surveille et revoit les activités liées au développement de systèmes externalisé.
- **8.31 — Séparation des environnements de développement, de test et de production** : les environnements de développement, de test et de production sont séparés et sécurisés — un contrôle simple dans son principe mais dont le non-respect (données de production réutilisées telles quelles en environnement de test, sans masquage) reste une des causes de fuite de données les plus fréquentes en pratique.
- **8.32 — Gestion des changements** : les changements apportés aux moyens de traitement de l'information et aux systèmes d'information sont soumis à des procédures de gestion des changements.
- **8.33 — Informations de test** : les informations de test sont sélectionnées, protégées et gérées de manière appropriée — le point de jonction direct avec 8.31 et le masquage des données (8.11).
- **8.34 — Protection des systèmes d'information pendant les tests d'audit** : les tests d'audit et autres activités d'assurance impliquant l'évaluation des systèmes en exploitation sont planifiés et convenus entre le testeur et le management approprié — un contrôle qui encadre notamment les tests d'intrusion, pour éviter qu'un test légitime ne cause lui-même une interruption de service non prévue.

## Ce que révèle la structure de ce dernier bloc

Le bloc "développement sécurisé" est le plus long bloc thématique cohérent de tout le thème technologique (dix contrôles consécutifs, 8.25 à 8.34), ce qui reflète le poids croissant accordé par la révision 2022 à la sécurité applicative — historiquement moins développée dans l'édition 2013 par rapport aux contrôles d'infrastructure et de réseau. Un organisme dont l'activité principale est le développement logiciel (un éditeur SaaS, par exemple) trouvera dans ce bloc l'essentiel des contrôles réellement structurants pour son activité, bien plus que dans les contrôles physiques ou même une partie des contrôles réseau, moins déterminants pour une organisation "cloud native" sans infrastructure physique propre.

## Une synthèse des 93 contrôles avant d'aborder la Déclaration d'Applicabilité

Ce module et le précédent ont couvert l'intégralité des 93 contrôles de l'Annexe A 2022 : 37 organisationnels (module 2), 8 liés aux personnes et 14 physiques (module 3), 34 technologiques (module 4). La leçon suivante explique comment ces 93 contrôles se traduisent concrètement dans le document central de toute certification ISO 27001 : la Déclaration d'Applicabilité.
