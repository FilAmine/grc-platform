# Les CIS Benchmarks : le niveau de configuration technique précise

## Distinguer clairement Controls et Benchmarks

Le premier parcours de cette plateforme a mentionné les CIS Benchmarks en une phrase, dans le module Cloud Security by Design, comme référentiel de configuration technique précise. Ce parcours permet maintenant de préciser une distinction souvent source de confusion, y compris chez des praticiens expérimentés : les **CIS Controls** (objet des modules précédents) définissent **quoi faire** à un niveau de programme de sécurité — "établir et maintenir une configuration sécurisée" (contrôle 4) — tandis que les **CIS Benchmarks** définissent **comment** le faire précisément, plateforme par plateforme, technologie par technologie : quel paramètre exact configurer sur quelle version d'un système d'exploitation, d'une base de données, ou d'un service cloud donné.

## Le catalogue des Benchmarks

Le CIS publie et maintient des centaines de Benchmarks, couvrant notamment :

- les systèmes d'exploitation (CIS Microsoft Windows Server Benchmark, CIS Ubuntu Linux Benchmark, CIS Red Hat Enterprise Linux Benchmark),
- les environnements cloud (CIS Amazon Web Services Foundations Benchmark, CIS Microsoft Azure Foundations Benchmark, CIS Google Cloud Platform Foundation Benchmark — déjà évoqués dans le premier parcours de cette plateforme),
- les technologies de conteneurisation (CIS Docker Benchmark, CIS Kubernetes Benchmark),
- les bases de données et serveurs applicatifs (CIS Oracle Database Benchmark, CIS Apache HTTP Server Benchmark),
- les navigateurs web et les applications de productivité bureautique.

Chaque Benchmark est développé par un processus communautaire ouvert similaire à celui des CIS Controls, associant des experts techniques de la technologie concernée, et fait l'objet de mises à jour régulières pour suivre l'évolution des versions logicielles couvertes.

## Les niveaux de profil : Level 1 et Level 2

Chaque recommandation d'un Benchmark est classée selon un **niveau de profil** :

- **Level 1** — des recommandations de durcissement de base, avec un impact minimal sur la fonctionnalité ou la performance du système, applicables à la quasi-totalité des environnements sans analyse approfondie préalable.
- **Level 2** — des recommandations destinées à un environnement exigeant une défense en profondeur plus poussée, potentiellement avec un impact plus significatif sur la fonctionnalité ou nécessitant une expertise technique plus approfondie pour être appliquées sans effet secondaire indésirable.

Cette distinction en deux niveaux rappelle directement, dans son principe, les Implementation Groups des CIS Controls développés au module 2 — une même logique de priorisation progressive, appliquée ici au niveau de la configuration technique précise plutôt qu'au niveau du programme de sécurité global.

## L'outil d'évaluation automatisée : CIS-CAT

Le CIS met à disposition **CIS-CAT (CIS Configuration Assessment Tool)**, un outil qui scanne automatiquement la configuration réelle d'un système et la compare au Benchmark correspondant, produisant un rapport de conformité détaillé, recommandation par recommandation. Cet outil joue, pour la vérification de configuration, un rôle comparable à celui des outils de **Cloud Security Posture Management (CSPM)** déjà évoqués dans le premier parcours de cette plateforme — la vérification continue et automatisée d'une configuration réelle par rapport à un référentiel documenté, plutôt qu'un audit ponctuel et manuel.

## Le lien direct avec le contrôle 4 des CIS Controls

Les Benchmarks ne sont jamais consultés isolément dans une démarche de sécurité structurée — ils servent de référence de mise en œuvre concrète pour le contrôle 4 (configuration sécurisée) des CIS Controls, développé au module 1 : une organisation qui documente sa conformité au contrôle 4 s'appuiera typiquement sur le Benchmark correspondant à chaque technologie de son parc (le Benchmark Windows Server pour ses serveurs, le Benchmark AWS Foundations pour son environnement cloud) plutôt que de définir ses propres règles de configuration de zéro.

## Un exemple concret : appliquer le Benchmark AWS Foundations ou le Benchmark Azure Foundations

Le **CIS Amazon Web Services Foundations Benchmark** détaille, par exemple, des recommandations précises telles que la désactivation de l'utilisateur racine (root) pour les tâches quotidiennes au profit de rôles IAM nominatifs, l'activation d'AWS CloudTrail dans toutes les régions pour journaliser l'ensemble des appels API, ou le chiffrement systématique des volumes EBS et des buckets S3 par défaut. Le **CIS Microsoft Azure Foundations Benchmark** couvre, de façon comparable, des recommandations telles que l'activation de l'authentification multifacteur pour tous les comptes disposant de privilèges d'administrateur, la restriction des règles entrantes des groupes de sécurité réseau (NSG), ou l'activation de Microsoft Defender for Cloud sur l'ensemble des abonnements. Une organisation exploitant simultanément les deux environnements applique ainsi deux Benchmarks distincts, chacun scanné automatiquement par un outil de type CSPM ou par CIS-CAT, plutôt que de tenter de transposer manuellement les recommandations de l'un vers l'autre — les deux plateformes cloud partageant des principes communs (moindre privilège, chiffrement par défaut, journalisation exhaustive) mais des mécanismes de configuration natifs entièrement différents.

## Comment cette articulation recoupe le tableau de comparaison déjà établi dans le premier parcours

Le premier parcours de cette plateforme avait déjà positionné les CIS Benchmarks au niveau le plus opérationnel d'un tableau comparatif de référentiels cloud, aux côtés de la CSA CCM (mapping transverse) et des Well-Architected Frameworks (conception d'architecture). Ce parcours permet de compléter ce positionnement : les **CIS Controls** occupent, dans cette même hiérarchie, un niveau intermédiaire entre la stratégie (ISO 27001, NIST CSF) et la configuration technique précise (les Benchmarks eux-mêmes) — un programme de sécurité structuré autour des CIS Controls comme référentiel de contrôles pivot, mis en œuvre techniquement via les Benchmarks correspondants à chaque technologie utilisée, illustre bien comment ces deux composantes de l'écosystème CIS, bien que distinctes, sont pensées pour fonctionner ensemble plutôt que comme deux référentiels concurrents.
