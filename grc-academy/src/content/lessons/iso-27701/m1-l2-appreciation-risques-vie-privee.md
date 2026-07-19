# L'architecture d'extension et le PIMS (2/2) : l'appréciation des risques spécifique à la vie privée

## Une seconde appréciation des risques, distincte de celle d'ISO 27001

ISO/IEC 27701 impose la conduite d'une **appréciation des risques spécifique à la vie privée (PIMS-specific risk assessment)**, distincte et complémentaire de l'appréciation des risques de sécurité de l'information déjà exigée par la clause 6.1.2 d'ISO 27001, développée dans le parcours dédié de cette plateforme. Cette distinction rejoint directement, et applique de façon très concrète à un contexte certifiable, celle déjà développée en détail dans le parcours NIST Privacy Framework de cette plateforme entre risque de sécurité (perte de confidentialité, d'intégrité ou de disponibilité) et risque vie privée (conséquences problématiques pour les personnes concernées, même en l'absence de toute faille de sécurité).

## Ce que cette appréciation évalue concrètement

Là où l'appréciation des risques d'ISO 27001 raisonne en termes d'actifs informationnels à protéger, l'appréciation des risques spécifique à la vie privée raisonne en termes de **conséquences pour les personnes physiques (PII principals)** dont les données sont traitées — le risque qu'un traitement de données, même parfaitement sécurisé, engendre une atteinte à la vie privée, une discrimination, ou tout autre préjudice pour la personne concernée. Cette approche centrée sur l'individu plutôt que sur l'organisation rejoint directement celle déjà développée pour la méthodologie d'appréciation du risque vie privée du NIST Privacy Framework, où le préjudice pour la personne concernée constitue une dimension distincte du seul risque pour l'organisation.

## Un double filtre de risque, plutôt qu'un simple ajout

Une organisation certifiée ISO/IEC 27701 applique ainsi, pour chaque traitement de données personnelles, un double filtre d'appréciation des risques : le filtre de sécurité de l'information (déjà développé dans ISO 27001) et le filtre spécifique à la vie privée développé dans cette leçon. Un traitement peut ainsi présenter un risque de sécurité faible (données correctement chiffrées, accès strictement contrôlé) tout en présentant un risque vie privée élevé (finalité disproportionnée, absence de base légale solide, collecte excessive au regard de l'objectif poursuivi) — une situation qui rappelle directement l'exemple déjà développé dans le parcours NIST Privacy Framework de cette plateforme d'un traitement parfaitement sécurisé mais néanmoins problématique du point de vue de la vie privée.

## Le lien direct avec l'analyse d'impact relative à la protection des données du RGPD

Cette appréciation des risques spécifique à la vie privée fournit une méthodologie structurée directement réutilisable pour satisfaire l'obligation d'**analyse d'impact relative à la protection des données (AIPD)** déjà développée en détail dans le parcours RGPD de cette plateforme — une organisation certifiée ISO/IEC 27701 dispose ainsi d'un processus documenté et régulièrement audité, qui peut alimenter directement le contenu substantiel d'une AIPD exigée par le RGPD pour tout traitement susceptible d'engendrer un risque élevé, plutôt que de conduire cet exercice de façon isolée et non structurée.

## Les facteurs propres à cette appréciation des risques

Cette appréciation des risques spécifique tient compte de facteurs propres à la vie privée que l'appréciation des risques de sécurité classique ne considère généralement pas — la nature particulièrement sensible de certaines catégories de données (santé, origine ethnique, opinions politiques, déjà développées comme catégories particulières dans le parcours RGPD de cette plateforme), le volume et la portée du traitement (un traitement à grande échelle touchant des millions de personnes présente un profil de risque différent d'un traitement limité à quelques dizaines de personnes), et le degré d'autonomie décisionnelle du traitement (un profilage entièrement automatisé présentant un risque supérieur à un traitement purement descriptif).

## Comment cette double appréciation s'articule avec les contrôles des Annexes A et B

Les risques identifiés lors de cette appréciation spécifique orientent directement la sélection et la priorisation des contrôles des Annexes A et B, développés aux modules 3 et 4 de ce parcours — un traitement identifié comme présentant un risque vie privée élevé lors de cette appréciation justifiera une mise en œuvre particulièrement rigoureuse des contrôles relatifs au consentement, aux droits des personnes concernées, ou aux transferts internationaux, développés au module 5 de ce parcours.

## Un tableau de synthèse des deux appréciations de risque

| Appréciation | Objet | Référentiel déjà développé dans cette plateforme |
|---|---|---|
| Appréciation des risques de sécurité (ISO 27001) | Confidentialité, intégrité, disponibilité des actifs informationnels | ISO 27001 |
| Appréciation des risques spécifique à la vie privée (ISO 27701) | Conséquences pour les personnes physiques dont les données sont traitées | NIST Privacy Framework, RGPD (AIPD) |

## Le lien avec le module suivant

Cette appréciation des risques doit être conduite en tenant compte du rôle exact assumé par l'organisation vis-à-vis des données traitées — responsable de traitement ou sous-traitant — une distinction développée en détail au module suivant de ce parcours.
