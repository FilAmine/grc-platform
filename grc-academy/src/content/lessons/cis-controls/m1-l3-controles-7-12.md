# Les 18 contrôles (2/3) : contrôles 7 à 12 — le durcissement opérationnel

## Contrôle 7 — Gestion continue des vulnérabilités

Développer un plan pour évaluer et suivre en continu les vulnérabilités sur l'ensemble des actifs de l'entreprise, afin de remédier et de minimiser la fenêtre d'opportunité pour les attaquants. Les Safeguards précisent des cadences concrètes — établir un processus de gestion des vulnérabilités documenté, réaliser des scans automatisés selon une fréquence adaptée à la criticité des actifs, et corriger en priorité les vulnérabilités exploitées activement (une notion directement liée au renseignement sur les menaces, développé dans les parcours NIST CSF et ISO 27001 de cette plateforme comme threat intelligence). Ce contrôle recoupe directement le contrôle RA-5 de SP 800-53 déjà développé dans le parcours NIST RMF de cette plateforme.

## Contrôle 8 — Gestion des journaux d'audit

Collecter, alerter, revoir et conserver les journaux d'audit des événements qui pourraient aider à détecter, comprendre ou se remettre d'une attaque. Ce contrôle recoupe directement la famille AU (Audit and Accountability) de SP 800-53 et le contrôle 8.15 (journalisation) de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme — avec, comme pour ces deux référentiels, une insistance particulière des Safeguards sur la **revue effective** des journaux collectés, et pas seulement leur accumulation passive, un piège déjà signalé à plusieurs reprises dans cette plateforme.

## Contrôle 9 — Protections de la messagerie et du navigateur web

Améliorer les protections et la détection des menaces provenant des vecteurs de messagerie électronique et de navigation web, qui offrent aux attaquants des opportunités de manipuler le comportement humain via un engagement direct. Ce contrôle reconnaît explicitement que la messagerie et le navigateur restent, dans la pratique, les deux vecteurs d'entrée les plus fréquemment exploités pour un accès initial (hameçonnage, téléchargement de contenu malveillant) — un contrôle qui n'a pas d'équivalent aussi ciblé et nommé explicitement dans ISO 27001 ou le NIST CSF, où ce sujet reste généralement dilué dans des contrôles plus génériques de sensibilisation et de protection contre les logiciels malveillants.

## Contrôle 10 — Défenses contre les logiciels malveillants

Empêcher ou contrôler l'installation, la propagation et l'exécution d'applications, de code ou de scripts malveillants sur les actifs de l'entreprise. Ce contrôle recoupe directement le contrôle SI-3 de SP 800-53 et le contrôle 8.7 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme.

## Contrôle 11 — Récupération des données

Établir et maintenir des pratiques de récupération des données suffisantes pour restaurer les actifs de l'entreprise dans leur état antérieur à un incident de sécurité fiable et connu. Un point directement lié aux exigences de sauvegarde et de test de restauration déjà rencontrées à plusieurs reprises dans cette plateforme (contrôle 8.13 d'ISO 27001, critère A1.3 de SOC 2, famille CP de SP 800-53) — les CIS Controls insistent, comme ces autres référentiels, sur le **test régulier** de la capacité de restauration, pas seulement l'existence théorique de sauvegardes.

## Contrôle 12 — Gestion de l'infrastructure réseau

Établir, mettre en œuvre et gérer activement (suivre, rapporter, corriger) les dispositifs réseau, afin d'empêcher les attaquants d'exploiter des services et des points d'accès réseau vulnérables. Les Safeguards couvrent notamment la maintenance d'une architecture réseau à jour et documentée, la sécurisation des dispositifs d'infrastructure réseau eux-mêmes (routeurs, commutateurs, pare-feux) selon des configurations durcies, et la centralisation de l'authentification et de l'autorisation pour l'accès à l'infrastructure réseau — un socle qui recoupe directement le contrôle SC-7 de SP 800-53 et le contrôle 8.20 de l'Annexe A d'ISO 27001 (segmentation réseau), déjà développés dans les parcours précédents de cette plateforme.

## Ce que ce deuxième bloc de contrôles révèle

Contrairement au premier bloc (contrôles 1 à 6, largement centré sur la connaissance et la maîtrise de ce que l'organisation possède), ce deuxième bloc de contrôles est tourné vers le **durcissement opérationnel actif** : réduire la surface d'attaque exploitable (vulnérabilités, configuration réseau), se prémunir contre les vecteurs d'attaque les plus fréquents (messagerie, navigateur, logiciels malveillants), et garantir une capacité de récupération en cas d'incident malgré tout survenu. C'est dans ce bloc que l'insistance du référentiel sur des données réelles d'attaque (développée dans l'introduction de ce parcours via le Community Defense Model) se manifeste le plus concrètement : chacun de ces six contrôles cible un vecteur d'attaque documenté et fréquemment observé, plutôt qu'une catégorie de risque théorique.
