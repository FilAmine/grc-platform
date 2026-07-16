# Le CSF face aux autres référentiels, et l'approfondissement de la chaîne d'approvisionnement

## Pourquoi ne pas choisir entre CSF et les autres référentiels

Comme évoqué dès la première leçon de ce parcours, le CSF est explicitement conçu pour se **mapper** vers ISO 27001, SOC 2, NIST SP 800-53 ou COBIT, plutôt que pour les concurrencer. En pratique, trois usages combinés sont les plus fréquents :

- **CSF comme langage stratégique**, utilisé en comité de direction pour communiquer la posture globale (via les Tiers) et les priorités (via les Profils), pendant qu'**ISO 27001 ou SOC 2** structurent la mise en œuvre certifiable/auditable en détail.
- **CSF comme grille d'auto-évaluation initiale**, plus légère à mettre en place qu'un audit ISO 27001 complet, pour une organisation qui veut d'abord évaluer sa maturité avant de s'engager dans une démarche de certification plus lourde.
- **CSF comme couche de consolidation** pour une organisation déjà certifiée ISO 27001 et/ou disposant d'un rapport SOC 2, afin de présenter une vision de maturité cohérente à des interlocuteurs (investisseurs, conseil d'administration) qui ne sont pas familiers du détail technique de ces certifications.

## Une comparaison synthétique

| Aspect | CSF 2.0 | ISO 27001 | SOC 2 |
|---|---|---|---|
| Nature | Cadre volontaire, non certifiable | Norme certifiable (SMSI) | Rapport d'audit (attestation) |
| Niveau de détail | Résultats de haut niveau | Système de management + catalogue de contrôles (Annexe A) | Contrôles définis par l'organisation, évalués contre des critères (TSC) |
| Usage typique | Communication stratégique, auto-évaluation, priorisation | Preuve formelle à un client international, appel d'offres | Preuve contractuelle, marché B2B nord-américain |
| Structuration du risque | Tiers (rigueur) + Profils (résultats priorisés) | Appréciation des risques + Déclaration d'Applicabilité | Contrôles définis librement par l'organisation |

## Le sujet le plus approfondi par CSF 2.0 : la gestion des risques de la chaîne d'approvisionnement (C-SCRM)

La catégorie **GV.SC**, vue au module 1 de ce parcours, mérite un développement plus concret tant elle a gagné en importance dans cette version du cadre. La gestion des risques de la chaîne d'approvisionnement cybersécurité couvre :

### L'évaluation des fournisseurs avant contractualisation

Avant de signer avec un fournisseur cloud, un éditeur logiciel ou un prestataire ayant accès aux systèmes de l'organisation, une évaluation de sa posture de sécurité est menée — via un questionnaire de sécurité, la revue de ses certifications existantes (ISO 27001, SOC 2 du fournisseur lui-même), ou une évaluation plus approfondie pour les fournisseurs jugés critiques.

### Les exigences contractuelles de sécurité

Les contrats avec les fournisseurs critiques intègrent des clauses de sécurité explicites : obligations de notification en cas d'incident affectant les données de l'organisation cliente, droit d'audit, exigences de chiffrement, engagements de niveau de service liés à la sécurité.

### La gestion du risque des composants logiciels tiers

Un sujet devenu central avec la multiplication des dépendances open source : la capacité à identifier quels composants tiers sont utilisés dans les logiciels de l'organisation (via un **SBOM — Software Bill of Materials**, une nomenclature logicielle), à suivre les vulnérabilités connues affectant ces composants, et à disposer d'un processus de mise à jour rapide en cas de vulnérabilité critique découverte dans une dépendance largement utilisée.

### La planification de la réponse en cas de compromission d'un tiers

Un plan de réponse à incident (RS.MA, vu au module 1) devrait explicitement couvrir le scénario où l'incident trouve son origine chez un fournisseur ou prestataire, avec des procédures de communication et de containment adaptées à ce cas — différentes d'un incident purement interne, notamment parce que l'organisation ne maîtrise pas directement les systèmes compromis.

## Pourquoi ce sujet a été élevé au rang de fonction Govern plutôt que laissé en contrôle technique

Le déplacement du C-SCRM vers Govern en 2.0 (il était auparavant une sous-catégorie d'Identify) reflète un changement de posture : la gestion des risques fournisseurs n'est plus traitée comme un contrôle opérationnel isolé (vérifier un questionnaire de sécurité une fois par an) mais comme une décision stratégique récurrente, engageant la responsabilité de la direction — cohérent avec la multiplication des incidents majeurs récents dont l'origine se trouve non pas dans les systèmes internes de la victime, mais dans un maillon de sa chaîne d'approvisionnement logicielle ou de services.
