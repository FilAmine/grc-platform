# La Déclaration d'Applicabilité (SoA) en profondeur

## Le document le plus scruté par un auditeur de certification

La Déclaration d'Applicabilité — **Statement of Applicability**, exigée par la clause 6.1.3(d) — est le document qui relie l'analyse de risque propre à l'organisme (clause 6.1.2) aux 93 contrôles de référence de l'Annexe A. C'est presque toujours le premier document qu'un auditeur de certification examine en détail, car il condense en un seul tableau la logique entière de la démarche.

## Ce que la SoA doit contenir pour chacun des 93 contrôles

1. **Si le contrôle est retenu ou exclu**, sans ambiguïté.
2. **La justification de l'inclusion ou de l'exclusion** — jamais une case cochée sans motivation. Une exclusion doit s'appuyer sur l'analyse de risque : par exemple, le contrôle 7.14 (mise au rebut sécurisée du matériel) peut être exclu si l'organisme n'opère que dans un environnement entièrement cloud sans aucun matériel physique propre — à condition que cette absence de matériel soit elle-même documentée et vérifiable.
3. **L'état de mise en œuvre** — le contrôle est-il déjà en place, en cours de déploiement, ou seulement planifié.
4. **Une référence vers la documentation ou la preuve** qui démontre la mise en œuvre effective — politique associée, procédure, configuration technique, ticket de mise en œuvre.

## L'erreur la plus fréquente : la SoA comme point de départ

Un piège classique, en particulier pour une organisation qui découvre ISO 27001, consiste à partir directement de la liste des 93 contrôles de l'Annexe A et à cocher ceux qu'elle applique déjà — en traitant la SoA comme une checklist à remplir. C'est l'inverse de la logique voulue par la norme : la SoA doit être la **conséquence** d'une analyse de risque réelle (clause 6.1.2) menée sur le domaine d'application défini (clause 4.3), pas son point de départ. Un auditeur expérimenté détecte rapidement une SoA "à l'envers" : les contrôles retenus ne correspondent à aucun risque identifié dans le registre de risques, ou pire, des risques significatifs identifiés dans le registre ne trouvent aucun contrôle correspondant dans la SoA.

## Une exclusion n'est jamais gratuite

Exclure un contrôle de la SoA reste possible et parfaitement légitime — la norme elle-même prévoit cette flexibilité — mais chaque exclusion doit répondre à une question simple et documentée : **quel risque couvre normalement ce contrôle, et pourquoi ce risque n'existe pas (ou est traité autrement) dans le contexte spécifique de cet organisme ?** Des exclusions groupées sans justification individuelle spécifique ("non applicable" répété sans explication pour plusieurs contrôles consécutifs) sont un signal d'alerte classique en audit, souvent révélateur d'une SoA rédigée rapidement en fin de projet plutôt qu'issue d'un travail d'analyse réel.

## La SoA comme document vivant

Comme le reste du SMSI, la SoA n'est jamais figée après la certification initiale — elle doit être révisée :

- lorsque l'appréciation des risques est mise à jour (clause 8.2, à intervalles planifiés ou lors de changements significatifs),
- lorsqu'un nouveau système ou processus entre dans le domaine d'application,
- lorsqu'un contrôle auparavant exclu devient nécessaire (par exemple, un organisme purement cloud qui ouvre un centre de données propre doit réintégrer les contrôles physiques auparavant exclus).

## Un exemple concret d'entrée de SoA bien rédigée

Pour illustrer le niveau de détail attendu, une entrée de SoA correctement documentée pour le contrôle **8.24 (utilisation de la cryptographie)** pourrait ressembler à : *"Retenu. Risque associé : divulgation de données clients stockées dans l'environnement cloud de production (risque R-014 du registre des risques). Mise en œuvre : chiffrement AES-256 au repos activé par défaut sur l'ensemble des volumes de stockage et bases de données du domaine d'application, géré via le service de gestion de clés du fournisseur cloud ; TLS 1.2 minimum imposé pour tous les flux en transit, y compris entre services internes. Preuve : politique de chiffrement PC-007 v3, configuration Terraform du module de stockage, revue trimestrielle de conformité aux CIS Benchmarks."*

Cette formulation relie explicitement le contrôle, le risque qu'il traite, sa mise en œuvre technique concrète, et la preuve documentaire disponible — exactement la structure qu'un auditeur cherchera à vérifier, contrôle par contrôle, lors de l'audit de certification développé dans le module suivant.
