# La catégorie Vie privée (Privacy) en détail

## La catégorie la plus substantielle des quatre critères additionnels

Contrairement à Confidentialité (2 critères) ou Disponibilité (3 critères), la catégorie Vie privée compte **huit familles de critères (P1 à P8)**, héritées du cadre historique AICPA/CICA *Generally Accepted Privacy Principles (GAPP)*, aujourd'hui intégrées aux Trust Services Criteria. Cette catégorie mérite une leçon à part entière, tant elle recoupe — sans s'y substituer — les principes de Privacy by Design et les obligations du RGPD déjà développés en profondeur dans le premier parcours de cette plateforme.

## Les huit familles de critères

### P1 — Notice et communication des objectifs

L'entité fournit une notification aux personnes concernées sur ses objectifs liés à la vie privée, formulée de manière suffisamment claire et proéminente — l'équivalent fonctionnel de l'obligation d'information et de transparence du RGPD (article 13-14).

### P2 — Choix et consentement

L'entité communique les choix disponibles concernant la collecte, l'utilisation, la conservation, la divulgation et l'élimination des informations personnelles, et obtient le consentement implicite ou explicite au moment de la collecte.

### P3 — Collecte

L'entité collecte des informations personnelles uniquement pour répondre aux objectifs identifiés dans la notification — l'équivalent direct du principe de minimisation des données déjà développé en profondeur dans le module Privacy by Design du premier parcours.

### P4 — Utilisation, conservation et élimination

L'entité limite l'utilisation des informations personnelles aux objectifs identifiés, conserve ces informations uniquement le temps nécessaire pour répondre à ces objectifs, et les élimine par la suite — recoupe directement la limitation de la conservation du RGPD.

### P5 — Accès

L'entité fournit aux personnes concernées un accès à leurs informations personnelles pour révision et mise à jour — l'équivalent du droit d'accès et de rectification du RGPD.

### P6 — Divulgation et notification

L'entité divulgue les informations personnelles à des tiers uniquement avec le consentement implicite ou explicite des personnes concernées, ou selon les objectifs identifiés, et notifie les personnes concernées en cas d'incident de confidentialité impliquant leurs informations personnelles.

### P7 — Qualité

L'entité maintient des informations personnelles exactes, complètes et pertinentes pour les objectifs identifiés — recoupe le principe d'exactitude du RGPD.

### P8 — Surveillance et application

L'entité surveille sa conformité à ses engagements et exigences liés à la vie privée, et dispose de procédures pour traiter les réclamations et litiges liés à la vie privée — le pendant du principe d'accountability (responsabilité) du RGPD développé dans le premier parcours : il ne suffit pas de respecter les principes, il faut pouvoir démontrer un dispositif de surveillance actif.

## Une différence fondamentale avec le RGPD : ce que SOC 2 Privacy ne couvre pas

Un rapport SOC 2 incluant la catégorie Vie privée **ne constitue en aucun cas une preuve de conformité RGPD complète**, pour plusieurs raisons structurantes déjà évoquées dans le premier parcours de cette plateforme, qu'il convient de rappeler précisément ici :

- SOC 2 Privacy évalue la conformité de l'organisation **à ses propres engagements déclarés** dans sa politique de confidentialité — pas à un standard légal externe fixé par une loi comme le RGPD. Une organisation aux engagements de vie privée volontairement modestes peut obtenir un rapport SOC 2 Privacy "propre" tout en étant en infraction avec le RGPD si elle traite des données de résidents européens.
- Le RGPD impose des mécanismes spécifiques (base légale de traitement, DPIA pour les traitements à risque élevé, désignation d'un DPO dans certains cas, délais légaux précis de réponse aux demandes d'exercice de droits) qu'aucun des huit critères P1-P8 ne détaille avec cette précision réglementaire.
- SOC 2 Privacy est un cadre **américain**, pensé dans un contexte juridique où, historiquement, il n'existait pas d'équivalent fédéral unique au RGPD — les huit familles de critères reflètent des principes de bonnes pratiques généraux (le cadre GAPP), pas la transposition d'une loi précise.

## Pourquoi la catégorie Vie privée reste néanmoins peu retenue en pratique

Malgré sa richesse, la catégorie Vie privée de SOC 2 reste moins fréquemment demandée par les clients qu'on pourrait s'y attendre, pour une raison pragmatique : la plupart des organisations qui traitent des données personnelles de résidents européens doivent de toute façon démontrer une conformité RGPD par des moyens dédiés (registre des traitements, DPIA, mentions d'information) — ce qui rend la valeur ajoutée d'un rapport SOC 2 Privacy, en plus de cette démarche RGPD déjà exigée par la loi, souvent limitée face à son coût d'audit supplémentaire. En pratique, beaucoup d'organisations préfèrent démontrer leur conformité vie privée via une documentation RGPD dédiée, et réserver le périmètre SOC 2 aux catégories Sécurité, Disponibilité et Confidentialité — un arbitrage de scoping développé plus en détail au module 5.
