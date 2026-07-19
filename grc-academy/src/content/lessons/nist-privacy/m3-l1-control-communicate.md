# Le Core (2/3) : Control-P et Communicate-P

## Control-P : donner à l'organisation et aux individus la capacité d'agir sur les données

La fonction **Control-P** couvre le développement et la mise en œuvre d'activités permettant à l'organisation, ou aux individus concernés eux-mêmes, de gérer les données avec une granularité suffisante pour maîtriser le risque vie privée — concrètement, la capacité de désactiver ou de limiter certaines data actions spécifiques, de corriger ou de supprimer des données personnelles à la demande d'un individu, et de gérer les consentements et les préférences exprimées par les personnes concernées. Cette fonction rejoint directement, dans son objectif de donner aux personnes une prise concrète sur leurs propres données, les **droits des personnes concernées** déjà développés en détail dans le parcours RGPD de cette plateforme — droit d'accès, de rectification, d'effacement, d'opposition.

## Ce qui distingue Control-P d'une simple case à cocher de conformité

Control-P ne se limite pas à la mise en place de mécanismes techniques permettant de répondre formellement à une demande d'exercice de droit — la fonction exige que l'organisation dispose d'une **granularité opérationnelle réelle**, c'est-à-dire la capacité technique effective d'identifier précisément quelles données appartiennent à quel individu, à travers quels systèmes, et de les modifier ou supprimer sans affecter les données d'autres personnes. Une organisation qui promettrait un droit à l'effacement sans disposer de l'architecture technique nécessaire pour l'exécuter précisément et complètement à travers l'ensemble de ses systèmes — y compris ses sauvegardes et ses environnements de test — se retrouve dans une situation où sa promesse de conformité dépasse sa capacité opérationnelle réelle, un piège déjà signalé sous des formes variées à travers cette plateforme.

## Communicate-P : le dialogue transparent avec les personnes concernées

La fonction **Communicate-P** couvre le développement et la mise en œuvre d'activités permettant à l'organisation et aux individus concernés d'avoir une compréhension fiable des pratiques de traitement de données et des risques vie privée associés, et d'engager un dialogue à ce sujet — concrètement, des politiques de confidentialité rédigées dans un langage compréhensible plutôt que dans un jargon juridique impénétrable, une transparence sur les usages réels des données (pas seulement sur les usages déclarés au moment de la collecte), et des canaux effectifs permettant aux personnes concernées de poser des questions ou d'exprimer des préoccupations.

## Pourquoi la transparence constitue un objectif à part entière, distinct de la sécurité

Cette fonction illustre, peut-être plus que toute autre, la distinction fondamentale entre risque vie privée et risque de sécurité développée au module 1 de ce parcours : une organisation peut parfaitement sécuriser des données tout en maintenant une opacité totale sur leurs usages réels — un manquement à Communicate-P qui n'a strictement rien à voir avec un manquement de sécurité au sens du NIST CSF. Cette exigence de transparence rejoint directement le principe de loyauté et de transparence de l'article 5 du RGPD, déjà développé dans le parcours dédié de cette plateforme, où l'information des personnes concernées constitue une obligation autonome, indépendante de la seule sécurité du traitement.

## Comment Control-P et Communicate-P s'articulent concrètement

Ces deux fonctions se renforcent mutuellement dans la pratique : une communication transparente sur les usages réels des données (Communicate-P) permet aux personnes concernées d'exercer en connaissance de cause les capacités de contrôle mises à leur disposition (Control-P) — un dispositif qui offrirait des mécanismes de contrôle sophistiqués sans jamais informer clairement les personnes de leur existence resterait largement théorique dans son efficacité pratique, de la même façon qu'un dispositif de communication transparent mais dépourvu de mécanismes de contrôle effectifs laisserait les personnes concernées informées mais impuissantes.

## Un tableau de synthèse de ces deux fonctions

| Fonction | Objectif | Exemple concret |
|---|---|---|
| Control-P | Donner à l'organisation et aux individus la capacité d'agir sur les données | Mécanisme technique de suppression granulaire à travers tous les systèmes, y compris les sauvegardes |
| Communicate-P | Assurer un dialogue transparent sur les pratiques de traitement | Politique de confidentialité en langage clair, transparence sur les usages réels |

## Le lien avec la fonction suivante

Ces deux fonctions, centrées sur la relation entre l'organisation et les personnes concernées, se complètent par une cinquième fonction orientée vers les mesures de protection technique des données elles-mêmes — Protect-P, qui constitue le pont le plus direct entre le NIST Privacy Framework et le NIST CSF, développé à la leçon suivante de ce parcours.
