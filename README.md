# Projet avec DVC (Data Version Control)

Ce projet utilise DVC pour gérer les données et Git pour gérer le code source. Suivez les étapes ci-dessous pour configurer et utiliser DVC avec Git.

## Guide d'utilisation

### 1. Initialisation du dépôt Git

```bash
git init
```
2. Initialisation de DVC

```bash

dvc init
```
3. Ajout des données à DVC

```bash

# Ajoutez les données que vous souhaitez suivre avec DVC.
dvc add <chemin_vers_les_données>
```
4. Configuration du stockage distant (Google Drive)

```bash

# Utilisez Google Drive comme stockage distant pour vos données DVC.
dvc remote add myremote gdrive://<ID_du_dossier_sur_Google_Drive>
```
5. Configuration des paramètres Google Drive

Assurez-vous que les paramètres suivants sont définis dans votre fichier de configuration dvc.conf :
```bash

[gdrive]
gdrive_acknowledge_abuse = true
dvc remote modify myremote gdrive_use_service_account true
et on ajoute le fichier .dvc/default.json ( qui contient les donnees personnelles de google drive)
```
6. Sélection du profil pour le stockage distant
```bash

dvc remote modify --local myremote profile myprofile
```



7. Commit et Push des données avec DVC

```bash

# Après avoir ajouté et suivi les modifications des données avec DVC, effectuez les étapes Git classiques pour les commit et push.
git add .
git commit -m "Ajout des données avec DVC"
git push origin main
```
8. Utilisation avec un autre local

## Guide d'utilisation
clone le projet github
  ```bash


git clone <nom de represotory>
```
### 1. Méthode pour travailler en local

#### Option 1: Utiliser un compte Google Drive personnel

Si vous travaillez en local, suivez ces étapes :

```bash
# Activer l'option pour reconnaître l'abus dans la configuration DVC
dvc remote modify --local myremote gdrive_acknowledge_abuse true

# Ajouter le profil pour le stockage distant
dvc remote modify --local myremote profile myprofile

# Effectuer le pull et le push des données avec DVC
dvc pull
dvc push
```
#### Option 2: Utiliser un compte de service Google

Pour utiliser un compte de service Google, exécutez la commande suivante :

```bash

# Activer l'utilisation du compte de service Google
dvc remote modify myremote gdrive_use_service_account true

# Implémenter le fichier default.json téléchargé depuis Google Cloud API
# Assurez-vous que le fichier default.json est correctement configuré avec les autorisations nécessaires
```
2. Méthode pour travailler avec le Cloud (CML - GitHub Actions)

Si vous utilisez le CML (GitHub Actions) pour travailler avec le Cloud, suivez ces étapes :

    1- Assurez-vous que le contenu du fichier default.json est ajouté au répertoire secret de GitHub.
    2- Modifiez le workflow GitHub Actions pour inclure les informations nécessaires pour accéder au fichier default.json.
    3- Effectuez un push pour déclencher le workflow. Assurez-vous que tout fonctionne correctement.

Monitoring des commits

Pour suivre les modifications apportées aux données et au code, vous pouvez utiliser git log pour les commits Git et dvc checkout pour les versions des données avec DVC :

    Utilisez git log pour voir l'historique des commits :

    ```bash

git log```

Utilisez git checkout pour revenir à une version précédente du code :

```bash

git checkout <hash_commit>```

Utilisez dvc checkout pour revenir à une version précédente des données :

```bash

dvc checkout```

