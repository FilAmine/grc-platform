# Atelier 3 : scénarios stratégiques et cartographie de l'écosystème

## L'écosystème comme vecteur d'attaque, plutôt qu'un simple point de conformité contractuelle

Le sujet de la gestion des risques liés aux fournisseurs et prestataires a déjà été développé à travers de nombreux référentiels de cette plateforme — mais le plus souvent sous l'angle de la **conformité contractuelle** (les clauses minimales exigées par l'article 28 du RGPD, l'article 15 de PCI DSS, ou les contrôles 5.19-5.23 d'ISO 27001, tous développés dans les parcours dédiés). L'Atelier 3 d'EBIOS RM adopte un angle sensiblement différent et complémentaire : il traite l'écosystème comme un **vecteur d'attaque à cartographier explicitement**, en modélisant graphiquement comment une source de risque pourrait passer par un prestataire, un partenaire ou un fournisseur pour atteindre finalement les valeurs métier de l'organisation cible — plutôt que d'attaquer directement et frontalement l'organisation elle-même, souvent mieux défendue que ses partenaires les plus vulnérables.

## Construire un scénario stratégique

Pour chaque couple source de risque / objectif visé priorisé à l'Atelier 2 (module précédent), l'étude construit un **scénario stratégique** — une description narrative et graphique du chemin d'attaque de haut niveau que cette source de risque emprunterait vraisemblablement pour atteindre son objectif, en identifiant les **parties prenantes intermédiaires** de l'écosystème qui pourraient constituer une étape de ce chemin : un sous-traitant informatique disposant d'un accès privilégié au système d'information de la cible, un fournisseur de logiciel largement déployé chez la cible, ou un partenaire commercial avec lequel des échanges de données réguliers ont lieu.

## La cartographie de l'écosystème

Cette démarche suppose une **cartographie précise de l'écosystème** de l'organisation, bien plus détaillée que la simple esquisse amorcée à l'Atelier 1 (module 1 de ce parcours) : chaque partie prenante est caractérisée selon sa **dépendance** vis-à-vis de l'organisation étudiée (à quel point l'organisation dépend-elle de cette partie prenante), sa **pénétration** (quel niveau d'accès cette partie prenante a-t-elle au système d'information de l'organisation), sa **maturité en cybersécurité** (dans quelle mesure cette partie prenante applique-t-elle elle-même des pratiques de sécurité robustes), et sa **confiance** (existe-t-il des raisons de penser que cette partie prenante pourrait être elle-même ciblée ou déjà compromise).

Une partie prenante à la fois **fortement pénétrante** (un accès technique étendu au système d'information de la cible) et à la **maturité de sécurité faible** constitue le maillon le plus préoccupant de l'écosystème — exactement le profil qu'un attaquant sophistiqué rechercherait pour contourner les défenses, généralement plus robustes, de l'organisation cible elle-même.

## Un exemple concret de scénario stratégique

Reprenons l'exemple du module précédent : pour le couple "cybercriminel organisé / extorsion par rançongiciel", un scénario stratégique plausible pourrait emprunter le chemin suivant : compromission initiale d'un prestataire de maintenance informatique disposant d'un accès à distance permanent au système d'information de l'organisation cible (une partie prenante à forte pénétration), utilisation de cet accès légitime mais compromis pour progresser latéralement jusqu'aux systèmes critiques hébergeant les valeurs métier identifiées à l'Atelier 1, puis déploiement du rançongiciel. Ce scénario, construit à un niveau encore stratégique (sans détailler les techniques précises employées à chaque étape — un niveau de détail réservé à l'Atelier 4, développé dans le module suivant de ce parcours), identifie déjà clairement le prestataire de maintenance comme un maillon critique de l'écosystème à sécuriser en priorité.

## Les mesures de sécurité sur l'écosystème

L'Atelier 3 débouche sur l'identification de **mesures de sécurité spécifiquement destinées à réduire le risque porté par l'écosystème** — par exemple, renforcer les exigences contractuelles de sécurité imposées au prestataire de maintenance identifié dans l'exemple précédent, limiter techniquement l'étendue de son accès à distance au strict nécessaire (l'application directe du principe de moindre privilège déjà développé dans le premier parcours de cette plateforme), ou exiger une preuve de conformité à un référentiel de sécurité reconnu comme condition de maintien de la relation contractuelle.

## Le lien avec les autres approches de la gestion des risques fournisseurs déjà étudiées

Cette approche par cartographie graphique de l'écosystème et modélisation explicite des chemins d'attaque via des parties prenantes intermédiaires constitue un apport méthodologique distinctif d'EBIOS RM, qui complète utilement les approches plus contractuelles et documentaires déjà développées dans cette plateforme — la catégorie GV.SC du NIST CSF, les contrôles 5.19-5.23 d'ISO 27001, la famille SR de SP 800-53, ou le chapitre V de DORA structurent la **gouvernance** de la relation avec les tiers ; EBIOS RM apporte, en complément, une méthode concrète pour **prioriser lesquels de ces tiers méritent l'attention la plus soutenue**, en fonction de leur position réelle dans les chemins d'attaque plausibles contre l'organisation plutôt que d'un traitement uniforme de l'ensemble du portefeuille de fournisseurs.

## Le lien avec l'atelier suivant

Les scénarios stratégiques construits dans cet atelier restent délibérément formulés à un niveau de détail encore élevé — leur traduction en modes opératoires techniques précis, avec une évaluation de leur vraisemblance réelle, fait l'objet de l'Atelier 4, développé dans le module suivant de ce parcours.
