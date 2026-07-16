# IAM, chiffrement et segmentation réseau dans le cloud

## IAM : le contrôle qui compte le plus

Dans une architecture cloud, il n'existe plus de périmètre réseau unique à défendre — **l'identité est devenue le nouveau périmètre**. La quasi-totalité des incidents cloud graves impliquent, à un moment de la chaîne, une mauvaise configuration IAM : rôle trop permissif, clé d'accès à privilèges élevés exposée, absence de MFA sur un compte à fort privilège.

### Principes IAM cloud non négociables

- **Rôles plutôt qu'utilisateurs partagés** — chaque service, chaque fonction applicative dispose de son propre rôle avec des permissions scoping précisément à ses besoins (moindre privilège appliqué techniquement, pas seulement en principe).
- **Pas de clés d'accès statiques quand un rôle temporaire est possible** — privilégier les identités de service à courte durée de vie (ex. rôles assumés, tokens temporaires) plutôt que des clés d'accès permanentes stockées dans du code ou des fichiers de configuration.
- **MFA obligatoire sur tout compte à privilège élevé**, en particulier les comptes racine/administrateur du compte cloud lui-même — un compte root cloud compromis équivaut à la compromission de l'ensemble de l'environnement.
- **Séparation des tâches (segregation of duties)** — la personne qui peut déployer du code en production ne devrait idéalement pas être la même qui peut modifier les règles d'audit/journalisation qui surveillent ce déploiement.
- **Revue périodique des accès et des rôles inutilisés** — un rôle créé pour un projet terminé, jamais désactivé, est une vulnérabilité dormante ; les outils cloud modernes (IAM Access Analyzer sur AWS, par exemple) peuvent détecter automatiquement les permissions accordées mais jamais utilisées.

## Chiffrement : au repos et en transit, par défaut

### Chiffrement au repos

Toute donnée stockée (base de données, objets de stockage, volumes de disque, sauvegardes) devrait être chiffrée par défaut, sans dépendre d'une action manuelle de configuration. Les fournisseurs cloud majeurs proposent un chiffrement natif quasi gratuit en performance — l'absence de chiffrement au repos est donc rarement justifiable techniquement, et de plus en plus rarement acceptée en audit (ISO 27001 Annexe A 8.24, SOC 2, RGPD article 32 l'exigent tous, sous des formulations différentes — voir le comparatif du module 2).

Un point souvent négligé : **qui détient les clés de chiffrement ?** Un chiffrement géré entièrement par le fournisseur protège contre le vol physique d'un disque, mais pas contre un accès administratif abusif du fournisseur lui-même (rarement un risque réaliste, mais parfois une exigence contractuelle explicite de certains clients). Des options de gestion de clés par le client (BYOK — Bring Your Own Key, ou des services de gestion de clés dédiés) existent pour ce niveau d'exigence.

### Chiffrement en transit

Tout flux réseau, y compris **entre services internes au sein d'un même réseau privé cloud**, devrait être chiffré (TLS), pas seulement les flux exposés à internet. C'est une application directe du principe Zero Trust (module 3) : ne pas supposer qu'un réseau "interne" est automatiquement sûr.

## Segmentation réseau dans le cloud

### Réseaux virtuels et sous-réseaux

Un réseau cloud (VPC sur AWS, VNet sur Azure, VPC sur GCP) doit être segmenté en sous-réseaux selon la sensibilité et la fonction : un sous-réseau public (rarement nécessaire, réservé aux points d'entrée strictement indispensables comme une passerelle applicative), des sous-réseaux privés pour les applications, des sous-réseaux encore plus restreints pour les bases de données, sans accès direct depuis internet.

### Groupes de sécurité et listes de contrôle d'accès

Les groupes de sécurité (security groups) définissent, service par service, quels flux entrants et sortants sont autorisés. La bonne pratique est un modèle **par défaut fermé** (deny by default) : aucun flux n'est autorisé sauf règle explicite — l'inverse de configurations héritées qui autorisent tout par défaut et retirent au cas par cas, bien plus risqué et bien plus difficile à auditer.

### Micro-segmentation (Zero Trust appliqué au réseau cloud)

Au-delà de la segmentation par sous-réseau, la micro-segmentation restreint les communications **service par service** : le service de paiement ne peut communiquer qu'avec la base de données de paiement et le service d'authentification, jamais directement avec le service de reporting analytique par exemple — même si les deux sont dans le même réseau privé.

## Comment ces trois piliers se combinent en pratique

Un scénario d'incident typique illustre pourquoi ces trois contrôles doivent être pensés ensemble : un attaquant exploite une vulnérabilité applicative (par exemple une injection) pour obtenir un accès initial. La segmentation réseau limite ce qu'il peut atteindre depuis ce point d'entrée. Si malgré tout il atteint une base de données, le chiffrement au repos limite la valeur de données exfiltrées si les clés ne sont pas elles-mêmes compromises. Et si l'attaquant tente de pivoter en utilisant des identifiants trouvés sur le système compromis, un IAM correctement scopé au moindre privilège limite drastiquement l'étendue de ce qu'il peut faire avec ces identifiants — c'est la défense en profondeur (module 3) appliquée concrètement à une architecture cloud.
