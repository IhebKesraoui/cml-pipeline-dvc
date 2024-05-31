# Project with DVC (Data Version Control)

This project uses DVC to manage data and Git to manage source code. Follow the steps below to set up and use DVC with Git.

## User Guide

### 1. Initialize the Git repository

```bash
git init
```
2. Initialize DVC

```bash

dvc init
```
3. Add data to DVC

```bash

# Add the data you want to track with DVC.
dvc add <path_to_data>
```
4. Configure remote storage (Google Drive)

```bash

# Use Google Drive as remote storage for your DVC data.
dvc remote add myremote gdrive://<Google_Drive_folder_ID>
```
5. Configure Google Drive settings

Make sure the following settings are defined in your configuration file dvc.conf:

ini

[gdrive]
gdrive_acknowledge_abuse = true

And then modify your remote:

```bash

dvc remote modify myremote gdrive_use_service_account true

Also, add the .dvc/default.json file (which contains your Google Drive personal data).
```
6. Select the profile for remote storage

```bash

dvc remote modify --local myremote profile myprofile
```
7. Commit and push data with DVC

```bash

# After adding and tracking data changes with DVC, perform the usual Git steps to commit and push.
git add .
git commit -m "Add data with DVC"
git push origin main
```
8. Using with another local environment
User Guide

Clone the GitHub project:

```bash

git clone <repository_name>
```
1. Method for working locally
Option 1: Use a personal Google Drive account

If you are working locally, follow these steps:

```bash

# Enable the option to acknowledge abuse in the DVC configuration
dvc remote modify --local myremote gdrive_acknowledge_abuse true

# Add the profile for remote storage
dvc remote modify --local myremote profile myprofile

# Pull and push data with DVC
dvc pull
dvc push
```
Option 2: Use a Google service account

To use a Google service account, run the following command:

```bash

# Enable the use of the Google service account
dvc remote modify myremote gdrive_use_service_account true

# Implement the default.json file downloaded from Google Cloud API
# Ensure the default.json file is correctly configured with the necessary permissions
```
2. Method for working with the Cloud (CML - GitHub Actions)

If you are using CML (GitHub Actions) to work with the Cloud, follow these steps:

    1- Ensure the content of the default.json file is added to the GitHub secrets directory.
    2- Modify the GitHub Actions workflow to include the necessary information to access the default.json file.
    3- Push to trigger the workflow. Ensure everything works correctly.

Monitoring commits

To track changes made to the data and code, you can use git log for Git commits and dvc checkout for data versions with DVC:

Use git log to see the commit history:

```bash

git log
```
Use git checkout to revert to a previous version of the code:

```bash

git checkout <commit_hash>
```
Use dvc checkout to revert to a previous version of the data:

```bash

dvc checkout
```