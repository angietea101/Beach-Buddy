"""
File: utils.py
Author: Angie Tran and Diego Cid
Description: Utility file that includes any utility functions and helper functions
"""
from csulb_course import CSULBCourse


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
