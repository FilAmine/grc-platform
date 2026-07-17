# Responsable de traitement, sous-traitant, et le contrat de sous-traitance

## Pourquoi cette qualification n'est jamais un simple choix contractuel

La qualification de responsable de traitement ou de sous-traitant, présentée au module 0, n'est pas une étiquette que les parties peuvent librement s'attribuer par contrat — elle découle d'une analyse **factuelle** de qui détermine réellement les finalités et les moyens du traitement, indépendamment de ce que le contrat prétend. Une organisation qui se qualifie contractuellement de simple "sous-traitant" alors qu'elle décide en réalité des finalités du traitement (par exemple, un prestataire qui réutilise les données de ses clients pour ses propres finalités d'amélioration produit, au-delà du strict mandat reçu) sera requalifiée en responsable de traitement par une autorité de contrôle ou une juridiction, avec toutes les obligations qui en découlent — y compris celles qu'elle pensait avoir déléguées contractuellement.

## Les obligations propres au responsable de traitement (article 24)

Le responsable du traitement doit mettre en œuvre des mesures techniques et organisationnelles appropriées pour s'assurer et être en mesure de démontrer que le traitement est effectué conformément au règlement — la formulation même de l'article 24 institutionnalise le principe d'**accountability** déjà rencontré dans le premier parcours de cette plateforme : ne pas seulement être conforme, mais pouvoir le démontrer.

## Les obligations propres au sous-traitant (article 28)

Le sous-traitant ne peut traiter les données que sur **instruction documentée** du responsable du traitement — y compris en ce qui concerne les transferts de données vers un pays tiers, sauf si une obligation légale l'exige, auquel cas il doit informer le responsable du traitement de cette obligation avant le traitement, sauf interdiction légale pour des motifs d'intérêt public. Le sous-traitant doit également garantir que les personnes autorisées à traiter les données se sont engagées à respecter la confidentialité, mettre en œuvre les mesures de sécurité de l'article 32 (module 4), et respecter les conditions du recours à un **sous-traitant ultérieur (sous-traitance en cascade)** — développées plus bas.

## Le contrat de sous-traitance (Data Processing Agreement — DPA)

Le recours à un sous-traitant doit être régi par un contrat ou un autre acte juridique, qui lie le sous-traitant à l'égard du responsable du traitement et qui définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, ainsi que les obligations et droits du responsable du traitement. L'article 28.3 impose un contenu minimal obligatoire à ce contrat, notamment que le sous-traitant :

- traite les données uniquement sur instruction documentée du responsable,
- veille à ce que les personnes autorisées à traiter les données s'engagent à la confidentialité,
- prenne les mesures de sécurité requises par l'article 32,
- respecte les conditions du recours à un autre sous-traitant (voir plus bas),
- aide le responsable du traitement, compte tenu de la nature du traitement, à répondre aux demandes d'exercice des droits des personnes concernées,
- aide le responsable du traitement à respecter ses obligations en matière de sécurité, de notification de violation et d'analyse d'impact (module 4),
- **efface ou renvoie**, au choix du responsable du traitement, toutes les données à caractère personnel au terme de la prestation de services, et détruit les copies existantes sauf obligation légale de conservation contraire,
- met à la disposition du responsable du traitement toutes les informations nécessaires pour démontrer le respect de ces obligations, et permette la réalisation d'audits, y compris des inspections, par le responsable du traitement ou un autre auditeur qu'il a mandaté.

Un contrat de prestation qui ne contient aucune de ces clauses, ou qui se contente d'une clause de confidentialité générique sans reprendre ces obligations spécifiques, ne satisfait pas l'exigence de l'article 28 — un point de vigilance essentiel lors de la contractualisation avec tout fournisseur qui traite des données personnelles pour le compte de l'organisation (hébergeur cloud, prestataire d'emailing, outil d'analyse d'audience, etc.).

## La sous-traitance ultérieure (en cascade)

Le sous-traitant ne peut recruter un autre sous-traitant sans **autorisation écrite préalable, spécifique ou générale**, du responsable du traitement. En cas d'autorisation générale, le sous-traitant doit informer le responsable du traitement de tout changement prévu concernant l'ajout ou le remplacement d'autres sous-traitants, donnant au responsable du traitement la possibilité d'émettre des objections. Le sous-traitant initial demeure **pleinement responsable**, à l'égard du responsable du traitement, de l'exécution des obligations du sous-traitant ultérieur — une chaîne de responsabilité qui ne s'efface jamais complètement, même lorsque le traitement effectif est délégué à plusieurs niveaux (un fournisseur cloud sous-jacent à un éditeur SaaS, lui-même sous-traitant d'un client final, par exemple).

## Le cas particulier des responsables conjoints (article 26)

Lorsque deux responsables du traitement déterminent conjointement les finalités et les moyens d'un traitement (déjà défini au module 0), ils doivent conclure un accord qui définit de manière transparente leurs obligations respectives, en particulier en ce qui concerne l'exercice des droits de la personne concernée et leurs obligations respectives de fournir les informations de l'article 13-14 — un accord distinct d'un contrat de sous-traitance classique, car aucune des deux parties n'agit ici pour le compte de l'autre : elles décident ensemble.

## Un exemple concret d'articulation de ces trois qualifications

Une plateforme SaaS de gestion RH illustre bien la coexistence de ces trois rôles dans un même écosystème : l'entreprise cliente qui utilise la plateforme pour gérer les données de ses salariés est **responsable de traitement** (elle détermine les finalités : gestion de la paie, des congés, de l'évaluation) ; l'éditeur de la plateforme SaaS est **sous-traitant** de cette entreprise cliente pour ce traitement précis, lié par un contrat de sous-traitance conforme à l'article 28 ; et si cet éditeur héberge sa plateforme chez un fournisseur cloud public, ce fournisseur cloud est à son tour **sous-traitant ultérieur**, dont le recours doit avoir été autorisé par l'entreprise cliente initiale — une chaîne à trois niveaux, chacun avec ses obligations propres, mais où la responsabilité de l'entreprise cliente initiale, en tant que responsable de traitement, ne disparaît jamais complètement quelle que soit la longueur de cette chaîne.
