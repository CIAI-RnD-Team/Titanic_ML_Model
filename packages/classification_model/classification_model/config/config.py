import pathlib

import classification_model

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(classification_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "Survived"

#variables
FEATURES=[
    "Sex",
    "Age",
    "Ticket",
    "Fare",
    "Embarked",
    "Cabin",
    "Name",
    "PassengerId"
]

CATEGORICAL_VARS = [
    "Sex", 
    "Cabin", 
    "Embarked", 
    "Ticket"
]

NUMERICAL_VARS = [
    "Age", 
    "Fare",
]

CABIN = "Cabin"


DROP_FEATURES = [
    "Name",
    "PassengerId"
]

NUMERICALS_LOG_VARS = ["Fare"]

NUMERICAL_VARS_WITH_NA = ["Age"]
CATEGORICAL_VARS_WITH_NA = ["Cabin","Embarked"]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]

PIPELINE_NAME = 'random_forest'
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

ACCEPTABLE_MODEL_DIFFERENCE = 0.05