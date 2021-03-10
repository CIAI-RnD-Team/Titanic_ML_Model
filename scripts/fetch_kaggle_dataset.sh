#!/usr/bin/env bash

kaggle competitions download -c titanic -f test.csv -p packages/classification_model/classification_model/datasets/
 
kaggle competitions download -c titanic -f train.csv -p packages/classification_model/classification_model/datasets/