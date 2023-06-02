#!/usr/bin/python3
'''
Entrypoint for the visualization package.
'''
import os
import sys
import json

from visualise import plot_bar_gender, plot_hist_age, plot_hist_fare, plot_heat_class_gender
from interface import generate_interface

def main():
    command = sys.argv[1]

    if command == "plot_bar_gender":
        data_path = f"{json.loads(os.environ['FILEPATH'])}/test_complete.csv"
        filepath_out = plot_bar_gender(data_path)
        return

    if command == "plot_hist_fare":
        data_path = f"{json.loads(os.environ['FILEPATH'])}/test_complete.csv"
        filepath_out = plot_hist_fare(data_path)
        return

    if command == "plot_hist_age":
        data_path = f"{json.loads(os.environ['FILEPATH'])}/test_complete.csv"
        filepath_out = plot_hist_age(data_path)
        return
    
    if command == "heat_class_gender":
        data_path = f"{json.loads(os.environ['FILEPATH'])}/test_complete.csv"
        filepath_out = plot_heat_class_gender(data_path)
        return

    if command == "generate_interface":
        plot_1 = f"{json.loads(os.environ['PLOT_1'])}/Survival Count by Gender.html"
        plot_2 = f"{json.loads(os.environ['PLOT_2'])}/Fare Distribution of Survivors by Gender.html"
        plot_3 = f"{json.loads(os.environ['PLOT_3'])}/Age Distribution of Survivors by Gender.html"
        plot_4 = f"{json.loads(os.environ['PLOT_4'])}/Survival Rate by Passenger Class and Gender.html"

        filepath_out = generate_interface([plot_1,plot_2,plot_3,plot_4])

if __name__ == '__main__':
    main()
