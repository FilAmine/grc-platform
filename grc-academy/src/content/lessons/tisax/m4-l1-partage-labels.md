# Le partage des résultats (1/2) : labels et consentement explicite

## Une différence structurante avec le FedRAMP Marketplace

Le parcours FedRAMP de cette plateforme a développé le FedRAMP Marketplace comme un **registre public**, consultable par toute agence fédérale sans autorisation préalable du fournisseur évalué. TISAX adopte un principe radicalement différent, mieux adapté à un contexte de relations commerciales privées entre entreprises concurrentes : le résultat d'une évaluation TISAX (le **label**) n'est **jamais visible par défaut** d'un partenaire commercial tiers — le fournisseur évalué doit explicitement **partager** son label, partenaire par partenaire, via le portail ENX, pour que celui-ci puisse le consulter.

## Le mécanisme de partage sur le portail ENX

Concrètement, un fournisseur qui a obtenu un label TISAX se connecte au portail ENX et **invite** chaque partenaire commercial souhaité (un OEM client, ou un fournisseur de rang supérieur dans la chaîne d'approvisionnement) à consulter son label — ce partenaire doit alors accepter cette invitation pour accéder au détail du résultat. Ce mécanisme de partage bilatéral et explicite, plutôt que la publication dans un registre unique et public, rappelle davantage le fonctionnement d'un rapport SOC 2, dont la diffusion reste habituellement restreinte aux clients et partenaires ayant un intérêt légitime et signé un accord de confidentialité, déjà développé dans le parcours dédié de cette plateforme — TISAX formalise simplement ce même principe de diffusion restreinte à travers une plateforme numérique dédiée plutôt que par l'échange de documents PDF.

## Ce que révèle, ou ne révèle pas, un label partagé

Un label TISAX partagé indique typiquement le niveau d'évaluation atteint (AL1, AL2 ou AL3), les objectifs d'évaluation couverts (sécurité de l'information, protection des prototypes, protection des données), et un résultat synthétique de conformité — mais ne divulgue pas nécessairement, par défaut, le détail complet du rapport d'évaluation sous-jacent (les niveaux de maturité précis obtenus pour chaque critère), qu'un partenaire particulièrement exigeant peut néanmoins demander à consulter dans le cadre d'une diligence renforcée. Cette gradation de transparence — un résultat synthétique largement partagé, un rapport détaillé réservé aux relations les plus critiques — rappelle celle déjà rencontrée pour les différents niveaux de détail d'un rapport SOC 2 (le rapport complet réservé aux clients existants et prospects sous accord de confidentialité, par opposition à une simple lettre d'attestation plus largement diffusable).

## Pourquoi ce modèle convient particulièrement bien à un secteur concurrentiel

Ce principe de partage par consentement explicite, plutôt qu'un registre entièrement public comme celui de FedRAMP, se justifie directement par la nature du secteur automobile : les fournisseurs évalués sont souvent en concurrence directe les uns avec les autres pour les mêmes marchés auprès des mêmes OEM, et un registre public dévoilerait des informations potentiellement sensibles sur leur posture de sécurité à des concurrents n'ayant aucune relation contractuelle légitime avec eux — une préoccupation de confidentialité concurrentielle sans équivalent direct dans le contexte de FedRAMP, où l'ensemble des parties prenantes (agences fédérales, CSP) opère dans un cadre gouvernemental unique plutôt que dans un écosystème de fournisseurs concurrents entre eux.

## Un tableau comparatif des deux modèles de diffusion

| Aspect | FedRAMP Marketplace | Portail ENX (TISAX) |
|---|---|---|
| Visibilité par défaut | Registre public | Invisible, partage explicite requis |
| Mécanisme d'accès | Consultation libre par toute agence fédérale | Invitation bilatérale acceptée par le partenaire |
| Contexte justifiant ce choix | Écosystème unique (gouvernement fédéral) | Fournisseurs souvent concurrents entre eux |
| Comparable, dans cette plateforme, à | Un registre public de certifications | Un rapport SOC 2 diffusé sous accord de confidentialité |

## Le lien avec la durée de validité, développée à la leçon suivante

Ce mécanisme de partage n'a de sens que si le label partagé reste à jour et fiable dans la durée — la question de la validité temporelle d'un label TISAX et des modalités de son renouvellement fait l'objet de la leçon suivante de ce parcours.
