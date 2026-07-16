# Référentiels cloud : CSA CCM, CIS Benchmarks, bonnes pratiques par fournisseur

## Pourquoi des référentiels spécifiques au cloud

ISO 27001, NIST CSF et SOC 2 (module 2) sont **agnostiques de la technologie** — ils décrivent des objectifs de contrôle ("le contrôle d'accès doit être approprié") sans prescrire de configuration précise pour un service cloud donné. Des référentiels complémentaires, spécifiquement dédiés au cloud, comblent ce niveau de détail technique.

## CSA CCM (Cloud Controls Matrix)

Développée par la **Cloud Security Alliance**, la CCM est une matrice de contrôles pensée spécifiquement pour les environnements cloud, organisée en domaines (gouvernance et gestion des risques, sécurité des applications et interfaces, chiffrement et gestion des clés, gestion des identités, sécurité des interfaces de programmation, etc.). Sa particularité utile : chaque contrôle est **mappé vers les référentiels généralistes** (ISO 27001, NIST, PCI DSS...), ce qui en fait un excellent outil de traduction entre les objectifs de contrôle génériques et leur implémentation cloud concrète.

La CSA propose également le programme **STAR (Security, Trust, Assurance and Risk)**, un registre public où les fournisseurs cloud publient leur auto-évaluation ou une attestation tierce de conformité à la CCM — utile lors de l'évaluation d'un fournisseur ou sous-traitant cloud (pertinent pour la cartographie des risques tiers du module 1).

## CIS Benchmarks

Le **Center for Internet Security (CIS)** publie des guides de configuration détaillés et prescriptifs, service par service et fournisseur par fournisseur (CIS AWS Foundations Benchmark, CIS Azure Foundations Benchmark, CIS Google Cloud Platform Foundation Benchmark, etc.). Contrairement à la CCM, les CIS Benchmarks sont **directement actionnables techniquement** : "le MFA doit être activé sur le compte root", "les logs d'accès doivent être conservés au moins 90 jours", "aucun bucket de stockage ne doit être accessible publiquement en lecture par défaut".

Un usage très répandu : automatiser la vérification de conformité aux CIS Benchmarks via des outils de **Cloud Security Posture Management (CSPM)**, qui scannent en continu la configuration réelle d'un environnement cloud et signalent les écarts par rapport au Benchmark — transformant un contrôle normalement vérifié ponctuellement en audit en une vérification continue, bien plus alignée avec le rythme de changement d'une infrastructure cloud moderne (déploiements fréquents, infrastructure as code).

## Les référentiels natifs des fournisseurs

Chaque grand fournisseur cloud publie son propre cadre de bonnes pratiques d'architecture, qui intègre la sécurité comme un pilier parmi d'autres (fiabilité, performance, coût, excellence opérationnelle) :

- **AWS Well-Architected Framework** — pilier "Security".
- **Azure Well-Architected Framework** — pilier "Security".
- **Google Cloud Architecture Framework** — pilier "Security, Privacy, and Compliance".

Ces cadres sont utiles en phase de conception d'architecture (revue d'architecture avant mise en production), tandis que les CIS Benchmarks sont plus utiles en vérification continue de configuration, et la CCM est plus utile pour le mapping de conformité transverse entre référentiels.

## Comment articuler ces référentiels avec la formation vue jusqu'ici

Ces trois familles de référentiels cloud ne remplacent pas ISO 27001, NIST CSF ou SOC 2 — ils **opérationnalisent** leurs exigences génériques pour un environnement cloud précis :

| Niveau | Référentiel | Rôle |
|---|---|---|
| Stratégique / gouvernance | ISO 27001, NIST CSF | Définir le système de management et la maturité globale |
| Contractuel / preuve externe | SOC 2, ISO 27001 | Démontrer la conformité à un client ou partenaire |
| Mapping cloud transverse | CSA CCM | Traduire les objectifs de contrôle génériques vers le cloud |
| Configuration technique précise | CIS Benchmarks | Vérifier et corriger la configuration réelle, service par service |
| Conception d'architecture | Well-Architected Frameworks (AWS/Azure/GCP) | Guider les choix d'architecture avant déploiement |

Une organisation mature en Security by Design cloud n'a donc pas à choisir entre ces référentiels : elle les utilise à des niveaux différents de la même démarche, du plus stratégique (pourquoi et à quel niveau de risque) au plus opérationnel (quel paramètre exact configurer sur quel service).
