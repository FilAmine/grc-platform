# Le catalogue CSCF et les types d'architecture (1/2) : les Architecture Types

## Pourquoi le périmètre d'application varie d'un utilisateur à l'autre

Contrairement à des référentiels comme ISO 27001 ou SOC 2, dont le périmètre est librement défini par chaque organisation, le périmètre exact des contrôles du **Customer Security Controls Framework (CSCF)** applicables à un utilisateur SWIFT donné dépend directement de la manière technique dont cet utilisateur se connecte au réseau — un principe de proportionnalité à la configuration technique réelle qui rappelle, dans sa logique, celui déjà rencontré pour les niveaux d'impact FedRAMP ou les niveaux d'évaluation TISAX, mais appliqué ici non pas à un choix de besoin de protection, mais à une réalité architecturale objective et déjà existante.

## Les quatre grands types d'architecture (Architecture Types)

SWIFT distingue plusieurs types d'architecture de connexion, chacun impliquant un périmètre de contrôles CSCF différent :

- **Architecture Type A1** — l'utilisateur héberge et exploite lui-même l'intégralité de son infrastructure de connectivité SWIFT (interface applicative, serveur de connexion, éventuellement un HSM pour la signature des messages) au sein de ses propres locaux — le périmètre de contrôles le plus large, puisque l'utilisateur porte l'entière responsabilité de la sécurité de bout en bout.
- **Architecture Type A2** — l'utilisateur héberge sa propre interface applicative, mais s'appuie sur un **prestataire de services de connexion (service bureau)** pour la partie connectivité réseau proprement dite — un partage de responsabilité qui rappelle directement celui déjà développé pour la répartition des responsabilités entre un fournisseur cloud et son client dans le parcours FedRAMP de cette plateforme.
- **Architecture Type A3** — l'utilisateur exploite uniquement une interface d'accès légère, l'essentiel de l'infrastructure étant hébergée et exploitée par un prestataire tiers ou par SWIFT lui-même (à travers ses propres offres de connectivité) — un périmètre de contrôles propres à l'utilisateur nettement plus restreint.
- **Architecture Type B** — l'utilisateur ne dispose d'aucune infrastructure de connexion propre et accède au réseau exclusivement par l'intermédiaire d'un tiers agissant en son nom (un "service bureau" au sens plein, ou une banque correspondante) — un cas où l'essentiel des contrôles CSCF incombe au prestataire plutôt qu'à l'utilisateur final lui-même.

## Une logique de responsabilité partagée déjà familière dans cette plateforme

Cette gradation des types d'architecture, où le périmètre de responsabilité de l'utilisateur diminue à mesure que davantage de composants techniques sont externalisés vers un prestataire, rejoint directement le modèle de responsabilité partagée déjà développé pour les environnements cloud dans le module Cloud Security by Design du premier parcours de cette plateforme, ou pour la répartition des rôles entre CSP et agence sponsor dans le parcours FedRAMP — plus une organisation externalise de composants techniques, plus elle doit s'assurer, en contrepartie, que son prestataire respecte lui-même les contrôles CSCF qui lui incombent.

## Pourquoi ce choix d'architecture n'est pas neutre pour la conformité

Un utilisateur SWIFT de petite taille, dépourvu d'équipe de sécurité informatique dédiée, a souvent tout intérêt à opter pour une architecture de type A3 ou B, transférant l'essentiel du fardeau de conformité CSCF vers un prestataire spécialisé disposant déjà de son propre dispositif de sécurité éprouvé — un choix qui rappelle celui déjà développé pour le recours à des prestataires cloud plutôt qu'à une infrastructure propre dans le parcours FedRAMP de cette plateforme. À l'inverse, une grande banque internationale, disposant de ses propres équipes de sécurité et soucieuse de garder la maîtrise complète de son infrastructure critique, opte plus fréquemment pour une architecture de type A1, malgré le périmètre de contrôles CSCF plus large qui en découle.

## Ce que ce choix ne dispense jamais de vérifier

Quel que soit le type d'architecture retenu, l'utilisateur reste toujours responsable de vérifier que son ou ses prestataires (service bureau, HSM partagé, interface hébergée) respectent effectivement les contrôles CSCF qui leur incombent au titre de l'architecture choisie — un principe qui rappelle directement celui déjà développé pour les Complementary User Entity Controls des rapports SOC 1 dans le parcours SOX de cette plateforme : l'externalisation d'un composant technique ne transfère jamais la responsabilité finale de la conformité, elle en modifie seulement la répartition opérationnelle.

## Un tableau de synthèse des types d'architecture

| Type d'architecture | Ce que l'utilisateur héberge lui-même | Périmètre de contrôles CSCF propres à l'utilisateur |
|---|---|---|
| A1 | L'intégralité de l'infrastructure de connexion | Le plus large |
| A2 | L'interface applicative, mais pas la connectivité réseau | Large, partagé avec un prestataire de connectivité |
| A3 | Une interface d'accès légère uniquement | Restreint |
| B | Aucune infrastructure propre, accès via un tiers | Le plus restreint, l'essentiel incombant au prestataire |

## Le lien avec la structure du CSCF, développée à la leçon suivante

Une fois le type d'architecture déterminé, l'utilisateur peut identifier précisément quels contrôles du catalogue CSCF lui sont applicables — la structure de ce catalogue, organisée en trois objectifs de sécurité et deux catégories de contrôles, fait l'objet de la leçon suivante de ce parcours.
