# Le catalogue CSCF et les types d'architecture (2/2) : structure du catalogue

## Trois objectifs de sécurité comme architecture générale

Le Customer Security Controls Framework organise l'ensemble de ses contrôles autour de **trois objectifs de sécurité**, développés en détail au module 2 de ce parcours :

- **Objectif 1 — Sécuriser votre environnement (Secure your environment)** — la protection de l'infrastructure locale utilisée pour accéder au réseau SWIFT.
- **Objectif 2 — Connaître et limiter les accès (Know and limit access)** — la gestion rigoureuse des identités et des privilèges d'accès aux systèmes SWIFT.
- **Objectif 3 — Détecter et réagir (Detect and respond)** — la capacité à détecter une activité anormale et à y répondre efficacement.

Cette architecture en trois objectifs rappelle directement, dans sa logique de couverture du cycle complet prévention/détection/réponse, celle déjà développée pour les six fonctions du NIST CSF 2.0 dans le parcours dédié de cette plateforme (Govern, Identify, Protect, Detect, Respond, Recover) — le CSCF concentre cependant son propre périmètre sur un sous-ensemble plus restreint et plus opérationnel, directement focalisé sur l'infrastructure de connexion au réseau de messagerie plutôt que sur l'ensemble de la posture de cybersécurité d'une organisation.

## Deux catégories de contrôles : obligatoires et consultatifs

Au sein de chaque objectif, le CSCF distingue deux catégories de contrôles :

- **Les contrôles obligatoires (mandatory controls)** — un socle minimal que tout utilisateur SWIFT doit impérativement implémenter, quel que soit son type d'architecture (module 1 de ce parcours), et dont le respect conditionne directement la validité de l'attestation annuelle développée au module 3.
- **Les contrôles consultatifs (advisory controls)** — des bonnes pratiques recommandées par SWIFT, non obligatoires mais fortement encouragées, qui préfigurent souvent les contrôles obligatoires des versions futures du catalogue, développées au module 6 de ce parcours.

Cette distinction entre un socle obligatoire et des recommandations non contraignantes rappelle celle déjà rencontrée pour les Safeguards des Implementation Groups des CIS Controls dans le parcours dédié de cette plateforme, où seul l'IG1 constitue un socle véritablement universel tandis que les IG2 et IG3 ajoutent des exigences progressivement plus poussées.

## Un exemple concret par objectif

Sans entrer dans le détail exhaustif développé au module 2, quelques exemples illustrent la nature des contrôles CSCF : au titre de l'Objectif 1, la segmentation du réseau local isolant l'environnement SWIFT du reste du système d'information de l'utilisateur — une exigence qui rappelle directement celle déjà développée pour la segmentation réseau réduisant le périmètre d'audit dans le parcours PCI DSS de cette plateforme ; au titre de l'Objectif 2, l'authentification multifacteur pour tout accès aux systèmes SWIFT ; au titre de l'Objectif 3, la détection d'anomalies dans les schémas de transaction habituels d'un utilisateur, directement inspirée des enseignements tirés de l'incident de la banque centrale du Bangladesh développé au module 0 de ce parcours.

## Comment ce catalogue se compare à l'Annexe A d'ISO 27001

Le CSCF partage avec l'Annexe A d'ISO 27001, déjà développée en détail dans le parcours dédié de cette plateforme, une structure de contrôles répartis par thème et directement actionnables — mais il s'en distingue par son caractère beaucoup plus resserré et spécifique : quelques dizaines de contrôles CSCF, concentrés exclusivement sur l'infrastructure de connexion au réseau SWIFT, contre 93 contrôles ISO 27001 couvrant l'ensemble du périmètre de sécurité de l'information d'une organisation. Un utilisateur SWIFT déjà certifié ISO 27001 dispose ainsi d'une large part de la documentation et des contrôles techniques nécessaires pour satisfaire le CSCF, selon le principe de mapping plutôt que de duplication déjà rencontré à de multiples reprises dans cette plateforme.

## Un tableau de synthèse des trois objectifs

| Objectif | Finalité | Exemple de contrôle |
|---|---|---|
| 1 — Sécuriser votre environnement | Protéger l'infrastructure locale de connexion | Segmentation du réseau isolant l'environnement SWIFT |
| 2 — Connaître et limiter les accès | Maîtriser les identités et privilèges | Authentification multifacteur pour tout accès SWIFT |
| 3 — Détecter et réagir | Identifier et traiter les activités anormales | Détection d'anomalies dans les schémas de transaction |

## Le lien avec le module suivant

Cette architecture générale en trois objectifs et deux catégories de contrôles mérite d'être développée plus en détail, objectif par objectif — l'objet du module suivant de ce parcours.
