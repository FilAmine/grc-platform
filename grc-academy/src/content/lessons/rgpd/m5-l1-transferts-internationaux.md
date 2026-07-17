# Les transferts internationaux de données

## Un principe d'interdiction, assorti de mécanismes d'exception

Le chapitre V du règlement pose un principe simple dans sa formulation mais lourd de conséquences pratiques : un transfert de données à caractère personnel vers un pays tiers (hors Espace économique européen) ou vers une organisation internationale ne peut avoir lieu que si l'un des mécanismes prévus par ce chapitre s'applique. L'objectif est d'éviter que le niveau de protection garanti par le règlement ne soit contourné simplement en déplaçant le traitement en dehors de l'Union.

## Les décisions d'adéquation (article 45)

La Commission européenne peut constater qu'un pays tiers, un territoire, un ou plusieurs secteurs déterminés dans ce pays tiers, ou une organisation internationale, assure un **niveau de protection adéquat** — un statut qui permet alors les transferts vers ce pays sans autorisation spécifique supplémentaire, comme s'il s'agissait d'un transfert au sein de l'Union. La Commission réexamine ces décisions périodiquement (au moins tous les quatre ans), et les pays bénéficiant d'une décision d'adéquation évoluent dans le temps.

## Les garanties appropriées (article 46) : le mécanisme le plus utilisé en pratique

En l'absence de décision d'adéquation, un transfert reste possible si le responsable du traitement ou le sous-traitant a fourni des **garanties appropriées**, et à condition que les personnes concernées disposent de droits opposables et de voies de droit effectives. Les mécanismes les plus fréquemment utilisés :

### Les clauses contractuelles types (Standard Contractual Clauses — SCC)

Des clauses contractuelles pré-rédigées et approuvées par la Commission européenne, que l'exportateur et l'importateur de données intègrent à leur contrat. La Commission a publié en 2021 un jeu modulaire de clauses couvrant quatre scénarios de transfert (responsable à responsable, responsable à sous-traitant, sous-traitant à sous-traitant, sous-traitant à responsable), remplaçant les anciennes clauses types de 2001 et 2010. C'est de très loin le mécanisme le plus utilisé par les organisations pour leurs transferts vers des pays tiers, notamment vers les États-Unis, en raison de sa simplicité relative de mise en œuvre comparée aux règles d'entreprise contraignantes.

### Les règles d'entreprise contraignantes (Binding Corporate Rules — BCR)

Des règles internes, approuvées par l'autorité de contrôle compétente, qu'un groupe d'entreprises engagées dans une activité économique conjointe adopte pour encadrer ses transferts internes de données entre ses différentes entités situées dans plusieurs pays. Plus lourdes à mettre en place que les clauses contractuelles types (l'approbation par l'autorité de contrôle peut prendre plusieurs mois, voire davantage), elles sont surtout adaptées aux grands groupes multinationaux avec des flux de données internes récurrents et complexes entre de nombreuses filiales.

### Les codes de conduite et mécanismes de certification (article 40-42)

Des codes de conduite approuvés, ou des certifications, assortis d'engagements contraignants et exécutoires de la part de l'importateur, peuvent également servir de garantie appropriée — un mécanisme encore relativement peu utilisé en pratique par rapport aux clauses contractuelles types.

## L'exigence supplémentaire posée par la jurisprudence Schrems

### L'arrêt Schrems I (2015) et l'invalidation du Safe Harbor

La Cour de justice de l'Union européenne a invalidé, en 2015, l'accord "Safe Harbor" qui organisait les transferts de données vers les États-Unis, jugé insuffisant au regard des pouvoirs de surveillance des autorités américaines — une décision qui a directement conduit à la négociation d'un accord de remplacement.

### L'arrêt Schrems II (2020) et l'invalidation du Privacy Shield

La Cour a ensuite invalidé, en 2020, l'accord "Privacy Shield" qui avait remplacé le Safe Harbor, pour des motifs similaires (accès disproportionné des services de renseignement américains aux données transférées, absence de voie de recours effective pour les personnes concernées européennes). Cette décision a eu une conséquence structurante au-delà du seul Privacy Shield : elle a précisé que même en s'appuyant sur des **clauses contractuelles types**, l'exportateur de données doit désormais évaluer, au cas par cas, si la législation du pays de destination permet réellement d'assurer un niveau de protection substantiellement équivalent à celui garanti dans l'Union — une obligation dite de **Transfer Impact Assessment (TIA)**, et le cas échéant, mettre en place des **mesures supplémentaires** (chiffrement renforcé avec des clés non accessibles à l'importateur, par exemple) pour combler l'écart identifié.

### Le Data Privacy Framework UE-États-Unis (2023)

Un nouvel accord-cadre, le **EU-U.S. Data Privacy Framework**, a été adopté par une décision d'adéquation de la Commission européenne en juillet 2023, introduisant de nouvelles garanties côté américain (limitation de l'accès des services de renseignement au strict nécessaire et proportionné, création d'une cour de réexamen indépendante pour les plaintes des personnes européennes). Les organisations américaines qui adhèrent formellement à ce cadre peuvent recevoir des données européennes sur la base de cette décision d'adéquation, sans recourir aux clauses contractuelles types — une situation qui reste néanmoins susceptible d'une nouvelle contestation devant la Cour de justice, suivant le précédent des deux invalidations précédentes, et qu'il convient donc de suivre dans la durée plutôt que de considérer comme définitivement acquise.

## Les dérogations pour des situations particulières (article 49)

En l'absence de décision d'adéquation et de garanties appropriées, un transfert reste possible dans des situations limitativement énumérées : consentement explicite de la personne concernée après information des risques encourus, nécessité pour l'exécution d'un contrat, motifs importants d'intérêt public, sauvegarde des intérêts vitaux de la personne. Ces dérogations sont d'interprétation **stricte** et ne doivent pas servir de solution de facilité pour des transferts réguliers et répétés — le CEPD a explicitement rappelé qu'elles sont pensées pour des situations occasionnelles et non systématiques, contrairement aux mécanismes de l'article 46 pensés pour des flux de données récurrents et structurels.

## Ce que cela implique concrètement pour une organisation cloud

Une organisation qui héberge ses données chez un fournisseur cloud disposant de centres de données en dehors de l'Union européenne — ou dont le support technique est assuré depuis un pays tiers, ce qui constitue également un transfert au sens du règlement — doit documenter précisément le mécanisme de transfert applicable (clauses contractuelles types le plus souvent), avoir réalisé le Transfer Impact Assessment exigé depuis Schrems II, et, le cas échéant, avoir mis en place les mesures techniques supplémentaires nécessaires — un sujet qui rejoint directement le modèle de responsabilité partagée et les enjeux de localisation des données développés dans le module Cloud Security by Design du premier parcours de cette plateforme, ici abordé sous son angle strictement juridique plutôt que technique.
