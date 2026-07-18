# La protection des données sensibles en détail : PAN, SAD et tokenisation

## Pourquoi le PAN reste la donnée pivot de tout le référentiel

Rappel du module 0 : sans **numéro de compte principal (PAN)**, aucune autre donnée ne relève des exigences PCI DSS relatives aux données de titulaires de carte — le nom du titulaire ou la date d'expiration, isolés du PAN, ne constituent pas des données de carte au sens du référentiel. Cette centralité du PAN structure l'ensemble des techniques de protection développées dans cette leçon : la stratégie la plus efficace de réduction de risque consiste souvent à **éliminer purement et simplement le PAN** des systèmes qui n'en ont pas un besoin strict, plutôt que de le protéger partout où il apparaît.

## Les techniques de protection du PAN au repos (exigence 3)

### Le chiffrement fort

Le PAN stocké doit être protégé par un chiffrement robuste, avec une gestion documentée du cycle de vie des clés cryptographiques (génération, distribution, stockage, rotation, révocation) — un sujet qui recoupe directement le contrôle 8.24 de l'Annexe A d'ISO 27001 et le contrôle SC-13 de SP 800-53, déjà développés dans les parcours précédents de cette plateforme.

### La troncature

La troncature consiste à ne conserver qu'une partie du PAN (typiquement les six premiers et les quatre derniers chiffres au maximum, jamais l'intégralité), rendant les chiffres manquants irrécupérables — une technique simple mais efficace pour des cas d'usage qui n'ont besoin que d'identifier partiellement une carte (affichage sur un reçu, par exemple), sans jamais avoir besoin du PAN complet.

### La tokenisation

La tokenisation remplace le PAN par un **jeton (token)** sans valeur exploitable en dehors du système qui a réalisé la substitution, avec une table de correspondance sécurisée conservée séparément (souvent chez un prestataire de tokenisation spécialisé). Un système qui ne manipule que des jetons, sans jamais avoir accès à la table de correspondance permettant de retrouver le PAN réel, peut dans certains cas être considéré comme substantiellement hors du périmètre PCI DSS pour les données ainsi tokenisées — une stratégie de réduction de périmètre directement liée au scoping déjà développé au module 2 de ce parcours, et qui rappelle, dans son principe, la pseudonymisation déjà développée dans le module Privacy by Design du premier parcours de cette plateforme : une donnée qui n'est plus directement exploitable sans une information complémentaire protégée séparément.

### Le hachage

Le hachage à sens unique (avec un algorithme robuste et, idéalement, un sel cryptographique) permet de conserver une empreinte du PAN utilisable pour des besoins de correspondance ou de déduplication, sans jamais permettre de retrouver le PAN d'origine à partir de l'empreinte seule.

## Le chiffrement point à point (P2PE)

Une solution de **chiffrement point à point (Point-to-Point Encryption — P2PE)** validée par le PCI SSC chiffre le PAN dès sa capture physique (au niveau du terminal de paiement lui-même) jusqu'à son déchiffrement chez le prestataire de solution P2PE, sans qu'aucun système intermédiaire du commerçant ne puisse jamais accéder au PAN en clair. Une solution P2PE validée permet généralement au commerçant d'utiliser le questionnaire d'auto-évaluation le plus léger de cette catégorie (SAQ P2PE, déjà mentionné au module 3), en contrepartie d'une réduction substantielle et vérifiée de son exposition réelle au risque.

## L'interdiction absolue de conservation des données d'authentification sensibles (SAD)

Contrairement au PAN, qui peut être conservé sous réserve d'une protection appropriée, les **données d'authentification sensibles (SAD)** — données de piste complète, codes de vérification CAV2/CVC2/CVV2/CID, codes PIN — ne doivent **jamais être stockées après autorisation de la transaction**, même sous forme chiffrée. Cette règle, plus stricte que celle applicable au PAN, s'explique par la nature même de ces données : elles ne servent qu'à authentifier une transaction ponctuelle, et leur conservation ne présente aucune valeur légitime pour l'entité au-delà du moment de l'autorisation — seulement un risque disproportionné en cas de compromission, puisque leur possession suffirait à autoriser une nouvelle transaction frauduleuse sans autre vérification.

Une organisation qui découvrirait, lors d'un audit ou d'une évaluation PCI DSS, qu'elle conserve par erreur des données SAD après autorisation (souvent le résultat d'un journal applicatif mal configuré qui capture par inadvertance l'intégralité d'une requête de paiement, code de vérification inclus) se trouve face à une non-conformité particulièrement grave, quelle que soit par ailleurs la qualité du reste de son dispositif de sécurité — un point de vigilance technique très concret que ce parcours recommande de vérifier en priorité lors de toute revue de conformité PCI DSS.

## Comment ces techniques s'articulent avec le scoping du module 2

La tokenisation et le chiffrement point à point ne sont pas seulement des mesures de protection de la donnée — ce sont, dans les faits, des **stratégies de réduction du périmètre CDE** aussi puissantes que la segmentation réseau développée au module 2 : un système qui ne manipule jamais le PAN en clair, ni la table de correspondance permettant de le retrouver, présente un profil de risque suffisamment réduit pour justifier, dans de nombreux cas, son exclusion partielle ou totale du périmètre d'évaluation complet — une confirmation supplémentaire que, dans PCI DSS comme dans les autres référentiels déjà étudiés dans cette plateforme, la meilleure façon de réduire l'effort de conformité reste souvent de réduire, en amont, l'exposition réelle au risque plutôt que d'empiler des contrôles sur un périmètre qui reste inutilement large.
