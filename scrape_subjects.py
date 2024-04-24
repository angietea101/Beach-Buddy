import html_scraper
import os.path
import time

file_name = "subjects.txt"


def scrape_fall():
    with open(file_name, 'r') as file:
        links = []
        file_paths = []
        for line in file:
            data = line.strip().split(', ')
            # gets rid of  - in subject names in order to name the files properly
            course_name = data[0].replace('-', '')
            course_abr = data[1]

            # link to request html
            subject_html = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/" \
                           + course_abr + ".html"
            # os path to the folders
            path = os.path.join("seasons/fall_2024", course_name.replace(' ', '_') + "_scraped_data.txt")

            # add the data to a list
            links.append(subject_html)
            file_paths.append(path)

    for i in range(len(links)):
        html_scraper.write_data_to_file(file_paths[i], links[i])


def main():
    scrape_fall()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
