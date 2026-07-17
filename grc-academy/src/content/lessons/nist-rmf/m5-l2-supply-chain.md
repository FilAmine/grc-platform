# La gestion des risques de la chaîne d'approvisionnement dans le RMF

## Une préoccupation ancienne, formalisée tardivement

La gestion des risques de la chaîne d'approvisionnement (Supply Chain Risk Management — SCRM) n'est pas un sujet nouveau pour le gouvernement fédéral américain — les préoccupations relatives à la provenance des composants matériels et logiciels critiques remontent à plusieurs décennies. Ce qui a changé avec SP 800-53 Rev. 5 (2020), c'est sa **formalisation en une famille de contrôles dédiée**, plutôt qu'un ensemble de préoccupations dispersées à travers plusieurs familles existantes.

## La famille SR (Supply Chain Risk Management)

La famille **SR**, ajoutée dans SP 800-53 Rev. 5, regroupe des contrôles couvrant l'ensemble du cycle de vie de la relation avec les fournisseurs et prestataires :

- **SR-1** — politique et procédures de gestion des risques de la chaîne d'approvisionnement.
- **SR-2** — plan de gestion des risques de la chaîne d'approvisionnement, propre à chaque système ou à l'organisation.
- **SR-3** — contrôle des flux et processus de la chaîne d'approvisionnement, notamment l'identification et la documentation des éléments critiques (composants matériels et logiciels dont la défaillance ou la compromission aurait un impact disproportionné).
- **SR-5** — stratégies d'acquisition, contrats et accords, exigeant l'intégration de clauses de sécurité dans les processus d'acquisition — un parallèle direct avec le contrat de sous-traitance de l'article 28 du RGPD ou les contrôles 5.19 à 5.23 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme.
- **SR-6** — évaluation et revue des fournisseurs, avant et pendant la relation contractuelle.
- **SR-10** — évaluation et vérification de l'authenticité des composants critiques, notamment pour prévenir l'introduction de composants contrefaits.
- **SR-11** — inspection des composants pour détecter d'éventuelles altérations malveillantes (falsification matérielle, logiciels compromis introduits en amont de la chaîne d'approvisionnement).

## Un risque spécifiquement pris au sérieux dans le contexte fédéral et de défense

Le contexte d'origine du RMF — les systèmes fédéraux américains, y compris ceux du ministère de la Défense — explique l'attention particulière portée à des scénarios de menace propres à ce secteur : la compromission délibérée d'un composant matériel ou logiciel par un acteur étatique adverse en amont de la chaîne d'approvisionnement, avant même que le composant n'atteigne l'organisation utilisatrice finale. Ce niveau de préoccupation, bien réel mais relativement spécifique à des systèmes à très haute sensibilité (défense, infrastructures critiques, renseignement), dépasse ce que la plupart des organisations privées ont besoin de considérer pour leurs propres chaînes d'approvisionnement logicielles courantes — un point de contexte à garder à l'esprit en comparant cette famille SR aux contrôles fournisseurs plus généraux d'ISO 27001, du NIST CSF (catégorie GV.SC) ou de SOC 2 (Common Criterion CC9.2), déjà développés dans les parcours précédents de cette plateforme.

## Le lien avec la Software Bill of Materials (SBOM)

La gestion des risques de la chaîne d'approvisionnement logicielle s'appuie de plus en plus, dans la pratique fédérale américaine récente (impulsée notamment par un décret présidentiel de 2021 sur l'amélioration de la cybersécurité nationale), sur l'exigence d'une **nomenclature logicielle (Software Bill of Materials — SBOM)** — un inventaire précis des composants et dépendances logicielles utilisés dans un système, permettant d'identifier rapidement l'exposition à une vulnérabilité découverte dans un composant tiers largement réutilisé. Ce mécanisme recoupe directement le sujet déjà évoqué dans le parcours NIST CSF de cette plateforme (catégorie GV.SC, gestion du cycle de vie des composants logiciels tiers) — la formalisation via SBOM constituant une traduction technique concrète et outillée de cette même préoccupation.

## Comment la famille SR s'articule avec le reste du processus RMF

La gestion des risques de la chaîne d'approvisionnement n'est pas une activité isolée, réalisée une seule fois à la signature d'un contrat fournisseur — elle s'intègre à chacune des sept étapes du RMF développées au module 1 : identifiée dès l'étape Prepare au niveau organisationnel, prise en compte dans la sélection des contrôles à l'étape Select, documentée dans le SSP à l'étape Implement, évaluée par l'évaluateur indépendant à l'étape Assess, considérée par l'Authorizing Official dans sa décision d'autorisation, et surveillée en continu à l'étape Monitor — notamment via une veille active sur les vulnérabilités affectant les composants tiers identifiés, plutôt qu'une évaluation figée réalisée une seule fois avant l'autorisation initiale.

## Ce que cette convergence confirme

La formalisation de la gestion des risques de la chaîne d'approvisionnement en une famille de contrôles dédiée dans SP 800-53 Rev. 5 (2020), quasiment simultanée avec l'élévation de ce même sujet en catégorie de gouvernance à part entière dans le NIST CSF 2.0 (2024) et son renforcement dans l'Annexe A d'ISO 27001:2022, confirme un mouvement de fond largement partagé entre les référentiels majeurs étudiés dans cette plateforme : la sécurité d'une organisation ne peut plus être pensée uniquement à l'intérieur de son propre périmètre technique, mais doit intégrer explicitement le risque porté par l'ensemble de son écosystème de fournisseurs, prestataires et composants logiciels tiers.
