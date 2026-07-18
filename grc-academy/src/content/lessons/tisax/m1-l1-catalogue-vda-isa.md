# Le catalogue VDA ISA et les niveaux de maturité (1/2) : structure du catalogue

## Un catalogue construit sur le socle d'ISO 27001, mais pas une simple redite

Le catalogue **VDA Information Security Assessment (VDA ISA)** structure ses critères de sécurité de l'information en groupes de contrôles très largement alignés sur les thèmes de l'Annexe A d'ISO/IEC 27001 déjà développée dans le parcours dédié de cette plateforme (organisation de la sécurité, gestion des accès, cryptographie, sécurité physique, sécurité des opérations, gestion des incidents, continuité d'activité, conformité) — une organisation qui permet à une entreprise déjà certifiée ISO 27001 de réutiliser une part significative de sa documentation existante plutôt que de repartir d'une feuille blanche, selon le même principe de mapping plutôt que de duplication déjà rencontré à de multiples reprises dans cette plateforme.

## Les modules spécifiques qui distinguent VDA ISA d'un catalogue de sécurité généraliste

Au-delà de ce socle commun avec ISO 27001, le catalogue VDA ISA ajoute des groupes de contrôles propres au contexte automobile, notamment sur la sécurité applicable au **développement de logiciels embarqués** (une préoccupation directement liée à la cybersécurité automobile et aux normes ISO/SAE 21434, non couvertes par les référentiels de sécurité de l'information généralistes déjà étudiés dans cette plateforme), ainsi que les modules dédiés à la protection des prototypes et à la protection des données personnelles déjà évoqués au module 0 de ce parcours, et développés respectivement aux modules 5 et 2 de ce parcours.

## La structure en contrôles et sous-critères évaluables

Chaque groupe de contrôles du catalogue VDA ISA se décompose en critères précis, chacun assorti d'une échelle d'évaluation de maturité (développée à la leçon suivante) plutôt que d'une simple case à cocher "conforme / non conforme" — une approche qui rejoint directement celle déjà rencontrée pour le modèle de niveaux de capacité de COBIT, aligné sur CMMI, dans le parcours dédié de cette plateforme : il ne s'agit pas seulement de vérifier qu'un contrôle existe, mais d'apprécier le degré de formalisation, de mise en œuvre effective et d'amélioration continue de ce contrôle.

## Une mise à jour régulière du catalogue

Le VDA publie des versions successives du catalogue ISA (les versions récentes intègrent, par exemple, des critères renforcés sur la sécurité du cloud et la gestion des risques de la chaîne d'approvisionnement logicielle), une évolution périodique qui rappelle celle déjà rencontrée pour les révisions successives d'ISO 27001 (2013 puis 2022) ou de PCI DSS (jusqu'à la version 4.0), déjà développées dans les parcours dédiés de cette plateforme — un fournisseur automobile doit ainsi suivre l'évolution du catalogue applicable à chaque nouvelle évaluation, plutôt que de considérer sa conformité comme acquise une fois pour toutes sur la base d'une version figée.

## Pourquoi ce catalogue reste propre à l'industrie automobile plutôt que largement générique

Contrairement à ISO 27001 ou au NIST CSF, conçus pour s'appliquer à tout secteur d'activité, le catalogue VDA ISA demeure fondamentalement un outil sectoriel, élaboré par et pour l'industrie automobile — un choix de conception qui permet d'intégrer des préoccupations très spécifiques à ce secteur (la confidentialité des prototypes non dévoilés, la sécurité des chaînes de production automatisées, la protection de la propriété intellectuelle liée au design des véhicules) qu'un référentiel généraliste n'aurait pas vocation à couvrir de façon aussi détaillée — une logique de spécialisation sectorielle qui rappelle, dans son principe, celle déjà rencontrée pour PCI DSS et son origine contractuelle propre aux marques de cartes de paiement, développée dans le parcours dédié de cette plateforme.

## Le lien avec le modèle de maturité, développé à la leçon suivante

La structure du catalogue en groupes de contrôles ne suffit cependant pas, à elle seule, à comprendre comment une évaluation TISAX aboutit à un résultat global exploitable par un OEM — c'est le modèle de niveaux de maturité, développé à la leçon suivante de ce parcours, qui permet de transformer l'évaluation détaillée de chaque critère en une appréciation synthétique et comparable d'un fournisseur à l'autre.
