# Atelier 4 : les scénarios opérationnels

## Descendre du stratégique au technique

Les scénarios stratégiques construits à l'Atelier 3 (module précédent) décrivent un chemin d'attaque plausible à un niveau encore relativement abstrait — quelles parties prenantes de l'écosystème sont impliquées, dans quel ordre. L'Atelier 4 traduit chacun de ces scénarios stratégiques en un ou plusieurs **scénarios opérationnels**, qui détaillent précisément les **modes opératoires techniques** que la source de risque emploierait réellement à chaque étape du chemin d'attaque — le niveau de détail nécessaire pour qu'un architecte ou un ingénieur sécurité puisse identifier des mesures de protection techniques concrètes.

## La structure d'un scénario opérationnel

Un scénario opérationnel se présente typiquement sous une forme graphique proche d'un enchaînement d'étapes techniques (souvent représenté comme un graphe d'attaque), détaillant par exemple : la méthode d'accès initial (hameçonnage ciblé, exploitation d'une vulnérabilité non corrigée, compromission d'un compte de prestataire déjà identifié à l'Atelier 3), les techniques de progression au sein du système d'information (élévation de privilèges, mouvement latéral, découverte des systèmes critiques), et enfin les actions sur l'objectif (exfiltration de données, chiffrement à des fins d'extorsion, sabotage).

Cette structuration en étapes techniques successives rappelle directement, dans son principe, un modèle de "chaîne de frappe" (kill chain) ou les techniques et procédures répertoriées par des référentiels comme MITRE ATT&CK — une base de connaissance largement utilisée dans l'industrie pour cataloguer les techniques d'attaque réellement observées, et de plus en plus mobilisée en complément d'EBIOS RM pour enrichir la précision technique des scénarios opérationnels avec des techniques documentées et récurrentes plutôt qu'imaginées de façon purement théorique.

## L'évaluation de la vraisemblance

Chaque scénario opérationnel fait l'objet d'une évaluation de sa **vraisemblance** — la probabilité qu'il se matérialise réellement, compte tenu des capacités de la source de risque concernée (déjà évaluées à l'Atelier 2) et des mesures de sécurité déjà en place (issues du socle de sécurité de l'Atelier 1, ou de mesures spécifiques déjà mises en œuvre). Cette évaluation de vraisemblance, combinée à la gravité des événements redoutés déjà déterminée à l'Atelier 1, permet de situer chaque risque sur une grille de criticité — l'équivalent, dans le vocabulaire d'EBIOS RM, de la cotation probabilité/impact déjà rencontrée à travers l'ensemble des méthodologies de gestion des risques étudiées dans cette plateforme (ISO 31000, le NIST RMF, la classification des incidents de DORA).

## Un exemple concret de scénario opérationnel

Reprenons le scénario stratégique du module précédent (compromission d'un prestataire de maintenance, puis progression vers les systèmes critiques). Sa traduction en scénario opérationnel pourrait détailler : hameçonnage ciblé d'un technicien du prestataire de maintenance pour obtenir ses identifiants d'accès à distance, utilisation de ces identifiants légitimes pour se connecter au réseau de l'organisation cible sans déclencher d'alerte immédiate (un accès qui apparaît normal puisqu'il utilise un compte autorisé), exploitation d'une segmentation réseau insuffisante pour progresser depuis le point d'entrée du prestataire jusqu'aux serveurs hébergeant les valeurs métier critiques, puis déploiement d'un rançongiciel sur ces serveurs. Ce niveau de détail permet d'identifier des mesures de protection très concrètes — authentification multifacteur pour les accès des prestataires, segmentation réseau stricte entre les accès tiers et les systèmes critiques, détection des comportements anormaux même sur des comptes légitimes — bien plus précises que ce que le seul scénario stratégique de haut niveau aurait permis d'identifier.

## Le lien avec le threat modeling déjà développé dans cette plateforme

Cette démarche de scénario opérationnel rejoint directement, dans son esprit, le threat modeling STRIDE déjà développé dans le module Security by Design du premier parcours de cette plateforme — les deux approches cherchent à décomposer un chemin d'attaque en étapes techniques précises pour en déduire des contre-mesures concrètes. La différence structurante réside dans le point de départ : STRIDE part généralement d'un système ou d'une architecture donnée et en examine méthodiquement les frontières de confiance, tandis qu'un scénario opérationnel EBIOS RM part d'une source de risque et d'un objectif déjà identifiés et priorisés (Atelier 2), en passant explicitement par l'écosystème (Atelier 3) — deux angles d'approche complémentaires plutôt que concurrents, qui peuvent d'ailleurs être combinés dans une même démarche de sécurité globale.

## Comment ces scénarios alimentent l'atelier final

L'ensemble des scénarios opérationnels, avec leur évaluation de vraisemblance et leur gravité associée, ainsi que les écarts au socle de sécurité déjà identifiés à l'Atelier 1, constituent la matière première complète du dernier atelier de la méthode — l'Atelier 5, développé dans le module suivant de ce parcours, qui synthétise l'ensemble de ces risques et décide de leur traitement.
