# Comparatif : comment ces référentiels s'articulent

## Une même réalité, quatre langages différents

ISO 27001, NIST CSF, SOC 2 et le RGPD ne sont pas concurrents — ils répondent à des questions différentes, souvent pour des audiences différentes, tout en se recoupant fortement sur le fond technique.

| Référentiel | Nature | Ce qu'il répond | Audience typique |
|---|---|---|---|
| **ISO 27001** | Norme certifiable | "Avons-nous un système de management de la sécurité qui fonctionne et s'améliore ?" | Clients internationaux, appels d'offres, marché européen/mondial |
| **NIST CSF 2.0** | Cadre volontaire (non certifiable) | "Quelle est notre maturité cybersécurité, fonction par fonction ?" | Direction, régulateurs américains, secteurs critiques |
| **SOC 2** | Rapport d'audit (attestation) | "Ces contrôles précis fonctionnent-ils réellement sur une période donnée ?" | Clients B2B SaaS, marché nord-américain |
| **RGPD** | Loi (obligation légale) | "Les données personnelles sont-elles traitées licitement et protégées ?" | Autorités de contrôle, personnes concernées — obligatoire, pas un choix |

## Où ils se recoupent

La majorité des contrôles techniques (contrôle d'accès, chiffrement, journalisation, gestion des vulnérabilités, réponse à incident) sont **communs** aux quatre référentiels, formulés différemment :

- ISO 27001 Annexe A 8.24 (cryptographie) ≈ SOC 2 critère de sécurité sur le chiffrement ≈ RGPD article 32 (mesures techniques appropriées, dont le chiffrement est cité explicitement) ≈ NIST CSF sous-catégorie "Protect — Data Security".
- ISO 27001 Annexe A 5.15 (contrôle d'accès) ≈ SOC 2 "Logical Access Controls" ≈ NIST CSF "Protect — Identity Management and Access Control".

C'est pourquoi une organisation qui vise plusieurs référentiels simultanément ne construit **pas quatre dispositifs de sécurité distincts**, mais un seul socle de contrôles techniques, avec une couche de mapping documentaire qui traduit chaque contrôle vers le vocabulaire attendu par chaque référentiel lors d'un audit ou d'une revue.

## Où ils divergent réellement

- **Champ d'application** : le RGPD porte spécifiquement sur les données personnelles ; ISO 27001, NIST CSF et SOC 2 portent sur l'information et les systèmes en général, personnelle ou non.
- **Force obligatoire** : le RGPD est une loi — sa violation expose à des sanctions administratives et judiciaires. ISO 27001, NIST CSF et SOC 2 sont des démarches volontaires ou contractuelles — leur "sanction" est commerciale (perte de contrats, d'appels d'offres) ou réputationnelle, jamais une amende d'autorité publique.
- **Preuve attendue** : ISO 27001 valide un *système* de management dans la durée (certificat sur 3 ans avec surveillance annuelle) ; SOC 2 Type II valide le *fonctionnement effectif* de contrôles précis sur une fenêtre d'observation ; NIST CSF n'aboutit à aucune preuve formelle externe, c'est un outil d'auto-évaluation et de communication.

## Une stratégie de mapping, pas une pile de projets

L'erreur classique d'une organisation qui découvre qu'elle doit répondre à plusieurs de ces référentiels est de créer une équipe et un projet séparé pour chacun. La bonne pratique GRC consiste à :

1. Construire **un seul catalogue de contrôles internes**, aligné sur le référentiel le plus structurant pour l'organisation (souvent ISO 27001, du fait de sa structure exhaustive).
2. Maintenir une **table de correspondance (crosswalk)** entre ce catalogue interne et les exigences de chaque référentiel externe demandé (SOC 2 TSC, articles du RGPD, sous-catégories NIST CSF).
3. Ne produire les preuves et rapports spécifiques à chaque référentiel qu'au moment de l'audit, à partir de ce même socle de contrôles.

C'est cette approche de mapping — plutôt que la duplication — qui permet à une organisation de passer, par exemple, d'ISO 27001 seul à ISO 27001 + SOC 2 Type II + conformité RGPD, sans tripler l'effort opérationnel. C'est aussi l'un des rôles structurants d'une plateforme GRC : représenter les référentiels comme des données (lignes de catalogue), et les contrôles internes comme les objets réels qu'on mappe vers chacun d'eux — plutôt que de coder en dur la logique d'un seul référentiel.
