# Les six bases légales de traitement, et les catégories de données particulières

## Pourquoi la base légale est la première question à se poser, pas la dernière

Une erreur fréquente consiste à concevoir un traitement de données, puis à chercher après coup une base légale qui le justifierait — alors que le RGPD exige l'inverse : **aucun traitement de données personnelles n'est licite sans qu'une base légale précise de l'article 6 ne s'applique dès sa conception**, un principe qui rejoint directement le "Proactif, non réactif" du premier des sept principes de Privacy by Design développés dans le premier parcours de cette plateforme.

## Les six bases légales de l'article 6

### Le consentement (article 6.1.a)

La personne concernée a consenti au traitement de ses données à caractère personnel pour une ou plusieurs finalités spécifiques. L'article 4.11 précise que le consentement doit être **libre, spécifique, éclairé et univoque**, manifesté par une déclaration ou un acte positif clair — ce qui exclut catégoriquement les cases pré-cochées, l'inaction, ou un consentement obtenu par des interfaces trompeuses (dark patterns). Le consentement doit également pouvoir être **retiré aussi facilement qu'il a été donné** (article 7.3) — une exigence technique directe qui a des conséquences concrètes sur la conception des interfaces de gestion des préférences.

### L'exécution d'un contrat (article 6.1.b)

Le traitement est nécessaire à l'exécution d'un contrat auquel la personne concernée est partie, ou à l'exécution de mesures précontractuelles prises à sa demande. Le mot **nécessaire** est déterminant : un traitement "utile" ou "pratique" pour la relation contractuelle, mais non strictement nécessaire à son exécution, ne peut pas s'appuyer sur cette base — il lui faut une autre base légale, souvent le consentement ou l'intérêt légitime.

### L'obligation légale (article 6.1.c)

Le traitement est nécessaire au respect d'une obligation légale à laquelle le responsable du traitement est soumis — par exemple, la conservation de documents comptables pendant une durée fixée par le droit national, ou la transmission de données à une autorité fiscale.

### La sauvegarde des intérêts vitaux (article 6.1.d)

Le traitement est nécessaire à la sauvegarde des intérêts vitaux de la personne concernée ou d'une autre personne physique — une base légale d'usage très restreint en pratique, typiquement invoquée dans des situations d'urgence médicale où la personne est dans l'incapacité de donner son consentement.

### La mission d'intérêt public (article 6.1.e)

Le traitement est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement — la base légale typique des administrations publiques et de leurs missions de service public.

### L'intérêt légitime (article 6.1.f)

Le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée. C'est la base légale la plus complexe à manier correctement, car elle exige un **test de mise en balance (balancing test)** documenté, en trois temps largement retenu par la doctrine et les autorités de contrôle :

1. **Test de finalité** — l'intérêt poursuivi est-il légitime, réel et suffisamment précis ?
2. **Test de nécessité** — le traitement envisagé est-il réellement nécessaire pour atteindre cette finalité, et n'existe-t-il pas de moyen moins intrusif d'y parvenir ?
3. **Test de mise en balance** — les intérêts du responsable du traitement l'emportent-ils sur les intérêts, droits et libertés fondamentaux de la personne concernée, compte tenu notamment de ses attentes raisonnables dans le contexte considéré ?

Cette base légale ne peut jamais être invoquée par les autorités publiques dans l'exercice de leurs missions (l'article 6.1.f l'exclut explicitement) — elle reste l'apanage des acteurs privés, sous réserve de documenter sérieusement ce test de mise en balance plutôt que de l'invoquer par défaut faute d'alternative plus simple.

## Le principe de non-hiérarchie, et son exception pratique

Le règlement ne hiérarchise pas ces six bases entre elles — aucune n'est "supérieure" ou "à privilégier par défaut". En pratique cependant, le consentement, souvent perçu comme la base légale la plus intuitive, est aussi la plus contraignante à maintenir dans la durée (retrait possible à tout moment, preuve du consentement à conserver) — ce qui conduit de nombreuses organisations à privilégier, lorsque c'est juridiquement possible, l'exécution du contrat ou l'intérêt légitime pour des traitements strictement nécessaires à leur activité, et à réserver le consentement aux traitements réellement optionnels (marketing direct par exemple, où le consentement reste d'ailleurs souvent imposé par des textes sectoriels complémentaires comme la directive ePrivacy pour les cookies).

## Les catégories de données particulières (article 9) et les données pénales (article 10)

### Article 9 — Catégories particulières de données

Le traitement de données révélant l'origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques, l'appartenance syndicale, de données génétiques, de données biométriques aux fins d'identifier une personne physique de manière unique, de données concernant la santé ou la vie sexuelle ou l'orientation sexuelle d'une personne physique est **interdit par principe**, sauf exception limitativement énumérée : consentement explicite (un standard plus élevé que le simple consentement de l'article 6), nécessité pour des motifs d'intérêt public important, nécessité aux fins de la médecine préventive ou du diagnostic médical, ou encore nécessité aux fins archivistiques, de recherche scientifique ou historique.

### Article 10 — Données relatives aux condamnations pénales et infractions

Le traitement de données relatives aux condamnations pénales et aux infractions ne peut être effectué que sous le contrôle de l'autorité publique, ou lorsqu'il est autorisé par le droit de l'Union ou par le droit d'un État membre prévoyant des garanties appropriées — un régime distinct des catégories particulières de l'article 9, mais tout aussi restrictif dans son principe.

## Le lien avec la Déclaration d'Applicabilité et la matrice de contrôles

Documenter précisément, pour chaque traitement, la base légale retenue (et le test de mise en balance le cas échéant pour l'intérêt légitime) constitue l'un des éléments centraux du registre des traitements exigé par l'article 30, développé en détail au module 4 — un exercice de documentation qui rejoint, dans sa logique, la Déclaration d'Applicabilité d'ISO 27001 ou la matrice de contrôles SOC 2 déjà rencontrées dans les parcours précédents de cette plateforme : la preuve d'une décision structurée et documentée, pas seulement la conformité de fait.
