# Les Common Criteria (1/2) : la gouvernance selon COSO

## Pourquoi les Trust Services Criteria s'appuient sur le référentiel COSO

Les **Trust Services Criteria (TSC)**, publiés et maintenus par l'AICPA, ne partent pas d'une feuille blanche pour définir ce qu'est un bon contrôle interne : ils s'appuient explicitement sur le référentiel **COSO** (Committee of Sponsoring Organizations of the Treadway Commission), en particulier son référentiel de contrôle interne intégré de 2013 (*Internal Control – Integrated Framework*), déjà la référence dominante en matière de contrôle interne financier depuis les années 1990 (popularisé notamment par la loi Sarbanes-Oxley aux États-Unis).

COSO structure le contrôle interne autour de **cinq composantes** et **dix-sept principes**. Les TSC traduisent ces cinq composantes en une série de critères appelés **Common Criteria (CC1 à CC9)** — communs à toute mission SOC 2, quelle que soit la catégorie retenue (Sécurité étant obligatoire, les autres optionnelles, comme vu dans le premier parcours). Les cinq premières séries de Common Criteria (CC1 à CC5) correspondent directement aux cinq composantes COSO ; les quatre suivantes (CC6 à CC9) sont spécifiques aux Trust Services et n'ont pas d'équivalent direct dans COSO — elles seront développées dans la leçon suivante.

## CC1 — Environnement de contrôle (Control Environment)

Correspond aux principes COSO 1 à 5. Couvre les fondations culturelles et structurelles du contrôle interne :

- l'engagement de l'organisation envers l'intégrité et les valeurs éthiques,
- l'indépendance du conseil d'administration (ou de l'organe de gouvernance équivalent) vis-à-vis de la direction, et sa capacité à exercer une supervision,
- l'établissement par la direction, sous supervision du conseil, des structures, lignes hiérarchiques et autorités/responsabilités appropriées pour atteindre les objectifs,
- l'engagement de l'organisation à attirer, développer et retenir des personnes compétentes en cohérence avec les objectifs,
- la responsabilisation des personnes vis-à-vis de leurs responsabilités en matière de contrôle interne.

Un auditeur SOC 2 qui évalue CC1 examine typiquement le code de conduite, l'organigramme, les descriptions de poste des rôles clés de sécurité, et la structure de gouvernance (existence d'un comité de sécurité ou de risques, indépendance de la fonction) — un socle proche, dans l'esprit, du modèle des trois lignes de maîtrise et de la gouvernance développés dans le premier parcours de cette plateforme.

## CC2 — Information et communication (Communication and Information)

Correspond aux principes COSO 13 à 15. Couvre :

- l'obtention ou la génération, et l'utilisation, d'informations pertinentes et de qualité pour soutenir le fonctionnement du contrôle interne,
- la communication interne des informations nécessaires au fonctionnement du contrôle interne, y compris des objectifs et responsabilités,
- la communication avec les parties externes (clients, régulateurs, fournisseurs) des sujets affectant le fonctionnement du contrôle interne.

En pratique, cela couvre par exemple la manière dont une politique de sécurité est diffusée et comprise par le personnel, et la manière dont l'organisation communique ses engagements de sécurité à ses clients (souvent via une page de confiance publique ou des clauses contractuelles).

## CC3 — Appréciation des risques (Risk Assessment)

Correspond aux principes COSO 6 à 9. Couvre :

- la définition d'objectifs suffisamment clairs pour permettre l'identification et l'appréciation des risques associés,
- l'identification des risques pesant sur la réalisation des objectifs, à travers l'ensemble de l'organisation, et leur analyse,
- la prise en compte du potentiel de fraude dans l'appréciation des risques,
- l'identification et l'appréciation des changements susceptibles d'affecter significativement le système de contrôle interne.

Cette catégorie recoupe directement la gestion des risques développée dans le premier parcours de cette plateforme (ISO 31000, EBIOS RM, NIST RMF) — sans imposer de méthodologie de cotation précise, à l'image de ce qui a déjà été observé pour ISO 27001 et le NIST CSF : chaque organisation reste libre de sa méthode, tant qu'elle est appliquée de façon cohérente et documentée.

## CC4 — Activités de surveillance (Monitoring Activities)

Correspond aux principes COSO 16 et 17. Couvre :

- la sélection, le développement et la réalisation d'évaluations continues et/ou ponctuelles pour vérifier si les composantes du contrôle interne sont présentes et fonctionnent,
- l'évaluation et la communication en temps opportun des déficiences de contrôle interne aux parties responsables des actions correctives, y compris la direction et le conseil le cas échéant.

Ce critère recoupe l'audit interne et la revue de direction déjà rencontrés dans le parcours ISO 27001 de cette plateforme (clauses 9.2 et 9.3) — la même logique de vérification continue, formulée ici dans le vocabulaire COSO plutôt que dans celui d'un système de management ISO.

## CC5 — Activités de contrôle (Control Activities)

Correspond aux principes COSO 10 à 12. Couvre :

- la sélection et le développement d'activités de contrôle qui contribuent à ramener les risques pesant sur la réalisation des objectifs à un niveau acceptable,
- la sélection et le développement d'activités de contrôle générales relatives à la technologie pour soutenir la réalisation des objectifs,
- le déploiement des activités de contrôle à travers des politiques qui établissent ce qui est attendu, et des procédures qui mettent en œuvre ces politiques.

CC5 est le pont conceptuel entre la gouvernance (CC1 à CC4, largement abstraite) et les contrôles techniques concrets développés dans les Common Criteria suivants (CC6 à CC9, objet de la leçon suivante) — c'est ici que la structure COSO générique commence à se rapprocher des pratiques Security by Design développées ailleurs dans cette plateforme.

## Pourquoi cette base COSO structure toute la suite du parcours

Comprendre que CC1 à CC5 ne sont pas des inventions propres aux Trust Services, mais l'application directe d'un référentiel de contrôle interne préexistant et largement éprouvé (COSO), permet de mieux anticiper ce qu'un auditeur SOC 2 recherche à ce niveau : des preuves de gouvernance et de pilotage global, avant même d'examiner un seul contrôle technique. Les quatre Common Criteria suivants (CC6 à CC9), spécifiques aux Trust Services et bien plus proches des pratiques Security by Design, sont développés dans la leçon suivante.
