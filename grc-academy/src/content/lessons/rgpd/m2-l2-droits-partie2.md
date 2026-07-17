# Les droits des personnes concernées (2/2) : portabilité, opposition, décisions automatisées

## Droit à la portabilité des données (article 20)

La personne concernée a le droit de recevoir les données à caractère personnel la concernant, qu'elle a fournies à un responsable du traitement, dans un format structuré, couramment utilisé et lisible par machine, et a le droit de transmettre ces données à un autre responsable du traitement sans que le premier y fasse obstacle. Ce droit ne s'applique que sous des conditions cumulatives précises :

- le traitement doit reposer sur le **consentement** ou sur un **contrat** (les bases légales des articles 6.1.a et 6.1.b uniquement — la portabilité ne s'applique pas à un traitement fondé sur l'intérêt légitime ou une obligation légale),
- le traitement doit être effectué **à l'aide de procédés automatisés**,
- la portabilité ne porte que sur les données **fournies** par la personne concernée elle-même — elle ne s'étend pas aux données dérivées ou déduites par le responsable du traitement à partir de ces données brutes (un score de crédit calculé, par exemple, n'est généralement pas couvert, contrairement aux données saisies par l'utilisateur qui ont servi à le calculer).

Lorsque c'est techniquement possible, la personne concernée a également le droit d'obtenir que ses données soient transmises directement d'un responsable du traitement à un autre — une exigence qui a directement inspiré des initiatives réglementaires sectorielles ultérieures (l'open banking européen, par exemple, repose sur une logique très proche de portabilité directe entre organismes).

## Droit d'opposition (article 21)

La personne concernée a le droit de s'opposer à tout moment, pour des raisons tenant à sa situation particulière, à un traitement fondé sur l'intérêt légitime ou sur une mission d'intérêt public. Le responsable du traitement ne peut alors plus traiter les données, sauf s'il démontre qu'il existe des **motifs légitimes et impérieux** pour le traitement qui prévalent sur les intérêts, les droits et les libertés de la personne concernée, ou pour la constatation, l'exercice ou la défense de droits en justice. C'est ici que le test de mise en balance de l'intérêt légitime, développé au module 1, redevient central : un responsable de traitement qui a documenté sérieusement ce test lors de la conception du traitement dispose d'un argumentaire déjà prêt pour répondre à une opposition, tandis qu'une organisation qui invoque l'intérêt légitime sans analyse préalable sérieuse se trouve démunie face à une opposition motivée.

Un régime distinct et **absolu** s'applique lorsque les données sont traitées à des fins de **prospection (marketing direct)** : la personne concernée peut s'opposer à tout moment, sans avoir à justifier d'un motif particulier, et le responsable du traitement doit alors cesser le traitement à cette fin sans possibilité de lui opposer un quelconque motif légitime impérieux — un droit d'opposition à la prospection qui n'admet aucune exception.

## Décisions individuelles automatisées, y compris le profilage (article 22)

La personne concernée a le droit de ne pas faire l'objet d'une décision fondée **exclusivement** sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant de manière significative ou l'affectant de manière significative de façon similaire — par exemple, un refus automatique de crédit ou une décision de recrutement entièrement automatisée sans intervention humaine réelle.

Ce droit connaît trois exceptions : la décision est nécessaire à la conclusion ou à l'exécution d'un contrat, elle est autorisée par le droit de l'Union ou d'un État membre qui prévoit des garanties appropriées, ou elle est fondée sur le **consentement explicite** de la personne. Même dans ces cas d'exception (hors autorisation légale spécifique), le responsable du traitement doit mettre en œuvre des mesures appropriées pour sauvegarder les droits et libertés de la personne, incluant **au minimum le droit d'obtenir une intervention humaine**, d'exprimer son point de vue et de contester la décision.

Un point de vigilance souvent mal interprété : le simple fait qu'un humain "valide formellement" une décision produite par un algorithme ne suffit pas à échapper à l'article 22 si cette validation n'est pas une intervention humaine **réelle et effective** — une supervision purement formelle, sans pouvoir réel de remettre en cause la recommandation automatisée, est généralement considérée comme insuffisante par les autorités de contrôle et la jurisprudence.

## Le lien entre ces droits et l'architecture technique du système

Chacun de ces droits impose des contraintes techniques concrètes qui, idéalement, sont anticipées dès la conception du système plutôt que traitées comme un chantier réactif après une première demande complexe :

- la **portabilité** suppose une capacité d'export structuré des données, distinguant clairement les données fournies par l'utilisateur des données dérivées,
- l'**opposition à la prospection** suppose un mécanisme de suppression immédiate et fiable d'une personne de toute liste ou campagne marketing, propagé à l'ensemble des systèmes qui l'utilisent,
- les **décisions automatisées** soumises à l'article 22 supposent la conservation d'une trace explicable de la logique de décision, suffisante pour permettre une intervention humaine informée en cas de contestation — un sujet qui recoupe directement les enjeux de transparence et d'explicabilité des systèmes algorithmiques, de plus en plus présents dans les traitements modernes à mesure que l'automatisation des décisions se généralise.

C'est cette anticipation technique en amont — plutôt que la simple connaissance théorique des droits — qui distingue une organisation réellement capable d'honorer ces droits dans les délais légaux d'une organisation qui découvre, à chaque nouvelle demande complexe, l'ampleur du travail nécessaire pour y répondre.
