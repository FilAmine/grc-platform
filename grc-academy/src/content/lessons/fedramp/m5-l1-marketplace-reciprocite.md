# Le FedRAMP Marketplace et le principe de réciprocité

## Un catalogue public des autorisations accordées

Le **FedRAMP Marketplace**, une plateforme publique maintenue par le FedRAMP PMO, recense l'ensemble des CSP autorisés (ou en cours de processus d'autorisation), avec pour chacun le niveau d'impact obtenu (module 1 de ce parcours), la voie d'autorisation empruntée (module 2), l'agence sponsor le cas échéant, et le statut courant de l'autorisation. Ce marketplace joue un rôle directement comparable, dans son principe de transparence publique, à celui des registres publics de certifications ISO 27001 tenus par certains organismes d'accréditation nationaux, ou à la liste publique des entités certifiées PCI DSS de niveau 1 — une transparence qui permet à toute agence fédérale d'identifier rapidement les CSP déjà autorisés répondant à son besoin, sans devoir engager sa propre recherche de fournisseur qualifié.

## Comment le Marketplace concrétise le principe de réciprocité

Le principe de réciprocité déjà évoqué au module 0 de ce parcours ("do once, use many times") trouve sa concrétisation opérationnelle précisément dans ce marketplace : une agence fédérale qui identifie, via le Marketplace, un CSP déjà autorisé par une autre agence (voie Agence) ou disposant d'une P-ATO du FedRAMP Board (voie FedRAMP Board) peut consulter le dossier de sécurité existant — SSP, SAR, POA&M, développés aux modules 2 et 4 de ce parcours — et prendre sa propre décision d'ATO avec un effort d'évaluation résiduel très réduit, généralement limité à la vérification que ses propres exigences spécifiques (souvent documentées dans un addendum propre à l'agence) sont satisfaites.

## Ce que la réciprocité ne dispense jamais de vérifier

Ce mécanisme de réutilisation ne dispense cependant jamais l'agence adoptante de sa propre responsabilité d'Authorizing Official : elle doit toujours examiner le dossier existant à la lumière de son propre contexte de risque, documenter sa propre décision d'ATO, et rester destinataire des livrables de surveillance continue mensuels développés au module 4 de ce parcours — un principe qui rejoint directement celui déjà développé pour les contrôles complémentaires attendus de l'entité utilisatrice (CUEC) dans le cadre des rapports SOC 1, où le client d'un prestataire reste toujours responsable de vérifier sa propre part du dispositif de contrôle, quand bien même il s'appuie sur l'évaluation d'un tiers.

## L'accroissement continu de la vitesse d'adoption

Le FedRAMP PMO a progressivement enrichi le Marketplace et les processus associés d'outils facilitant davantage encore la réutilisation — notamment des modèles de dossiers standardisés et des indicateurs de maturité de la documentation — dans le cadre d'une préoccupation constante du programme : réduire le délai moyen d'obtention d'une autorisation FedRAMP, historiquement critiqué par les fournisseurs cloud comme un frein commercial significatif comparé au rythme d'adoption du cloud dans le secteur privé. Cette préoccupation de réduction des délais rappelle celle déjà rencontrée pour les initiatives de simplification des référentiels dans plusieurs parcours de cette plateforme, notamment l'introduction de l'approche personnalisée dans PCI DSS v4.0.

## Le marché secondaire de la revente de services déjà autorisés

Un CSP autorisé FedRAMP dont le service cloud constitue une brique technique pour d'autres fournisseurs (par exemple, un fournisseur d'infrastructure IaaS autorisé, sur lequel s'appuient de nombreux éditeurs SaaS) permet à ces éditeurs de construire leur propre demande d'autorisation en s'appuyant partiellement sur l'autorisation déjà obtenue par leur fournisseur d'infrastructure sous-jacent, plutôt que de démontrer eux-mêmes la sécurité de l'ensemble de la pile technique de bout en bout — un mécanisme de mutualisation en cascade qui rappelle directement celui déjà développé pour les rapports SOC 1 des sous-traitants de sous-traitants, ou pour l'héritage de contrôles entre différents niveaux d'un environnement cloud partagé.

## Ce que confirme, une fois de plus, le succès du principe de réciprocité

Le Marketplace et le mécanisme de réciprocité qu'il concrétise confirment un principe déjà dégagé à plusieurs reprises dans cette plateforme : la mutualisation d'un audit ou d'une évaluation coûteuse entre de multiples parties prenantes, plutôt que sa répétition intégrale par chacune d'entre elles, constitue l'un des leviers les plus efficaces pour concilier un niveau d'exigence élevé avec un coût de mise en conformité soutenable à grande échelle — un principe que le module suivant de ce parcours permet d'examiner sous l'angle des programmes apparentés qui s'en inspirent directement.
