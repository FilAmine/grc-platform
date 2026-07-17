# SOC 1, SOC 3, bridge letters, et mapping avec d'autres référentiels

## SOC 1 : le contrôle interne relatif au reporting financier

SOC 1, régi par la même norme d'attestation SSAE 18 (section AT-C 320 spécifiquement), s'adresse à un besoin différent de SOC 2 : évaluer si les contrôles d'un prestataire de services sont pertinents pour le **contrôle interne relatif au reporting financier (ICFR)** de ses clients. Pertinent typiquement pour :

- un prestataire de paie, dont les erreurs de traitement affecteraient directement les états financiers de ses clients,
- un administrateur de fonds ou de portefeuille, dont les calculs de valorisation entrent directement dans les comptes de ses clients,
- un prestataire de services de facturation ou de recouvrement.

Un rapport SOC 1 existe, comme SOC 2, en Type I et Type II, avec la même logique de distinction (conception à un instant donné vs fonctionnement effectif sur une période). La différence structurante avec SOC 2 ne réside pas dans la méthodologie d'audit, mais dans son **objet** : SOC 1 répond à un besoin d'audit financier (souvent demandé par les propres commissaires aux comptes des clients du prestataire, dans le cadre de leur propre audit financier), tandis que SOC 2 répond à un besoin de confiance opérationnelle et sécurité.

Une organisation peut avoir besoin des deux rapports simultanément si son activité touche à la fois au traitement financier de ses clients et à des enjeux de sécurité/disponibilité plus larges — par exemple, un prestataire de paie SaaS peut être amené à produire un SOC 1 (pour les commissaires aux comptes de ses clients) et un SOC 2 (pour les équipes sécurité de ces mêmes clients).

## SOC 3 : le rapport à diffusion publique

SOC 3 s'appuie sur les mêmes Trust Services Criteria que SOC 2, évalués selon la même méthodologie d'audit — mais produit un rapport **allégé et à diffusion publique** :

- pas de description détaillée du système (équivalent de la section III d'un rapport SOC 2),
- pas de détail des tests de contrôles et de leurs résultats (section IV, absente d'un rapport SOC 3),
- uniquement l'assertion de la direction et l'opinion de l'auditeur, résumées de façon accessible à un public non spécialisé.

Cette différence de contenu explique directement la différence d'usage : un rapport SOC 2 complet reste un document à diffusion restreinte (souvent sous accord de confidentialité), tandis qu'un rapport SOC 3 peut être librement publié — affiché sur un site web sous la forme d'un **sceau SOC 3 (SOC 3 seal)**, utilisé comme argument commercial visible par n'importe quel visiteur, sans qu'aucune information sensible sur l'architecture technique de l'organisation ne soit exposée publiquement.

En pratique, une organisation qui a fait auditer son SOC 2 peut, à moindre coût additionnel, demander à son auditeur de produire également un SOC 3 dérivé du même examen — les deux rapports proviennent du même travail d'audit sous-jacent, seule leur présentation et leur niveau de détail diffèrent.

## Les bridge letters (ou gap letters)

Entre la date de clôture d'un rapport Type II et la date de délivrance du rapport suivant (souvent plusieurs semaines, le temps que le cabinet d'audit finalise son rapport), un client peut avoir besoin d'une assurance couvrant cette période intermédiaire — par exemple pour son propre audit financier annuel, dont le calendrier ne coïncide pas exactement avec celui du prestataire. Une **bridge letter** (ou gap letter) est un courrier, produit par la direction de l'organisation auditée (pas par l'auditeur lui-même), attestant qu'aucun changement significatif n'est intervenu dans l'environnement de contrôle depuis la fin de la période couverte par le dernier rapport disponible. Ce n'est pas un document officiellement défini par l'AICPA, mais une pratique de place largement répandue, acceptée par la plupart des clients et de leurs propres auditeurs comme une assurance intermédiaire raisonnable en attendant le rapport suivant.

## Mapping avec ISO 27001 et NIST CSF

Comme déjà observé à plusieurs reprises dans les parcours précédents de cette plateforme, la majorité des Common Criteria (CC1 à CC9) recoupent directement des contrôles d'autres référentiels :

| Common Criterion SOC 2 | Équivalent ISO 27001 (Annexe A) | Équivalent NIST CSF 2.0 |
|---|---|---|
| CC1 (environnement de contrôle) | 5.1 à 5.4 | GV.RR, GV.PO |
| CC3 (appréciation des risques) | Clause 6.1.2 | ID.RA |
| CC6 (accès logiques/physiques) | 5.15 à 5.18, 7.1 à 7.14 | PR.AA |
| CC7 (opérations système) | 8.15, 8.16 | DE.CM, DE.AE, RS.MA |
| CC8 (gestion des changements) | 8.32 | PR.PS |
| CC9.2 (risques fournisseurs) | 5.19 à 5.23 | GV.SC |

Une organisation déjà certifiée ISO 27001, ou déjà alignée sur le NIST CSF, dispose donc d'une base de contrôles internes largement réutilisable pour construire sa matrice de contrôles SOC 2 — la même logique de mapping plutôt que de duplication, déjà développée dans le premier parcours de cette plateforme, s'applique ici de façon très concrète : le travail de fond (les contrôles eux-mêmes) reste largement commun, seul le vocabulaire et le format de preuve exigé varient d'un référentiel à l'autre.

## Ce que le mapping ne résout jamais entièrement

Malgré ce fort recoupement, un mapping ne dispense jamais totalement d'un travail spécifique à chaque référentiel : les exigences de preuve (échantillonnage et méthodes de test pour SOC 2, Déclaration d'Applicabilité pour ISO 27001) restent propres à chacun, et une organisation qui vise plusieurs référentiels simultanément doit tout de même adapter la présentation de ses preuves au format attendu par chaque audit — le socle de contrôles est commun, l'exercice de démonstration reste, pour partie, spécifique à chaque référentiel.
