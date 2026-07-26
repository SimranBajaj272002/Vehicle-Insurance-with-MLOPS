# 🚗 Vehicle Data MLOps Pipeline

This repository contains a complete End-to-End Machine Learning project with a fully integrated MLOps pipeline. It covers everything from data ingestion using MongoDB to model deployment using AWS (S3, ECR, EC2) and GitHub Actions for CI/CD.

---

## 🛠️ Phase 1: Environment Setup

Follow these steps to initialize your local development environment:

* Create the project template by executing the `template.py` file.


* Configure the local package imports in your `setup.py` and `pyproject.toml` files (refer to `crashcourse.txt` for details).


* Create and activate a virtual environment using Conda: `conda create -n vehicle python=3.10 -y` followed by `conda activate vehicle`.


* Add your required modules to `requirements.txt` and install them running `pip install -r requirements.txt`.


* Verify your local packages are installed correctly by running `pip list` in the terminal.



---

## 🗄️ Phase 2: Database Configuration (MongoDB)

This project relies on MongoDB for data storage and retrieval.

* Sign up for MongoDB Atlas, create a new project, and deploy an M0 service cluster.


* Set up a database user with a username and password.


* Configure network access to allow IP address `0.0.0.0/0` so the database can be accessed from anywhere.


* Copy your Python 3.6+ driver connection string from the MongoDB dashboard.


* Inside a `notebook` folder, utilize the dataset and push your data to the MongoDB database using a Jupyter Notebook (`mongoDB_demo.ipynb`) running on the Python vehicle kernel.


* Verify the data upload by browsing your collection via the MongoDB Atlas database UI to ensure it is in key-value format.


* Export your MongoDB connection string as a local environment variable (`MONGODB_URL`) via your terminal or Windows environment settings.



---

## 🧠 Phase 3: Core MLOps Components

### 1. Logging, Exceptions, and EDA

* Implement and test custom logger and exception handling scripts inside `demo.py`.


* Review the provided notebooks for Exploratory Data Analysis (EDA) and Feature Engineering.



### 2. Pipeline Development

* **Data Ingestion:** Configure database connections to fetch MongoDB key-value data and transform it into a DataFrame, updating `entity` and `components` files accordingly.


* **Data Validation:** Define the dataset schema in `config.schema.yaml` and implement validation utilities.


* **Data Transformation:** Build the transformation component and add the `estimator.py` file to the entity folder.


* **Model Trainer:** Implement the training component by adding the relevant class to `estimator.py`.



---

## ☁️ Phase 4: Cloud Storage Integration (AWS S3)

Before evaluating and pushing the model, you must configure AWS S3 to act as a model registry.

* Log into the AWS Console (`us-east-1` region) and create a new IAM user named `firstproj` with `AdministratorAccess`.


* Generate and download CLI access keys for this user, then set them as local environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).


* Create an S3 Bucket named `my-model-mlopsproj` (unchecking "Block all public access") to store models.


* Update `constants.__init__.py` with AWS credentials, region, bucket name, S3 key (`model-registry`), and set the `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE` to `0.02`.


* Create an `s3_estimator.py` script inside the `entity` directory to handle all functions required to pull and push models to S3.


* Complete the Model Evaluation and Model Pusher components.



---

## 🌐 Phase 5: Web Application Setup

* Construct the code structure for the Prediction Pipeline.


* Set up your `app.py` script to serve as the backend application.


* Add the `static` and `template` directories to host the front-end interface.



---

## 🚀 Phase 6: CI/CD Pipeline & EC2 Deployment

Automate deployments using Docker, GitHub Actions, and AWS EC2.

### 1. Docker & AWS Prep

* Set up your `Dockerfile` and `.dockerignore` files.


* Create a `.github/workflows` directory containing your `aws.yaml` workflow file.


* Create a new AWS IAM user named `usvisa-user` with CLI access keys for deployment.


* Create an Amazon ECR repository named `vehicleproj` in the `us-east-1` region to store your Docker images.



### 2. EC2 Server Setup

* Launch a `T2 Medium` EC2 instance running Ubuntu Server 24.04 (named `vehicledata-machine`), allowing HTTP/HTTPS traffic and allocating 30GB of storage.


* Connect to the instance via EC2 Instance Connect and install Docker using the official script (`get-docker.sh`).


* Add the `ubuntu` user to the docker group.



### 3. GitHub Actions Integration

* In your GitHub repository settings, set up a new Self-Hosted Linux Runner.


* Execute the provided configuration and run commands on your EC2 instance to connect it to GitHub.


* Add your AWS Access Keys, Default Region, and ECR Repo URL to your GitHub Repository Secrets.


* Push your code to trigger the automated CI/CD deployment pipeline.



### 4. Launching the App

* Edit the EC2 Security Group inbound rules to allow Custom TCP traffic on port `5000` from `0.0.0.0/0`.


* Access the live web application by visiting `<your-ec2-public-ip>:5000` in your browser.


* You can trigger a new model training cycle directly via the `/training` route.