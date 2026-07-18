# HIPAA face aux autres référentiels, et feuille de route de mise en conformité

## HIPAA ne prescrit aucun référentiel technique, à l'image des autres textes légaux déjà étudiés

Comme le RGPD, NIS2, DORA et PCI DSS déjà développés dans les parcours précédents de cette plateforme, la Security Rule énonce des objectifs de sécurité sans prescrire de catalogue de contrôles technique détaillé — un principe de neutralité technologique explicitement affirmé dans le texte lui-même. En pratique, une entité couverte ou un Business Associate s'appuie généralement sur un référentiel technique déjà étudié dans cette plateforme pour construire un dispositif de contrôles concret et démontrable.

## Le guide NIST SP 800-66

Le NIST a publié un **guide de ressources introductif pour la mise en œuvre de la Security Rule (SP 800-66)**, qui propose une correspondance directe entre chaque norme et spécification de la Security Rule et les contrôles pertinents de **SP 800-53**, déjà développé en détail dans le parcours NIST RMF de cette plateforme. Une entité de santé déjà familière avec l'écosystème NIST — en particulier une entité liée d'une manière ou d'une autre à des programmes fédéraux américains — dispose ainsi d'un chemin de mise en œuvre technique déjà balisé, sans avoir à reconstruire un dispositif de contrôles entièrement distinct spécifiquement pour HIPAA.

## HITRUST CSF : un référentiel sectoriel dédié à l'harmonisation

Le secteur de la santé américain a développé son propre référentiel certifiable, le **HITRUST CSF (Common Security Framework)**, maintenu par une organisation à but non lucratif du même nom, spécifiquement conçu pour harmoniser les exigences de multiples référentiels pertinents pour la santé — HIPAA, mais aussi PCI DSS (pour les organismes de santé qui traitent des paiements par carte, développé dans le parcours dédié de cette plateforme), ISO 27001, NIST CSF, et diverses réglementations étatiques américaines. Une organisation de santé certifiée HITRUST CSF peut ainsi démontrer sa conformité à HIPAA et à plusieurs autres référentiels simultanément, via une seule évaluation structurée — un exemple concret et sectoriel de la stratégie de mapping plutôt que de duplication déjà développée à de multiples reprises dans cette plateforme, ici institutionnalisée sous la forme d'un référentiel certifiable dédié plutôt que d'une simple table de correspondance.

## Comparaison synthétique avec le RGPD

| Aspect | HIPAA | RGPD |
|---|---|---|
| Portée | Sectorielle (santé), entités couvertes et Business Associates uniquement | Universelle, tout secteur traitant des données de résidents européens |
| Base légale par défaut | Triptyque Treatment/Payment/Healthcare Operations | Six bases légales symétriques (article 6) |
| Délai de notification aux personnes | 60 jours | Pas de délai direct vers les personnes (72h vers l'autorité, "sans délai" vers les personnes si risque élevé) |
| Publicité de la violation | Obligatoire au-delà de 500 personnes (médias, registre public) | Non systématique |
| Rôle de conformité désigné | Security Official et Privacy Official (obligatoires) | Délégué à la Protection des Données (DPO, obligatoire sous conditions) |
| Sanction pénale intégrée au texte | Oui, pour violation intentionnelle | Non directement (relève du droit pénal national le cas échéant) |
| Autorité de contrôle | OCR (fédéral unique) + procureurs généraux des États | Autorités nationales + guichet unique |

Cette comparaison confirme, une dernière fois, un principe déjà établi à de multiples reprises dans cette plateforme : deux textes poursuivant un objectif de fond similaire (protéger des données personnelles sensibles) peuvent aboutir à des architectures juridiques sensiblement différentes selon le contexte institutionnel, sectoriel et culturel dans lequel ils ont été conçus.

## Construire une feuille de route de conformité

### Priorité 1 — Déterminer précisément son statut

Vérifier si l'organisation est une entité couverte, un Business Associate, ou aucun des deux — une qualification qui n'est pas toujours évidente pour des organisations à la frontière du secteur de la santé (une entreprise de bien-être numérique traitant des données de santé sans être un prestataire de soins, par exemple, peut se trouver hors du champ d'application de HIPAA malgré la sensibilité de ses données).

### Priorité 2 — Conduire une analyse de risque à l'échelle de l'ensemble de l'organisation

Compte tenu de la centralité de cette exigence dans les dossiers d'exécution de l'OCR (module 5), en faire la première priorité absolue plutôt qu'un exercice réalisé en fin de projet.

### Priorité 3 — Cartographier les Business Associates et sécuriser les BAA

Recenser l'ensemble des prestataires ayant accès à des PHI, et s'assurer qu'un Business Associate Agreement en bonne et due forme est en place avec chacun d'eux (module 3) — un chantier qui recoupe directement celui déjà développé pour les contrats de sous-traitance du RGPD et de DORA dans les parcours précédents de cette plateforme.

### Priorité 4 — Documenter rigoureusement les décisions sur les spécifications Addressable

Pour chaque spécification Addressable de la Security Rule (module 2), documenter explicitement le raisonnement d'évaluation, plutôt que de laisser cette décision implicite — un point de vigilance déjà développé en détail dans ce parcours, qui constitue l'un des pièges les plus fréquents pour les organisations découvrant HIPAA.

### Priorité 5 — Préparer la procédure de notification des violations

Structurer, avant qu'un incident réel ne survienne, le processus de qualification d'une violation selon les quatre facteurs de risque (module 4), et la chaîne de décision pour la notification aux personnes, au HHS et, le cas échéant, aux médias.

## En clôture de ce parcours

Ce parcours a couvert HIPAA de bout en bout : la Privacy Rule et le triptyque Treatment/Payment/Healthcare Operations, les droits des patients, la Security Rule et ses trois catégories de sauvegardes, le mécanisme de flexibilité Required/Addressable, les Business Associates et leur contrat obligatoire, la règle de notification des violations, le régime d'application et de sanctions de l'OCR, les méthodes de dé-identification des données de santé, et enfin l'articulation de HIPAA avec les référentiels déjà étudiés dans cette plateforme. Combiné aux onze autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels majeurs qui structurent une démarche GRC moderne, à travers les continents, les secteurs et les natures de textes — normes volontaires, rapports d'attestation, cadres de gouvernance globale, textes légaux européens et américains, et exigences contractuelles sectorielles.
