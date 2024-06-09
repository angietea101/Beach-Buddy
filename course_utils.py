from cache_system import ensure_cache_initialized, CLASS_CACHE_FALL, CLASS_CACHE_SUMMER, initialize_caches
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
    elif season == "summer_2024":
        for key in CLASS_CACHE_SUMMER.items():
            if abbreviation in key[0]:
                match = re.search(pattern, key[0])
                if match:
                    course_codes.append(match.group())
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


def main():
    initialize_caches()
    # print(CLASS_CACHE_FALL)
    print(get_course_codes("fall_2024", "CECS"))


if __name__ == "__main__":
    main()

