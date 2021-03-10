import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import joblib

from classification_model import pipeline
from classification_model.processing.data_management import load_dataset, save_pipeline
from classification_model.config import config
from classification_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)

def run_training():
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.TARGET, axis=1),
        data[config.TARGET],
        test_size=0.2,
        random_state=0)  # we are setting the seed here

    pipeline.titanic_pipe.fit(X_train, y_train)
    joblib.dump(pipeline.titanic_pipe, config.PIPELINE_NAME)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.titanic_pipe)


if __name__ == '__main__':
    run_training()
