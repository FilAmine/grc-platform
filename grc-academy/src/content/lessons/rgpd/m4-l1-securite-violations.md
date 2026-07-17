# Sécurité du traitement et notification des violations de données

## Sécurité du traitement (article 32) : une obligation de moyens graduée par le risque

Le responsable du traitement et le sous-traitant doivent mettre en œuvre les mesures techniques et organisationnelles appropriées pour garantir un niveau de sécurité adapté au risque, en tenant compte de l'état des connaissances, des coûts de mise en œuvre, de la nature, de la portée, du contexte et des finalités du traitement, ainsi que des risques pour les droits et libertés des personnes physiques. Le règlement cite explicitement, à titre d'exemple et non de manière exhaustive :

- la **pseudonymisation et le chiffrement** des données à caractère personnel — déjà développés en détail dans le module Privacy by Design du premier parcours de cette plateforme,
- des moyens permettant de garantir la **confidentialité, l'intégrité, la disponibilité et la résilience constantes** des systèmes et des services de traitement,
- des moyens permettant de **rétablir la disponibilité** des données à caractère personnel et l'accès à celles-ci dans des délais appropriés en cas d'incident physique ou technique,
- une procédure destinée à **tester, analyser et évaluer régulièrement** l'efficacité des mesures techniques et organisationnelles pour assurer la sécurité du traitement.

Cette formulation — "adapté au risque", sans liste de contrôles imposée — rejoint directement la logique observée pour ISO 27001, le NIST CSF et SOC 2 dans les parcours précédents de cette plateforme : le RGPD ne prescrit pas de mesures techniques précises, il exige une démarche de gestion des risques proportionnée, documentée et démontrable. Un système chiffré au repos et en transit, avec un contrôle d'accès rigoureux et un programme de test de sécurité régulier, satisfait largement l'esprit de l'article 32 — sans qu'aucune disposition du RGPD n'exige un algorithme de chiffrement ou une configuration technique précise, laissée à l'appréciation du responsable du traitement au regard de l'état de l'art.

## Qu'est-ce qu'une violation de données à caractère personnel (article 4.12)

Une violation de données est une violation de la sécurité entraînant, de manière accidentelle ou illicite, la **destruction**, la **perte**, l'**altération**, la **divulgation non autorisée** de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'**accès non autorisé** à de telles données. Cette définition est volontairement large : elle couvre non seulement le vol ou la fuite de données (divulgation), mais aussi une simple perte accidentelle (un disque dur défaillant sans sauvegarde), une altération non maîtrisée (une corruption de données), ou un accès non autorisé sans exfiltration avérée (un employé consultant sans droit le dossier d'un collègue).

## La notification à l'autorité de contrôle (article 33) : la règle des 72 heures

En cas de violation de données à caractère personnel, le responsable du traitement la notifie à l'autorité de contrôle compétente **dans les meilleurs délais et, si possible, 72 heures au plus tard** après en avoir pris connaissance — sauf si la violation n'est pas susceptible d'engendrer un risque pour les droits et libertés des personnes physiques, auquel cas aucune notification n'est requise. Ce délai de 72 heures court à partir du moment où le responsable du traitement **a connaissance** de la violation, pas à partir du moment où elle s'est effectivement produite — une nuance importante lorsque la découverte intervient longtemps après l'incident réel.

Si la notification n'intervient pas dans les 72 heures, elle doit être accompagnée des motifs du retard — le règlement anticipe explicitement que certaines violations complexes ne pourront pas être pleinement analysées dans ce délai, et permet une **notification par phases** : une première notification initiale, même incomplète, suivie d'informations complémentaires fournies au fur et à mesure de l'avancement de l'analyse forensique.

La notification doit décrire la nature de la violation, y compris, si possible, les catégories et le nombre approximatif de personnes concernées et d'enregistrements de données concernés, communiquer le nom et les coordonnées du DPO ou d'un autre point de contact, décrire les conséquences probables de la violation, et décrire les mesures prises ou envisagées pour y remédier, y compris les mesures pour atténuer ses éventuelles conséquences négatives.

## La notification aux personnes concernées (article 34) : un seuil plus élevé

Lorsque la violation est susceptible d'engendrer un **risque élevé** pour les droits et libertés des personnes physiques — un critère plus exigeant que le simple "risque" déclenchant la notification à l'autorité de contrôle — le responsable du traitement doit également communiquer la violation aux personnes concernées elles-mêmes, dans les meilleurs délais, en des termes clairs et simples. Cette notification individuelle n'est **pas requise** dans trois cas :

- le responsable du traitement a mis en œuvre des mesures de protection technique appropriées (notamment le **chiffrement**) rendant les données incompréhensibles pour toute personne non autorisée à y accéder — un exemple direct et concret de la valeur préventive du chiffrement, qui peut littéralement éviter l'obligation de notification individuelle en cas de violation ultérieure,
- le responsable du traitement a pris des mesures ultérieures garantissant que le risque élevé pour les personnes n'est plus susceptible de se matérialiser,
- la communication exigerait des efforts disproportionnés, auquel cas une communication publique ou une mesure similaire, permettant une information tout aussi efficace, est utilisée à la place.

## Le rôle du sous-traitant dans la chaîne de notification

Le sous-traitant qui constate une violation de données doit la notifier au responsable du traitement **dans les meilleurs délais** après en avoir pris connaissance — le point de départ du délai de 72 heures court, pour le responsable du traitement, à partir du moment où **lui-même** en a connaissance, ce qui inclut la connaissance qu'en a son sous-traitant. Cette chaîne de notification rapide entre sous-traitant et responsable du traitement, souvent formalisée par une clause dédiée dans le contrat de sous-traitance (article 28, module 3), est indispensable pour respecter le délai global de 72 heures — un sous-traitant qui tarde à informer son client responsable du traitement compromet directement la capacité de ce dernier à respecter ses propres obligations légales.

## Une procédure interne à préparer en amont, pas à improviser

La contrainte des 72 heures rend illusoire toute improvisation au moment où une violation réelle survient : une organisation mature dispose, en amont, d'une procédure documentée définissant qui doit être alerté en interne dès la détection d'un incident suspect, comment qualifier rapidement s'il s'agit d'une violation au sens de l'article 4.12, comment évaluer le niveau de risque pour déterminer si la notification à l'autorité de contrôle et/ou aux personnes concernées est requise, et qui rédige et valide la notification elle-même — une procédure qui recoupe directement la gestion des incidents de sécurité déjà développée dans les parcours ISO 27001, NIST CSF et SOC 2 de cette plateforme, avec cette contrainte de délai réglementaire supplémentaire et non négociable qui lui est propre.
