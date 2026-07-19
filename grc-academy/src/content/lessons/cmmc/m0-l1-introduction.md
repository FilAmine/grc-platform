# CMMC en profondeur : introduction et repères

## Un problème déjà rencontré, mais pour le marché fédéral de la défense plutôt que civil

Le parcours FedRAMP de cette plateforme a déjà développé un programme fédéral américain d'autorisation des fournisseurs cloud pour les besoins des agences civiles. Le **Cybersecurity Maturity Model Certification (CMMC)** répond à un problème structurellement analogue, mais pour un public entièrement différent : les dizaines de milliers d'entreprises, des plus grands industriels de défense jusqu'aux plus petits sous-traitants, qui composent la **base industrielle de défense (Defense Industrial Base — DIB)** américaine et manipulent, à ce titre, des informations non classifiées contrôlées (Controlled Unclassified Information — CUI) pour le compte du Department of Defense.

## L'échec du modèle d'auto-attestation pure qui a précédé CMMC

Avant la création de CMMC, les contractants de la défense devaient simplement **s'auto-attester** de leur conformité au catalogue de contrôles NIST SP 800-171, développé en détail au module 2 de ce parcours, sans qu'aucune vérification indépendante ne soit systématiquement exigée — un modèle d'auto-déclaration sans corroboration qui rappelle directement celui déjà signalé comme insuffisant pour SWIFT CSP à ses débuts, avant le renforcement vers une exigence de corroboration indépendante, développé dans le parcours dédié de cette plateforme. Cette auto-attestation non vérifiée s'est révélée structurellement défaillante : plusieurs incidents majeurs de perte de propriété intellectuelle militaire sensible, provenant de sous-traitants ayant déclaré une conformité qui ne correspondait pas à leur réalité opérationnelle, ont directement motivé la création de CMMC à partir de 2019.

## Un dispositif de vérification à plusieurs niveaux, plutôt qu'une simple déclaration

CMMC introduit ainsi, en réponse directe à cet échec, un dispositif structuré de **trois niveaux de certification** (développés au module 1 de ce parcours), avec des voies d'évaluation variables selon la sensibilité des informations traitées — de la simple auto-évaluation à l'évaluation par un organisme tiers accrédité, développées au module 3 de ce parcours — un principe de gradation de la rigueur d'évaluation en fonction du besoin de protection déjà rencontré à de multiples reprises dans cette plateforme, notamment pour les niveaux d'évaluation AL1/AL2/AL3 de TISAX ou les niveaux d'impact de FedRAMP.

## La gouvernance du programme : le Cyber-AB sous la supervision du DoD

CMMC est administré par le **Cyber-AB (Cyber Accreditation Body)**, un organisme à but non lucratif chargé d'accréditer les évaluateurs tiers du programme, sous la supervision globale du Department of Defense — une architecture de gouvernance qui rappelle directement celle déjà développée pour le FedRAMP PMO dans le parcours dédié de cette plateforme, avec une différence notable : CMMC s'appuie sur un unique client fédéral (le DoD et l'ensemble de ses composantes) plutôt que sur la pluralité d'agences civiles fédérales desservies par FedRAMP.

## Pourquoi ce parcours complète directement FedRAMP dans cette plateforme

Un fournisseur technologique d'envergure servant à la fois des agences civiles américaines et le Department of Defense doit fréquemment satisfaire simultanément FedRAMP et CMMC — deux dispositifs distincts, gérés par des organismes différents, mais partageant une même origine (la nécessité de sécuriser la chaîne d'approvisionnement du gouvernement fédéral américain) et de nombreux principes méthodologiques communs, développés tout au long de ce parcours. Cette complémentarité rappelle directement celle déjà observée pour la coexistence d'ISO 27001, SOC 2 et FedRAMP chez un même fournisseur cloud international, développée dans le parcours FedRAMP de cette plateforme.

## Ce que ce parcours couvre

Ce parcours développe les trois niveaux de CMMC 2.0 (module 1), le catalogue de pratiques NIST SP 800-171 qui constitue le socle technique du niveau 2 (module 2), les voies d'évaluation — auto-évaluation, évaluation par un organisme tiers accrédité (C3PAO), et évaluation gouvernementale (module 3), le mécanisme du Plan of Action and Milestones et la certification conditionnelle (module 4), la cascade des exigences à travers la chaîne d'approvisionnement de la défense et le Supplier Performance Risk System (module 5), la clause contractuelle DFARS 252.204-7012 et la notification des incidents (module 6), et enfin le mapping avec FedRAMP, le NIST RMF et les autres référentiels déjà étudiés dans cette plateforme ainsi qu'une feuille de route de mise en conformité (module 7).
