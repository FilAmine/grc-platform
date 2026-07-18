# Validation de conformité (2/2) : le rôle du QSA et les scans ASV

## Le Qualified Security Assessor (QSA)

Un **Qualified Security Assessor (QSA)** est une personne physique ou un cabinet certifié directement par le PCI SSC pour réaliser des évaluations de conformité PCI DSS et produire des **Rapports de conformité (Report on Compliance — RoC)**, exigés pour les entités de Niveau 1 (module 3, leçon précédente). Cette certification, délivrée et retirée par le PCI SSC lui-même, joue un rôle comparable à l'accréditation d'un organisme de certification ISO 27001 par un organisme national d'accréditation, ou à l'accréditation d'un cabinet d'audit SOC 2 selon les normes de l'AICPA, déjà développées dans les parcours dédiés de cette plateforme — avec cette différence que l'accréditation des QSA relève entièrement du PCI SSC, un organisme privé sectoriel, sans intervention d'un organisme d'accréditation national indépendant.

## Le contenu du Rapport de conformité (RoC)

Un RoC documente, exigence par exigence et sous-exigence par sous-exigence, la méthode d'évaluation utilisée par le QSA, les preuves examinées, et la conclusion de conformité ou de non-conformité — une structure de preuve directement comparable au Rapport d'Évaluation de Sécurité (SAR) du NIST RMF ou aux sections d'un rapport SOC 2 détaillant les tests réalisés et leurs résultats, déjà développés dans les parcours précédents de cette plateforme. Un RoC valide généralement pour une période de douze mois, après quoi une nouvelle évaluation complète doit être réalisée — un cycle annuel plus fréquent que le cycle triennal de certification ISO 27001 déjà développé dans le parcours dédié de cette plateforme, mais cohérent avec le rythme des audits de surveillance annuels de ce même référentiel.

## Le rôle de l'Internal Security Assessor (ISA)

Le PCI SSC propose également une certification **Internal Security Assessor (ISA)**, destinée au personnel interne d'une grande organisation, lui permettant de réaliser certaines évaluations de conformité en interne plutôt que de recourir systématiquement à un QSA externe — une possibilité qui recoupe, dans son esprit, le recours à des testeurs internes autorisé pour le programme de tests de base de DORA (sous conditions d'indépendance), déjà développé dans le parcours dédié de cette plateforme, bien que le RoC formel destiné aux marques de cartes pour les entités de Niveau 1 nécessite généralement malgré tout la signature d'un QSA externe.

## L'Approved Scanning Vendor (ASV) et les scans trimestriels

L'exigence 11 (module 1) impose des **scans de vulnérabilités externes trimestriels**, réalisés obligatoirement par un **Approved Scanning Vendor (ASV)** — un prestataire spécifiquement accrédité par le PCI SSC pour réaliser ce type de scan selon une méthodologie standardisée. Contrairement à un scan de vulnérabilités interne (qui peut être réalisé par les équipes de l'entité elle-même ou un outil interne), le scan externe ASV doit systématiquement produire un résultat **conforme (passing scan)** — sans vulnérabilité critique non corrigée — pour que l'entité reste en conformité continue, indépendamment du cycle annuel de RoC ou de SAQ.

Cette exigence de scan trimestriel, bien plus fréquente que le cycle annuel d'évaluation globale, illustre un principe déjà rencontré à travers plusieurs référentiels de cette plateforme : la conformité à un instant T (le RoC ou le SAQ annuel) ne suffit jamais à garantir une sécurité réelle et continue — un principe de surveillance continue entre deux évaluations formelles, comparable dans son esprit à la surveillance continue déjà développée dans les parcours NIST RMF et ISO 27001 de cette plateforme.

## L'attestation de conformité (AoC)

À l'issue d'un RoC ou d'un SAQ, l'entité (ou le QSA pour un RoC) produit une **Attestation de conformité (Attestation of Compliance — AoC)** — un document résumé, plus court que le RoC ou le SAQ complet, destiné à être transmis à l'acquéreur de l'entité et, potentiellement, à ses propres clients qui souhaiteraient vérifier son statut de conformité. Cette AoC joue, pour PCI DSS, un rôle assez proche du rapport SOC 3 déjà développé dans le parcours dédié de cette plateforme : un document simplifié et diffusable, distinct du rapport complet et détaillé réservé à un usage restreint (le RoC ou le SAQ lui-même).

## Ce qui distingue ce dispositif des mécanismes de preuve déjà étudiés dans cette plateforme

Le dispositif de validation de PCI DSS combine des éléments déjà rencontrés séparément dans d'autres référentiels de cette plateforme — l'audit par un tiers accrédité (comme ISO 27001 ou SOC 2), l'auto-évaluation (rappelant, dans son principe, le CIS Controls Self Assessment Tool déjà développé dans le parcours dédié), et une surveillance continue par scan automatisé (rappelant les outils de Cloud Security Posture Management déjà évoqués dans le premier parcours de cette plateforme) — dans un seul et même dispositif gradué selon le niveau de risque de l'entité, une architecture de preuve qui reflète bien la nature hybride et pragmatique de ce référentiel né d'un consortium industriel plutôt que d'un texte de loi ou d'une norme de management générique.
