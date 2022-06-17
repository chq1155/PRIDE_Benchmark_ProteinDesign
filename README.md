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



## 2. Benchmark Evaluation Metric

### 2.1 Data Manipulation Process 

Here're the code and command of evaluation metric including: sequence recovery rate, perplexity, TM-score, Diversity-Identity Score Metric.

**1. Sequence recovery rate**

>Input: Two .fasta files

>Output: Percentile of element-wise similarity between two input sequences.

>Usage:  `SEQ_REC 1.fasta 2.fasta testout 2`

**2. Perplexity**

>Input:

>Output:

>Usage: 

**3. TM-score**

>Input: Two .pdb files

>Output: Structural similarity between two input files

>Usage: `TM-score 1.pdb 2.pdb`

**4. Diversity-Identity Score**

>Input: Batch of sequence and their corresponding structure predicted by [Alphafold2]{https://github.com/deepmind/alphafold}

>Output: Corresponding score among the batch of sequences

>Usage: 

### 2.2 Diversity-Identity Score Metric

With the above two evaluation metrics, we can probe the structural similarity between the input and the model’s output. Also, we can test the model’s uncertainty on generative quality. However, one protein structure can obtain various output protein sequences. Here, function G evaluates the diversity of the generated sequences. Moreover, evaluation on diversity without considering the generated quality lacks the authority of the effectiveness, thus a structure similarity measuring fuction F is introduced. We combined both functions and designed Diversity-Identity Score Metric. The diversity-identity score E on sequence set S is formulated as a sum of negative-log functions:

$$ E(S) = \frac{1}{N}\sum-log[G^{-\gamma}(s_i,s_{i,cmp}) \cdot F(s_i)]\label{eq1} $$

where $s_i$ denotes the sequence in S, $s_{i,cmp}$ denotes the complement of sequence $s_i$ in S, $N$ is the amount of sequences, $gamma$ is the trade-off parameter, function G is the diversity measurement between sequence $s_i$ and $s_{i,cmp}$, and function F is the structural identity between 3D-structure of $s_i$ after folding and the input structure. 
