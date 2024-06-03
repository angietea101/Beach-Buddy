import csv
from csulb_course import CSULBCourse

CLASS_CACHE_SUMMER = {}
CLASS_CACHE_FALL = {}


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


def ensure_cache_initialized():
    if not CLASS_CACHE_FALL or not CLASS_CACHE_SUMMER:
        raise RuntimeError("Cache has not been created.")


def create_cache(cache_dict, file_path):
    with open(file_path, 'r', encoding='windows-1252') as file:
        reader = csv.reader(file)
        for line in reader:
            course_string = ', '.join(map(str, line))
            if line[0] not in cache_dict:
                cache_dict[line[0]] = []
            cache_dict[line[0]].append(create_CSULBCourse_object(course_string))
    print(f"Successfully created cache in {file_path}.")


def initialize_caches():
    # key: abbreviation + course code, value: CSULBCourse object
    create_cache(CLASS_CACHE_FALL, "seasons/fall_2024.csv")
    create_cache(CLASS_CACHE_SUMMER, "seasons/summer_2024.csv")


def main():
    fall = "fall_2024"
    summer = "summer_2024"
    # key: abbreviation + course code, value: CSULBCourse object
    initialize_caches()
    # print(get_course_codes(fall, "CECS"))
    # print(check_existing_abbreviation(fall, "CECS"))


if __name__ == "__main__":
    main()
