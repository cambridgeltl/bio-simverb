# bio-simverb
This repository contains the evaluation datasets for the paper Bio-SimVerb and Bio-SimLex: Wide-coverage Evaluation Sets of Word Similarity in Biomedicine by Billy Chiu, Sampo Pyysalo and Anna Korhonen.

## 0. Bio-SimVerb and Bio-SimLex:
The evaluation datasets created in this paper can be download via: https://drive.google.com/file/d/0BzMCqpcgEJgiZXNIWjhGRmQxRUU/view

There are two evaluations mentioned in this paper: 

## 1. For intrinsic evaluation: (folder: wvlib): 
Main files in the wvlib folder:

word-similarities: all intrinsic evaluation datasets used in this paper

evalrank.py: perform intrinsic evaluation.

Example Usage: python evalrank.py -q 'path/to/vectorfile' 'path/to/dataset' 

batch_eval.sh: The script to produce the intrinsic evaluation in this paper. 

Example Usage: ./batch_eval.sh 'FOLDER/to/vectorfile'

The evaluation score will be printed on screen

## 2. For extrinsic evaluation: (folder: NER)

Main files in the NER folder:

The corpora used for the experiments (which can be re-distributed) are in the data folder.
**Note:**The re-distribution status of the BioCreative IV Chemical and Drug (BC4CHEMD) named entity recognition task corpus is unclear but it can be publicly accessed at http://www.biocreative.org/tasks/biocreative-v/track-3-cdr/.

The models can be found in the NER/models folder.

There are several files in the models folder:

baseline.py: The MLP model used as a baseline for the extrinsic evaluation.

Example Usage: python baseline.py 'path/to/dataset' 'path/to/vectorfile'

baseline_config.py: The configurable variables and their values for the MLP baseline model (baseline.py).

config.py: The configurable variables and their values for the convolutional models.

run-wordvecs.sh: The script to produce the extrinsic evaluation in this paper. 

Example Usage: ./run-wordvecs.sh

The model will output two files:

logs: store the f-score for the NER. 

predictions: store the prediction outputted by the NER model.
