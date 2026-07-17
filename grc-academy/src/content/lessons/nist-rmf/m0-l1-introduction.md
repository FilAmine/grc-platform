# NIST RMF en profondeur : introduction et repères

## Un référentiel bien distinct du NIST CSF, malgré le nom commun

Le deuxième parcours de cette plateforme a couvert le **NIST Cybersecurity Framework (CSF) 2.0** — un cadre volontaire, orienté résultats, pensé pour toute organisation quel que soit son secteur. Le **NIST RMF (Risk Management Framework)**, objet de ce parcours, est un référentiel bien plus ancien, bien plus prescriptif, et conçu dans un contexte différent : celui des systèmes d'information fédéraux américains soumis à une obligation légale de conformité. Confondre les deux référentiels sous prétexte qu'ils portent tous deux le sigle "NIST" est une erreur fréquente qu'il convient de dissiper d'emblée.

## L'origine légale : la FISMA

Le RMF trouve sa source dans le **Federal Information Security Management Act (FISMA)** de 2002 (modifié en 2014 par le Federal Information Security Modernization Act, qui en a précisé et actualisé les dispositions), une loi fédérale américaine qui impose à chaque agence gouvernementale de mettre en place un programme de sécurité de l'information pour ses systèmes, avec une obligation de reporting annuel au Congrès. Contrairement au NIST CSF (volontaire) ou même à ISO 27001 (contractuel ou volontaire), l'application du RMF aux systèmes fédéraux américains découle directement d'une **obligation légale** — un système fédéral qui n'obtient pas d'autorisation d'exploitation dans le cadre du RMF ne peut, en principe, pas être mis en production.

## Des processus disparates à un cadre unifié

Avant l'unification du RMF, plusieurs processus de certification et d'accréditation coexistaient selon les administrations : le processus **NIACAP** (National Information Assurance Certification and Accreditation Process) pour les systèmes de sécurité nationale, et le **DIACAP** (DoD Information Assurance Certification and Accreditation Process) au ministère de la Défense. Le RMF, formalisé par le NIST dans la **Special Publication 800-37** (première édition en 2010, révision majeure **Rev. 2 en décembre 2018**), a progressivement remplacé et unifié ces processus disparates — y compris au ministère de la Défense, qui a adopté sa propre déclinaison du RMF (RMF for DoD IT) en 2014 en remplacement du DIACAP.

## La famille de publications qui structure le RMF

Contrairement à ISO 27001 (une norme unique complétée par ISO 27002) ou SOC 2 (un seul jeu de critères), le RMF s'appuie sur un **écosystème de publications NIST** distinctes, chacune couvrant une facette précise du processus — cette architecture modulaire est développée en détail au fil de ce parcours, mais mérite d'être présentée dès l'introduction :

- **SP 800-37 Rev. 2** — le document central qui décrit le processus RMF lui-même, en sept étapes (module 1).
- **FIPS 199** — la norme fédérale obligatoire qui définit la méthode de catégorisation de sécurité d'un système (module 1).
- **SP 800-60** — le guide qui aide à cartographier les types d'information traités vers les niveaux d'impact de FIPS 199.
- **FIPS 200** — la norme fédérale qui fixe les exigences de sécurité minimales, opérationnalisées par le choix d'une base de référence de contrôles.
- **SP 800-53 Rev. 5** — le catalogue détaillé des contrôles de sécurité et de vie privée, organisé en 20 familles (module 2).
- **SP 800-53B** — les bases de référence (baselines) de contrôles associées à chaque niveau d'impact (Faible, Modéré, Élevé).
- **SP 800-53A** — les procédures d'évaluation permettant de vérifier que chaque contrôle est effectivement mis en œuvre (module 1).
- **SP 800-30** — le guide méthodologique pour la conduite d'une appréciation des risques.
- **SP 800-137** — le guide de surveillance continue de la sécurité de l'information (ISCM), pertinent pour la dernière étape du RMF (module 1).

## Pourquoi le RMF reste pertinent bien au-delà des agences fédérales américaines

Bien que né d'une obligation légale propre au gouvernement fédéral américain, le RMF structure aujourd'hui des écosystèmes bien plus larges : les contractants de la Défense américaine, les fournisseurs de services cloud souhaitant héberger des charges de travail gouvernementales via le programme **FedRAMP** (développé au module 4), et plus largement toute organisation qui souhaite s'appuyer sur l'un des catalogues de contrôles les plus détaillés et les plus rigoureusement maintenus au monde (SP 800-53), y compris hors de tout contexte fédéral américain, en s'en inspirant comme référentiel de contrôles techniques.

## Ce que ce parcours couvre

Sept modules structurent ce parcours : les sept étapes du processus RMF en détail (module 1), le catalogue de contrôles SP 800-53 et ses familles clés (module 2), les rôles et responsabilités propres au RMF — Authorizing Official, ISSO, et les autres (module 3), la comparaison du RMF avec les autres référentiels déjà étudiés dans cette plateforme et son application concrète via FedRAMP (module 4), la vie privée et la gestion des risques de la chaîne d'approvisionnement au sein du RMF (module 5), et enfin la construction d'un dossier d'autorisation et une feuille de route réaliste (module 6).
