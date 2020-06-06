def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    TP, FN, FP, TN = (0, 0, 0, 0)

    for y_test, y_train in zip(prediction, ground_truth):
        if y_test == True and y_train == True:
            TP += 1
        if y_test == False and y_train == True:
            FN += 1
        if y_test == True and y_train == False:
            FP += 1
        if y_test == False and y_train == False:
            TN += 1

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    f1 = 2 * (precision * recall) / (precision + recall)
    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = 0
    cnt_truth = 0
    for y_pred, y_test in zip(prediction, ground_truth):
        if y_pred == y_test:
            cnt_truth += 1

    accuracy = cnt_truth / len(prediction)

    return accuracy
