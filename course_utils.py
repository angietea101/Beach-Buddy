from cache_system import ensure_cache_initialized, CLASS_CACHE_FALL, CLASS_CACHE_SUMMER, initialize_caches, \
    CLASS_CACHE_SPRING
import re


def get_course_codes(season, abbreviation):
    course_codes = []
    ensure_cache_initialized()
    pattern = r'\b\d{2,3}[A-Z]?\b'
    if season == "fall_2024":
        for key in CLASS_CACHE_FALL.items():
            if abbreviation in key[0]:
                match = re.search(pattern, key[0])
                if match:
                    course_codes.append(match.group())
    elif season == "spring_2025":
        for key in CLASS_CACHE_SPRING.items():
            if abbreviation in key[0]:
                match = re.search(pattern, key[0])
                if match:
                    course_codes.append(match.group())
    else:
        print("An unexpected error occurred while getting course "
              "codes")
        return
    return course_codes


def check_existing_abbreviation(season, abbreviation):
    ensure_cache_initialized()
    if season == "fall_2024":
        for key in CLASS_CACHE_FALL.items():
            if abbreviation in key[0]:
                return True
    elif season == "spring_2025":
        for key in CLASS_CACHE_SPRING.items():
            if abbreviation in key[0]:
                return True
    else:
        print("An unexpected error occurred while checking existing "
              "abbreviation")
        return
    return False


def get_all_prof_course(last_name, course_abbr, cache):
    matching_courses = []

    for abbr, course_list in cache.items():
        if course_abbr not in abbr:
            continue  # Skip if the abbreviation doesn't match

        for course in course_list:
            if last_name.lower() in course.instructor.lower():
                matching_courses.append(course)

    return matching_courses


def get_courses_by_key_part(key_part, courses_dict):
    matching_courses = []

    for course_key, course_list in courses_dict.items():
        if key_part in course_key:
            matching_courses.extend(course_list)

    return matching_courses


def format_season(season: str):
    return season.lower().replace(" ", "_")

def main():
    initialize_caches()
    print(get_all_prof_course("Terrell", "CECS", CLASS_CACHE_FALL))
    print(get_courses_by_key_part("CECS", CLASS_CACHE_SPRING))
    print(check_existing_abbreviation("fall_2024", "CECS"))


if __name__ == "__main__":
    main()
