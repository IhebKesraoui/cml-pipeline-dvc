# README - Projet avec DVC

Ce projet utilise DVC (Data Version Control) pour gérer les données et Git pour gérer le code source. Ce README explique les étapes pour configurer et utiliser DVC avec Git.

## Étapes pour implémenter le projet avec DVC et Git

```bash
# 1. Initialisation du dépôt Git
git init 
```bash
# 2. Initialisation de DVC
dvc init

# 3. Ajout des données à DVC
# Ajoutez les données que vous souhaitez suivre avec DVC.
dvc add <chemin_vers_les_données>

# 4. Configuration du stockage distant
# Utilisez Google Drive comme stockage distant pour vos données DVC.
dvc remote add myremote gdrive://<ID_du_dossier_sur_Google_Drive>

# 5. Configuration des paramètres Google Drive
# Pour utiliser Google Drive, assurez-vous que les paramètres suivants sont définis dans votre fichier de configuration `dvc.conf` :
# [gdrive]
# gdrive_acknowledge_abuse = true

# 6. Sélection du profil pour le stockage distant (facultatif)
# Si vous utilisez plusieurs profils Google Drive, spécifiez le profil à utiliser avec DVC.
# [remote "myremote"]
# profile = myprofile

# 7. Configuration pour l'utilisation locale (optionnel)
# Si vous travaillez en local, vous pouvez désactiver `gdrive_acknowledge_abuse` et utiliser le stockage local.

# 8. Configuration pour l'utilisation du compte Google (optionnel)
# Si vous souhaitez utiliser votre compte Google pour l'accès à Google Drive, assurez-vous que `gdrive_acknowledge_abuse` est activé et que vous avez configuré vos identifiants Google Drive.

# 9. Commit et Push des données avec DVC
# Après avoir ajouté et suivi les modifications des données avec DVC, effectuez les étapes Git classiques pour les commit et push.
git add .
git commit -m "Ajout des données avec DVC"
git push origin main

# 10. Utilisation avec le CML (Continuous Machine Learning) (optionnel)
# Si vous utilisez le CML, assurez-vous que les informations d'identification Google Drive sont disponibles pour les workflows.
