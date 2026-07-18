# Business Associates et le contrat obligatoire (BAA)

## Une responsabilité directe introduite tardivement, contrairement au RGPD

Le premier parcours de cette plateforme, comme le parcours RGPD dédié, ont déjà développé la distinction entre responsable de traitement et sous-traitant, ce dernier portant depuis toujours (sous le RGPD comme sous sa directive prédécesseure) une part de responsabilité propre. HIPAA a suivi une trajectoire différente : à l'origine (1996-2003), seules les entités couvertes portaient une responsabilité directe devant le régulateur — les Business Associates n'étaient liés que par un **contrat** avec l'entité couverte, sans risquer de sanction directe de l'OCR en cas de manquement. Ce n'est qu'avec le **HITECH Act (2009)**, développé au module 0 de ce parcours, que les Business Associates sont devenus directement responsables devant l'OCR pour le respect de la Security Rule et de certaines dispositions de la Privacy Rule — une évolution qui rappelle, dans son principe, l'évolution similaire déjà observée pour le RGPD lui-même par rapport à la directive de 1995 qu'il a remplacée.

## Qui est un Business Associate

Un Business Associate est toute personne ou entité qui exerce une fonction ou une activité pour le compte d'une entité couverte impliquant l'utilisation ou la divulgation d'informations de santé protégées — sans faire elle-même partie de la main-d'œuvre de l'entité couverte. Les exemples les plus fréquents incluent : un hébergeur cloud stockant des dossiers médicaux électroniques, un prestataire de facturation médicale, un cabinet d'avocats ayant accès à des dossiers de patients dans le cadre d'un contentieux, un consultant en sécurité informatique auditant les systèmes d'une entité couverte, ou un éditeur de logiciel de gestion de cabinet médical.

Un point de vigilance souvent mal anticipé : la définition de Business Associate couvre également les **sous-traitants ultérieurs (subcontractors)** d'un Business Associate — un prestataire cloud utilisé par un Business Associate lui-même prestataire d'une entité couverte devient à son tour un Business Associate, avec les mêmes obligations directes envers l'OCR, formant une chaîne de responsabilité qui rappelle directement la sous-traitance en cascade déjà développée dans le parcours RGPD de cette plateforme (article 28.4).

## Le contrat obligatoire : le Business Associate Agreement (BAA)

Toute relation entre une entité couverte et un Business Associate — et, de la même manière, entre un Business Associate et son propre sous-traitant — doit être formalisée par un **Business Associate Agreement (BAA)**, un contrat dont le contenu minimal est précisément défini par la réglementation, à l'image du contenu contractuel minimal déjà développé pour l'article 28 du RGPD, les clauses minimales de DORA, ou l'obligation contractuelle de l'exigence 12 de PCI DSS, tous développés dans les parcours précédents de cette plateforme.

## Le contenu minimal d'un BAA

Un BAA doit notamment prévoir que le Business Associate :

- n'utilise ou ne divulgue les PHI que dans les limites permises par le contrat ou exigées par la loi,
- mette en œuvre des **sauvegardes appropriées** pour prévenir toute utilisation ou divulgation non autorisée des ePHI, en cohérence avec la Security Rule déjà développée au module 2,
- signale à l'entité couverte toute utilisation ou divulgation non autorisée, y compris toute **violation de données** dont il aurait connaissance (un point qui prépare directement la règle de notification des violations développée au module 4 de ce parcours),
- s'assure que tout sous-traitant auquel il fournit des PHI accepte, par contrat, les mêmes restrictions et conditions,
- mette les PHI à disposition pour permettre à l'entité couverte de répondre aux demandes d'exercice des droits des patients déjà développées au module 1,
- mette à disposition ses livres et dossiers pour permettre à l'entité couverte, ou au HHS, de vérifier sa conformité,
- au terme du contrat, retourne ou détruit les PHI, dans la mesure où cela est réalisable — une clause directement comparable à l'obligation similaire déjà rencontrée pour l'article 28.3 du RGPD, développée dans le parcours dédié de cette plateforme.

## Un point de vigilance propre au secteur de la santé : les fournisseurs cloud

L'essor de l'hébergement cloud des dossiers médicaux électroniques a soulevé une question spécifique, tranchée explicitement par le HHS : un fournisseur cloud qui héberge des ePHI pour le compte d'une entité couverte ou d'un autre Business Associate est lui-même un Business Associate, **même s'il n'accède jamais activement au contenu des données qu'il héberge** (un scénario dit de "no-view services", où le fournisseur ne fait que stocker des données chiffrées sans jamais les consulter). Cette clarification, comparable dans son esprit à l'inclusion explicite des fournisseurs cloud dans le périmètre des sous-traitants du RGPD, développée dans le parcours dédié de cette plateforme, empêche un fournisseur cloud de se soustraire à ses obligations HIPAA au seul motif qu'il n'exploite pas activement les données qu'il héberge.

## Ce que l'absence de BAA signifie concrètement

Une entité couverte qui confie des ePHI à un prestataire sans avoir conclu de BAA en bonne et due forme se trouve, à elle seule, en situation de manquement à la Security Rule — indépendamment de savoir si le prestataire respecte par ailleurs des pratiques de sécurité robustes. C'est un point de vigilance fréquemment cité dans les accords de résolution de l'OCR développés au module 5 de ce parcours : l'absence de BAA constitue souvent un manquement identifié en parallèle de manquements plus substantiels, révélateur d'un dispositif de gouvernance des relations avec les prestataires insuffisamment structuré — un piège directement comparable à celui déjà signalé pour le contrat de sous-traitance du RGPD dans le parcours dédié de cette plateforme.
