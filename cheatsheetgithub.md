# 🐙 GitHub Cheatsheet

> Mémo rapide pour maîtriser GitHub au quotidien — de la config initiale aux workflows avancés.
---

## ⚙️ Configuration initiale

```bash
git config --global user.name "TonPseudo"
git config --global user.email "ton@email.com"
```

Vérifier la config :

```bash
git config --list
```

---

## 📦 Créer / Cloner un repo

| Action | Commande |
|---|---|
| Initialiser un repo local | `git init` |
| Lier à un repo GitHub | `git remote add origin git@github.com:user/repo.git` |
| Cloner un repo existant | `git clone git@github.com:user/repo.git` |
| Cloner une branche spécifique | `git clone -b ma-branche git@github.com:user/repo.git` |

---

## 🔄 Le cycle Stage → Commit → Push

C'est **le concept fondamental** à comprendre. Chaque étape a un rôle distinct :

```
Fichiers modifiés         Zone de staging           Historique local          GitHub (remote)
┌─────────────┐          ┌──────────────┐          ┌──────────────┐         ┌──────────────┐
│  Working     │  ──────► │   Staged     │  ──────► │  Committed   │ ──────► │   Pushed     │
│  Directory   │ git add  │   (index)    │ git      │  (local)     │ git     │   (remote)   │
│              │          │              │ commit   │              │ push    │              │
└─────────────┘          └──────────────┘          └──────────────┘         └──────────────┘
```

### Stage (`git add`)

Prépare les fichiers pour le prochain commit. C'est une **zone tampon** qui te permet de choisir précisément ce qui entre dans le commit.

```bash
git add fichier.txt          # Stage un fichier
git add .                    # Stage tout le répertoire courant
git add -p                   # Stage interactif (choisir morceau par morceau)
git reset fichier.txt        # Unstage un fichier (le retire du staging)
```

### Commit (`git commit`)

Crée un **snapshot local** des fichiers stagés. Le commit n'existe que sur ta machine à ce stade.

```bash
git commit -m "feat: ajout du login"   # Commit avec message
git commit -am "fix: correction bug"   # Stage + commit les fichiers déjà trackés
git commit --amend                      # Modifier le dernier commit (message ou contenu)
```

### Push (`git push`)

Envoie tes commits locaux vers **GitHub** (le remote). C'est seulement à ce moment que les autres peuvent voir ton travail.

```bash
git push                               # Push vers la branche trackée
git push origin ma-branche             # Push une branche spécifique
git push -u origin ma-branche          # Push + définir le tracking (1ère fois)
git push --force-with-lease            # Force push sécurisé (vérifie que personne n'a push entre-temps)
```






### Stratégie de nommage courante

| Préfixe | Usage |
|---|---|
| `feature/` | Nouvelle fonctionnalité — `feature/login-page` |
| `fix/` | Correction de bug — `fix/navbar-crash` |
| `hotfix/` | Fix urgent en production — `hotfix/security-patch` |
| `chore/` | Maintenance, CI, deps — `chore/update-deps` |
| `release/` | Préparation d'une release — `release/v2.0` |

---

## 🔀 Merge vs Rebase

### Merge

Fusionne une branche dans une autre en créant un **commit de merge**.




---

## 🔃 Pull Requests (PR)
### Qu'est-ce qu'une Pull Request ?

Une **Pull Request** (PR) est une **demande de fusion** entre deux branches. C'est un mécanisme GitHub (pas Git natif) qui permet de :
- Proposer des changements avant de les fusionner
- Déclencher une **review par l'équipe**
- Discuter, commenter, suggérer des améliorations
- Vérifier que tout passe les **tests automatisés** (CI/CD)
- Approuver ou demander des modifications avant le merge final

En résumé : c'est un **processus de contrôle qualité** avant d'intégrer du code dans `main`.

### Workflow classique

```
1. Créer une branche       →  git switch -c feature/truc
2. Coder + commit + push   →  git push -u origin feature/truc
3. Ouvrir une PR sur GitHub →  github.com/user/repo/compare
4. Review par l'équipe      →  commentaires, suggestions, approve
5. Merge la PR              →  squash, merge commit, ou rebase
6. Supprimer la branche     →  bouton sur GitHub ou git push origin --delete
```

### Types de merge dans une PR

| Type | Résultat |
|---|---|
| **Merge commit** | Garde tous les commits + un commit de merge |
| **Squash and merge** | Combine tous les commits en un seul |
| **Rebase and merge** | Rejoue les commits sur main (historique linéaire) |

### Bonnes pratiques PR

- Titre clair et descriptif, ex : `feat: add user authentication`
- Description avec contexte, screenshots si UI
- Petites PRs = review plus rapide
- Utiliser les **draft PRs** quand c'est encore en cours


### Workflow classique

```
1. Créer une branche       →  git switch -c feature/truc
2. Coder + commit + push   →  git push -u origin feature/truc
3. Ouvrir une PR sur GitHub →  github.com/user/repo/compare
4. Review par l'équipe      →  commentaires, suggestions, approve
5. Merge la PR              →  squash, merge commit, ou rebase
6. Supprimer la branche     →  bouton sur GitHub ou git push origin --delete
```

### Types de merge dans une PR

| Type | Résultat |
|---|---|
| **Merge commit** | Garde tous les commits + un commit de merge |
| **Squash and merge** | Combine tous les commits en un seul |
| **Rebase and merge** | Rejoue les commits sur main (historique linéaire) |

### Bonnes pratiques PR

- Titre clair et descriptif, ex : `feat: add user authentication`
- Description avec contexte, screenshots si UI
- Petites PRs = review plus rapide
- Utiliser les **draft PRs** quand c'est encore en cours

---









## 📂 Fichiers spéciaux GitHub

| Fichier | Rôle |
|---|---|
| `README.md` | Page d'accueil du repo |
| `.gitignore` | Fichiers à ne pas tracker |
| `LICENSE` | Licence du projet |
---

