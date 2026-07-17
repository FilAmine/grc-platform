# NIS2 face aux autres référentiels, et feuille de route de mise en conformité

## NIS2 et le RGPD : deux textes distincts, souvent déclenchés par un même incident

Le parcours RGPD de cette plateforme a développé en détail les obligations relatives aux données personnelles. NIS2 et le RGPD restent des textes **juridiquement distincts**, protégeant des intérêts différents (la continuité et la résilience des services essentiels d'un côté, les droits des personnes concernées de l'autre), avec des autorités compétentes potentiellement différentes et des délais de notification qui, bien que proches (72 heures pour les deux), ne sont pas régis par le même mécanisme procédural. Une organisation confrontée à un incident affectant à la fois la disponibilité de son service et la confidentialité de données personnelles doit donc conduire **deux analyses de notification distinctes**, potentiellement vers deux autorités différentes, même si le fait générateur technique est identique — une coordination interne qui gagne à être anticipée dans la procédure de gestion des incidents plutôt que découverte dans l'urgence.

## NIS2 et DORA : la clause de lex specialis

Le règlement **DORA** (Digital Operational Resilience Act), qui impose au secteur financier européen des exigences de résilience opérationnelle numérique, est explicitement désigné par NIS2 comme un texte pouvant primer sur elle en tant que **lex specialis** : lorsqu'un acte juridique sectoriel de l'Union impose des exigences au moins équivalentes à celles de NIS2, les dispositions sectorielles s'appliquent à la place de NIS2 pour les entités concernées, évitant ainsi une double couche réglementaire pour un même secteur. Une banque ou un établissement financier relevant à la fois du secteur bancaire de l'Annexe I de NIS2 et du périmètre de DORA appliquera donc principalement les exigences de DORA pour sa gestion des risques informatiques, plutôt qu'un cumul intégral des deux textes — un principe de non-duplication réglementaire qui rejoint, dans son esprit, la logique de mapping entre référentiels déjà développée à de nombreuses reprises dans cette plateforme, ici appliquée entre deux textes de nature légale plutôt qu'entre deux référentiels volontaires.

## NIS2 comme cadre légal, ISO 27001/NIST CSF/CIS Controls comme couche de mise en œuvre

À l'image de ce qui a déjà été observé pour l'article 32 du RGPD et l'article 21 de NIS2 lui-même (module 2), le texte ne prescrit ni méthodologie de risque, ni catalogue de contrôles technique détaillé. En pratique, une organisation soumise à NIS2 s'appuie généralement sur l'un des référentiels techniques déjà étudiés dans cette plateforme pour démontrer sa conformité aux dix domaines de l'article 21 :

| Domaine de l'article 21 | Référentiel de mise en œuvre déjà étudié |
|---|---|
| Politiques d'analyse des risques | ISO 31000, EBIOS RM, méthodologie de risque du NIST RMF (SP 800-30) |
| Gestion des incidents | Contrôles 5.24-5.28 d'ISO 27001, fonction Respond du NIST CSF, contrôle 17 des CIS Controls |
| Continuité des activités | Contrôle 8.13 d'ISO 27001, famille CP de SP 800-53, contrôle 11 des CIS Controls |
| Sécurité de la chaîne d'approvisionnement | Contrôles 5.19-5.23 d'ISO 27001, catégorie GV.SC du NIST CSF, famille SR de SP 800-53, contrôle 15 des CIS Controls |
| Acquisition/développement/maintenance sécurisés | Contrôles 8.25-8.34 d'ISO 27001, contrôle 16 des CIS Controls |
| Cyberhygiène et formation | Contrôle 6.3 d'ISO 27001, contrôle 14 des CIS Controls |
| Cryptographie | Contrôle 8.24 d'ISO 27001, contrôle SC-13 de SP 800-53 |
| RH, contrôle d'accès, gestion des actifs | Contrôles 5.9-5.18 et 6.1-6.8 d'ISO 27001 |
| MFA et communications sécurisées | Contrôle 8.5 d'ISO 27001, famille IA de SP 800-53 |

Une organisation déjà certifiée ISO 27001, ou déjà alignée sur le NIST CSF ou les CIS Controls (parcours dédiés de cette plateforme), dispose donc d'une base de contrôles très largement réutilisable pour démontrer sa conformité à l'article 21 — sans avoir à construire un dispositif entièrement distinct spécifiquement pour NIS2.

## Construire une feuille de route de conformité

### Priorité 1 — Déterminer précisément son statut

Avant tout investissement technique, déterminer si l'organisation relève effectivement de NIS2 (secteur Annexe I ou II, seuil de taille ou inclusion automatique, module 1), et si elle est qualifiée d'entité essentielle ou importante — une qualification qui détermine directement le régime de supervision applicable (module 5) et qui doit être vérifiée auprès de l'autorité compétente nationale, l'auto-qualification restant sujette à contestation.

### Priorité 2 — Engager les organes de direction dès le départ

Compte tenu de la responsabilité personnelle introduite par l'article 20 (module 3), associer les organes de direction dès la phase de cadrage du programme, plutôt que de leur présenter un dispositif déjà construit pour simple validation formelle — un piège de gouvernance déjà signalé à plusieurs reprises dans cette plateforme, mais dont les conséquences sont ici potentiellement personnelles pour les dirigeants concernés.

### Priorité 3 — Combler les écarts par rapport aux dix domaines de l'article 21

S'appuyer sur un référentiel technique déjà maîtrisé par l'organisation (ISO 27001, NIST CSF, ou les CIS Controls) pour cartographier précisément sa couverture actuelle des dix domaines de l'article 21 (module 2), en documentant les écarts et un plan de remédiation priorisé.

### Priorité 4 — Structurer la procédure de notification des incidents

Documenter et exercer, avant qu'un incident réel ne survienne, la procédure de notification à plusieurs paliers de l'article 23 (module 4) — qui alerter en interne, comment qualifier rapidement le caractère significatif d'un incident, qui rédige et transmet l'alerte précoce à 24 heures — un exercice de préparation d'autant plus critique que le délai initial de 24 heures laisse une marge de manœuvre nettement plus étroite que celle déjà observée pour le RGPD dans le parcours dédié de cette plateforme.

### Priorité 5 — Se préparer au régime de supervision applicable

Une entité essentielle doit anticiper une supervision proactive potentiellement déclenchée à tout moment (module 5), ce qui suppose une documentation et des preuves d'application continue plutôt qu'une préparation ponctuelle avant un contrôle programmé.

## En clôture de ce parcours

Ce parcours a couvert NIS2 de bout en bout : le champ d'application élargi et la distinction entre entités essentielles et importantes, les dix domaines de mesures de gestion des risques de l'article 21, la responsabilité personnelle des organes de direction introduite par l'article 20, le processus de notification des incidents en plusieurs paliers, le régime différencié de supervision et les sanctions, l'écosystème de coopération européenne et la divulgation coordonnée des vulnérabilités, et enfin l'articulation de NIS2 avec les autres référentiels déjà étudiés dans cette plateforme. Combiné aux sept autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels et réglementations majeurs qui structurent une démarche GRC moderne en Europe et aux États-Unis.
