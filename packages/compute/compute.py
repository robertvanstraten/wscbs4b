#!/usr/bin/python3


import sys
import os
import json

from preprocess import one_hot, drop_columns, impute_median, standardize
from model import train_model, predict


def main():
    command = sys.argv[1]
    test_path = f"{json.loads(os.environ['FILEPATH'])}/test.csv"
    train_path = f"{json.loads(os.environ['FILEPATH'])}/train.csv"
    
    if command == "one_hot":
        filepath_out = one_hot(test_path)
        filepath_out = one_hot(train_path)
        return

    if command == "drop_columns":
        filepath_out = drop_columns(test_path)
        filepath_out = drop_columns(train_path)
        return

    if command == "impute_median":
        filepath_out = impute_median(test_path)
        filepath_out = impute_median(train_path)
        return

    if command == "standardize":
        filepath_out = standardize(test_path)
        filepath_out = standardize(train_path)
        return

    if command == "train_model":
        filepath_model = train_model(train_path)
        return

    if command == "predict":
        model_path = f"{json.loads(os.environ['MODEL'])}/model.pickle"
        filepath_out = predict(model_path, test_path)
        return


if __name__ == '__main__':
    main()
