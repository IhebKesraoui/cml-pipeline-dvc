# README

## Table of Contents
1. [Introduction](#introduction)
2. [Tools Used](#tools-used)
3. [How to Install and Setup the Application](#how-to-install-and-setup-the-application)
4. [How to Pull the Project and Data](#how-to-pull-the-project-and-data)
5. [How to Run the Pipeline](#how-to-run-the-pipeline)
6. [Roadmap](#roadmap)
7. [Useful Links](#useful-links)


## Introduction
The project is a robust MLOps pipeline that emphasizes CI/CD principles. The primary goal is to facilitate seamless integration and deployment of machine learning models. This pipeline is designed to react to any modifications in the data or functions by triggering a series of automated steps including debugging, testing, training, and deploying the model to the cloud.

![Pipeline Overview](./image1.png)

Key features of the pipeline:
- **Data Versioning and Control**: Utilizing DVC to manage data changes effectively.
- **Model Tracking**: Implementing MLflow to keep track of experiments, metrics, and parameters.
- **Deployment**: Using BentoML to deploy models efficiently.

This approach ensures that any change in the data or codebase automatically initiates the pipeline, maintaining the integrity and performance of the deployed models.

![MLOps Workflow](./image2.png)
## Tools Used
- **DVC**: Data Version Control for managing datasets and versions.
- **VSCode**: Integrated Development Environment for coding and debugging.
- **Google Drive**: Cloud storage for data management.
- **MLflow**: Platform for managing the lifecycle of machine learning models.
- **BentoML**: Framework for serving and deploying machine learning models.

## How to Install and Setup the Application

## How to Install and Setup the Application
1. Clone the repository and switch to the verified branch:
      Open your code editor (e.g., VSCode) to start working on the project.

   ```sh
   git clone -b verified <repository-url>
  
    Install the required dependencies:

    sh

    pip install -r requirements.txt


How to Pull the Project and Data

    Copy the default.json and config.local files from Google Drive and place them inside the ./.dvc folder in your project directory.
    Pull the data using DVC:

    sh

dvc pull
