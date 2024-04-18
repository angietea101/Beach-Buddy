from CSULB_course import CSULBCourse
def main():
    courses = []
    with open('scraped_data.txt', 'r') as file:
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
                CSULBCourse(course_abr, course_name, section, number, reserved_cap, class_notes, class_type, days, time, open_seats,
                       location, instructor, comment))

    # Print each course

    user_course = input("Enter course to check open sections: ")
    for course in courses:
        user_course.upper()
        if course._course_abr == user_course and course._open_seats == 'Open':
            print(course)
main()