# Les Common Criteria (2/2) : les contrôles techniques spécifiques aux Trust Services

## CC6 à CC9 : là où COSO s'arrête et où les Trust Services commencent

Contrairement à CC1-CC5 (leçon précédente), les quatre derniers Common Criteria n'ont pas d'équivalent direct dans le référentiel COSO générique — ils ont été développés spécifiquement par l'AICPA pour les Trust Services, parce que COSO, conçu à l'origine pour le contrôle interne financier au sens large, ne détaille pas la sécurité des systèmes d'information en tant que telle. C'est dans ces quatre catégories que se concentre l'essentiel du travail d'un auditeur SOC 2 sur le terrain technique, et le recoupement le plus direct avec les pratiques Security by Design développées dans le premier parcours de cette plateforme.

## CC6 — Contrôles d'accès logiques et physiques

La catégorie la plus volumineuse, structurée en huit critères (CC6.1 à CC6.8), couvrant notamment :

- l'implémentation de logiciels, d'infrastructures et d'architectures pour soutenir l'identification et l'authentification des utilisateurs autorisés, et pour restreindre l'accès logique aux ressources protégées,
- l'enregistrement et l'autorisation formelle de nouveaux comptes internes et externes avant l'octroi de l'accès (application technique directe du contrôle d'accès et du moindre privilège vus dans le premier parcours),
- la restriction de l'accès physique aux installations et actifs protégés,
- la protection contre les menaces externes (limites du réseau, pare-feux, segmentation),
- la protection des informations lors de leur transmission, de leur stockage et de leur élimination — chiffrement au repos et en transit, effacement sécurisé.

Un auditeur teste CC6 en examinant un échantillon de comptes créés, modifiés et désactivés sur la période d'audit (particulièrement pertinent en Type II, développé au module 3), en vérifiant l'existence de l'authentification multifacteur sur les accès à privilège, et en contrôlant la configuration effective des groupes de sécurité réseau.

## CC7 — Opérations système (System Operations)

Structurée en cinq critères (CC7.1 à CC7.5), couvrant le fonctionnement courant des systèmes :

- la détection et la surveillance des composants susceptibles d'introduire de nouvelles vulnérabilités, et la surveillance des vulnérabilités connues,
- la conception, le développement et l'implémentation d'activités pour détecter les événements de sécurité anormaux,
- la mise en œuvre de la réponse aux incidents de sécurité identifiés,
- la restauration des opérations normales et la reprise des services après un incident,
- la communication liée aux incidents identifiés.

Cette catégorie recoupe très directement les fonctions Detect, Respond et Recover du NIST CSF 2.0, étudiées en profondeur dans le deuxième parcours de cette plateforme — un excellent exemple concret de la manière dont plusieurs référentiels différents décrivent, avec un vocabulaire distinct, un socle de pratiques largement commun.

## CC8 — Gestion des changements (Change Management)

Un seul critère principal (CC8.1), mais couvrant un périmètre large : l'organisation autorise, conçoit, développe ou acquiert, configure, documente, teste, approuve et implémente les changements apportés à l'infrastructure, aux logiciels de données et aux procédures pour répondre à ses objectifs.

En pratique, ce critère est vérifié via un échantillon de changements (déploiements applicatifs, modifications d'infrastructure) déployés pendant la période d'audit, en s'assurant que chacun a suivi le processus documenté : demande formalisée, revue de code ou approbation technique, tests avant déploiement, approbation finale, traçabilité complète. CC8 est fréquemment la source d'exceptions relevées lors d'un audit (module 3), car un processus de gestion des changements appliqué de façon incohérente (certains changements urgents contournant le processus normal, sans documentation rétroactive) est un défaut courant, y compris dans des organisations par ailleurs matures sur les autres Common Criteria.

## CC9 — Atténuation des risques (Risk Mitigation)

Deux critères (CC9.1 et CC9.2), couvrant :

- l'identification, le développement et l'implémentation d'activités d'atténuation des risques découlant de perturbations potentielles des activités,
- l'évaluation et la gestion des risques associés aux fournisseurs et partenaires commerciaux (business partners).

CC9.2 est le point de jonction direct avec la gestion des risques de la chaîne d'approvisionnement — le même sujet traité sous l'angle de la catégorie GV.SC du NIST CSF 2.0 et des contrôles 5.19 à 5.23 de l'Annexe A d'ISO 27001, déjà rencontrés dans les parcours précédents de cette plateforme. Un auditeur SOC 2 examine typiquement le processus d'évaluation de sécurité des fournisseurs critiques, l'existence de clauses contractuelles de sécurité, et le suivi des incidents impliquant des tiers.

## Comment les neuf Common Criteria s'articulent en un ensemble cohérent

Les Common Criteria ne forment pas neuf silos indépendants — ils décrivent un système cohérent, de la gouvernance la plus abstraite (CC1, l'environnement de contrôle) jusqu'à l'exécution opérationnelle la plus concrète (CC6 à CC9, l'accès, les opérations, les changements, les risques tiers), avec au milieu l'appréciation des risques (CC3) et la surveillance (CC4) qui bouclent la boucle entre les deux niveaux — une architecture qui rappelle directement la relation entre gouvernance et Security by Design développée dans le premier parcours de cette plateforme, ici formalisée dans le vocabulaire spécifique de l'audit SOC 2.

## Le lien avec les catégories additionnelles

Les neuf Common Criteria (CC1 à CC9) constituent le socle obligatoire de **toute** mission SOC 2, quelle que soit la catégorie retenue — c'est la définition même de la catégorie Sécurité (obligatoire dans tout rapport SOC 2, comme vu dans le premier parcours). Les quatre autres catégories optionnelles (Disponibilité, Intégrité de traitement, Confidentialité, Vie privée) ajoutent des **critères additionnels**, spécifiques à chacune, qui viennent compléter — et non remplacer — ce socle commun. C'est précisément le sujet du module suivant.
