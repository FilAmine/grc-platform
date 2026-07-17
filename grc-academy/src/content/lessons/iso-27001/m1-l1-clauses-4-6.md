# Clauses 4 à 6 : contexte, leadership et planification

## Clause 4 — Contexte de l'organisme

### 4.1 Compréhension de l'organisme et de son contexte

L'organisme doit déterminer les enjeux externes et internes pertinents pour sa finalité et qui affectent sa capacité à atteindre les résultats attendus de son SMSI. En pratique : contexte concurrentiel, contraintes réglementaires sectorielles, dépendances technologiques, culture interne — un exercice souvent formalisé par une analyse de type PESTEL ou SWOT, sans que la norme n'impose de méthode précise.

### 4.2 Compréhension des besoins et attentes des parties intéressées

L'organisme doit identifier les parties intéressées pertinentes pour le SMSI (clients, actionnaires, régulateurs, salariés, sous-traitants) et leurs exigences pertinentes en matière de sécurité de l'information — y compris celles qui doivent être traitées via le SMSI (juridiques, réglementaires, contractuelles). C'est ici que se construit le lien avec la cartographie des obligations réglementaires : RGPD, exigences sectorielles, clauses contractuelles clients.

### 4.3 Détermination du domaine d'application du SMSI

L'organisme doit déterminer les limites et l'applicabilité du SMSI pour établir son **domaine d'application (scope)** — probablement la décision la plus structurante de tout le projet de certification. Un domaine mal choisi (trop large, englobant des systèmes peu maîtrisés ; trop étroit, excluant artificiellement des systèmes qui interagissent avec le périmètre certifié) complique disproportionnellement tout le reste de la démarche. Le domaine doit être disponible sous forme d'information documentée — c'est un document que l'auditeur de certification examine en tout premier lieu.

### 4.4 Système de management de la sécurité de l'information

L'organisme doit établir, mettre en œuvre, tenir à jour et améliorer en continu un SMSI, y compris les processus nécessaires et leurs interactions — la clause qui pose le principe général, développé par les clauses suivantes.

## Clause 5 — Leadership

### 5.1 Leadership et engagement

La direction doit démontrer son leadership et son engagement vis-à-vis du SMSI : s'assurer que la politique et les objectifs de sécurité sont établis et compatibles avec l'orientation stratégique, intégrer les exigences du SMSI dans les processus métier, s'assurer que les ressources nécessaires sont disponibles, communiquer l'importance du management de la sécurité, s'assurer que le SMSI atteint les résultats attendus, orienter et soutenir le personnel, promouvoir l'amélioration continue.

Cette clause n'est pas une formalité rhétorique : un auditeur ISO 27001 sérieux vérifie des **preuves concrètes** d'engagement de la direction (comptes rendus de comité de direction traitant explicitement de sécurité, allocation budgétaire documentée), pas seulement une signature en bas d'une politique.

### 5.2 Politique

La direction doit établir une politique de sécurité de l'information appropriée à la finalité de l'organisme, incluant des objectifs de sécurité (ou un cadre pour les établir), un engagement à satisfaire les exigences applicables et à l'amélioration continue. La politique doit être disponible sous forme d'information documentée, communiquée au sein de l'organisme, et disponible aux parties intéressées pertinentes le cas échéant.

### 5.3 Rôles, responsabilités et autorités organisationnels

La direction doit s'assurer que les responsabilités et autorités pour les rôles pertinents en matière de sécurité de l'information sont attribuées et communiquées — y compris explicitement la responsabilité de rendre compte de la performance du SMSI à la direction elle-même.

## Clause 6 — Planification

### 6.1.1 Actions à mettre en œuvre face aux risques et opportunités (généralités)

Lors de la planification du SMSI, l'organisme doit prendre en compte les enjeux et exigences déterminés en 4.1 et 4.2, et déterminer les risques et opportunités qui doivent être traités pour donner l'assurance que le SMSI peut atteindre ses résultats attendus, prévenir ou réduire les effets indésirables, et s'améliorer en continu.

### 6.1.2 Appréciation des risques de sécurité de l'information

C'est la clause la plus substantielle sur le fond technique. L'organisme doit définir et appliquer un processus d'appréciation des risques qui :

- établit et maintient des critères de risque, incluant les critères d'acceptation du risque et les critères pour réaliser les appréciations,
- assure que des appréciations répétées produisent des résultats cohérents, valides et comparables,
- identifie les risques associés à la perte de confidentialité, d'intégrité et de disponibilité d'informations dans le domaine d'application du SMSI, et identifie les propriétaires de ces risques,
- analyse les risques : évalue les conséquences potentielles, évalue la vraisemblance réaliste, détermine les niveaux de risque,
- évalue les risques : compare les résultats de l'analyse aux critères établis, priorise les risques analysés pour le traitement.

L'organisme doit conserver des informations documentées sur ce processus. C'est ici que la norme s'articule le plus directement avec **ISO 27005**, qui fournit des lignes directrices détaillées sans être elle-même prescriptive sur la méthode de cotation à utiliser — laissant, fidèle à l'esprit de la norme, chaque organisme libre de choisir sa propre méthodologie (échelle qualitative, quantitative, méthode EBIOS RM) tant que les critères sont documentés et appliqués de façon cohérente.

### 6.1.3 Traitement des risques de sécurité de l'information

L'organisme doit définir et appliquer un processus de traitement des risques pour :

- choisir les options de traitement des risques appropriées, en tenant compte des résultats de l'appréciation des risques,
- déterminer tous les contrôles nécessaires pour mettre en œuvre les options de traitement choisies,
- comparer les contrôles déterminés avec ceux de l'**Annexe A**, pour vérifier qu'aucun contrôle nécessaire n'a été omis,
- produire une **Déclaration d'Applicabilité (SoA)** contenant les contrôles nécessaires, leur justification, s'ils sont mis en œuvre ou non, et la justification des exclusions par rapport à l'Annexe A (développée en profondeur au module 5),
- formuler un plan de traitement des risques,
- obtenir l'approbation des propriétaires des risques pour le plan de traitement et l'acceptation des risques résiduels.

Ce point de comparaison explicite avec l'Annexe A est structurant : l'Annexe A n'est jamais le point de départ de l'analyse (on ne part pas de la liste de contrôles pour en déduire des risques), c'est un **filet de sécurité** utilisé après coup pour vérifier qu'aucun risque significatif et déjà connu par la profession n'a été oublié par l'analyse de risque propre à l'organisme.

### 6.2 Objectifs de sécurité de l'information et plans pour les atteindre

L'organisme doit établir des objectifs de sécurité de l'information aux fonctions et niveaux pertinents. Ces objectifs doivent être cohérents avec la politique, mesurables (si possible), tenir compte des exigences applicables et des résultats de l'appréciation et du traitement des risques, être communiqués, mis à jour, et disponibles sous forme d'information documentée. Pour chaque objectif, l'organisme doit déterminer ce qui sera fait, les ressources nécessaires, les responsables, les échéances et comment les résultats seront évalués — une structure de plan d'action très concrète, pas une simple déclaration d'intention.

### 6.3 Planification des modifications (nouvelle en 2022)

Lorsque l'organisme détermine le besoin de modifier le SMSI, les modifications doivent être réalisées de manière planifiée — une clarification ajoutée en 2022 pour éviter des changements ad hoc non maîtrisés du système de management lui-même.
