"""
File: main.py
Author: Angie Tran and Diego Cid
Description: Main function to run our script
"""
from csulb_course import CSULBCourse


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
            section = data[3]
            number = data[4]
            reserved_cap = data[5]
            class_notes = data[6]
            class_type = data[8]
            days = data[9]
            time = data[10]
            open_seats = data[11]
            location = data[12]
            instructor = data[13]
            comment = data[14]
            courses.append(
                CSULBCourse(course_abr, course_name, section, number, reserved_cap, class_notes, class_type, days, time,
                            open_seats, location, instructor, comment))
    return courses


def main():
    courses = create_CSULBCourse_objects('cecs_scraped_data.txt')
    # Print each course
    user_course = input("Enter course number: ")
    print("Courses currently open:\n")
    for course in courses:
        user_course.upper()
        if course.course_abr == user_course and course.open_seats is True:
            print(course)


if __name__ == "__main__":
    main()
