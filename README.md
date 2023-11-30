# PRIDE-New-Benchmark-Dataset-For-Protein-Structural-Design

## About this Repo

This repo is open-source for all protein design learners for providing the benchmark of the paper PRIDE: [A benchmark for structure-guided protein design evaluation]. All constructed dataset described in the paper as well as the corresponding scripts are here. Welcome all peotein structural design researchers!

## Menu

- [PRIDE: New Benchmark Dataset For Protein Structural Design](#PRIDE-New-Benchmark-Dataset-For-Protein-Structural-Design)
  - [About this Repo](#About-this-Repo)
  - [Menu](#Menu)
  - [1. Benchmark Datasets](#1-Benchmark-Datasets)
    - [1.1 Training Dataset](#11-Training-Dataset)
    - [1.2 Test Dataset](#12-Test-Dataset)
  - [2. Benchmark Evaluation Metric](#2-Benchmark-Evaluation-Metric)
    - [2.1 Data Manipulation and Evaluation Scripts](#21-Data-Manipulation-and-Evaluation-Scripts)
    - [2.2 Diversity-Identity Score Metric](#22-Diversity-Identity-Score-Metric)
  - [3. Benchmark Models](#3-Benchmark-Models)


## 1. Benchmark Datasets

We design our benchmark to based on two fundamental principles about generative protein design models: The capacity and sequence diversity of our benchmark should meet the training and testing needs of deep learning models; No data leak or sequence redundancy between training and test set.

### 1.1 Training Dataset

Our training dataset is made up of the CATH dataset. CATH S35 V4.3. consists of 32389 proteins ranges up to date 21-Oct-2010. Please go to the dictionary ```./Data/1.Train_CATH```

1.Raw_Data: 

>**CATH_Domain_Boundaries.txt:** Domain boundaries for each CATH ID.
>
>```CATH_ID   Boundaries```
>
>**CATH_S35_V4.3.0_Domain_List.txt:** Domain list for CAHT S35 V4.3.0
>
>```
>Column 1:  CATH domain name (seven characters)
>Column 2:  Class number
>Column 3:  Architecture number
>Column 4:  Topology number
>Column 5:  Homologous superfamily number
>Column 6:  S35 sequence cluster number
>Column 7:  S60 sequence cluster number
>Column 8:  S95 sequence cluster number
>Column 9:  S100 sequence cluster number
>Column 10: S100 sequence count number
>Column 11: Domain length
>Column 12: Structure resolution (Angstroms)
>           (999.000 for NMR structures and 1000.000 for obsolete PDB entries)
>```
>
>**CATH_Final_List.txt:** All 32389 CATH files with partial domain information as well as domain boundaries merged.
>
>```
>Column 1:  CATH domain name (seven characters)
>Column 2:  Class number
>Column 3:  Architecture number
>Column 4:  Topology number
>Column 5:  Homologous superfamily number
>Column 6:  S35 sequence cluster number
>Column 7:  Chain ID
>Column 8:  Domain doundaries
>```

<div align=center><img width="520" height="240" src="https://github.com/chq1155/PRIDE-Benchmark-For-Protein-Structural-Design/blob/main/Img_Folder/figure2.png"/></div>

2.Processing:

>**CATH_stat:** code for obtaining statistics of training files. (Users need to change address of file on line 2)
>
>```python CATH_stat.py```
>
>**TV_Split:** code or train/valid split, divide CATH_Final_List.txt intp 10 equal lists. (Users need to change the file names on line3, 8, 20. Also, user can change the >percentile of train/valid based on our code.)
>
>```python TV_Split.py```

3.Final_Data:

>**list0.txt-list9.txt:** all 10 files splited from TV_Split.py

<div align=center><img width="480" height="320" src="https://github.com/chq1155/PRIDE-Benchmark-For-Protein-Structural-Design/blob/main/Img_Folder/figure1s.png"/></div>


4.Download:

>**PDB_Load:** Input string of training files, download the corresponding .pdb files into current folder.
>
>```PDB_Load list0.txt```

### 1.2 Test Dataset

Here, we utilized CAMEO as an independent test set to test existing models’ performance. Users can directly run the script we provide to update the test set to evaluate the performance of the models. Our chosen proteins dataset ranges in CAMEO from 17-07-2021 to 12-03-2022 and consists of 504 proteins. We selected the hard samples and guaranteed no redundancy exists between the training set. Please go to the dictionary ```./Data/2.Test_CAMEO```

1. Raw_Data

>**CAMEO_Version1.zip:** PDB Files of test set.
>
>**CAMEO_List:** Corresponding CAMEO list of CAMEO_Version1.zip.

2. Processing


3. Final_Data

>**valid_h:** List of 'hard' CAMEO in CAMEO_List.
>
>**valid_hm:** List of 'hard' & 'medium' CAMEO in CAMEO_List.
>
>**valid_hme:** List of 'hard' & 'medium' & 'easy' CAMEO in CAMEO_List.




## 2. Benchmark Evaluation Metric

### 2.1 Data Manipulation and Evaluation Scripts

Here're the code and command of evaluation metric including: sequence recovery rate, perplexity, TM-score, Diversity-Identity Score Metric.

**1. Sequence recovery rate**

>Input: Two .fasta files

>Output: Percentile of element-wise similarity between two input sequences.

>Usage:  `SEQ_REC 1.fasta 2.fasta testout 2`

**2. Perplexity**

>Input: Batch of sequence

>Output: Corresponding perplexity

>Usage: `Refer to notebook from [Hugging Face](https://colab.research.google.com/github/huggingface/notebooks/blob/main/transformers_doc/en/pytorch/perplexity.ipynb)`

**3. TM-score**

>Input: Two .pdb files

>Output: Structural similarity between two input files

>Usage: `TM-score 1.pdb 2.pdb`

**4. Diversity-Identity Score**

>Input: Batch of sequence and their corresponding structure predicted by [Alphafold2](https://github.com/deepmind/alphafold)

>Output: Corresponding score among the batch of sequences

>Usage: 

<div align=center><img width="480" height="320" src="https://github.com/chq1155/PRIDE-Benchmark-For-Protein-Structural-Design/blob/main/Img_Folder/figure6s.png"/></div>

### 2.2 Diversity-Identity Score Metric

With the above two evaluation metrics, we can probe the structural similarity between the input and the model’s output. Also, we can test the model’s uncertainty on generative quality. However, one protein structure can obtain various output protein sequences. Here, function G evaluates the diversity of the generated sequences. Moreover, evaluation on diversity without considering the generated quality lacks the authority of the effectiveness, thus a structure similarity measuring fuction F is introduced. We combined both functions and designed Diversity-Identity Score Metric. The diversity-identity score E on sequence set S is formulated as a sum of negative-log functions:

$$ E(S) = \frac{1}{N}\sum-log[G^{-\gamma}(s_i,s_{i,cmp}) \cdot F(s_i)] $$

where $s_i$ denotes the sequence in S, $s_{i,cmp}$ denotes the complement of sequence $s_i$ in S, $N$ is the amount of sequences, $gamma$ is the trade-off parameter, function G is the diversity measurement between sequence $s_i$ and $s_{i,cmp}$, and function F is the structural identity between 3D-structure of $s_i$ after folding and the input structure. 

<div align=center><img width="560" height="240" src="https://github.com/chq1155/PRIDE-Benchmark-For-Protein-Structural-Design/blob/main/Img_Folder/figure7s.png"/></div>

### 2.3 Experimental results

Performance on Cameo dataset. We present experimental results of various commonly used evaluation metrics and the defined Diversity-Identity Score. BLOSUM62 score measures the similarity of designed sequences. TM-score and RMSD scores evaluate the structural identity of designed and ground truth proteins. pLDDT evaluates the accuracy and reliability of predicted protein structures of designed protein sequences. For RFdiffusion, since it is a structure diffusion model, we adopt ProteinMPNN for sequence design based on the structure generated by RFdiffusion. Besides, we only compare the five sequence design models for fair benchmark. The best model performance under each matrix is highlighted.

<div align=center><img width="700" height="240" src="https://github.com/chq1155/PRIDE-Benchmark-For-Protein-Structural-Design/blob/main/Img_Folder/results_table.png"/></div>

## 3. Benchmark Models

SPROF: https://github.com/biomed-AI/SPROF 

GVPTransformer (esm-if): https://github.com/facebookresearch/esm 

GVP: https://github.com/drorlab/gvp-pytorch 

GraphTrans: https://github.com/jingraham/neurips19-graph-protein-design 

ProteinMPNN: https://github.com/dauparas/ProteinMPNN 


