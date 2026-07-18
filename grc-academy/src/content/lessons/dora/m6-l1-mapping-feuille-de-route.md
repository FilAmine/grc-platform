# DORA face aux autres référentiels, et feuille de route de mise en conformité

## DORA comme lex specialis face à NIS2

Le parcours NIS2 de cette plateforme a déjà mentionné ce principe : lorsqu'un acte juridique sectoriel de l'Union impose des exigences au moins équivalentes à celles de NIS2, ce texte sectoriel s'applique en tant que **lex specialis**, à la place des dispositions générales de NIS2. DORA est explicitement désigné comme un tel texte pour le secteur financier — une entité financière relevant à la fois du secteur bancaire ou d'un autre secteur de l'Annexe I de NIS2, et du périmètre des entités financières de DORA, applique donc principalement les exigences de DORA pour sa gestion des risques liés aux TIC, plutôt qu'un cumul intégral des deux textes. Ce principe de non-duplication réglementaire évite qu'une même banque ne se retrouve simultanément soumise à deux calendriers de notification d'incidents distincts (24h/72h/1 mois pour NIS2, un calendrier propre pour DORA développé au module 2 de ce parcours) pour un seul et même incident.

## DORA et le RGPD : deux textes qui peuvent se déclencher simultanément

Comme déjà signalé au module 2, un incident affectant à la fois la disponibilité d'un service financier et des données personnelles de clients peut déclencher deux notifications distinctes et non substituables l'une à l'autre : DORA protège la résilience opérationnelle et la stabilité financière, le RGPD protège les droits des personnes concernées — deux intérêts juridiques différents, qui restent séparés même lorsqu'un même incident technique en est à l'origine.

## Le cadre de gestion des risques liés aux TIC face aux référentiels techniques déjà étudiés

Comme déjà observé pour l'article 21 de NIS2 dans le parcours dédié de cette plateforme, DORA énonce des objectifs de haut niveau pour le cadre de gestion des risques liés aux TIC (module 1), sans prescrire de catalogue de contrôles technique détaillé — une entité financière s'appuie généralement sur un référentiel déjà étudié dans cette plateforme pour construire son dispositif de contrôles concret :

| Exigence de DORA | Référentiel de mise en œuvre déjà étudié |
|---|---|
| Cadre de gestion des risques liés aux TIC (module 1) | ISO 27001 (SMSI complet), NIST CSF (fonctions alignées) |
| Inventaire des actifs informationnels et TIC | Contrôle 1 des CIS Controls, contrôle 5.9 d'ISO 27001 |
| Continuité des activités et objectifs RTO/RPO | Contrôle 8.13 d'ISO 27001, famille CP de SP 800-53 |
| Programme de tests de base (module 3) | Contrôle 7 (vulnérabilités) et 18 (tests d'intrusion) des CIS Controls |
| Gestion des risques liés aux prestataires tiers (module 4) | Contrôles 5.19-5.23 d'ISO 27001, catégorie GV.SC du NIST CSF, famille SR de SP 800-53 |

Le TLPT (module 3) et le régime de supervision directe des prestataires critiques (module 4) restent, en revanche, des dispositifs propres à DORA, sans équivalent direct de mise en œuvre dans les référentiels techniques génériques déjà étudiés dans cette plateforme.

## Construire une feuille de route de conformité

### Priorité 1 — Déterminer précisément son statut et son niveau de proportionnalité

Vérifier si l'entité relève effectivement du périmètre des entités financières de DORA, et si elle peut bénéficier du régime simplifié prévu pour certaines catégories d'entités de taille modeste (module 0) — une qualification qui conditionne l'intensité des exigences applicables, notamment en matière de tests (module 3).

### Priorité 2 — Engager l'organe de direction dès le départ

Compte tenu de la responsabilité directe de l'organe de direction posée par l'article 5 (module 1), associer la direction dès la phase de cadrage du programme de conformité — un principe déjà recommandé pour NIS2 dans le parcours dédié de cette plateforme, tout aussi pertinent ici.

### Priorité 3 — Cartographier et renégocier les contrats avec les prestataires TIC critiques pour l'activité

Recenser l'ensemble des prestataires TIC dont dépendent les fonctions critiques ou importantes de l'entité, évaluer les risques de concentration (module 4), et engager, si nécessaire, une renégociation contractuelle pour intégrer les clauses minimales exigées par DORA — un chantier souvent long, en particulier avec de grands fournisseurs cloud dont les contrats standards ne prévoient pas nécessairement, par défaut, l'ensemble de ces clauses.

### Priorité 4 — Structurer la classification et la notification des incidents

Documenter et exercer, avant qu'un incident réel ne survienne, la grille de critères de classification des incidents majeurs et le processus de notification à trois paliers (module 2) — un exercice de préparation qui gagne à être coordonné avec la procédure de notification RGPD déjà existante, pour éviter une improvisation en cas d'incident affectant simultanément les deux dimensions.

### Priorité 5 — Dimensionner le programme de tests selon le profil de l'entité

Construire le programme de tests de base (module 3) proportionné au profil de risque de l'entité, et anticiper, pour les entités les plus systémiques, l'organisation d'un premier TLPT — un exercice qui suppose une coordination étroite avec l'autorité compétente et, généralement, le recours à des prestataires spécialisés externes accrédités.

## En clôture de ce parcours

Ce parcours a couvert DORA de bout en bout : le cadre de gestion des risques liés aux TIC et la responsabilité de l'organe de direction, la classification et la notification des incidents majeurs, le régime de tests de résilience opérationnelle numérique incluant les tests de pénétration fondés sur la menace, la gestion des risques liés aux prestataires tiers et l'innovation du régime de supervision directe des prestataires critiques, le partage d'informations et le régime de sanctions largement renvoyé au droit national, et enfin l'articulation de DORA avec les autres référentiels déjà étudiés dans cette plateforme. Combiné aux huit autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels et réglementations majeurs qui structurent une démarche GRC moderne, du cadre le plus générique et volontaire (NIST CSF) jusqu'au texte sectoriel le plus spécifique et le plus institutionnellement novateur (DORA).
