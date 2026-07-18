# La cascade des objectifs

## Traduire une intention stratégique large en objectifs IT concrets

La **cascade des objectifs (goals cascade)** est le mécanisme par lequel COBIT relie les besoins des parties prenantes de l'entreprise, à travers plusieurs niveaux successifs, jusqu'aux objectifs de gouvernance et de management précis développés au module 2 — un mécanisme qui répond à une question déjà posée sous des formes différentes dans plusieurs parcours de cette plateforme : comment s'assurer qu'un contrôle technique précis (un objectif de management COBIT, un contrôle SP 800-53, un Safeguard des CIS Controls) se rattache réellement à une intention stratégique de l'entreprise, plutôt que d'exister isolément sans justification claire.

## Les quatre niveaux de la cascade

### Niveau 1 — Les besoins des parties prenantes (Stakeholder Drivers and Needs)

Le point de départ : les attentes et les besoins des parties prenantes de l'entreprise (actionnaires, direction, clients, régulateurs, employés), influencés par des facteurs contextuels (l'environnement concurrentiel, les évolutions technologiques, le contexte réglementaire).

### Niveau 2 — Les objectifs d'entreprise (Enterprise Goals)

Ces besoins sont traduits en un ensemble d'**objectifs d'entreprise**, formulés selon plusieurs dimensions (financière, client, interne, apprentissage et croissance — une structure qui rappelle directement le tableau de bord prospectif, ou Balanced Scorecard, dont COBIT s'inspire explicitement) : par exemple, la conformité aux lois et réglementations externes, la gestion des risques métier, ou la qualité de l'information de gestion.

### Niveau 3 — Les objectifs d'alignement (Alignment Goals)

Ces objectifs d'entreprise sont ensuite traduits en **objectifs d'alignement**, spécifiques à la contribution de l'IT — par exemple, l'alignement de la stratégie IT avec la stratégie d'entreprise, la conformité de l'IT avec les lois et réglementations externes, ou la sécurité de l'information, du traitement et des infrastructures. C'est à ce niveau que la sécurité, sujet central des neuf autres parcours de cette plateforme, trouve sa place explicite dans la logique de COBIT — comme une contribution parmi d'autres à des objectifs d'entreprise plus larges, plutôt que comme une fin en soi déconnectée de la stratégie globale.

### Niveau 4 — Les objectifs de gouvernance et de management

Enfin, ces objectifs d'alignement se traduisent en objectifs de gouvernance et de management précis parmi les quarante du référentiel (développés au module 2) — le niveau le plus concret et le plus directement actionnable de la cascade.

## Pourquoi cette cascade fonctionne dans les deux sens

Comme la relation entre gouvernance et management développée dans la leçon précédente, la cascade des objectifs n'est pas un mécanisme à sens unique : elle sert autant à **descendre** (traduire une stratégie en objectifs concrets) qu'à **remonter** (justifier pourquoi un objectif de management précis existe, en le retraçant jusqu'aux besoins des parties prenantes qui le motivent). Une organisation qui ne peut pas expliquer, pour un objectif de management donné, à quel objectif d'entreprise il contribue in fine, dispose probablement d'un objectif mal priorisé ou superflu — un test de cohérence qui rappelle directement le principe de proportionnalité déjà rencontré dans les parcours NIS2 et DORA de cette plateforme.

## Un exemple concret de cascade complète

Prenons un exemple filé à travers les quatre niveaux : une entreprise cotée doit répondre aux attentes de ses actionnaires et régulateurs en matière de conformité réglementaire (niveau 1, besoins des parties prenantes). Cela se traduit en un objectif d'entreprise de "conformité aux lois et réglementations externes" (niveau 2). Cet objectif d'entreprise se décline en un objectif d'alignement IT de "conformité de l'IT avec les lois et réglementations externes" (niveau 3) — pertinent, par exemple, si l'entreprise est soumise à NIS2 ou DORA, déjà développés dans les parcours dédiés de cette plateforme. Cet objectif d'alignement se traduit enfin en objectifs de management concrets comme **MEA03 (gestion de la conformité aux exigences externes)** et **APO13 (gestion de la sécurité)**, développés au module 2 — le niveau où l'organisation met effectivement en œuvre des contrôles vérifiables.

## Le lien avec la logique de mapping déjà développée dans cette plateforme

Cette cascade recoupe, dans son principe, la logique de mapping entre référentiels déjà développée à de multiples reprises dans cette plateforme (entre ISO 27001, NIST CSF, SOC 2 et le NIST RMF, par exemple) : de la même façon qu'un contrôle interne peut être relié à plusieurs référentiels externes par une table de correspondance, un objectif COBIT peut être relié, à travers la cascade, à l'objectif d'entreprise qui le justifie — une même logique de traçabilité verticale entre le concret et le stratégique, appliquée ici non pas entre référentiels distincts, mais entre les niveaux internes d'un seul et même référentiel.
