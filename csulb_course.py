class CSULBCourse:
    def __init__(self, course_abr, course_name, units, section, number, reserved_cap, class_notes, class_type, days,
                 time, open_seats, location, instructor, comment):
        self._course_abr = course_abr
        self._course_name = course_name
        self._units = units
        self._course_section = section
        self._course_number = number
        if reserved_cap.strip() == "RESERVED SEATS":
            self._reserved_cap = True
        else:
            self._reserved_cap = False
        self._class_notes = class_notes
        self._type = class_type
        self._days = days
        self._time = time
        self._open_seats = open_seats
        self._location = location
        self._instructor = instructor
        self._comment = comment

    def __str__(self):
        if self._open_seats == 'NONE':
            self._open_seats = 'CLOSED'
        if self._open_seats == 'OPEN (RESERVED)':
            self._open_seats = 'OPEN'
        return (f'{self._course_abr}: {self._course_name} {self._type} ({self._units})\n'
                f'Professor: {self._instructor}\n'
                f'Section number: {self._course_section}\t\tCourse Number: {self._course_number}\n'
                f'Reserved Seats: {self._reserved_cap}\tOpen Seats: {self._open_seats}\n'
                f'Location: {self._location}\t\tDays: {self._days}\t\t\tTime: {self._time}\n'
                f'Additional Notes: {self._comment}\n')

    @property
    def course_abr(self):
        return self._course_abr

    @property
    def course_name(self):
        return self._course_name

    @property
    def units(self):
        return self._units

    @property
    def course_section(self):
        return self._course_section

    @property
    def course_number(self):
        return self._course_number

    @property
    def reserved_cap(self):
        if self._reserved_cap is True:
            return "TRUE"
        else:
            return "False"

    @property
    def class_notes(self):
        return self.class_notes

    @property
    def type(self):
        return self._type

    @property
    def days(self):
        return self._days

    @property
    def time(self):
        return self._time

    @property
    def open_seats(self):
        return self._open_seats

    @open_seats.setter
    def open_seats(self, open_seats: str):
        if open_seats == "NONE":
            self._open_seats = False
        else:
            self._open_seats = True

    @property
    def location(self):
        return self._location

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, new_instructor):
        self._instructor = new_instructor

    @property
    def comment(self):
        return self._comment
