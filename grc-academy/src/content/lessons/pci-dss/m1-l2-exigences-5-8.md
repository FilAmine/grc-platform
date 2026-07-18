# Les douze exigences (2/3) : gestion des vulnérabilités et contrôle d'accès

## Objectif 3 — Maintenir un programme de gestion des vulnérabilités

### Exigence 5 — Protéger tous les systèmes et réseaux contre les logiciels malveillants

Cette exigence impose le déploiement de solutions anti-malware sur tous les systèmes couramment ciblés par ce type de menace, avec des mécanismes de détection active, de mise à jour régulière des signatures, et de génération de journaux d'audit exploitables — un contrôle qui recoupe directement le contrôle SI-3 de SP 800-53 et le contrôle 10 des CIS Controls, déjà développés dans les parcours précédents de cette plateforme. La v4.0 étend explicitement cette exigence aux mécanismes anti-hameçonnage pour les systèmes de messagerie électronique.

### Exigence 6 — Développer et gérer des systèmes et logiciels sécurisés

Cette exigence couvre l'ensemble du cycle de vie du développement logiciel : un processus de gestion des correctifs de sécurité priorisé selon la criticité des vulnérabilités (avec des délais resserrés pour les vulnérabilités critiques touchant des systèmes exposés au public), des pratiques de développement sécurisé conformes à des standards reconnus, et surtout une exigence spécifique à la v4.0 particulièrement discutée : la protection des **pages de paiement contre les scripts malveillants côté client** — une réponse directe aux attaques dites de "e-skimming" (injection de code malveillant dans une page de paiement pour intercepter les données de carte au moment de leur saisie), un vecteur d'attaque qui n'a pas d'équivalent aussi nommément ciblé dans les autres référentiels déjà étudiés dans cette plateforme.

## Objectif 4 — Mettre en œuvre des mesures de contrôle d'accès strictes

### Exigence 7 — Restreindre l'accès aux composants du système et aux données de titulaires de carte selon le besoin professionnel de connaître

L'application directe du principe de moindre privilège déjà développé dans le module Security by Design du premier parcours de cette plateforme, avec une exigence de **refus par défaut** : tout accès non explicitement autorisé doit être refusé.

### Exigence 8 — Identifier les utilisateurs et authentifier l'accès aux composants du système

Cette exigence a été substantiellement renforcée en v4.0 : l'**authentification multifacteur (MFA)** est désormais exigée pour **tout accès au CDE**, pas seulement pour les accès administratifs ou les accès à distance comme sous la version précédente du référentiel — une extension notable qui recoupe l'insistance croissante sur le MFA déjà observée dans de nombreux référentiels de cette plateforme (contrôle 8.5 d'ISO 27001, famille IA de SP 800-53, domaine j de l'article 21 de NIS2), mais poussée ici à un périmètre d'application particulièrement large. Cette exigence couvre également la gestion des identifiants uniques par utilisateur (interdiction des comptes partagés, sauf exceptions documentées), et des politiques de mots de passe robustes.

### Exigence 9 — Restreindre l'accès physique aux données de titulaires de carte

Cette exigence couvre la sécurité physique des locaux hébergeant le CDE (contrôle d'accès physique, vidéosurveillance, distinction entre visiteurs et personnel), mais aussi des sujets propres au contexte du paiement physique : la protection contre la substitution frauduleuse de terminaux de point de vente (skimming physique), et la destruction sécurisée des supports contenant des données de titulaires de carte lorsqu'ils ne sont plus nécessaires — un point qui recoupe directement le contrôle 7.14 de l'Annexe A d'ISO 27001 (mise au rebut sécurisée), déjà développé dans le parcours dédié de cette plateforme.

## Ce que ce deuxième bloc révèle sur la spécificité du secteur des paiements

Ce bloc d'exigences illustre bien comment PCI DSS, tout en reprenant des principes largement communs aux référentiels de sécurité généralistes (moindre privilège, MFA, gestion des vulnérabilités), les décline systématiquement sur des scénarios de menace **propres au paiement par carte** : la protection contre le e-skimming (exigence 6), la substitution physique de terminaux (exigence 9) — des préoccupations qui n'ont pas d'équivalent aussi ciblé dans ISO 27001, le NIST CSF ou les CIS Controls, précisément parce que ces référentiels génériques ne sont pas construits autour d'un secteur d'activité unique.
