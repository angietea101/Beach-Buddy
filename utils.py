"""
File: utils.py
Author: Angie Tran and Diego Cid
Description: Utility file that includes any utility functions and helper functions
"""
from csulb_course import CSULBCourse
import pandas as pd
import numpy as np
import csv


def get_csv_path(season: str, abbreviation: str, subjects_abbreviation: dict):
    """
    Get the .csv file name given the abbreviation
    :season: season of the desired course
    :abbreviation: the abbreviation of the course
    :subjects_abbreviation: dictionary of the subjects with key abbreviation and value full name
    :return: string name of the file path
    """
    full_name = subjects_abbreviation[abbreviation]
    csv_path = f"seasons/{season}/{full_name}_scraped_data.csv"
    return csv_path


def get_course_codes(subject_file: str):
    """
    Get a set of all available course codes given a subject
    :param subject_file: the subject file with all course sections
    :return: a list of valid course codes
    """
    column_to_read = [0]
    dataframe = pd.read_csv(subject_file, usecols=column_to_read)
    data_array = dataframe.to_numpy()
    data_list = set(np.ravel(data_array))
    codes = [course.split()[1] for course in data_list]
    return codes


def get_class_infos(season: str, abbreviation: str, csv_dictionary: dict, code: str):
    """
    Get all class section information given a course
    :param season: the season of the course
    :param abbreviation: the abbreviation i.e. CECS, MATH, BIOL
    :param csv_dictionary: a dictionary with the abbreviation as the key and the full name of the course as the value
    :param code: the course code i.e. 100, 329, 491A
    :return: list of objects with all sections of the course
    """
    csv_file = get_csv_path(season, abbreviation, csv_dictionary)
    course = f"{abbreviation} {code}"
    all_courses = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == course:
                course_string = ', '.join(map(str, line))
                all_courses.append(create_CSULBCourse_object(course_string))
    return all_courses


def reformat_course_name(course_name: str):
    """
    :param course_name: the full course name
    :return: string of the full course name reformatted to file naming name
    """
    course_renamed = course_name.replace('-', '').replace(' ', '_').lower()
    return course_renamed


def csv_to_dictionary(subjects_csv: str):
    """
    :param subjects_csv: subjects.csv file of all available subjects full name and the corresponding abbreviation
    :return: dictionary of abbreviation as the key and the full name as the value
    """
    subjects_dict = {}
    with open(subjects_csv, 'r') as file:
        for line in file:
            subject, abbreviation = line.strip().split(', ')
            subject = reformat_course_name(subject)
            subjects_dict[abbreviation] = subject
    return subjects_dict


def create_CSULBCourse_object(course: str):
    """
    Create CSULBCourse object of course string
    :course: A string with all the course information separated by commas
    :return: a CSULBCourse object
    """
    data = course.strip().split(', ')
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
    return CSULBCourse(course_abr, course_name, units, section, number, reserved_cap, class_notes,
                       class_type, days, time, open_seats, location, instructor, comment)


def main():
    fall_path = "seasons/fall_2024"
    summer_path = "seasons/summer_2024"
    subjects_csv = "subjects.csv"
    subjects_abbreviation = csv_to_dictionary(subjects_csv)
    subjects_keys_list = list(subjects_abbreviation.keys())
    csv_path = get_csv_path("fall_2024", "CECS", subjects_abbreviation)
    course_infos = get_class_infos("summer_2024", "CECS", subjects_abbreviation, "326")
    print(course_infos)


if __name__ == "__main__":
    main()
