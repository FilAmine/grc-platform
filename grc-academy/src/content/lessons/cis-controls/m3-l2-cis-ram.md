# CIS RAM : justifier le caractère "raisonnable" des Safeguards choisis

## Une question juridique à laquelle les Implementation Groups ne répondent qu'en partie

Les Implementation Groups (module 2) offrent un point de départ pragmatique pour prioriser les Safeguards, mais ils ne répondent pas complètement à une question qu'un tribunal, un régulateur ou une compagnie d'assurance peut poser après un incident : l'organisation a-t-elle mis en œuvre des mesures de sécurité **raisonnables**, compte tenu de son contexte spécifique — pas seulement un profil générique prédéfini, mais une analyse propre à sa situation réelle ? Le **CIS RAM (Risk Assessment Method)**, développé par le CIS en partenariat avec la société de conseil HALOCK Security Labs, répond directement à cette question.

## Le fondement méthodologique : le DoCRA

CIS RAM s'appuie sur le standard **DoCRA (Duty of Care Risk Analysis)**, un référentiel qui structure l'évaluation du risque autour d'un principe emprunté au droit de la responsabilité civile plutôt qu'à la seule discipline technique de la cybersécurité : une mesure de sécurité est jugée **raisonnable** lorsque son coût et sa contrainte pour l'organisation ne sont pas manifestement disproportionnés par rapport au risque qu'elle permet d'éviter pour les tiers potentiellement affectés (clients, partenaires, personnes dont les données sont traitées).

Ce principe de mise en balance rappelle directement le test de proportionnalité déjà rencontré pour la base légale de l'intérêt légitime du RGPD, développé dans le parcours dédié de cette plateforme — les deux méthodes cherchent, avec des vocabulaires distincts (l'un juridique européen, l'autre issu du droit américain de la responsabilité civile), à arbitrer explicitement entre le coût d'une mesure de sécurité et le bénéfice qu'elle procure aux personnes potentiellement affectées par le risque qu'elle traite.

## Comment CIS RAM structure l'analyse

La méthode invite à évaluer chaque Safeguard envisagé selon trois dimensions mises en balance :

1. **Le risque évité** — quelle est la probabilité et l'impact du risque que ce Safeguard permet de réduire, pour l'organisation elle-même et pour les tiers potentiellement affectés ?
2. **Le fardeau du Safeguard** — quel est le coût, la complexité, et l'impact opérationnel de la mise en œuvre de ce Safeguard pour l'organisation ?
3. **L'équilibre entre les deux** — le risque évité justifie-t-il raisonnablement le fardeau imposé, compte tenu des pratiques communément admises par des organisations comparables ?

Un Safeguard dont le fardeau de mise en œuvre est manifestement disproportionné par rapport au risque réel qu'il permet d'éviter peut légitimement ne pas être retenu, à condition que cette décision soit **documentée et justifiée** — une logique directement comparable à la justification d'exclusion de la Déclaration d'Applicabilité d'ISO 27001, déjà développée dans le parcours dédié de cette plateforme, mais formalisée ici selon un standard reconnu et défendable devant un tiers externe (régulateur, tribunal, assureur).

## Pourquoi cette méthode compte particulièrement aux États-Unis

Le standard de la **"sécurité raisonnable" (reasonable security)** est directement référencé par de nombreuses lois américaines de protection des données au niveau des États, ainsi que par les actions de mise en application de la Federal Trade Commission (FTC) en matière de pratiques commerciales déloyales ou trompeuses lorsqu'une organisation prétend assurer un niveau de sécurité qu'elle ne respecte pas réellement — sans qu'aucune de ces sources légales ne définisse précisément ce que "raisonnable" signifie techniquement. CIS RAM comble directement ce vide en offrant une méthode structurée et documentée pour démontrer, après coup, que les décisions de sécurité de l'organisation reposaient sur une analyse de proportionnalité réelle plutôt que sur l'absence de toute réflexion.

## L'articulation entre CIS RAM et les Implementation Groups

Ces deux outils ne sont pas concurrents mais complémentaires : les Implementation Groups (module 2) offrent un point de départ rapide et éprouvé par consensus communautaire, utile en particulier pour une organisation qui découvre le sujet ; CIS RAM permet, dans un second temps, d'**affiner et de justifier** ce choix de Safeguards au regard du contexte réellement spécifique de l'organisation — en documentant, par exemple, pourquoi tel Safeguard normalement classé IG2 a été avancé au rang de priorité immédiate compte tenu d'un risque particulier identifié, ou pourquoi tel autre Safeguard IG1 a été temporairement différé faute de menace réaliste dans le contexte précis de l'organisation, avec toute la rigueur de justification qu'une telle dérogation appelle.

## Ce que cette méthode ajoute à la panoplie déjà développée dans cette plateforme

CIS RAM introduit, dans cette plateforme, un angle qui n'avait pas encore été développé aussi frontalement : la dimension de **défendabilité juridique** d'une décision de sécurité, au-delà de sa seule justification technique ou de gestion des risques interne. C'est un rappel utile que la gestion des risques de cybersécurité, aussi rigoureuse soit-elle sur le plan technique, doit souvent aussi pouvoir se justifier a posteriori devant des parties externes qui n'ont pas participé à la décision initiale — un point de convergence direct avec le principe d'accountability déjà développé à plusieurs reprises dans cette plateforme, notamment dans les parcours ISO 27001 et RGPD.
