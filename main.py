"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""
from csulb_course import CSULBCourse
from utils import csv_to_dictionary


def main():
    fall_path = "seasons/fall_2024"
    summer_path = "seasons/summer_2024"
    subjects_csv = "subjects.csv"
    subjects_abbreviation = csv_to_dictionary(subjects_csv)
    print(subjects_abbreviation)


if __name__ == "__main__":
    main()
