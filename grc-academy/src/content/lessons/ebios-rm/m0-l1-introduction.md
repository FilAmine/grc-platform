# ANSSI et EBIOS RM en profondeur : introduction et repères

## Une agence nationale, pas seulement une méthode

Ce treizième parcours couvre à la fois une **institution** — l'ANSSI, l'agence française de cybersécurité — et sa **méthode phare de gestion des risques**, EBIOS RM, déjà mentionnée brièvement dans le premier parcours de cette plateforme aux côtés d'ISO 31000 et du NIST RMF. Contrairement aux parcours NIST RMF ou CIS Controls, centrés sur un texte ou un catalogue précis, ce parcours adopte une focale plus large : comprendre EBIOS RM suppose de comprendre le rôle institutionnel de l'ANSSI qui la porte, et réciproquement, comprendre l'ANSSI suppose de saisir comment sa méthode de référence structure concrètement l'analyse de risque en France.

## L'ANSSI : origines et missions

L'**Agence Nationale de la Sécurité des Systèmes d'Information (ANSSI)** a été créée en 2009, placée sous l'autorité du Secrétariat général de la défense et de la sécurité nationale (SGDSN), lui-même rattaché au Premier ministre — une position institutionnelle qui place l'ANSSI au cœur de l'appareil d'État plutôt que comme une simple agence sectorielle. Ses missions se déclinent en quatre axes :

- **Prévention** — élaboration de règles de sécurité, conseil aux administrations et aux opérateurs, qualification de produits et de prestataires de services (développée au module 6 de ce parcours).
- **Défense** — détection, alerte et réponse aux incidents affectant l'État et les opérateurs les plus critiques, via son centre de réponse aux incidents, le **CERT-FR** (développé au module 6).
- **Réglementation** — désignation et encadrement des opérateurs les plus critiques au titre de la Loi de Programmation Militaire (LPM), et rôle d'autorité nationale pour la transposition française de NIS2, déjà développée dans le parcours dédié de cette plateforme (module 6 de ce parcours).
- **Rayonnement international** — contribution aux travaux normatifs et à la coopération européenne en matière de cybersécurité.

## Un précurseur nettement antérieur à NIS2

Un point souvent méconnu, qui mérite d'être signalé dès cette introduction : le régime français des **Opérateurs d'Importance Vitale (OIV)**, instauré par la Loi de Programmation Militaire de 2013, a précédé de près d'une décennie la directive NIS2 déjà développée dans le parcours dédié de cette plateforme — imposant déjà, pour un périmètre resserré d'opérateurs jugés vitaux pour la Nation, des règles de sécurité et une obligation de déclaration des incidents à l'ANSSI. NIS2 a, dans une certaine mesure, généralisé à l'échelle européenne une logique que la France appliquait déjà nationalement à un périmètre plus restreint — un point développé plus en détail au module 6 de ce parcours.

## D'EBIOS à EBIOS RM

**EBIOS** (Expression des Besoins et Identification des Objectifs de Sécurité) est une méthode d'analyse et de gestion des risques développée par l'ANSSI, dont la première version remonte aux années 1990. La version actuelle, **EBIOS Risk Manager (EBIOS RM)**, publiée en 2018 par l'ANSSI en collaboration avec le **Club EBIOS** (une association rassemblant praticiens, éditeurs et experts), a profondément renouvelé la méthode par rapport à sa version précédente (EBIOS 2010) — en délaissant une approche plus mécanique centrée sur l'inventaire exhaustif des risques au profit d'une approche **par scénarios**, construite autour de la manière dont un attaquant réel et motivé pourrait atteindre les objectifs qu'il vise.

## Une philosophie distinctive : raisonner depuis l'attaquant, pas depuis la checklist

Le premier parcours de cette plateforme avait déjà signalé, à propos du threat modeling STRIDE, l'intérêt de raisonner "depuis l'attaquant" plutôt que "depuis la checklist". EBIOS RM pousse ce principe au rang de méthode structurante de bout en bout : plutôt que de partir d'un catalogue générique de menaces à croiser mécaniquement avec un inventaire d'actifs, la méthode construit des **scénarios narratifs et crédibles**, mettant en scène des sources de risque réelles (développées au module 2), leurs objectifs propres, et les chemins d'attaque plausibles — y compris à travers l'écosystème de partenaires et de fournisseurs de l'organisation (développé au module 3), un sujet traité avec un formalisme graphique propre à EBIOS RM et sans équivalent aussi structuré dans les référentiels déjà étudiés dans cette plateforme.

## L'articulation avec ISO 27005 et les autres méthodologies déjà étudiées

EBIOS RM n'est jamais présentée par l'ANSSI comme un référentiel concurrent d'ISO 27005 (les lignes directrices génériques de gestion des risques de sécurité de l'information) — mais comme une **méthode française qui met en œuvre concrètement** ce que ce standard générique décrit à un niveau de principe. Le résultat d'une étude EBIOS RM peut directement alimenter l'appréciation des risques exigée par la clause 6.1.2 d'ISO 27001, déjà développée dans le parcours dédié de cette plateforme, ou justifier les mesures de gestion des risques de l'article 21 de NIS2 — une articulation qui rejoint directement la logique de mapping entre méthodes de risque et référentiels de contrôles déjà observée à de multiples reprises dans cette plateforme.

## Ce que ce parcours couvre

Huit modules structurent ce parcours : le cadrage de l'étude et le socle de sécurité (module 1, Atelier 1 d'EBIOS RM), les sources de risque et leurs objectifs visés (module 2, Atelier 2), les scénarios stratégiques et la cartographie de l'écosystème (module 3, Atelier 3), les scénarios opérationnels (module 4, Atelier 4), le traitement du risque et le plan d'amélioration continue (module 5, Atelier 5), l'écosystème plus large de l'ANSSI — qualifications, certifications et rôle réglementaire (module 6), et enfin l'articulation d'EBIOS RM avec les référentiels déjà étudiés dans cette plateforme ainsi qu'une feuille de route pour une première étude (module 7).
