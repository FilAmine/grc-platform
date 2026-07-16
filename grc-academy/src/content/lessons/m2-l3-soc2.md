# SOC 2 : les Trust Services Criteria

## Un rapport américain devenu standard de facto B2B SaaS

**SOC 2** (System and Organization Controls 2) est un cadre défini par l'AICPA (American Institute of Certified Public Accountants), initialement pensé pour les prestataires de services américains. Il est devenu, de fait, l'exigence contractuelle la plus fréquemment demandée par les clients B2B à un éditeur SaaS — souvent avant même ISO 27001, notamment sur le marché nord-américain.

Contrairement à ISO 27001, SOC 2 n'est **pas une certification** : c'est un **rapport d'audit** (attestation), produit par un cabinet d'expertise comptable habilité, qui décrit le système de l'organisation et évalue si ses contrôles atteignent certains critères. Il n'y a pas de "certificat SOC 2" à afficher — il y a un rapport, généralement partagé sous NDA avec les clients ou prospects qui le demandent.

## Les cinq Trust Services Criteria (TSC)

Un audit SOC 2 s'articule autour de cinq catégories de critères, dont une seule est obligatoire :

### Security (obligatoire)

Le critère commun, présent dans tout rapport SOC 2 : protection contre l'accès non autorisé (logique et physique), aux systèmes utilisés pour fournir le service. C'est le socle.

### Availability (optionnel)

Le système est disponible pour l'exploitation et l'utilisation conformément aux engagements pris (SLA, plan de continuité, gestion de la capacité).

### Processing Integrity (optionnel)

Le traitement des données est complet, valide, précis, en temps opportun et autorisé — pertinent notamment pour les systèmes financiers ou de traitement de transactions.

### Confidentiality (optionnel)

Les informations désignées comme confidentielles sont protégées conformément aux engagements pris (souvent recoupe le NDA avec le client).

### Privacy (optionnel)

La collecte, l'utilisation, la conservation et la divulgation des informations personnelles sont conformes aux engagements de l'organisation et aux principes de confidentialité généralement admis (AICPA Privacy Framework) — à ne pas confondre avec une conformité RGPD complète, qu'un rapport SOC 2 Privacy ne garantit pas à lui seul.

Un éditeur SaaS B2B choisit généralement Security + Availability + Confidentiality comme périmètre standard ; Processing Integrity et Privacy sont ajoutés selon le profil du produit.

## Type I vs Type II : la différence qui compte vraiment

- **Type I** évalue la conception des contrôles à une date donnée (un instantané). Utile comme première étape ou pour rassurer rapidement un client, mais faible valeur probante : "les contrôles sont bien conçus sur le papier" ne dit rien de leur application réelle.
- **Type II** évalue le fonctionnement effectif des contrôles sur une **période d'observation** (généralement 6 à 12 mois). L'auditeur teste des échantillons réels : tickets d'incidents traités, revues d'accès effectuées, déploiements passés par le processus de revue de code, etc.

Un client sérieux dans un cycle d'achat B2B demandera systématiquement un rapport **Type II**, jamais un Type I seul — le Type I ne prouve que l'intention.

## Ce qu'un ingénieur doit comprendre de SOC 2

Contrairement à ISO 27001 qui impose une structure de SMSI standardisée, SOC 2 laisse l'organisation **définir elle-même ses contrôles**, tant qu'ils répondent aux critères des TSC choisis — c'est l'auditeur qui juge ensuite si les contrôles définis sont adaptés et appliqués. Cette flexibilité est à double tranchant : elle permet d'adapter les contrôles à une architecture cloud-native moderne (contrairement à des référentiels plus prescriptifs), mais elle exige une auto-discipline forte pour ne pas définir des contrôles trop faibles qui passeraient quand même l'audit.

En pratique, la majorité des contrôles Security d'un rapport SOC 2 recoupent très directement les pratiques Security by Design étudiées dans cette formation : gestion des accès (IAM, MFA, moindre privilège), gestion du changement (revue de code, CI/CD contrôlé), surveillance (logging, alerting), et gestion des vulnérabilités (scans, patchs).
