# Colonne Active

Webapp de séances guidées de renforcement profond du dos, de mobilité, de travail des tendons et des fascias, avec suivi de l'assiduité (renfo, natation, course).

**Ouvrir l'app : https://deniscyril.github.io/colonne-active/**

> ⚠️ Programme personnel construit sur des principes généraux (méthode McGill, rééducation de la scoliose, charge progressive des tendons). Il ne remplace pas l'avis d'un kinésithérapeute ou d'un médecin. Fais valider chaque exercice avant de le pratiquer.

## Contenu

- Trois séances : courte A (dos), courte B (jambes) et longue.
- Un lecteur guidé avec minuteur, bips, rythme des répétitions et annonces vocales.
- 23 fiches d'exercices avec schémas, étapes, niveaux, vidéos et avis du kiné.
- Un suivi : journal, douleur, effort en emoji, grille sur 8 semaines.
- Des outils de motivation : séries de jours consécutifs, 16 médailles, assiduité natation (hors petites vacances de la zone B).

Le détail est dans [CAHIER_DES_CHARGES.md](CAHIER_DES_CHARGES.md).

## Données

La version GitHub Pages enregistre le journal et les réglages **dans le navigateur** (`localStorage`). Rien n'est envoyé sur un serveur. Pour sauvegarder ou changer d'appareil, va dans **Réglages → Données → Exporter le journal** puis importe le fichier JSON sur l'autre appareil.

Sur iPhone : ouvre l'app dans Safari, puis Partager → « Sur l'écran d'accueil ».

## Structure

| Fichier | Rôle |
|---|---|
| `src/colonne-active.html` | Source unique (aussi publiée comme artifact claude.ai) |
| `build.py` | Génère `index.html` (document complet pour GitHub Pages) |
| `index.html` | L'app servie par GitHub Pages |
| `manifest.webmanifest`, `icon*` | Installation sur l'écran d'accueil |

Mise à jour : modifier `src/colonne-active.html`, puis :

```bash
python3 build.py src/colonne-active.html index.html
```
