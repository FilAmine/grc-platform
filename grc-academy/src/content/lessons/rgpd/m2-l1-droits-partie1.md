# Les droits des personnes concernées (1/2) : information, accès, rectification, effacement, limitation

## Une mécanique procédurale précise, pas seulement une liste de principes

Le premier parcours de cette plateforme a déjà énuméré les droits des personnes concernées. Cette leçon va plus loin : elle détaille les délais, modalités et exceptions précises qui conditionnent la mise en œuvre réelle de chaque droit — la partie du RGPD la plus directement testée par les autorités de contrôle lors d'une réclamation individuelle.

## Le délai commun à la plupart des droits : un mois, extensible à trois

Sauf disposition contraire, le responsable du traitement doit répondre à une demande d'exercice de droit dans un délai d'**un mois** à compter de sa réception. Ce délai peut être prolongé de **deux mois supplémentaires** si nécessaire, compte tenu de la complexité et du nombre de demandes, à condition d'en informer la personne concernée **dans le délai initial d'un mois**, avec les motifs du report — un report tardif, notifié après l'expiration du premier mois, n'est pas valable. Si le responsable du traitement ne donne pas suite à la demande, il doit informer la personne concernée sans tarder, et au plus tard dans un délai d'un mois, des motifs de son inaction et de la possibilité d'introduire une réclamation auprès d'une autorité de contrôle.

## Droit à l'information (articles 13 et 14)

Le responsable du traitement doit fournir, au moment de la collecte des données (article 13, lorsque les données sont collectées directement auprès de la personne) ou dans un délai raisonnable (article 14, lorsque les données proviennent d'une autre source), un ensemble d'informations : son identité et ses coordonnées, celles du DPO le cas échéant, les finalités et la base légale du traitement, les destinataires des données, la durée de conservation, l'existence des droits, et le cas échéant l'existence d'un transfert international. Ces informations, généralement rassemblées dans une politique de confidentialité, ne sont pas qu'une formalité de transparence : elles constituent la matière première qui permet à la personne concernée de savoir qu'elle peut exercer les droits suivants, et sur quel fondement.

## Droit d'accès (article 15)

La personne concernée a le droit d'obtenir du responsable du traitement la confirmation que des données à caractère personnel la concernant sont ou ne sont pas traitées, et, le cas échéant, l'accès à ces données ainsi qu'un ensemble d'informations les concernant (finalités, catégories de données, destinataires, durée de conservation envisagée). Une **première copie** de ces données doit être fournie gratuitement ; le responsable du traitement peut exiger le paiement de frais raisonnables pour toute copie supplémentaire demandée. Une demande d'accès manifestement infondée ou excessive, notamment en cas de caractère répétitif, peut être facturée ou refusée — mais cette exception s'interprète strictement, et la charge de la preuve du caractère abusif repose sur le responsable du traitement.

## Droit de rectification (article 16)

La personne concernée a le droit d'obtenir la rectification des données à caractère personnel inexactes la concernant, ainsi que le droit d'obtenir que des données incomplètes soient complétées, y compris en fournissant une déclaration complémentaire. Ce droit est rarement contesté en pratique — sa mise en œuvre technique dépend surtout de la capacité du système d'information à propager la correction à l'ensemble des copies de la donnée (bases de production, entrepôts analytiques, sauvegardes), un sujet directement lié à la cartographie des flux de données développée dans le module Privacy by Design du premier parcours de cette plateforme.

## Droit à l'effacement, dit "droit à l'oubli" (article 17)

La personne concernée a le droit d'obtenir l'effacement de ses données dans plusieurs cas précis : les données ne sont plus nécessaires au regard des finalités pour lesquelles elles ont été collectées, la personne retire son consentement (et il n'existe pas d'autre base légale), la personne s'oppose au traitement (voir la leçon suivante) et il n'existe pas de motif légitime impérieux, les données ont fait l'objet d'un traitement illicite, ou l'effacement est nécessaire pour respecter une obligation légale.

Ce droit connaît des **exceptions substantielles** (article 17.3) : il ne s'applique pas dans la mesure où le traitement est nécessaire à l'exercice du droit à la liberté d'expression et d'information, au respect d'une obligation légale de conservation (documents comptables, par exemple), pour des motifs d'intérêt public dans le domaine de la santé publique, à des fins archivistiques ou de recherche scientifique, ou à la constatation, l'exercice ou la défense de droits en justice. Un responsable de traitement confronté à une demande d'effacement doit donc systématiquement vérifier si l'une de ces exceptions s'applique avant de refuser d'y donner suite — un refus non justifié constitue lui-même une violation du droit.

Lorsque le responsable du traitement a rendu publiques les données concernées (par exemple sur son propre site web) et doit les effacer, il doit prendre des **mesures raisonnables** pour informer les autres responsables du traitement qui traitent ces données que la personne concernée a demandé l'effacement de tout lien vers ces données ou de toute copie — une obligation de diligence "raisonnable", pas un résultat garanti, mais qui suppose un effort réel et documenté plutôt qu'une inaction.

## Droit à la limitation du traitement (article 18)

La personne concernée a le droit d'obtenir la limitation du traitement lorsque l'exactitude des données est contestée (pendant la vérification), lorsque le traitement est illicite mais que la personne s'oppose à l'effacement et demande une limitation à la place, lorsque le responsable du traitement n'a plus besoin des données mais que la personne en a besoin pour la constatation, l'exercice ou la défense de droits en justice, ou pendant la vérification portant sur le motif légitime en cas d'opposition (article 21, développé dans la leçon suivante). Concrètement, une donnée "limitée" doit être marquée comme telle et ne peut plus être traitée (hors conservation) sans le consentement de la personne, sauf exceptions similaires à celles de l'article 17 — un état intermédiaire entre la conservation normale et l'effacement complet, techniquement plus délicat à implémenter qu'un simple champ booléen "supprimé", car il exige de bloquer sélectivement certains usages tout en conservant la donnée elle-même.

## Ce que cette mécanique implique pour la conception d'un système

Honorer ces droits dans les délais légaux suppose, en amont, une architecture capable de localiser rapidement l'ensemble des données d'une personne à travers potentiellement de nombreux systèmes (bases de production, journaux, sauvegardes, systèmes analytiques, prestataires tiers) — un système qui ne peut répondre à une demande d'accès qu'au prix d'une recherche manuelle fastidieuse dans des dizaines de bases disparates prend un risque réel de dépasser les délais légaux, en particulier lorsque le volume de demandes augmente avec la notoriété de l'organisation.
