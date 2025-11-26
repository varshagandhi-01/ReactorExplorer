# ReactorExplorer

ReactorExplorer is a data science and machine learning pipeline designed to process, validate, transform, and analyze data related to global power plants, with a focus on nuclear energy. The project uses Nearest neighbour algorithm to match reactors with a selected reactor.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Data Ingestion**: Download and extract raw datasets.
- **Data Validation**: Validate the dataset against predefined schemas.
- **Data Transformation**: Clean and transform data for analysis.
- **Model Training**: Train a recommendation model using `NearestNeighbors`.
- **Recommendation System**: Suggest similar power plants based on input criteria.

---

## Project Structure
```
ReactorExplorer/
│
├── src/
├── tests/
├── data/
├── research/
├── CHANGELOG.md
├── README.md
└── ...
```
---
**Changelog:** See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS Console

### 2. Create IAM user for deployment

### 3. Create ECR repo to store/save docker image

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine:
```
#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

#confirm
docker --version
```
### 6. Configure EC2 as self-hosted runner
```
github>setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
### 7. Setup github secrets
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```
### Input:
List of reactors (as per data file source: WRI)

Data source sample:
![CSV data](image-1.png)

### Output:
![Find matching reactors](image.png)