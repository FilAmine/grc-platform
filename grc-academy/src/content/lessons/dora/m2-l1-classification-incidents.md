# La classification des incidents liés aux TIC

## Une classification à critères multiples, plutôt qu'un seuil unique

Le parcours NIS2 de cette plateforme a développé la notion d'incident significatif, définie par deux critères relativement généraux (perturbation opérationnelle grave, ou dommages considérables pour des tiers). DORA va plus loin en imposant une méthodologie de classification structurée autour de **critères précis et cumulables**, que chaque entité financière doit appliquer pour déterminer si un incident lié aux TIC doit être qualifié de **majeur**.

## Les critères de classification

Les normes techniques de réglementation associées à DORA précisent des critères matériels, parmi lesquels :

- le **nombre et/ou la pertinence des clients ou contreparties financières touchés** par l'incident, notamment lorsqu'ils relèvent d'un seuil quantitatif ou qualitatif défini,
- la **durée de l'incident**, en particulier lorsqu'elle dépasse une durée de service maximale tolérable définie par l'entité elle-même,
- l'**étendue géographique** de l'incident, notamment s'il affecte plusieurs États membres,
- les **pertes de données** occasionnées, en termes de disponibilité, d'authenticité, d'intégrité ou de confidentialité,
- la **criticité des services affectés**, notamment s'ils soutiennent des fonctions critiques ou importantes de l'entité,
- l'**impact économique** de l'incident, notamment les coûts et pertes directs et indirects,
- l'**impact de réputation**, apprécié par exemple à travers la couverture médiatique de l'incident ou les plaintes de clients.

Cette approche multicritère, plus détaillée que celle de NIS2, reflète la nature du secteur financier : un incident affectant un nombre limité de clients peut néanmoins être classé comme majeur s'il touche une fonction critique dont la défaillance aurait un effet systémique — une préoccupation de stabilité financière qui dépasse la seule logique de continuité opérationnelle déjà rencontrée dans les référentiels de sécurité génériques étudiés dans cette plateforme.

## Les incidents de cybermenace importante

Au-delà des incidents déjà matérialisés, DORA introduit également la notion de **cybermenace importante** — une circonstance dont la probabilité de matérialisation présente un niveau de risque élevé, susceptible d'affecter les réseaux et systèmes d'information de l'entité financière. Une entité financière peut, sur une base volontaire, **notifier** une cybermenace importante à l'autorité compétente, même en l'absence d'incident avéré — un mécanisme proactif qui recoupe l'esprit de la threat intelligence déjà rencontrée à travers de multiples référentiels de cette plateforme (contrôle 5.7 d'ISO 27001, catégorie ID.RA du NIST CSF, contrôle RA-10 de SP 800-53).

## Pourquoi cette classification précède toute décision de notification

Cette classification n'est pas un exercice académique — elle conditionne directement le déclenchement du processus de notification développé dans la leçon suivante : seul un incident qualifié de **majeur** selon ces critères déclenche l'obligation de notification aux autorités compétentes. Une entité financière doit donc disposer, en amont, d'une procédure documentée et exercée pour appliquer rapidement cette grille de critères dès la détection d'un incident potentiel — un exercice de préparation directement comparable à celui déjà recommandé pour la qualification d'un incident significatif sous NIS2, développée dans le parcours dédié de cette plateforme, mais avec une grille de critères sensiblement plus détaillée et quantifiée à appliquer sous la pression du temps.

## Le rôle de l'harmonisation par les normes techniques de réglementation

Un point de méthode important : les critères précis de classification (seuils quantitatifs exacts, définitions opérationnelles) ne figurent pas dans le texte du règlement DORA lui-même, mais dans des **normes techniques de réglementation (Regulatory Technical Standards — RTS)**, élaborées par les autorités européennes de surveillance (l'Autorité bancaire européenne, l'Autorité européenne des marchés financiers, et l'Autorité européenne des assurances et des pensions professionnelles, collectivement désignées les "AES") et adoptées par la Commission européenne. Ce mécanisme à deux niveaux — un règlement de niveau 1 fixant les principes, des normes techniques de niveau 2 précisant les seuils et modalités — est une caractéristique structurante de la réglementation financière européenne, distincte de la structure plus directement autoportante d'ISO 27001 ou du NIST CSF déjà étudiés dans cette plateforme, où le texte de référence contient directement l'ensemble du niveau de détail nécessaire.

## Ce que cette classification implique pour la préparation d'une entité financière

Une entité financière qui prend DORA au sérieux ne se contente pas de documenter la grille de critères — elle l'intègre directement dans son processus opérationnel de gestion des incidents, avec des seuils quantitatifs pré-calculés et documentés pour chaque fonction critique, permettant une classification rapide dès la détection d'un événement suspect, plutôt qu'une analyse construite dans l'urgence — un exercice de préparation développé plus en détail dans la feuille de route du module 6 de ce parcours.
