# Atelier 1 (2/2) : le socle de sécurité

## Un principe d'efficacité : ne pas tout traiter par le scénario

Une fois les valeurs métier, biens supports et événements redoutés identifiés (leçon précédente), EBIOS RM introduit un principe d'efficacité qui structure toute la suite de la méthode : certains risques sont suffisamment **courants et bien connus** pour être traités par un socle de mesures standard, sans qu'il soit nécessaire de construire un scénario d'attaque sophistiqué pour les justifier — seuls les risques les plus spécifiques et les plus ciblés méritent l'effort d'analyse fine des Ateliers 2 à 4 développés dans les modules suivants de ce parcours.

## Le socle de sécurité : une base de mesures d'hygiène

Le **socle de sécurité** est cet ensemble de mesures de sécurité de référence, applicables indépendamment de tout scénario de risque spécifique — un socle généralement construit à partir de référentiels reconnus : le **Guide d'hygiène informatique de l'ANSSI** (42 recommandations de sécurité de base, développé plus loin dans cette leçon), les contrôles de l'Annexe A d'ISO 27001, ou les Safeguards de l'Implementation Group 1 des CIS Controls, tous deux déjà développés dans les parcours précédents de cette plateforme.

Cette logique de socle rappelle directement, dans son principe, l'**hygiène cyber essentielle** de l'Implementation Group 1 des CIS Controls déjà développée dans le parcours dédié de cette plateforme : un ensemble de mesures fondamentales, non négociables, qui doivent être appliquées par toute organisation avant même de commencer à raisonner sur des scénarios de risque plus sophistiqués et ciblés.

## Le Guide d'hygiène informatique de l'ANSSI

L'ANSSI publie et maintient un **Guide d'hygiène informatique**, qui recense 42 recommandations organisées en règles de base pour sécuriser un système d'information — sensibilisation des utilisateurs, gestion des comptes et des privilèges, sécurisation des postes, du réseau, de l'administration, et supervision. Ce guide constitue, en France, l'équivalent fonctionnel le plus direct de l'Implementation Group 1 des CIS Controls déjà développé dans le parcours dédié de cette plateforme — un socle minimal accessible à toute organisation, y compris celles ne disposant pas d'une expertise cybersécurité approfondie, avant d'envisager une démarche EBIOS RM complète.

## L'écart entre l'existant et le socle : la première source de risques identifiés

L'Atelier 1 se conclut par une évaluation de l'écart entre les mesures de sécurité effectivement en place dans l'organisation et le socle de sécurité de référence retenu — cet écart constitue en lui-même une première catégorie de risques à traiter, indépendamment des scénarios plus élaborés des ateliers suivants. Une organisation qui découvre, à ce stade, des écarts substantiels par rapport à un socle d'hygiène de base devrait généralement prioriser leur comblement avant d'investir massivement dans l'analyse de scénarios sophistiqués visant des sources de risque avancées — un principe de priorisation qui rappelle directement celui déjà développé pour les Implementation Groups des CIS Controls : les fondations d'abord, la sophistication ensuite.

## Comment cette architecture à deux niveaux structure l'ensemble d'EBIOS RM

Cette distinction entre socle de sécurité (traité une fois, de façon relativement statique) et scénarios de risque (développés de façon dynamique et itérative dans les Ateliers 2 à 4) est ce qui permet à EBIOS RM de rester praticable dans un temps raisonnable : plutôt que de construire un scénario d'attaque détaillé pour chaque risque imaginable — un exercice qui deviendrait rapidement disproportionné —, la méthode concentre l'effort d'analyse fine sur les risques qui échappent au socle standard, typiquement ceux portés par des sources de risque suffisamment motivées et capables pour chercher activement à contourner les mesures de base — les sources de risque développées au module 2 de ce parcours.

## Un exemple concret de cette répartition

Le risque qu'un poste de travail soit compromis par un logiciel malveillant générique diffusé massivement (une attaque opportuniste, non ciblée) relève typiquement du socle de sécurité — une protection anti-malware à jour et une politique de correctifs suffisent à le traiter sans nécessiter un scénario dédié. À l'inverse, le risque qu'un acteur étatique motivé cherche spécifiquement à compromettre le système d'information d'un opérateur d'importance vitale pour accéder à des informations stratégiques précises relève d'un scénario, car ce risque suppose de comprendre les motivations et les capacités propres de cette source de risque particulière, développées en détail dans le module suivant de ce parcours.
