# Le cadre de gestion des risques liés aux TIC (2/2) : exigences spécifiques

## L'inventaire des actifs informationnels et TIC

L'entité financière doit tenir à jour un **inventaire de tous ses actifs informationnels et actifs TIC**, y compris ceux situés sur des sites distants, les ressources réseau, et les actifs matériels, en documentant leur configuration et leurs interconnexions et interdépendances — un contrôle qui recoupe directement le contrôle 1 des CIS Controls (inventaire et contrôle des actifs de l'entreprise) et le contrôle 5.9 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme. DORA exige en outre explicitement une **cartographie des interdépendances** entre ces actifs — un niveau de détail qui va au-delà d'un simple inventaire statique, en documentant comment une défaillance d'un actif se propagerait aux autres.

## La politique de continuité des activités liée aux TIC

Les entités financières doivent établir une **politique de continuité des activités liée aux TIC**, dans le cadre de leur politique globale de continuité des activités, structurée notamment autour de :

- des **plans de continuité des activités** spécifiques aux TIC, comprenant des mesures et des plans pour faire face aux perturbations liées aux TIC,
- des **plans de réponse et de rétablissement**, avec des objectifs de temps de reprise (Recovery Time Objective — RTO) et de point de reprise (Recovery Point Objective — RPO) définis pour chaque fonction critique ou importante,
- des **tests réguliers** de ces plans, dans une logique déjà rencontrée à travers de multiples référentiels de cette plateforme — le contrôle 8.13 d'ISO 27001, le critère A1.3 de SOC 2, la famille CP de SP 800-53, ou le contrôle 11 des CIS Controls insistent tous sur le test réel plutôt que sur l'existence théorique d'un plan.

Les objectifs RTO et RPO occupent une place particulièrement structurante dans DORA : ils traduisent, en engagement quantifié et vérifiable, le niveau de résilience attendu pour chaque fonction critique — un degré de précision généralement plus poussé que ce qu'exigent la plupart des référentiels génériques déjà étudiés dans cette plateforme, à l'exception peut-être de la planification de la capacité déjà rencontrée dans le critère A1.1 de SOC 2.

## La politique de sauvegarde et de restauration des données

DORA exige des politiques et procédures de sauvegarde spécifiant la portée des données couvertes, la fréquence minimale de sauvegarde en fonction de la criticité des informations, et des systèmes et procédures de restauration des données qui garantissent qu'elles peuvent être restaurées de manière sécurisée — avec, là encore, une exigence explicite de **test régulier** des procédures de restauration.

## Les plans de communication de crise

Les entités financières doivent disposer de plans de communication de crise permettant une **divulgation responsable**, au minimum, des incidents ou vulnérabilités majeurs liés aux TIC aux clients concernés et, le cas échéant, au public. Cette exigence rejoint, dans son principe, la notification aux destinataires des services de l'article 23 de NIS2 déjà développée dans le parcours dédié de cette plateforme, mais avec une insistance particulière sur la dimension de communication de crise organisée et anticipée, plutôt qu'improvisée au moment de l'incident.

## La revue et l'audit du cadre

DORA exige un **audit interne indépendant**, réalisé selon un plan pluriannuel approuvé par l'organe de direction, portant sur le cadre de gestion des risques liés aux TIC — une exigence directement comparable à la clause 9.2 d'ISO 27001 (audit interne) déjà développée dans le parcours dédié de cette plateforme, avec la même insistance sur l'indépendance de l'auditeur vis-à-vis des équipes opérationnelles auditées.

## Comment ce cadre s'articule avec les référentiels techniques déjà étudiés

À l'image de l'article 21 de NIS2 et de l'article 32 du RGPD déjà développés dans les parcours précédents de cette plateforme, le cadre de gestion des risques liés aux TIC de DORA énonce des objectifs de haut niveau sans prescrire de catalogue de contrôles technique détaillé. En pratique, une entité financière soumise à DORA s'appuie généralement sur l'un des référentiels techniques déjà étudiés dans cette plateforme (ISO 27001, NIST CSF, ou les CIS Controls) pour traduire concrètement ces exigences en contrôles opérationnels vérifiables — une entité financière déjà certifiée ISO 27001 dispose ainsi d'une base de contrôles très largement réutilisable pour démontrer sa conformité au cadre de gestion des risques liés aux TIC de DORA.

## Ce qui distingue malgré tout DORA d'un simple habillage sectoriel d'ISO 27001 ou du NIST CSF

Si la structure générale du cadre de gestion des risques liés aux TIC recoupe largement les référentiels déjà étudiés dans cette plateforme, DORA introduit deux éléments sans équivalent direct ailleurs dans ce parcours de formation : un régime de tests de résilience gradué incluant les tests de pénétration fondés sur la menace (module 3), et surtout un régime de supervision directe des prestataires tiers de services TIC critiques (module 4) — deux innovations qui justifient à elles seules qu'un texte sectoriel distinct, plutôt qu'une simple application du cadre générique de NIS2, ait été jugé nécessaire pour le secteur financier.
