from cache_system import ensure_cache_initialized, CLASS_CACHE_FALL, CLASS_CACHE_SUMMER


def get_course_codes(season, abbreviation):
    course_codes = []
    ensure_cache_initialized()
    if season == "fall_2024":
        for key in CLASS_CACHE_FALL.items():
            if abbreviation in key[0]:
                to_string = str(key[0])
                stripped = to_string.split(" ", 1)[1]
                course_codes.append(stripped)
    elif season == "summer_2024":
        for key in CLASS_CACHE_SUMMER.items():
            if abbreviation in key[0]:
                to_string = str(key[0])
                stripped = to_string.split(" ", 1)[1]
                course_codes.append(stripped)
    else:
        print("An unexpected error occurred")
        return
    return course_codes


def check_existing_abbreviation(season, abbreviation):
    ensure_cache_initialized()
    if season == "fall_2024":
        for key in CLASS_CACHE_FALL.items():
            if abbreviation in key[0]:
                return True
    elif season == "summer_2024":
        for key in CLASS_CACHE_SUMMER.items():
            if abbreviation in key[0]:
                return True
    else:
        print("An unexpected error occurred")
        return
    return False

