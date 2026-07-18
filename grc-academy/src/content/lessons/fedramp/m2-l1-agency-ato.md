# Les voies d'autorisation (1/2) : la voie Agence

## Deux voies distinctes pour un même objectif

FedRAMP propose deux voies d'autorisation distinctes, adaptées à des situations commerciales différentes mais aboutissant, dans les deux cas, à un dossier de sécurité reconnu et réutilisable via le principe de réciprocité développé au module 5 de ce parcours : la **voie Agence (Agency Authorization)**, développée dans cette leçon, et la voie du **FedRAMP Board** — anciennement le Joint Authorization Board (JAB) —, développée à la leçon suivante.

## Le principe de la voie Agence

Dans la voie Agence, une agence fédérale spécifique, ayant un besoin identifié pour le service cloud d'un CSP donné, **sponsorise** elle-même l'ensemble du processus d'autorisation. Cette agence sponsor joue directement le rôle d'**Authorizing Official (AO)** déjà développé dans le parcours NIST RMF de cette plateforme : elle examine le dossier de sécurité produit par le CSP, contresigné par l'évaluation indépendante du 3PAO (développé au module 3 de ce parcours), et prend elle-même la décision formelle d'accorder une **Authorization to Operate (ATO)** pour ses propres besoins.

## Un processus qui suit fidèlement les étapes du RMF

Le processus de la voie Agence reproduit fidèlement la logique séquentielle des sept étapes du RMF déjà développées dans le parcours dédié de cette plateforme, adaptée au vocabulaire propre de FedRAMP :

1. **Préparation et catégorisation** — le CSP détermine le niveau d'impact visé (module 1 de ce parcours) et rédige la documentation initiale.
2. **Élaboration du System Security Plan (SSP)** — un document exhaustif décrivant l'architecture du système, l'implémentation de chaque contrôle de la base de référence applicable, et les responsabilités partagées entre le CSP et ses clients agences.
3. **Évaluation indépendante par le 3PAO** — le 3PAO teste effectivement l'implémentation des contrôles et produit un Security Assessment Report (SAR), documentant les constats et les éventuelles faiblesses relevées.
4. **Élaboration du Plan of Action and Milestones (POA&M)** — pour toute faiblesse identifiée par le 3PAO, un plan de remédiation avec échéances, développé plus en détail au module 4 de ce parcours.
5. **Décision d'autorisation** — l'agence sponsor, en sa qualité d'Authorizing Official, examine l'ensemble du dossier (SSP, SAR, POA&M) et prend la décision formelle d'accorder ou non l'ATO.

## Les avantages et les limites de la voie Agence

La voie Agence présente l'avantage d'une **plus grande souplesse de calendrier** — le CSP négocie directement avec son agence sponsor le rythme du processus, sans dépendre de la disponibilité d'un organe collégial partagé entre de nombreux CSP candidats — et convient particulièrement bien à un CSP dont le marché cible initial se limite à une ou quelques agences déterminées. Sa limite principale réside précisément dans cette spécificité : l'ATO obtenue via la voie Agence reste, en théorie, propre à l'agence sponsor, bien que le principe de réciprocité (module 5 de ce parcours) permette à d'autres agences de s'appuyer sur ce même dossier avec un effort d'évaluation résiduel réduit plutôt que nul.

## Le rôle du CSP dans le choix de sa voie d'autorisation

Un CSP candidat à FedRAMP doit généralement identifier lui-même une agence fédérale disposée à le sponsoriser avant de pouvoir emprunter la voie Agence — une étape commerciale préalable qui suppose souvent l'existence d'un contrat ou d'un besoin déjà exprimé par cette agence, un CSP ne pouvant que rarement obtenir une autorisation FedRAMP en l'absence de tout client fédéral identifié. Ce préalable rejoint, dans son principe, une logique déjà rencontrée pour la nécessité d'un cas d'usage concret avant l'engagement d'une démarche de certification, observée par exemple pour SOC 2 dans le parcours dédié de cette plateforme.

## Le lien avec la leçon suivante

Pour un CSP dont l'offre présente un potentiel de demande beaucoup plus large, touchant potentiellement des dizaines d'agences fédérales simultanément, la voie du FedRAMP Board, développée à la leçon suivante, offre un mécanisme différent, plus exigeant en amont mais produisant une autorisation directement reconnue comme référence par l'ensemble de l'écosystème fédéral.
