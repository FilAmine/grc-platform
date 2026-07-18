# La catégorisation par niveaux d'impact (2/2) : bases de référence et adaptations cloud

## Ce que FedRAMP ajoute concrètement à SP 800-53

Le catalogue SP 800-53, déjà développé en détail dans le parcours NIST RMF de cette plateforme, constitue le socle de chacune des bases de référence de contrôles FedRAMP — mais FedRAMP ne se contente pas de reprendre telles quelles les bases de référence génériques du RMF : il les enrichit de **paramètres spécifiques au cloud** (des valeurs précises pour les contrôles laissés paramétrables par SP 800-53, par exemple la fréquence exacte d'une revue d'accès ou la durée de conservation d'un journal) et de **contrôles supplémentaires propres au contexte cloud**, absents des bases de référence génériques du RMF, portant notamment sur la séparation logique entre locataires (tenant isolation) dans les environnements multi-clients, la portabilité et la récupération des données en cas de changement de fournisseur, et la transparence sur la localisation géographique des données hébergées.

## Le contrôle de la localisation des données et de la chaîne d'approvisionnement

FedRAMP impose des exigences renforcées sur la localisation des données traitées et stockées — les données d'une agence fédérale doivent, sauf exception documentée, demeurer sur le territoire des États-Unis, y compris pour les sauvegardes et les environnements de reprise après sinistre. Cette exigence de souveraineté des données rappelle, par son principe bien que dans un contexte réglementaire différent, les exigences de localisation ou de restriction des transferts internationaux déjà développées dans le parcours RGPD de cette plateforme — une préoccupation de souveraineté qui traverse, sous des formes variées, plusieurs référentiels déjà étudiés. FedRAMP exige également une transparence complète sur la chaîne d'approvisionnement du CSP, notamment l'identification de tout sous-traitant impliqué dans l'hébergement ou le traitement des données, un principe qui rejoint directement la gestion des risques de la chaîne d'approvisionnement déjà développée dans la famille SR du RMF.

## Les Significant Change Requests comme mécanisme de maintien de la base de référence

Une fois l'autorisation obtenue, toute modification substantielle de l'architecture, des composants techniques ou du périmètre du service cloud autorisé doit être notifiée à l'agence sponsor ou au FedRAMP Board via une **Significant Change Request (SCR)**, avant sa mise en œuvre — un mécanisme développé plus en détail au module 4 de ce parcours, qui garantit que la base de référence de contrôles validée lors de l'autorisation initiale continue de refléter fidèlement l'environnement technique réellement exploité, plutôt que de devenir progressivement obsolète au fil des évolutions du service.

## Comment cette structure de bases de référence se compare à la logique des Trust Services Criteria

Le parcours SOC 2 de cette plateforme a développé les cinq catégories de Trust Services Criteria (Sécurité, Disponibilité, Intégrité de traitement, Confidentialité, Vie privée), que chaque organisation sélectionne et adapte librement à son contexte. FedRAMP suit une logique sensiblement différente et beaucoup plus prescriptive : il n'existe pas de sélection libre de catégories, mais un choix binaire du niveau d'impact (Faible, Modéré, Élevé, ou Tailored) qui détermine intégralement et de façon non négociable la liste exacte des contrôles applicables — une rigueur qui rappelle davantage celle du catalogue de contrôles PCI DSS, où les douze exigences s'appliquent uniformément dès lors que le périmètre des données de cartes de paiement est concerné, déjà développé dans le parcours dédié de cette plateforme.

## Un tableau de synthèse des trois bases de référence

| Aspect | Faible | Modéré | Élevé |
|---|---|---|---|
| Volume de contrôles (ordre de grandeur) | Le plus faible des trois | Le plus fréquemment visé par les CSP | Le plus volumineux et le plus exigeant |
| Exemples de données typiques | Informations publiques ou à faible sensibilité | Données administratives et métiers courantes | Application de la loi, santé publique, systèmes financiers critiques |
| Exigences de chiffrement et de journalisation | Standards | Renforcées | Les plus strictes du programme |
| Fréquence typique de visée par les CSP commerciaux | Rare | Très fréquente | Réservée aux marchés les plus sensibles |

## Le lien avec le choix de la voie d'autorisation

Le niveau d'impact visé influence directement le choix de la voie d'autorisation développée à la leçon suivante : historiquement, le FedRAMP Board (anciennement le Joint Authorization Board) concentrait ses ressources d'évaluation sur les CSP visant le niveau Modéré à forte demande potentielle inter-agences, tandis que la voie Agence restait ouverte à l'ensemble des niveaux d'impact, y compris le niveau Élevé pour des besoins plus spécifiques à une agence sponsor déterminée.
