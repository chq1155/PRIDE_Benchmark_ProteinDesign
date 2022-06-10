# PRIDE-New-Benchmark-Dataset-For-Protein-Structural-Design

## About this Repo

This repo is open-source for all protein design learners for providing the benchmark of the paper PRIDE: [A benchmark for structure-guided protein design evaluation]. All constructed dataset described in the paper as well as the corresponding scripts are here. Welcome all peotein structural design researchers!

## Menu



## 1. Benchmark Datasets

We design our benchmark to based on two fundamental principles about generative protein design models: The capacity and sequence diversity of our benchmark should meet the training and testing needs of deep learning models; No data leak or sequence redundancy between training and test set.

### 1.1 Training Dataset

Our training dataset is made up of the CATH dataset. CATH S35 V4.3. consists of 32389 proteins ranges up to date 21-Oct-2010. 

### 1.2 Test Dataset

Here, we utilized CAMEO as an independent test set to test existing models’ performance. Users can directly run the script we provide to update the test set to evaluate the performance of the models. Our chosen proteins dataset ranges in CAMEO from 17-07-2021 to 12-03-2022 and consists of 504 proteins. We selected the hard samples and guaranteed no redundancy exists between the training set.

### 1.3 Data Manipulation Process

Users can use our provided scripts to create their own dataset for flexibility.
