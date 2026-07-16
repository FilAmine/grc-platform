# Catégories, sous-catégories et références informatives : lire le Core

## La structure hiérarchique du Core

Le Core du CSF s'organise en trois niveaux :

1. **Fonction** (6 au total : Govern, Identify, Protect, Detect, Respond, Recover) — le niveau le plus abstrait, celui qu'on présente à un comité de direction.
2. **Catégorie** (ex. "Asset Management" au sein d'Identify) — un regroupement thématique de résultats liés.
3. **Sous-catégorie** — le résultat concret et vérifiable (ex. "les inventaires de matériels et logiciels sont maintenus").

## Lire un identifiant de sous-catégorie

Chaque sous-catégorie porte un code structuré, par exemple **GV.SC-01** :

- **GV** — la fonction (Govern).
- **SC** — la catégorie (Supply Chain Risk Management).
- **01** — le numéro de la sous-catégorie au sein de cette catégorie.

Ce code sert de langage commun : dans un audit, une revue de direction ou un document de mapping, on peut référencer précisément "GV.SC-01" sans ambiguïté, plutôt que de paraphraser un résultat en langage libre à chaque fois — un bénéfice similaire à celui des identifiants de contrôle de l'Annexe A d'ISO 27001.

## Les références informatives : le pont vers les autres référentiels

Chaque sous-catégorie du CSF est accompagnée, dans la documentation officielle et les outils associés (comme le CSF Reference Tool du NIST), de **références informatives** — des pointeurs vers des contrôles équivalents dans d'autres référentiels reconnus :

- **NIST SP 800-53** — le catalogue de contrôles fédéral américain, très détaillé, souvent la référence la plus prescriptive associée à chaque sous-catégorie.
- **ISO/IEC 27001 Annexe A** — pour les organisations qui maintiennent en parallèle une certification ISO.
- **COBIT** — pour la gouvernance IT au sens large.
- **CIS Controls** — pour une déclinaison plus opérationnelle et priorisée.

Ces références ne sont **pas exhaustives ni figées** — le NIST les met à jour, et des organisations tierces (dont la CSA, vue dans le premier parcours de cette plateforme) publient leurs propres tables de correspondance, parfois plus détaillées pour un secteur ou une technologie donnés (le mapping CSF ↔ CSA CCM pour le cloud, par exemple).

## Pourquoi cette structure évite la duplication d'effort

C'est cette architecture à trois niveaux, combinée aux références informatives, qui permet à une organisation de construire **un seul dispositif de contrôles internes**, puis de le déclarer conforme (ou de mesurer son alignement) simultanément vis-à-vis du CSF, d'ISO 27001 et d'autres référentiels — sans construire un programme séparé pour chacun. C'est exactement la logique de "mapping plutôt que duplication" déjà rencontrée dans le parcours GRC & Security by Design de cette plateforme, appliquée ici spécifiquement à la structure du CSF.

## Un exemple de lecture croisée

Prenons la sous-catégorie **PR.AA-05** ("l'accès est géré en cohérence avec le principe de moindre privilège et la séparation des tâches"). Une organisation qui a déjà implémenté le contrôle **5.15 (Contrôle d'accès)** et **8.2 (Droits d'accès privilégiés)** de l'Annexe A d'ISO 27001 peut, via les références informatives, documenter directement que PR.AA-05 est satisfaite par ces contrôles existants — sans réinventer une preuve ou un contrôle distinct spécifiquement "pour le CSF".

## Une nuance importante : le Core n'est pas exhaustif par construction

Le CSF assume explicitement de **ne pas viser l'exhaustivité** des contrôles possibles — il vise la couverture des résultats de haut niveau les plus universellement pertinents. Une organisation dans un secteur très réglementé (santé, finance) devra presque toujours compléter le Core avec des exigences sectorielles plus spécifiques (HDS, DORA, PCI DSS) que le CSF ne couvre pas en détail — le Core reste le socle commun, pas le plafond de ce qui est attendu.
