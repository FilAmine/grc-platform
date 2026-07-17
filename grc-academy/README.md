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
cours de [`src/content/courses/*.ts`](src/content/courses). Chaque cours référence des leçons Markdown dans
[`src/content/lessons/<slug-du-cours>/*.md`](src/content/lessons). Quatre parcours à ce jour :

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

Pour ajouter un nouveau parcours : créer un dossier de leçons Markdown, un fichier `src/content/courses/monCours.ts`
qui les assemble en `Course`, et l'ajouter au tableau `courses` de `catalog.ts`.

La progression (leçons marquées comme terminées) est stockée en local (`localStorage`, clé par cours/module/leçon),
sans backend ni compte utilisateur.
