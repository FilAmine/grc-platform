# Le risque de l'IA (1/2) : une nature sociotechnique et un cycle de vie étendu

## Le risque sociotechnique, au-delà de la seule performance technique

Déjà esquissée au module 0 de ce parcours, la nature **sociotechnique** du risque IA mérite d'être développée précisément : un système d'intelligence artificielle peut afficher une performance statistique excellente sur ses données de test — une précision élevée, un taux d'erreur faible — tout en engendrant des conséquences problématiques une fois déployé dans un contexte social réel, en raison de biais présents dans les données d'entraînement, d'une utilisation par des personnes dans un contexte que les concepteurs n'avaient jamais anticipé, ou d'une confiance excessive des utilisateurs envers des résultats présentés comme objectifs alors qu'ils reflètent des choix de conception implicites. Cette distinction rappelle directement celle déjà développée dans le parcours NIST Privacy Framework de cette plateforme entre risque de sécurité et risque vie privée — ici, la distinction s'établit entre performance technique du modèle et risque sociotechnique de son usage réel.

## Des risques émergents et difficiles à anticiper

L'AI RMF souligne que les risques posés par un système d'IA peuvent **émerger** progressivement, après le déploiement, plutôt que d'être entièrement identifiables au moment de la conception — un modèle de langage peut développer des usages détournés inattendus une fois exposé à un large public, ou un système de recommandation peut amplifier progressivement certains biais à mesure qu'il apprend des interactions réelles des utilisateurs. Cette dimension émergente distingue le risque IA de la plupart des risques de sécurité de l'information déjà étudiés dans cette plateforme, généralement plus stables une fois un système correctement sécurisé et configuré.

## Le cycle de vie étendu d'un système d'intelligence artificielle

L'AI RMF structure son analyse autour d'un **cycle de vie** en plusieurs étapes, plus étendu que celui généralement considéré pour un système d'information classique : la planification et la conception, la collecte et le traitement des données d'entraînement, la construction et l'entraînement du modèle, la vérification et la validation, le déploiement et l'usage effectif, l'exploitation et la surveillance continue, et enfin le retrait ou la mise hors service. Ce cycle de vie rappelle, par sa structuration en étapes successives, celui déjà développé pour les sept étapes du NIST RMF dans le parcours dédié de cette plateforme, mais y ajoute des étapes spécifiques à l'apprentissage automatique — la collecte de données d'entraînement et la construction du modèle — qui n'ont pas d'équivalent direct dans le cycle de vie d'un système d'information traditionnel.

## Pourquoi les données d'entraînement constituent un maillon critique propre à l'IA

L'étape de collecte et de traitement des données d'entraînement mérite une attention particulière, car elle concentre une part significative du risque sociotechnique développé plus haut dans cette leçon : des données d'entraînement historiques reflétant des discriminations passées (dans le recrutement, l'octroi de crédit, la justice) peuvent conduire un modèle à reproduire, voire amplifier, ces mêmes discriminations, indépendamment de toute intention malveillante des concepteurs — un risque qui n'a pas d'équivalent direct dans les référentiels de sécurité de l'information déjà étudiés dans cette plateforme, mais qui rejoint directement les préoccupations de discrimination algorithmique déjà esquissées dans le parcours NIST Privacy Framework à travers les problematic data actions.

## Les AI Actors : une taxonomie de rôles élargie

L'AI RMF introduit la notion d'**AI Actors** — une taxonomie de rôles impliqués tout au long du cycle de vie d'un système d'IA, bien plus large que les rôles habituellement rencontrés dans les référentiels de sécurité déjà étudiés dans cette plateforme : les concepteurs et développeurs du modèle, les équipes de test, évaluation, vérification et validation (TEVV), les déployeurs qui intègrent le modèle dans un produit ou service, les opérateurs qui l'exploitent au quotidien, et les personnes ou communautés impactées par ses décisions, qui n'ont souvent aucune relation contractuelle directe avec l'organisation ayant conçu ou déployé le système. Cette dernière catégorie — les personnes impactées sans lien contractuel — constitue une singularité par rapport à la plupart des référentiels déjà étudiés dans cette plateforme, où les parties prenantes concernées entretiennent généralement une relation contractuelle ou d'emploi avec l'organisation.

## Le lien avec la leçon suivante

Face à cette nature sociotechnique et à ce cycle de vie étendu, l'AI RMF propose un ensemble de caractéristiques qui définissent ce que signifie, concrètement, un système d'intelligence artificielle digne de confiance — l'objet de la leçon suivante de ce parcours.
