from utils import *

SUMMER_PATH = "seasons/summer_2024.csv"
FALL_PATH = "seasons/fall_2024.csv"

# key: abbreviation + course code, value: CSULBCourse object
CLASS_CACHE_SUMMER = {}
CLASS_CACHE_FALL = {}


def create_cache_summer():
    with open(SUMMER_PATH, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            course_string = ', '.join(map(str, line))
            if line[0] not in CLASS_CACHE_SUMMER:
                CLASS_CACHE_SUMMER[line[0]] = []
            CLASS_CACHE_SUMMER[line[0]].append(create_CSULBCourse_object(course_string))
    print("Successfully created summer cache.")


def create_cache_fall():
    with open(FALL_PATH, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            course_string = ', '.join(map(str, line))
            if line[0] not in CLASS_CACHE_FALL:
                CLASS_CACHE_FALL[line[0]] = []
            CLASS_CACHE_FALL[line[0]].append(create_CSULBCourse_object(course_string))
    print("Successfully created fall cache.")
