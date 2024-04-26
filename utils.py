"""
File: utils.py
Author: Angie Tran and Diego Cid
Description: Utility file that includes any utility functions and helper functions
"""
from csulb_course import CSULBCourse
import pandas as pd
import numpy as np


def get_course_codes(subject_file: str):
    column_to_read = [0]
    dataframe = pd.read_csv(subject_file, usecols=column_to_read)
    data_array = dataframe.to_numpy()
    data_list = list(np.ravel(data_array))
    codes = [course.split()[1] for course in data_list]
    return codes


def reformat_course_name(course_name):
    course_renamed = course_name.replace('-', '').replace(' ', '_').lower()
    return course_renamed


def csv_to_dictionary(subjects_csv):
    subjects_dict = {}
    with open(subjects_csv, 'r') as file:
        for line in file:
            subject, abbreviation = line.strip().split(', ')
            subject = reformat_course_name(subject)
            subjects_dict[abbreviation] = subject
    return subjects_dict


def create_CSULBCourse_objects(file_name: str):
    """
    Creates CSULBCourse objects of all courses obtained in the given text file
    file_name -- The file .txt that contains the scraped data
    Return a list that contains all the objects
    """
    with open(file_name, 'r') as file:
        courses = []
        for line in file:
            data = line.strip().split(', ')
            course_abr = data[0]
            course_name = data[1]
            units = data[2]
            section = data[3]
            number = data[4]
            reserved_cap = data[6]
            class_notes = data[7]
            class_type = data[8]
            days = data[9]
            time = data[10]
            open_seats = data[11]
            location = data[12]
            instructor = data[13]
            comment = data[14]
            courses.append(
                CSULBCourse(course_abr, course_name, units, section, number, reserved_cap, class_notes, class_type,
                            days, time,
                            open_seats, location, instructor, comment))
    return courses


def main():
    fall_path = "seasons/fall_2024"
    summer_path = "seasons/summer_2024"
    subjects_csv = "subjects.csv"
    subjects_abbreviation = csv_to_dictionary(subjects_csv)
    subjects_keys_list = list(subjects_abbreviation.keys())
    subject = "/accountancy_scraped_data.csv"
    file_path = fall_path + subject
    print(get_course_codes(file_path))


if __name__ == "__main__":
    main()