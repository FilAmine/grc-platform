# GRC Academy

Application web autonome de formation : GRC (gouvernance, risque, conformité) et Security by Design (privacy, cloud).

Indépendante du reste de `grc-platform` — pas de dépendance à son backend, son auth ou sa base de données. Stack : React + TypeScript + Vite + MUI + react-router-dom, contenu en Markdown.

## Démarrer

```bash
cd grc-academy
npm install
npm run dev
```

Ouvre http://localhost:5183

### Avec Docker

```bash
docker compose up --build grc-academy
```

Ouvre http://localhost:3100 (service défini dans le `docker-compose.yml` racine — build multi-stage Node → nginx, comme `frontend/`, sans dépendance aux autres services).

## Contenu

Le catalogue de parcours est défini dans [`src/content/catalog.ts`](src/content/catalog.ts), qui assemble les
métadonnées des cours de [`src/content/courses/*.ts`](src/content/courses) (titres, structure des modules/leçons —
statique, léger). Le texte de chaque leçon vit dans un fichier séparé sous
[`src/content/courses/content/*Content.ts`](src/content/courses/content), qui importe les fichiers
[`src/content/lessons/<slug-du-cours>/*.md`](src/content/lessons) et est chargé à la demande via
[`src/content/contentLoaders.ts`](src/content/contentLoaders.ts) — chaque cours n'ajoute ainsi qu'un chunk JS
séparé, chargé uniquement à l'ouverture d'une de ses leçons, plutôt que de faire grossir le bundle principal.
Dix-sept parcours à ce jour :

- **Fondamentaux GRC & Security by Design** (7 modules, 18 leçons) — gouvernance/risque/conformité, ISO 27001,
  NIST CSF, SOC 2, RGPD, Security by Design, Privacy by Design, sécurité cloud.
- **NIST Cybersecurity Framework 2.0 — Guide complet** (5 modules, 11 leçons) — origines et philosophie, les six
  fonctions du Core (Govern, Identify, Protect, Detect, Respond, Recover), structure du Core, Tiers, Profils,
  mise en œuvre en sept étapes, mapping avec les autres référentiels et gestion des risques fournisseurs.
- **ISO/IEC 27001 en profondeur** (9 modules, 13 leçons) — les clauses 4 à 10 du SMSI en détail, les 93 contrôles
  de l'Annexe A 2022 organisés par thème (organisationnels, personnes, physiques, technologiques), la Déclaration
  d'Applicabilité, le processus de certification (Stage 1/2, surveillance, recertification) et le maintien du
  SMSI dans la durée.
- **SOC 2 en profondeur** (8 modules, 11 leçons) — les Common Criteria (CC1 à CC9) alignés sur le référentiel
  COSO, les cinq catégories de Trust Services Criteria (Sécurité, Disponibilité, Intégrité de traitement,
  Confidentialité, Vie privée), le déroulement de l'audit et les types d'opinion, l'anatomie complète du rapport,
  la préparation d'un audit, et la distinction avec SOC 1/SOC 3.
- **RGPD en profondeur** (8 modules, 13 leçons) — champ d'application territorial et les six bases légales, les
  droits des personnes concernées en détail procédural, la relation responsable de traitement/sous-traitant et
  le rôle du DPO, la sécurité du traitement et la notification des violations (72h), le registre des traitements
  et l'AIPD, les transferts internationaux (Schrems I/II, Data Privacy Framework), la gouvernance des autorités
  de contrôle et les sanctions.
- **NIST RMF en profondeur** (7 modules, 12 leçons) — origines dans la FISMA, les sept étapes du processus
  d'autorisation (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor), le catalogue de contrôles
  SP 800-53 et ses familles clés, les rôles nommément désignés (Authorizing Official, ISSO, SAISO...), FedRAMP,
  et l'intégration de la vie privée et de la gestion des risques de la chaîne d'approvisionnement.
- **CIS Controls en profondeur** (6 modules, 11 leçons) — origines (Consensus Audit Guidelines, SANS Top 20), les
  18 contrôles et leurs 153 Safeguards, le système de priorisation par Implementation Groups (IG1/IG2/IG3),
  l'écosystème CIS (Benchmarks, CIS RAM), le mapping avec les autres référentiels, et une feuille de route de
  première adoption.
- **NIS2 en profondeur** (8 modules, 11 leçons) — champ d'application élargi (secteurs des Annexes I/II, entités
  essentielles/importantes, seuils et juridiction), les dix domaines de mesures de l'article 21, la responsabilité
  personnelle des organes de direction (article 20), la notification des incidents en plusieurs paliers
  (24h/72h/1 mois), le régime différencié de supervision et les sanctions, la coopération européenne, et le
  mapping avec le RGPD, DORA et les référentiels techniques.
- **DORA en profondeur** (7 modules, 11 leçons) — règlement vs directive, le cadre de gestion des risques liés aux
  TIC aligné sur le NIST CSF et la responsabilité de l'organe de direction (article 5), la classification et la
  notification des incidents majeurs, les tests de résilience dont les tests de pénétration fondés sur la menace
  (TLPT, héritage de TIBER-EU), la gestion des risques liés aux prestataires tiers et le régime de supervision
  directe des prestataires TIC critiques (Lead Overseer, astreintes), le partage d'informations et les sanctions
  (renvoyées au droit national), et le mapping avec NIS2 (lex specialis), le RGPD et ISO 27001/NIST CSF.
- **PCI DSS en profondeur** (8 modules, 11 leçons) — origine contractuelle (PCI SSC, marques de cartes) plutôt que
  légale, les douze exigences en détail, le scoping et la segmentation réseau comme leviers de réduction de
  périmètre, les niveaux de validation et types de SAQ, le rôle du QSA et des scans ASV, l'approche personnalisée
  et l'analyse de risque ciblée (v4.0), la protection du PAN et l'interdiction de conservation des SAD, et le
  régime de sanctions contractuelles (sans plafond réglementaire, jusqu'à la révocation du droit d'accepter les
  paiements).
- **COBIT en profondeur** (8 modules, 11 leçons) — un cadre de gouvernance et de gestion de l'IT dans son ensemble
  plutôt qu'un référentiel de sécurité, la distinction gouvernance/management et la cascade des objectifs, les
  cinq domaines et quarante objectifs (EDM/APO/BAI/DSS/MEA), les sept composants génériques, les facteurs de
  conception et Focus Areas, le modèle de niveaux de capacité aligné sur CMMI, et la position de COBIT comme
  cadre-cible au-dessus d'ISO 27001/ITIL/PMI et des autres référentiels déjà étudiés.
- **HIPAA en profondeur** (7 modules, 11 leçons) — la loi fédérale américaine sur les données de santé : entités
  couvertes/Business Associates, la Privacy Rule (triptyque Treatment/Payment/Healthcare Operations, minimum
  nécessaire, droits des patients), la Security Rule (sauvegardes administratives/physiques/techniques, l'analyse
  de risque comme exigence la plus citée par l'OCR, le mécanisme Required/Addressable), le contrat obligatoire
  avec les Business Associates (BAA), la Breach Notification Rule (évaluation en quatre facteurs, délai de 60
  jours), les sanctions civiles graduées et pénales, les méthodes de dé-identification (Safe Harbor, Expert
  Determination), et le mapping avec le RGPD et les référentiels techniques.
- **ANSSI et EBIOS RM en profondeur** (8 modules, 11 leçons) — l'agence française de cybersécurité (missions,
  CERT-FR, le régime OIV/LPM comme précurseur de NIS2) et sa méthode de gestion des risques par scénarios : les
  cinq ateliers d'EBIOS RM (cadrage/valeurs métier/socle de sécurité, sources de risque et objectifs visés,
  scénarios stratégiques et cartographie de l'écosystème comme vecteur d'attaque, scénarios opérationnels,
  traitement du risque et PACS), l'écosystème de qualifications ANSSI (PASSI, PDIS, PRIS, SecNumCloud, CSPN), et
  le mapping avec ISO 31000/27005 et le NIST RMF.
- **ITIL en profondeur** (8 modules, 11 leçons) — complément opérationnel naturel de COBIT : le Service Value
  System et les quatre dimensions de la gestion des services, les sept principes directeurs, la chaîne de valeur
  des services et les flux de valeur, les 34 pratiques (gestion des incidents/problèmes, centre de services,
  gestion des demandes), la facilitation des changements (Change Enablement, CAB), la gestion des niveaux de
  service, le modèle d'amélioration continue, et le mapping avec COBIT/ISO 20000/DevOps.
- **SOX en profondeur** (8 modules, 11 leçons) — le Sarbanes-Oxley Act américain né des scandales Enron/WorldCom et
  la création du PCAOB, la certification personnelle et pénale des dirigeants (sections 302 et 906), la section
  404 et l'évaluation du contrôle interne sur le reporting financier (ICFR) structurée par le référentiel COSO,
  les quatre domaines de contrôles généraux informatiques (ITGC) et la séparation des tâches, la classification
  des déficiences de contrôle (déficience/déficience significative/faiblesse matérielle), les rôles de gouvernance
  (comité d'audit, audit interne, auditeur externe, PCAOB, protection des lanceurs d'alerte), le rôle des rapports
  SOC 1 pour les processus financiers externalisés, et le mapping avec COBIT/ISO 27001/ITIL et le régime de
  sanctions (civiles, pénales, disciplinaires).
- **FedRAMP en profondeur** (8 modules, 11 leçons) — le programme fédéral américain d'autorisation des fournisseurs
  cloud né du principe « do once, use many times » : la catégorisation par niveaux d'impact (Faible/Modéré/Élevé/
  LI-SaaS) et les bases de référence de contrôles adaptées au cloud, les deux voies d'autorisation (Agence et
  FedRAMP Board avec sa P-ATO), les acteurs de l'écosystème et le rôle central du 3PAO, la surveillance continue
  mensuelle et la gestion du POA&M, le FedRAMP Marketplace et le principe de réciprocité, les programmes
  apparentés (StateRAMP, les niveaux d'impact du Department of Defense), et le mapping avec le NIST RMF/ISO
  27001/SOC 2.
- **TISAX en profondeur** (8 modules, 11 leçons) — le dispositif contractuel de l'industrie automobile européenne
  (VDA, ENX Association) né de la volonté de mutualiser les audits entre OEM et fournisseurs : le catalogue VDA
  ISA et son modèle de maturité à six niveaux (0 à 5), les niveaux d'évaluation (AL1/AL2/AL3) et les trois
  objectifs d'évaluation modulaires (sécurité de l'information, protection des prototypes, protection des
  données), le rôle des Audit Providers accrédités par l'ENX Association, le partage des labels par consentement
  explicite et leur validité triennale, le module unique de protection des prototypes, l'absence de sanction
  légale directe compensée par la sanction commerciale de la perte d'accès au marché, et le mapping avec ISO
  27001/PCI DSS/RGPD.

Pour ajouter un nouveau parcours : créer un dossier de leçons Markdown, un fichier `src/content/courses/monCours.ts`
avec les métadonnées (`Course` sans texte de leçon), un fichier `src/content/courses/content/monCoursContent.ts`
avec les imports `?raw` et la table `CourseContent`, puis l'enregistrer dans `catalog.ts` et `contentLoaders.ts`.

La progression (leçons marquées comme terminées) est stockée en local (`localStorage`, clé par cours/module/leçon),
sans backend ni compte utilisateur.
