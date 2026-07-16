# Le modèle de responsabilité partagée dans le cloud

## Le malentendu le plus coûteux du cloud

L'incident de sécurité cloud le plus fréquent n'est pas une faille dans l'infrastructure du fournisseur — c'est une **mauvaise configuration côté client** : un bucket de stockage public par erreur, une base de données exposée sans mot de passe, un rôle IAM trop permissif. La cause profonde est presque toujours la même : une mauvaise compréhension de qui est responsable de quoi.

Le **modèle de responsabilité partagée** (Shared Responsibility Model), formalisé par tous les grands fournisseurs (AWS, Azure, GCP), répond précisément à cette question. Le principe général : **le fournisseur est responsable de la sécurité *du* cloud, le client est responsable de la sécurité *dans* le cloud.**

## Comment la frontière se déplace selon le modèle de service

La répartition exacte dépend du modèle de service utilisé :

### IaaS (Infrastructure as a Service — ex. VM, stockage brut)

- **Fournisseur** : sécurité physique des datacenters, infrastructure réseau globale, hyperviseur.
- **Client** : système d'exploitation (patchs, durcissement), configuration réseau (groupes de sécurité, pare-feu), gestion des identités et des accès, chiffrement des données, application et son code.

C'est le modèle où le client porte la responsabilité la plus large — presque tout au-dessus de la couche matérielle.

### PaaS (Platform as a Service — ex. bases de données managées, plateformes applicatives)

- **Fournisseur** : en plus de l'IaaS, le système d'exploitation sous-jacent, le moteur applicatif ou de base de données, les correctifs de la plateforme.
- **Client** : configuration de la plateforme (paramètres de sécurité, réseau d'accès), gestion des identités, chiffrement, et surtout **le code applicatif et les données qu'il traite**.

### SaaS (Software as a Service — ex. un logiciel complet utilisé via navigateur)

- **Fournisseur** : quasiment tout l'empilement technique.
- **Client** : configuration des paramètres de sécurité disponibles (SSO, politiques de mot de passe, permissions utilisateurs), et surtout **la gestion des données que l'organisation choisit d'y stocker et des accès qu'elle accorde**.

Même en SaaS, la responsabilité du client ne disparaît jamais complètement : mal configurer les permissions de partage d'un SaaS de documents reste une négligence du client, pas du fournisseur.

## Ce que "responsabilité partagée" ne veut PAS dire

Ce modèle ne dit pas que la sécurité est à moitié la responsabilité du fournisseur et à moitié celle du client de façon uniforme — c'est une frontière précise qui **se déplace** selon le modèle de service choisi, et qui doit être documentée précisément pour chaque service cloud utilisé (une organisation utilise typiquement un mélange d'IaaS, PaaS et SaaS simultanément, avec une frontière différente à chaque fois).

Une erreur fréquente en audit : une organisation invoque "c'est la responsabilité du fournisseur cloud" pour justifier l'absence d'un contrôle qui, en réalité, relève clairement de sa propre responsabilité selon le modèle de service utilisé (typiquement : la configuration IAM, qui est **toujours** de la responsabilité du client, quel que soit le modèle de service).

## Le lien avec la gestion des risques (module 1)

Le modèle de responsabilité partagée doit être **explicitement intégré au registre de risques**. Pour chaque service cloud utilisé, la cartographie des risques doit préciser : quelle part du risque est portée nativement par le fournisseur (et donc couverte par ses propres certifications — ISO 27001, SOC 2 du fournisseur lui-même, qu'on peut consulter), et quelle part reste un risque propre de l'organisation, nécessitant ses contrôles à elle.

C'est une erreur d'audit fréquente que de citer la certification ISO 27001 d'AWS ou Azure comme preuve de la conformité de sa **propre** organisation — cette certification couvre la sécurité *du* cloud (le fournisseur), pas automatiquement ce que l'organisation cliente construit et configure *dans* le cloud.

## Traduction opérationnelle : la checklist de frontière

Pour chaque service cloud adopté, une organisation rigoureuse en Security by Design documente au minimum :

1. Quel modèle de service (IaaS/PaaS/SaaS) et donc quelle frontière de responsabilité s'applique.
2. Quelles certifications/attestations le fournisseur publie pour sa part de responsabilité (rapport SOC 2 du fournisseur, certificat ISO 27001, etc.).
3. Quels contrôles précis restent à la charge de l'organisation (configuration IAM, chiffrement applicatif, gestion des secrets, surveillance applicative).
4. Qui, en interne, possède (au sens du module 1 — risk owner) chacun de ces contrôles côté client.

Cette checklist n'est pas une formalité théorique : elle conditionne directement les décisions techniques développées dans les deux leçons suivantes — IAM, chiffrement, segmentation réseau.
