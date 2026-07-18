# HIPAA en profondeur : introduction et repères

## Une loi fédérale américaine née d'un objectif bien différent de son usage actuel

**HIPAA** (Health Insurance Portability and Accountability Act) a été adoptée en 1996 par le Congrès américain — mais son intitulé complet révèle un objectif initial très éloigné de ce pour quoi elle est aujourd'hui la plus connue : garantir la **portabilité** de la couverture d'assurance maladie des travailleurs américains changeant d'emploi, et la **simplification administrative** des transactions électroniques de santé (normalisation des formats d'échange entre professionnels de santé, assureurs et administrations). Les volets consacrés à la **confidentialité** et à la **sécurité** des données de santé, aujourd'hui au cœur de ce que "HIPAA" évoque dans le langage courant, n'ont été développés que dans un second temps, par voie réglementaire du Department of Health and Human Services (HHS) : la **Privacy Rule** (règle de confidentialité, effective en 2003) et la **Security Rule** (règle de sécurité, effective en 2005).

## Les évolutions majeures : HITECH et l'Omnibus Rule

- **Le HITECH Act (2009)** — Health Information Technology for Economic and Clinical Health Act, adopté dans le cadre d'un plan de relance économique plus large, a considérablement renforcé le dispositif HIPAA : introduction d'une obligation de **notification des violations** (développée au module 4 de ce parcours), extension de la **responsabilité directe** aux prestataires de services (Business Associates, développés au module 3) — auparavant seulement liés par contrat sans responsabilité directe devant le régulateur —, et incitation financière à l'adoption des dossiers médicaux électroniques.
- **L'Omnibus Rule (2013)** — a mis en œuvre concrètement les modifications introduites par HITECH, finalisé le régime de responsabilité directe des Business Associates, révisé le seuil de déclenchement de la notification de violation (passant d'un critère de "dommage" à une évaluation de risque en quatre facteurs, développée au module 4), et renforcé plusieurs droits des personnes.

## L'autorité de contrôle : l'Office for Civil Rights

Contrairement au RGPD ou à NIS2 (chacun supervisé par des autorités nationales ou sectorielles multiples, déjà développées dans les parcours dédiés de cette plateforme), HIPAA est appliqué par une **autorité fédérale unique** : l'**Office for Civil Rights (OCR)**, une division du Department of Health and Human Services, qui reçoit les plaintes, conduit des enquêtes et des audits, et prononce les sanctions développées au module 5 de ce parcours. Les procureurs généraux de chaque État américain (State Attorneys General) disposent également, depuis HITECH, d'un pouvoir d'action en justice pour les violations affectant les résidents de leur État — une architecture de supervision à deux niveaux qui rappelle, dans son principe, le mécanisme de guichet unique combiné à des autorités nationales déjà rencontré pour le RGPD dans le parcours dédié de cette plateforme.

## Les entités couvertes : Covered Entities et Business Associates

HIPAA distingue deux catégories d'acteurs soumis à ses obligations :

- les **Covered Entities (entités couvertes)** — les régimes d'assurance santé (health plans), les chambres de compensation de soins de santé (healthcare clearinghouses), et les prestataires de soins de santé qui transmettent des informations de santé par voie électronique dans le cadre de certaines transactions normalisées (facturation, remboursement),
- les **Business Associates (prestataires associés)** — toute personne ou entité qui exerce une fonction ou un service pour le compte d'une entité couverte impliquant l'utilisation ou la divulgation d'informations de santé protégées : un hébergeur cloud, un prestataire de facturation, un consultant en sécurité informatique, un éditeur de logiciel de dossier médical.

Cette distinction rappelle directement celle déjà développée entre responsable de traitement et sous-traitant dans le parcours RGPD de cette plateforme — avec une différence structurante développée au module 3 : depuis HITECH, les Business Associates portent une **responsabilité directe** devant l'OCR pour le respect de la Security Rule et de certaines dispositions de la Privacy Rule, et pas seulement une obligation contractuelle envers l'entité couverte.

## Les informations de santé protégées : PHI et ePHI

HIPAA protège les **Protected Health Information (PHI)** — toute information de santé individuellement identifiable, détenue ou transmise par une entité couverte ou un Business Associate, sous quelque forme que ce soit (électronique, papier, orale). Le sous-ensemble des PHI sous forme électronique, les **ePHI**, fait l'objet d'un régime spécifique : c'est à elles seules que s'applique la Security Rule, développée en détail au module 2 de ce parcours — la Privacy Rule, elle, couvre l'ensemble des PHI quel que soit leur support.

## Un contraste structurant avec le RGPD déjà développé dans cette plateforme

HIPAA se distingue du RGPD, déjà développé en détail dans le parcours dédié de cette plateforme, par une portée sensiblement plus étroite : elle ne s'applique **qu'aux entités couvertes et à leurs Business Associates**, dans le seul secteur de la santé, sans la portée extraterritoriale universelle du RGPD (applicable à toute organisation traitant des données de résidents européens, quel que soit son secteur). Un hôpital américain qui transmettrait des données de santé à un chercheur ou à un employeur, en dehors du périmètre des entités couvertes et Business Associates, peut voir ces données échapper entièrement au champ d'application de HIPAA — une différence de portée qui aura des conséquences concrètes tout au long de ce parcours, notamment sur le régime de notification des violations (module 4) et sur la comparaison finale entre les deux textes (module 6).

## Ce que ce parcours couvre

Sept modules structurent ce parcours : la Privacy Rule et la gestion des divulgations autorisées (module 1), la Security Rule et ses trois catégories de sauvegardes (module 2), les Business Associates et leur contrat obligatoire (module 3), la règle de notification des violations (module 4), l'application du dispositif et le régime de sanctions (module 5), et enfin les méthodes de dé-identification des données ainsi que l'articulation de HIPAA avec les référentiels déjà étudiés dans cette plateforme et une feuille de route de mise en conformité (module 6).
