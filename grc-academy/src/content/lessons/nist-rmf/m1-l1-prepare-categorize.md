# Les sept étapes du RMF (1/4) : Prepare et Categorize

## Une septième étape ajoutée tardivement, mais devenue la plus structurante

Le RMF, dans sa version initiale (SP 800-37 Rev. 1), comptait six étapes commençant par la catégorisation du système. La révision majeure de 2018 (**Rev. 2**) a ajouté une étape préalable, **Prepare**, en reconnaissant explicitement ce que d'autres référentiels étudiés dans cette plateforme avaient déjà formalisé sous d'autres noms : sans préparation organisationnelle et sans gouvernance clarifiée en amont, les étapes suivantes du processus produisent des résultats incohérents. Cette évolution rappelle directement l'ajout de la fonction **Govern** au NIST CSF 2.0, étudiée dans le deuxième parcours de cette plateforme — les deux référentiels ont indépendamment reconnu la même lacune dans leurs versions antérieures.

## Étape 1 — Prepare (Préparer)

Cette étape se décompose en deux niveaux, une distinction essentielle propre au RMF :

### Le niveau organisationnel

L'organisation identifie les rôles clés (développés en détail au module 3 : Authorizing Official, Chief Information Security Officer, etc.), établit une stratégie de gestion des risques au niveau de l'organisation entière, réalise une évaluation des risques au niveau organisationnel, définit une stratégie de contrôles communs (les contrôles fournis de façon centralisée par un **Common Control Provider** et hérités par plusieurs systèmes, plutôt que réimplémentés système par système), et établit une stratégie de surveillance continue à l'échelle de l'organisation.

### Le niveau système

Pour le système d'information spécifique concerné, cette étape identifie sa mission et les processus métier qu'il soutient, ses parties prenantes, ses actifs, son périmètre d'autorisation (authorization boundary — l'équivalent, dans le vocabulaire du RMF, du domaine d'application d'un SMSI ISO 27001 déjà développé dans le parcours dédié de cette plateforme), et réalise une évaluation des risques propre au système.

Le périmètre d'autorisation mérite une attention particulière : il détermine précisément quels composants techniques sont couverts par l'autorisation d'exploitation qui sera obtenue à l'issue du processus (étape 6) — un périmètre mal défini produit les mêmes déséquilibres déjà observés pour le domaine d'application ISO 27001 ou le scoping SOC 2 dans les parcours précédents de cette plateforme : trop large, il complique disproportionnellement le reste du processus ; trop étroit, il risque de laisser hors de l'autorisation des composants critiques pour la mission du système.

## Étape 2 — Categorize (Catégoriser)

Cette étape s'appuie sur une norme fédérale à caractère obligatoire : **FIPS 199** (Federal Information Processing Standards Publication 199), qui impose de catégoriser chaque système selon le niveau d'impact potentiel — **Faible, Modéré ou Élevé** — d'une atteinte à sa confidentialité, son intégrité et sa disponibilité.

### La méthode de catégorisation

Pour chaque type d'information traité par le système, on détermine séparément l'impact potentiel sur la confidentialité, l'intégrité et la disponibilité, en cas de perte de cette propriété de sécurité — le guide **SP 800-60** aide à cartographier des types d'informations courants (données financières, données de ressources humaines, données de santé) vers des niveaux d'impact recommandés, sans dispenser d'une analyse propre au contexte réel du système.

La catégorisation globale du système retient, pour chacune des trois propriétés (confidentialité, intégrité, disponibilité), le niveau le plus élevé parmi tous les types d'information traités — un principe dit du **"high-water mark"** (plus haut niveau atteint). Un système qui traite majoritairement des données à faible enjeu, mais qui inclut un seul type d'information à impact Élevé sur la confidentialité, sera catégorisé Élevé sur cette propriété pour l'ensemble du système — une règle volontairement conservatrice, qui pousse à isoler dans des systèmes distincts, dès la conception, les données les plus sensibles plutôt que de les mélanger avec des données à moindre enjeu si l'on souhaite éviter que l'ensemble du système hérite du niveau de contrôle le plus exigeant.

### Un exemple concret de catégorisation

Un système de gestion des ressources humaines d'une agence fédérale, traitant des données d'identification de ses employés (impact Modéré sur la confidentialité en cas de divulgation), des données de paie (impact Modéré sur l'intégrité, une erreur de paie affectant significativement mais pas gravement les employés concernés), et devant rester disponible pendant les périodes de paie sans que son indisponibilité ponctuelle ne compromette gravement la mission de l'agence (impact Faible sur la disponibilité), sera catégorisé globalement **Modéré** — le plus haut niveau atteint parmi confidentialité et intégrité, la disponibilité restant en retrait sans influencer la catégorisation globale à la hausse.

## Pourquoi ces deux étapes conditionnent tout le reste du processus

La catégorisation obtenue à l'étape 2 détermine directement, à l'étape suivante, quelle **base de référence de contrôles** (baseline) parmi les trois définies par SP 800-53B — Faible, Modéré, ou Élevé — devra être sélectionnée comme point de départ. Une erreur de catégorisation en amont (sous-évaluer l'impact réel d'une atteinte à la confidentialité d'un système, par exemple) se répercute mécaniquement sur l'ensemble du processus : un jeu de contrôles insuffisant sera sélectionné, implémenté et évalué, jusqu'à ce qu'un audit ou un incident révèle l'écart — une dynamique qui rappelle directement l'importance, déjà soulignée pour la Déclaration d'Applicabilité d'ISO 27001 dans le parcours dédié de cette plateforme, de fonder chaque étape ultérieure sur une analyse de risque initiale réellement rigoureuse plutôt que sur une évaluation de complaisance.
