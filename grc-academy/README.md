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

## Contenu

Le parcours pilote "Fondamentaux GRC & Security by Design" (7 modules, 18 leçons) est défini dans
[`src/content/course.ts`](src/content/course.ts), avec le texte de chaque leçon dans
[`src/content/lessons/*.md`](src/content/lessons). Pour ajouter un nouveau parcours, dupliquer ce
pattern (module/leçons Markdown + entrée dans une structure `Course`).

La progression (leçons marquées comme terminées) est stockée en local (`localStorage`), sans backend ni compte utilisateur.
