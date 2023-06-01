#!/usr/bin/python3


import sys
import os
import json
import yaml
import pandas as pd

from preprocess import one_hot, drop_columns, impute_median, standardize
from model import train_model, predict, combine


def print_output(data: dict):
    """
    Creates a marked section in the standard output
    of the container in order for Brane to isolate the result.

    Parameters
    ----------
    data: `dict`
    Any valid Python dictionary that is YAML serializable.
    """
    print("--> START CAPTURE")
    print(yaml.dump(data))
    print("--> END CAPTURE")

def main():
    command = sys.argv[1]
    
    if command == "one_hot":
        data_path = json.loads(os.environ["FILEPATH"])
        one_hot(data_path)

    elif command == "drop_columns":
        data_path = json.loads(os.environ["FILEPATH"])
        drop_columns(data_path)

    elif command == "impute_median":
        data_path = json.loads(os.environ["FILEPATH"])
        impute_median(data_path)

    elif command == "standardize":
        data_path = json.loads(os.environ["FILEPATH"])
        standardize(data_path)

    elif command == "train_model":
        data_path = json.loads(os.environ["FILEPATH"])
        train_model(data_path)

    elif command == "predict":
        model_path = json.loads(os.environ['MODEL'])
        data_path = json.loads(os.environ["FILEPATH"])
        predict(model_path, data_path)

    elif command == "combine":
        submission = json.loads(os.environ['SUBMISSION'])
        data_path = json.loads(os.environ["FILEPATH"])
        combine(data_path, submission)    
    pass


if __name__ == '__main__':
    main()
