# Les tests de pénétration fondés sur la menace (TLPT)

## L'héritage direct de TIBER-EU

Les **tests de pénétration fondés sur la menace (Threat-Led Penetration Testing — TLPT)** exigés par DORA reprennent directement la méthodologie du cadre **TIBER-EU**, développé par la Banque centrale européenne avant même l'adoption de DORA, et déjà utilisé sur une base volontaire par plusieurs banques centrales et autorités de supervision nationales en Europe. DORA transforme ce cadre volontaire en obligation réglementaire pour les entités financières identifiées comme les plus systémiques — l'un des exemples les plus concrets, dans l'ensemble des référentiels étudiés dans cette plateforme, d'un cadre né comme bonne pratique volontaire finissant par être élevé au rang d'obligation légale directe.

## Qui est soumis au TLPT

Contrairement au programme de tests de base (leçon précédente), applicable à toutes les entités financières selon un principe de proportionnalité, le TLPT ne s'applique qu'aux entités identifiées par les autorités compétentes comme présentant un profil suffisamment systémique — en tenant compte notamment de l'impact potentiel des perturbations liées aux TIC sur le secteur financier, de la stabilité financière, et de leur profil de risque spécifique. Les micro, petites et moyennes entreprises au sens du droit de l'Union sont explicitement exclues de cette obligation, cohérent avec le principe de proportionnalité déjà rencontré au module 0 de ce parcours.

## La méthodologie du TLPT

Un TLPT reproduit les tactiques, techniques et procédures d'acteurs de la menace réels et pertinents pour l'entité testée, en s'appuyant sur des **renseignements sur la menace (threat intelligence)** spécifiquement collectés pour construire des scénarios d'attaque réalistes — plutôt qu'un test d'intrusion générique appliquant une méthodologie standardisée sans lien avec le profil de menace réel de l'organisation. Cette approche recoupe directement la threat intelligence déjà rencontrée à travers de multiples référentiels de cette plateforme (contrôle 5.7 d'ISO 27001, contrôle RA-10 de SP 800-53), mais l'applique ici spécifiquement à la construction d'un scénario de test offensif plutôt qu'à une simple veille défensive.

## Les acteurs impliqués

Un TLPT implique une structure d'acteurs bien plus formalisée qu'un test d'intrusion classique :

- une **équipe de renseignement sur la menace (threat intelligence provider)**, chargée de produire un rapport de renseignement sur la menace ciblant spécifiquement l'entité testée,
- une **équipe de test (red team)**, chargée de mener l'attaque simulée en s'appuyant sur ce renseignement,
- une **équipe de contrôle interne (white team)**, restreinte à quelques personnes de l'entité testée informées du test en cours, chargée de superviser son bon déroulement sans en informer le reste de l'organisation — afin de préserver le réalisme du test en testant également la capacité de détection et de réponse des équipes non informées,
- l'**autorité compétente**, qui valide le périmètre du test et en supervise le déroulement.

## Le recours à des testeurs externes

Contrairement au programme de tests de base qui autorise des testeurs internes sous condition d'indépendance (leçon précédente), le TLPT impose en principe le recours à des **testeurs externes**, accrédités ou reconnus par l'autorité compétente, pour l'équipe de test elle-même — une exigence d'indépendance renforcée, cohérente avec la nature particulièrement sensible et sophistiquée de ce type de test. Un recours à des testeurs internes reste possible sous des conditions strictes définies par les normes techniques de réglementation, notamment pour certains éléments du test, mais reste l'exception plutôt que la règle.

## La fréquence et la portée du test

Un TLPT doit être réalisé **au moins tous les trois ans**, sur le périmètre des fonctions critiques ou importantes de l'entité, en conditions réelles de production plutôt que sur un environnement de test isolé — une exigence qui rapproche le TLPT d'un exercice de simulation de crise réel plutôt que d'un audit technique isolé.

## Ce qui distingue le TLPT des tests d'intrusion déjà rencontrés dans cette plateforme

Le contrôle 18 des CIS Controls et le contrôle 8.34 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme, exigent des tests d'intrusion réguliers, mais sans imposer la même structure méthodologique formalisée (threat intelligence dédiée, équipes red/white distinctes, validation par une autorité compétente) ni la même fréquence minimale précisément fixée. Le TLPT représente, parmi l'ensemble des référentiels étudiés dans cette plateforme, le régime de test offensif le plus rigoureusement encadré et le plus directement rattaché à une obligation légale — une conséquence directe de l'enjeu de stabilité financière systémique que DORA cherche à protéger, bien au-delà de la seule sécurité de l'information d'une organisation individuelle.

## Le lien avec la reconnaissance mutuelle transfrontalière

DORA prévoit un mécanisme de **reconnaissance mutuelle** des TLPT réalisés à l'échelle transfrontière : une entité financière opérant dans plusieurs États membres peut, sous certaines conditions, faire reconnaître un TLPT réalisé sous la supervision d'une autorité compétente par les autorités des autres États membres où elle opère, évitant ainsi la duplication de tests coûteux et complexes pour chaque juridiction — un principe d'efficacité qui rappelle, dans son intention, le principe de réciprocité des autorisations déjà rencontré dans le parcours NIST RMF de cette plateforme.
