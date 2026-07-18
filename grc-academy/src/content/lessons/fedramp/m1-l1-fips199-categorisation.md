# La catégorisation par niveaux d'impact (1/2) : FIPS 199 appliqué au cloud

## Un point de départ déjà familier : la catégorisation FIPS 199

Le parcours NIST RMF de cette plateforme a déjà développé en détail la catégorisation FIPS 199, première étape (Categorize) du processus RMF : chaque système est évalué selon l'impact potentiel d'une atteinte à sa confidentialité, son intégrité et sa disponibilité, sur une échelle **Faible / Modéré / Élevé**, le niveau global du système retenant le plus élevé des trois impacts évalués séparément (le principe du "high-water mark" déjà développé dans ce parcours). FedRAMP reprend directement cette même logique de catégorisation, sans en modifier les fondements méthodologiques, mais en l'appliquant spécifiquement au contexte des services cloud destinés aux agences fédérales.

## Trois niveaux d'impact, trois bases de référence de contrôles

FedRAMP décline cette catégorisation en trois bases de référence de contrôles spécifiquement adaptées au cloud, chacune bâtie sur le catalogue SP 800-53 déjà développé dans le parcours NIST RMF de cette plateforme, mais enrichie de paramètres et de contrôles supplémentaires propres au contexte cloud :

- **Le niveau Faible (Low)** — destiné aux services cloud traitant des informations dont la perte de confidentialité, d'intégrité ou de disponibilité aurait un impact limité sur les opérations, les actifs ou les individus d'une agence — une base de référence relativement légère, comparable en volume à la base de référence Faible de SP 800-53 elle-même.
- **Le niveau Modéré (Moderate)** — de très loin le niveau le plus fréquemment visé par les fournisseurs cloud, car il couvre la grande majorité des systèmes d'information administratifs et métiers des agences fédérales qui ne traitent pas de données extrêmement sensibles — une base de référence substantiellement enrichie par rapport au niveau Faible.
- **Le niveau Élevé (High)** — réservé aux services cloud traitant les données les plus sensibles : informations relatives à l'application de la loi, à la santé publique d'urgence, aux systèmes financiers critiques, ou à d'autres missions dont une atteinte grave à la confidentialité, l'intégrité ou la disponibilité pourrait avoir un effet catastrophique sur les opérations d'une agence — la base de référence la plus volumineuse et la plus exigeante parmi les trois niveaux, avec des exigences renforcées notamment sur le chiffrement, la journalisation et la gestion des identités.

## Un quatrième palier allégé pour les cas d'usage limités : FedRAMP Tailored (LI-SaaS)

FedRAMP propose également une base de référence allégée, dite **FedRAMP Tailored** ou **Low-Impact Software-as-a-Service (LI-SaaS)**, destinée aux services SaaS de faible complexité technique ne traitant pas de données personnellement identifiables sensibles ni de données financières — par exemple, un outil collaboratif simple ou un service de gestion de projet. Cette base allégée illustre un principe de proportionnalité déjà rencontré à plusieurs reprises dans cette plateforme, notamment pour le régime simplifié de DORA applicable aux petites entités financières, ou pour les niveaux de validation PCI DSS gradués selon le volume de transactions traité — l'objectif étant d'éviter d'imposer à un service à faible enjeu le même volume de contrôles qu'à un système critique.

## Pourquoi la catégorisation initiale conditionne tout le reste du parcours d'autorisation

Comme pour la catégorisation FIPS 199 dans le RMF, le choix du niveau d'impact FedRAMP au tout début du processus détermine directement le volume de contrôles à implémenter, le nombre de preuves à produire pour le 3PAO (développé au module 3 de ce parcours), et la charge de la surveillance continue ultérieure (module 4) — un fournisseur cloud qui viserait, par excès de prudence ou par erreur d'appréciation commerciale, un niveau d'impact supérieur à celui réellement requis par son marché cible s'imposerait ainsi un effort de mise en conformité disproportionné, tandis qu'un niveau sous-évalué exposerait l'agence cliente à un dispositif de contrôle insuffisant au regard de la sensibilité réelle des données traitées.

## Qui décide du niveau d'impact visé

Contrairement à la catégorisation FIPS 199 du RMF, qui résulte d'un travail conjoint entre le System Owner et l'Authorizing Official d'une agence pour un système donné, le niveau d'impact FedRAMP visé par un CSP est le plus souvent une **décision commerciale préalable** du fournisseur lui-même, guidée par les besoins de son marché cible (une agence civile aux besoins courants visera généralement le niveau Modéré ; un fournisseur souhaitant servir des missions de sécurité nationale ou de santé publique visera le niveau Élevé) — une décision qui doit néanmoins être validée et confirmée par l'agence sponsor ou le FedRAMP Board lors du lancement effectif du processus d'autorisation, développé au module 2 de ce parcours.
