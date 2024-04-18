class CSULBCourse:
    def __init__(self, course_abr, course_name, section, number, reserved_cap, class_notes, class_type, days, time,
                 open_seats, location, instructor, comment):
        self._course_abr = course_abr
        self._course_name = course_name
        self._course_section = section
        self._course_number = number
        self._reserved_cap = reserved_cap
        self._class_notes = class_notes
        self._type = class_type
        self._days = days
        self._time = time
        if open_seats == "NONE":
            self._open_seats = False
        else:
            self._open_seats = True
        self._location = location
        self._instructor = instructor
        self._comment = comment

    def __str__(self):
        if not self._open_seats:
            self._open_seats = 'CLOSED'
        else:
            self._open_seats = 'OPEN'
        return (f'{self._course_abr}: {self._course_name}: {self._type}\n'
                f'Professor: {self._instructor}\n'
                f'Section number: {self._course_section} Course Number: {self._course_number}\n'
                f'Reserved Seats: {self._reserved_cap} Open Seats: {self._open_seats}\n'
                f'Location: {self._location} Days: {self._days} Time: {self._time}\n'
                f'Additional Notes: {self._comment}\n')
