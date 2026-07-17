# CIS Controls en profondeur : introduction et repères

## Un référentiel né d'une question très concrète : "que faisons-nous en premier ?"

Le premier parcours de cette plateforme a mentionné les CIS Benchmarks en une phrase, comme référentiel de configuration technique précise pour le cloud. Ce parcours va bien au-delà : il couvre les **CIS Controls** (Critical Security Controls), un référentiel distinct des Benchmarks — développé, comme on le verra, précisément pour répondre à une question que ni ISO 27001, ni le NIST CSF, ni SOC 2 ne posent aussi frontalement : face à des ressources toujours limitées, **par quels contrôles commencer en priorité** pour réduire le risque le plus efficacement possible.

## Une origine née d'un constat d'urgence, pas d'un exercice académique

En 2008, à la suite de pertes de données significatives constatées au sein du ministère de la Défense américain, un consortium associant la NSA, des agences fédérales américaines (dont le DHS US-CERT), et des experts du secteur privé de la réponse à incident et des tests d'intrusion, s'est réuni pour répondre à une question pragmatique : quels contrôles, parmi tous ceux possibles, avaient réellement empêché ou limité les attaques les plus fréquemment observées sur le terrain ? Le résultat de ce travail, initialement appelé **Consensus Audit Guidelines (CAG)**, deviendra les **"20 Critical Security Controls"**, popularisés sous l'appellation informelle de **SANS Top 20** lorsque le SANS Institute en a assuré la diffusion et la mise à jour dans les années suivantes.

## Le transfert de gouvernance vers le Center for Internet Security

La gouvernance du référentiel est passée du SANS Institute au **Council on Cyber Security** en 2013, puis, en 2015, au **Center for Internet Security (CIS)** — l'organisme à but non lucratif qui maintient également les CIS Benchmarks — qui l'a rebaptisé **CIS Critical Security Controls**, nom sous lequel il est connu aujourd'hui. Ce transfert de gouvernance n'a rien d'anecdotique : il a consolidé, sous une même organisation, deux référentiels complémentaires mais distincts (développés en détail au module 3), tout en préservant le modèle original de **consensus communautaire** — les CIS Controls continuent d'évoluer par un processus ouvert, associant des centaines de professionnels de la sécurité, des retours d'expérience terrain et des données réelles d'attaques, plutôt que par la seule décision d'un comité restreint.

## Les grandes évolutions de version

- **Versions 1 à 6 (jusqu'en 2015)** — les "20 Critical Security Controls" originaux, structurés en trois catégories informelles : contrôles de base (Basic), fondamentaux (Foundational) et organisationnels (Organizational).
- **Version 7 (mars 2018)** — reformulation des 20 contrôles avec des sous-contrôles (sub-controls) détaillés.
- **Version 7.1 (avril 2019)** — introduction des **Implementation Groups (IG1, IG2, IG3)**, développés en détail au module 2 : l'innovation la plus structurante du référentiel, qui organise nativement une priorisation des contrôles selon le profil de risque et les ressources de l'organisation.
- **Version 8 (mai 2021)** — révision majeure : consolidation à **18 contrôles**, réorganisés non plus selon qui gère l'équipement (une distinction devenue moins pertinente avec la généralisation du cloud et du travail à distance) mais selon le **type d'activité de sécurité** concernée. Les sous-contrôles sont renommés **Safeguards**.
- **Version 8.1 (juin 2023)** — mise à jour mineure, renforçant la cartographie vers le **CIS Community Defense Model** et la dimension gouvernance, en écho direct à l'évolution similaire déjà observée pour le NIST CSF 2.0 et sa nouvelle fonction Govern, étudiée dans le deuxième parcours de cette plateforme.

## Une philosophie fondée sur la donnée réelle, pas seulement sur le principe

Ce qui distingue le plus nettement les CIS Controls des référentiels déjà étudiés dans cette plateforme est leur méthode de justification : le CIS maintient un **Community Defense Model (CDM)**, une analyse qui confronte chaque contrôle et chaque Safeguard aux techniques d'attaque réellement observées (en s'appuyant notamment sur le référentiel MITRE ATT&CK et des rapports sectoriels d'incidents comme le Data Breach Investigations Report) pour démontrer, avec des données concrètes, quels contrôles réduisent le plus efficacement le risque face aux menaces les plus fréquentes. Un contrôle ISO 27001 ou une sous-catégorie NIST CSF se justifie par un principe de bonne pratique ou une exigence de gestion des risques générale ; un Safeguard CIS Controls revendique, en plus, une justification empirique directe : "ce contrôle précis a démontré son efficacité contre ces techniques d'attaque précises, observées dans ces incidents réels".

## Ce que ce parcours couvre

Six modules structurent ce parcours : la structure des 18 contrôles et de leurs Safeguards (module 1), le système de priorisation par Implementation Groups qui constitue l'innovation la plus distinctive du référentiel (module 2), l'écosystème complet du CIS au-delà des seuls Controls — Benchmarks et CIS RAM (module 3), le mapping avec les référentiels déjà étudiés dans cette plateforme (module 4), et une feuille de route réaliste pour une organisation qui découvre les CIS Controls (module 5).
