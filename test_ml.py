import pytest
# TODO: add necessary import
from ml.model import compute_model_metrics
from train_model import model, X_test, y_test, preds, train, test
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_algo_type():
    """
    Test if the ML model uses the expected algorithm.
    """
    # expected algorithm
    expected_algorithm = RandomForestClassifier  # Replace with the expected algorithm class

    # Use assert to check if the model uses the expected algorithm
    assert isinstance(model, expected_algorithm), f"Expected algorithm: {expected_algorithm}, Actual algorithm: {type(model)}"

# TODO: implement the second test. Change the function name and input as needed
def test_metrics():
    """
    Test if the computing metrics functions return the expected value.
    """
    actual_metrics = compute_model_metrics(y_test, preds)
    actual_metrics = [round(x, 3) for x in actual_metrics]

    expected_precision = 0.742
    expected_recall = 0.638
    expected_f1 = 0.686
    expected_metrics = [expected_precision,expected_recall,expected_f1]

    # Use assertions to check if the actual metrics match the expected metrics
    assert actual_metrics == expected_metrics, f"Expected metrics: {expected_metrics}, Actual metrics: {actual_metrics}"


# TODO: implement the third test. Change the function name and input as needed
def test_train_test_size():
    """
    Test if the training and test datasets have the expected size.
    """
    train_dataset = round(len(train) / (len(train) + len(test)),1)
    test_dataset = round(len(test) / (len(train) + len(test)),1)
    expected_train_size = 0.8
    expected_test_size = 0.2
    # Check if the training dataset has the expected size
    assert train_dataset == expected_train_size, f"Expected training dataset size: {expected_train_size}, Actual size: {train_dataset}"

    # Check if the test dataset has the expected size
    assert test_dataset == expected_test_size, f"Expected test dataset size: {expected_test_size}, Actual size: {test_dataset}"
