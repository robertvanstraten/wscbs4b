#!/usr/bin/python3
'''
Entrypoint for the visualization package.
'''
import os
import sys
import json

from visualise import plot_bar_gender, plot_hist_age, plot_hist_fare, plot_heat_class_gender

def main():
    command = sys.argv[1]
    data_path = f"{json.loads(os.environ['FILEPATH'])}/test_complete.csv"

    if command == "plot_bar_gender":
        filepath_out = plot_bar_gender(data_path)
        return

    if command == "plot_hist_fare":
        filepath_out = plot_hist_fare(data_path)
        return

    if command == "plot_hist_age":
        filepath_out = plot_hist_age(data_path)
        return
    
    if command == "heat_class_gender":
        filepath_out = plot_heat_class_gender(data_path)
        return

if __name__ == '__main__':
    main()
