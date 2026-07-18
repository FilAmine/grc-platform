# Les douze exigences (1/3) : réseau sécurisé et protection des données de compte

## Une structure à six objectifs, douze exigences

PCI DSS v4.0 organise ses exigences en **six objectifs de contrôle**, chacun décliné en une ou deux exigences numérotées de 1 à 12 — une architecture à deux niveaux qui rappelle, dans son principe, celle des dix domaines de l'article 21 de NIS2 ou des dix-huit contrôles des CIS Controls déjà développés dans les parcours précédents de cette plateforme, quoique PCI DSS descende ensuite à un niveau de détail nettement plus prescriptif à travers des centaines de sous-exigences numérotées.

## Objectif 1 — Développer et gérer un réseau et des systèmes sécurisés

### Exigence 1 — Installer et gérer des contrôles de sécurité réseau

Renommée en v4.0 (auparavant centrée sur les seuls pare-feux), cette exigence couvre l'ensemble des **contrôles de sécurité réseau** au sens large : pare-feux, mais aussi d'autres technologies de contrôle des flux (comme des solutions de sécurité cloud-native). Elle exige notamment une documentation des flux réseau autorisés entre le CDE et les autres réseaux, la restriction des connexions entrantes et sortantes au strict nécessaire, et l'interdiction des connexions directes non contrôlées entre l'internet public et le CDE. Cette exigence recoupe directement le contrôle SC-7 de SP 800-53 et le contrôle 8.20 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme.

### Exigence 2 — Appliquer des configurations sécurisées à tous les composants du système

Cette exigence impose de modifier systématiquement les **paramètres par défaut des fournisseurs** avant la mise en production de tout composant système — mots de passe par défaut, comptes de démonstration, services et protocoles inutiles désactivés. Elle recoupe directement le contrôle 4 des CIS Controls (configuration sécurisée) et le contrôle 8.9 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme. Un point de vigilance PCI DSS spécifique : cette exigence s'applique explicitement aux **appareils sans fil**, souvent négligés dans une revue de configuration générique.

## Objectif 2 — Protéger les données de compte

### Exigence 3 — Protéger les données de compte stockées

Cette exigence structure l'ensemble des règles de protection du PAN au repos, développées en détail au module 5 : minimiser la conservation des données de compte au strict nécessaire, ne jamais stocker les données d'authentification sensibles après autorisation, et rendre le PAN illisible partout où il est stocké (par chiffrement fort, troncature, tokenisation, ou hachage). Elle exige également une gestion documentée du cycle de vie des clés cryptographiques utilisées pour protéger ces données.

### Exigence 4 — Protéger les données de titulaires de carte avec une cryptographie forte lors de leur transmission sur des réseaux publics ouverts

Cette exigence impose l'utilisation de protocoles de chiffrement robustes et à jour (le référentiel exclut explicitement les versions obsolètes de TLS et SSL) pour toute transmission de données de titulaires de carte sur un réseau public ouvert — internet, réseaux sans fil, réseaux mobiles. Elle interdit également explicitement l'envoi de PAN non protégés via des technologies de messagerie utilisateur final (email, messagerie instantanée, SMS), une précision qui recoupe directement l'interdiction déjà rencontrée dans d'autres contextes de cette plateforme concernant l'envoi de données sensibles par des canaux non sécurisés.

## Ce que ce premier bloc révèle

Ces quatre premières exigences posent les fondations techniques les plus classiques déjà rencontrées à travers de nombreux référentiels de cette plateforme (segmentation réseau, durcissement de configuration, chiffrement) — leur spécificité PCI DSS réside moins dans leur contenu technique que dans leur **application ciblée et exclusive aux données de cartes de paiement** : un système qui ne touche jamais au CDE peut légitimement rester hors du périmètre de ces exigences, un principe de scoping développé en détail au module 2 de ce parcours.
