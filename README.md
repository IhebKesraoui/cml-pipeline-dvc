# Projet avec DVC (Data Version Control)

Ce projet utilise DVC pour gérer les données et Git pour gérer le code source. Suivez les étapes ci-dessous pour configurer et utiliser DVC avec Git.

## Guide d'utilisation

### 1. Initialisation du dépôt Git

```bash
git init

2. Initialisation de DVC

bash

dvc init

3. Ajout des données à DVC

bash

# Ajoutez les données que vous souhaitez suivre avec DVC.
dvc add <chemin_vers_les_données>

4. Configuration du stockage distant (Google Drive)

bash

# Utilisez Google Drive comme stockage distant pour vos données DVC.
dvc remote add myremote gdrive://<ID_du_dossier_sur_Google_Drive>

5. Configuration des paramètres Google Drive

Assurez-vous que les paramètres suivants sont définis dans votre fichier de configuration dvc.conf :

ini

[gdrive]
gdrive_acknowledge_abuse = true

6. Sélection du profil pour le stockage distant (facultatif)

Si vous utilisez plusieurs profils Google Drive, spécifiez le profil à utiliser avec DVC.

ini

[remote "myremote"]
profile = myprofile

7. Commit et Push des données avec DVC

bash

# Après avoir ajouté et suivi les modifications des données avec DVC, effectuez les étapes Git classiques pour les commit et push.
git add .
git commit -m "Ajout des données avec DVC"
git push origin main

8. Utilisation avec le CML (Continuous Machine Learning) (optionnel)

Si vous utilisez le CML, assurez-vous que les informations d'identification Google Drive sont disponibles pour les workflows.
