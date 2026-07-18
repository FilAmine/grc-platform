# Construire une feuille de route réaliste de mise en conformité PCI DSS

## Une priorité de départ différente de celle des autres référentiels de cette plateforme

Pour ISO 27001, NIS2 ou DORA, ce parcours et les précédents ont systématiquement recommandé de commencer par une analyse de risque ou une cartographie des obligations. Pour PCI DSS, l'étape la plus déterminante et la plus spécifique à ce référentiel est différente : c'est le **scoping**, développé au module 2, qui conditionne le plus directement l'ampleur de tout le reste du projet — une entité qui investit du temps en amont pour réduire son périmètre CDE (par la segmentation réseau, l'externalisation, la tokenisation) réduit mécaniquement l'ensemble de l'effort de mise en conformité qui suivra.

## Les étapes typiques d'un premier projet de conformité

### Étape 1 — Déterminer son niveau de validation et son type de SAQ

Identifier son volume de transactions et son architecture de traitement des paiements (module 3) pour déterminer si l'entité relève d'un RoC ou d'un SAQ, et lequel des différents types de SAQ correspond réellement à son architecture — une erreur de qualification à ce stade invaliderait tout le travail réalisé par la suite.

### Étape 2 — Réduire le périmètre avant de le sécuriser

Avant d'investir dans la sécurisation exhaustive de l'ensemble de son infrastructure, évaluer systématiquement les options de réduction du périmètre CDE (module 2 et module 5) : segmentation réseau, externalisation vers un prestataire déjà validé, tokenisation ou chiffrement point à point — chaque système exclu du périmètre est un système qui n'a plus besoin de satisfaire à l'intégralité des douze exigences.

### Étape 3 — Combler les écarts par rapport aux douze exigences

Une fois le périmètre stabilisé, cartographier l'état actuel des contrôles existants par rapport aux douze exigences (module 1), en s'appuyant, si l'entité dispose déjà d'un référentiel technique maîtrisé (ISO 27001, CIS Controls), sur le mapping déjà développé au module 6 pour éviter de reconstruire un dispositif entièrement distinct.

### Étape 4 — Mettre en place la surveillance continue

Contractualiser les scans trimestriels avec un Approved Scanning Vendor (module 3), et mettre en place les mécanismes de journalisation et de détection de défaillance des contrôles critiques exigés par l'exigence 10 (module 1) — des mécanismes qui doivent fonctionner en continu, bien au-delà du seul jour de l'évaluation annuelle.

### Étape 5 — Réaliser l'évaluation formelle

Selon le niveau de validation déterminé à l'étape 1, compléter le SAQ applicable ou engager un QSA pour réaliser le RoC complet (module 3), en anticipant que ce dernier suppose généralement plusieurs semaines de préparation et de collecte de preuves, à l'image des audits de certification déjà développés pour ISO 27001 et SOC 2 dans les parcours précédents de cette plateforme.

## Les pièges les plus fréquents

- **Sous-estimer l'effort de scoping initial** — une entité qui saute directement à la sécurisation de l'ensemble de son infrastructure, sans avoir d'abord cherché à réduire son périmètre CDE, s'inflige un effort de conformité disproportionné par rapport à son activité réelle de paiement.
- **Mal qualifier son type de SAQ** — un choix de SAQ trop léger par rapport à l'architecture réelle de traitement des paiements (module 3) produit une auto-évaluation invalide, susceptible d'être contestée après un incident.
- **Oublier les données d'authentification sensibles cachées dans les journaux applicatifs** — un piège technique très concret déjà signalé au module 5 : une capture involontaire de codes de vérification dans un journal de débogage applicatif constitue une non-conformité grave, souvent découverte tardivement.
- **Traiter la conformité comme un exercice annuel isolé** — négliger les scans trimestriels obligatoires (module 3) ou les tests de segmentation réguliers (module 1) entre deux évaluations annuelles, un piège de "projet qui s'arrête à l'évaluation" déjà signalé à de multiples reprises dans les parcours précédents de cette plateforme pour d'autres référentiels.

## Le rôle d'un QSA en amont du projet, pas seulement à la fin

Contrairement à une idée reçue, un QSA n'intervient pas seulement pour produire le RoC final — de nombreux QSA proposent des évaluations préliminaires (readiness assessment) similaires à celles déjà développées dans les parcours ISO 27001 et SOC 2 de cette plateforme, permettant d'identifier les écarts et de valider la stratégie de scoping avant l'évaluation formelle. Ce recours anticipé à l'expertise externe est particulièrement utile pour les questions de scoping et pour évaluer si un projet d'approche personnalisée (module 4) est réellement viable, compte tenu de la charge documentaire renforcée qu'elle suppose.

## En clôture de ce parcours

Ce parcours a couvert PCI DSS de bout en bout : les douze exigences organisées en six objectifs de contrôle, le scoping et la segmentation réseau comme leviers essentiels de maîtrise de l'effort de conformité, les niveaux de validation et les différents types de questionnaires d'auto-évaluation, le rôle du QSA et des scans ASV, l'approche personnalisée et l'analyse de risque ciblée introduites par la version 4.0, la protection en détail des données de titulaires de carte et l'interdiction absolue de conservation des données d'authentification sensibles, et enfin le régime de sanctions contractuelles propre à ce référentiel ainsi que son articulation avec les référentiels génériques déjà étudiés dans cette plateforme. Combiné aux neuf autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels majeurs — normes volontaires, rapports d'attestation, textes de loi, et exigences contractuelles sectorielles — qui structurent une démarche GRC moderne.
