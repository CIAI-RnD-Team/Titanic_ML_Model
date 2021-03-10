import math
import numpy as np

from classification_model.predict import make_prediction
from classification_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)
    S1 = subject.get('predictions')[0]


    # Then
    assert subject is not None
    assert isinstance(S1, np.int64)
    assert math.ceil(subject.get('predictions')[0]) == 0


def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = len(test_data)
    multiple_test_input = test_data

    # When
    subject = make_prediction(input_data=multiple_test_input)

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == 417

    # We expect some rows to be filtered out
    assert len(subject.get('predictions')) != original_data_length
