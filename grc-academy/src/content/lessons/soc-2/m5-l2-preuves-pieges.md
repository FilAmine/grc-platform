# Préparer un audit SOC 2 (2/2) : collecte de preuves et pièges fréquents

## Le principe central : produire la preuve en continu, pas au moment de l'audit

L'erreur de préparation la plus fréquente pour une première mission Type II consiste à traiter la collecte de preuves comme une tâche de fin de période, réalisée juste avant l'arrivée de l'auditeur — une approche structurellement incompatible avec la nature même d'un audit Type II, qui porte précisément sur le fonctionnement des contrôles **tout au long** de la période observée. Une preuve reconstituée a posteriori (par exemple, un tableau de revues d'accès rempli rétroactivement) est non seulement contraire à l'esprit de l'exercice, mais généralement détectable par un auditeur expérimenté (absence d'horodatage cohérent, incohérences de format entre les preuves censées avoir été produites à des dates différentes).

## Les domaines où les preuves manquent le plus souvent

### Gestion des changements (CC8)

Le Common Criterion le plus fréquemment source d'exceptions en pratique. Un processus de gestion des changements bien conçu sur le papier échoue souvent en preuve parce que des changements urgents ("hotfix" en production) contournent le processus formel sans documentation rétroactive — chaque changement, y compris les correctifs d'urgence, doit laisser une trace exploitable (ticket, pull request approuvée, journal de déploiement).

### Revues d'accès (CC6)

Une revue d'accès périodique documentée dans une politique mais non réalisée de façon régulière et tracée sur toute la période d'observation est l'une des exceptions les plus classiques — le même piège déjà signalé pour le contrôle 5.18 de l'Annexe A d'ISO 27001 dans le parcours dédié de cette plateforme : la revue doit produire une preuve exploitable (export daté, ticket de validation) à chaque occurrence, pas seulement exister comme intention documentée.

### Gestion des fournisseurs (CC9.2)

Une évaluation de sécurité des fournisseurs critiques réalisée une seule fois à la signature du contrat, sans suivi ni mise à jour sur la durée de la période auditée, ne suffit généralement pas à démontrer un contrôle CC9.2 réellement effectif sur l'ensemble de la période.

### Continuité et tests de restauration (A1.3, si Disponibilité est retenue)

Une organisation qui dispose de sauvegardes mais ne peut produire aucune preuve de test de restauration réellement exécuté pendant la période d'observation s'expose presque systématiquement à une exception sur ce critère.

## L'automatisation de la collecte de preuves

Face au volume de preuves à maintenir en continu pour un programme SOC 2 mature, de nombreuses organisations adoptent des plateformes de conformité automatisée qui se connectent directement aux systèmes de production (fournisseur cloud, outil de gestion des identités, système de tickets, plateforme de CI/CD) pour collecter et archiver automatiquement les preuves associées à chaque contrôle — réduisant fortement le travail manuel de collecte et le risque d'oubli, tout en produisant une preuve horodatée nativement plutôt que reconstituée après coup. Ces outils ne remplacent jamais le travail de fond (définir les bons contrôles, les exécuter réellement) — ils réduisent uniquement le coût de la démonstration de ce travail, un point de vigilance à garder à l'esprit face à des solutions parfois présentées comme une "conformité automatique" qui resterait vide de contenu opérationnel réel.

## Le piège du périmètre qui dérive pendant la période d'observation

Un projet lancé, un nouveau fournisseur cloud adopté, une nouvelle équipe créée en cours de période d'observation Type II peuvent faire dériver le périmètre réel de l'organisation par rapport au périmètre initialement défini pour l'audit — sans qu'un ajustement formel de la matrice de contrôles et de la description du système ne suive. Une bonne pratique consiste à revoir explicitement le périmètre et la matrice de contrôles à intervalles réguliers (trimestriels, par exemple) pendant toute la durée d'observation, plutôt que de découvrir cet écart seulement au moment où l'auditeur commence son examen.

## Le rôle d'un consultant externe, et ses limites

Comme pour un projet ISO 27001 (développé dans le parcours dédié de cette plateforme), le recours à un consultant spécialisé en préparation SOC 2 accélère souvent utilement le cadrage initial et la construction de la matrice de contrôles — mais ne dispense jamais l'organisation de bâtir en interne la discipline de collecte continue de preuves, seule capable de produire, mois après mois, la matière première réellement testée lors de l'audit Type II.
