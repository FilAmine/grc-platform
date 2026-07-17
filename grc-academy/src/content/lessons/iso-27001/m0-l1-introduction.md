# ISO 27001 en profondeur : introduction et repères historiques

## Pourquoi un parcours entier dédié à une seule norme

Le premier parcours de cette plateforme consacre une leçon à ISO 27001, au même niveau que NIST CSF, SOC 2 ou le RGPD — suffisant pour comprendre où la norme se situe dans le paysage GRC. Ce parcours va beaucoup plus loin : il traite la norme clause par clause, contrôle par contrôle, et couvre le processus de certification et le maintien du SMSI dans la durée — le niveau de détail nécessaire à quelqu'un qui doit réellement **piloter** une démarche ISO 27001, pas seulement en comprendre les grandes lignes.

## Une origine britannique, devenue norme internationale

ISO 27001 descend directement de la norme britannique **BS 7799**, publiée en deux parties dans les années 1990 (partie 1 : code de bonnes pratiques, devenue plus tard ISO 27002 ; partie 2 : spécification d'un système de management, devenue ISO 27001). L'ISO a repris et internationalisé cette base en 2005, avec une première édition ISO/IEC 27001:2005.

### Les révisions majeures

- **ISO 27001:2005** — première édition internationale.
- **ISO 27001:2013** — alignement sur la "High Level Structure" commune à toutes les normes ISO de systèmes de management (la même architecture de clauses 4 à 10 que ISO 9001, ISO 22301, ISO 14001), facilitant les systèmes de management intégrés. L'Annexe A comptait alors 114 contrôles répartis en 14 catégories (A.5 à A.18).
- **ISO 27001:2022** — révision majeure de l'Annexe A : les 114 contrôles ont été consolidés, reformulés et réorganisés en **93 contrôles** répartis en **4 thèmes** (organisationnels, personnes, physiques, technologiques). Onze contrôles entièrement nouveaux ont été introduits — notamment la threat intelligence (5.7), la sécurité des services cloud (5.23), la préparation aux TIC pour la continuité d'activité (5.30), la surveillance physique (7.4), la gestion de configuration (8.9), la suppression d'information (8.10), le masquage des données (8.11), la prévention de la fuite de données (8.12), la surveillance des activités (8.16), le filtrage web (8.23) et le codage sécurisé (8.28). Les clauses 4 à 10 elles-mêmes n'ont subi que des ajustements mineurs.

Les organisations certifiées selon l'édition 2013 disposaient d'une période de transition de trois ans après la publication de l'édition 2022 — la date limite de transition était fixée au **31 octobre 2025**. À l'heure où ce parcours est écrit, cette transition est donc déjà derrière nous : toute certification ISO 27001 valide aujourd'hui repose nécessairement sur l'édition 2022.

## ISO 27001 vs ISO 27002 : la distinction à ne jamais perdre de vue

- **ISO 27001** est la norme **certifiable** — elle définit les exigences (clauses 4 à 10) d'un système de management, et liste dans son Annexe A les intitulés des contrôles de référence, sans les détailler.
- **ISO 27002** n'est **pas certifiable seule** — c'est le guide de mise en œuvre qui détaille chaque contrôle de l'Annexe A : objectif, ligne directrice de mise en œuvre, informations complémentaires. La numérotation des contrôles est strictement identique entre les deux normes depuis l'édition 2022, ce qui facilite grandement la navigation entre les deux documents.

Dans la pratique d'un projet de certification, les deux normes sont utilisées en parallèle : 27001 pour structurer le système de management et son audit, 27002 comme référence de mise en œuvre concrète de chaque contrôle retenu.

## La famille ISO 27000 : ne pas confondre les normes satellites

ISO 27001 fait partie d'une famille de normes plus large, dont plusieurs seront mobilisées dans ce parcours :

- **ISO 27005** — lignes directrices pour la gestion des risques de sécurité de l'information, référence naturelle pour l'appréciation des risques exigée en clause 6.1.2.
- **ISO 27004** — mesures et indicateurs pour évaluer l'efficacité du SMSI.
- **ISO 27017 / 27018** — extensions sectorielles pour les services cloud (sécurité pour 27017, protection des données personnelles pour 27018).
- **ISO 27701** — extension pour un système de management de la protection de la vie privée (PIMS), construite comme une couche additionnelle par-dessus un SMSI ISO 27001 existant.

## Comment ce parcours est organisé

Neuf modules structurent ce parcours, dans un ordre pensé pour suivre la logique réelle d'un projet de certification : d'abord la structure exigée par les clauses 4 à 10 (modules 1), puis le détail de chaque thème de l'Annexe A (modules 2 à 4), puis la Déclaration d'Applicabilité qui relie les deux (module 5), puis le processus de certification lui-même (module 6), et enfin le maintien du dispositif dans la durée et la construction d'une feuille de route réaliste (modules 7 et 8).
