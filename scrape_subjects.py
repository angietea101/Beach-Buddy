import html_scraper
import os.path
import csv
import time


def scrape_fall(subjects_file):
    with open(subjects_file, 'r') as file:
        links = []
        file_paths = []
        for line in file:
            data = line.strip().split(', ')
            # gets rid of  - in subject names in order to name the files properly
            course_name = data[0].replace('-', '').lower()
            course_abr = data[1]

            # link to request html
            subject_html = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/" \
                           + course_abr + ".html"
            # os path to the folders
            path = os.path.join("seasons/fall_2024", course_name.replace(' ', '_') + "_scraped_data.csv")

            # add the data to a list
            links.append(subject_html)
            file_paths.append(path)

    for i in range(len(links)):
        html_scraper.write_data_to_file(file_paths[i], links[i])


def scrape_summer(subjects_file):
    with open(subjects_file, 'r') as file:
        links = []
        file_paths = []
        for line in file:
            data = line.strip().split(', ')
            # gets rid of  - in subject names in order to name the files properly
            course_name = data[0].replace('-', '').lower()
            course_abr = data[1]

            # link to request html
            subject_html = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Summer_2024/By_Subject/" \
                           + course_abr + ".html"
            # os path to the folders
            path = os.path.join("seasons/summer_2024", course_name.replace(' ', '_') + "_scraped_data.csv")

            # add the data to a list
            links.append(subject_html)
            file_paths.append(path)

    for i in range(len(links)):
        html_scraper.write_data_to_file(file_paths[i], links[i])


def main():
    subjects_file = "subjects.csv"
    scrape_fall(subjects_file)
    scrape_summer(subjects_file)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
