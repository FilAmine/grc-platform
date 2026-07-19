# Le Core (3/3) : Protect-P, le pont explicite vers le NIST CSF

## Une fonction délibérément construite comme un pont

La fonction **Protect-P** occupe une place singulière au sein du Core du NIST Privacy Framework : contrairement à Govern-P, Identify-P, Control-P et Communicate-P, dont les catégories et sous-catégories ont été spécifiquement rédigées pour le Privacy Framework, les sous-catégories de Protect-P sont **directement empruntées à la fonction Protect du NIST CSF**, déjà développée en détail dans le parcours dédié de cette plateforme. Ce choix délibéré illustre la philosophie fondatrice du Privacy Framework, déjà évoquée au module 0 de ce parcours : les deux cadres sont conçus pour être utilisés **ensemble** par une même organisation, et Protect-P constitue le point de jonction méthodologique explicite entre les deux.

## Pourquoi cette fonction recoupe directement la sécurité de l'information

Cette conception rejoint directement la reconnaissance, déjà faite au module 1 de ce parcours, que le risque vie privée et le risque de sécurité, bien que conceptuellement distincts, se recoupent largement sur un point précis : la protection des données personnelles contre un accès non autorisé, une altération ou une perte relève très directement des mêmes mesures de sauvegarde techniques déjà développées dans le NIST CSF — le contrôle d'accès, la protection des données au repos et en transit, la gestion des vulnérabilités, la sécurité des plateformes et des processus. Protect-P ne réinvente ainsi jamais ces contrôles, mais les intègre tels quels au sein du Core du Privacy Framework pour couvrir cette zone de recoupement.

## Ce que cette conception révèle sur la relation entre les deux cadres

Cette architecture révèle une répartition claire des responsabilités entre les deux cadres, utile pour toute organisation qui les déploie conjointement : le NIST CSF porte l'intégralité de la protection technique contre les menaces de sécurité (via ses six fonctions Govern, Identify, Protect, Detect, Respond, Recover), tandis que le NIST Privacy Framework ajoute les dimensions que la sécurité seule ne couvre jamais — la gouvernance spécifique à la vie privée (Govern-P), la compréhension des flux de données personnelles (Identify-P), la capacité d'action sur ces données (Control-P) et la transparence envers les personnes concernées (Communicate-P) — Protect-P servant de raccord entre les deux, plutôt que de duplication redondante des mêmes contrôles techniques.

## Un exemple concret d'articulation

Une organisation qui a déjà déployé le NIST CSF pour l'ensemble de son système d'information dispose ainsi directement, à travers la fonction Protect déjà implémentée, de l'essentiel des sous-catégories nécessaires pour satisfaire Protect-P au sein du Privacy Framework — sans effort supplémentaire de duplication. Ce qu'elle doit ajouter pour compléter sa démarche de gestion du risque vie privée réside précisément dans les quatre autres fonctions du Privacy Framework (Govern-P, Identify-P, Control-P, Communicate-P), qui couvrent des dimensions que le CSF, centré sur la sécurité, ne développe jamais.

## Pourquoi cette architecture évite une duplication coûteuse

Cette conception illustre, une fois de plus, le principe de mapping plutôt que de duplication déjà rencontré à de multiples reprises dans cette plateforme — plutôt que d'obliger une organisation à maintenir deux catalogues de contrôles techniques entièrement distincts et potentiellement incohérents entre eux (l'un pour la sécurité, l'autre pour la vie privée), le NIST a délibérément conçu ses deux cadres pour partager la même fonction Protect, réservant l'effort réellement nouveau aux dimensions authentiquement spécifiques à la vie privée.

## Un tableau de synthèse des cinq fonctions du Core

| Fonction | Spécificité par rapport au CSF |
|---|---|
| Govern-P | Propre au Privacy Framework, orientée gouvernance de la vie privée |
| Identify-P | Propre au Privacy Framework, orientée cartographie des données personnelles |
| Control-P | Propre au Privacy Framework, orientée capacité d'action sur les données |
| Communicate-P | Propre au Privacy Framework, orientée transparence envers les personnes concernées |
| Protect-P | Directement empruntée à la fonction Protect du CSF, sans duplication |

## Le lien avec le module suivant

Une fois le Core pleinement compris à travers ses cinq fonctions, l'organisation peut l'utiliser pour construire ses propres Profils, décrivant l'état actuel et l'état cible de sa gestion du risque vie privée — un mécanisme développé au module suivant de ce parcours.
