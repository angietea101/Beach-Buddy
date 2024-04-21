from bs4 import BeautifulSoup
import requests


def write_data_to_file(subject, course_blocks):
    file_name = str(f"{subject.lower()}_scraped_data.txt")

    with open(file_name, 'w') as file:
        for course_block in course_blocks:
            course_code = course_block.find('span', class_='courseCode').text
            course_title = course_block.find('span', class_='courseTitle').text
            units = course_block.find('span', class_='units').text

            # Find all tables within the current course block
            tables = course_block.find_all('table', class_='sectionTable')
            for table in tables:
                rows = table.find_all('tr')
                for i, row in enumerate(rows):
                    if i == 0:
                        continue
                    cells = row.find_all(['td', 'th'])

                    # Extract and organize data from each row
                    row_data = [course_code, course_title, units]
                    for cell in cells:
                        div_tag = cell.find('div')
                        if div_tag and div_tag.find('img') and div_tag.img.get('title') == "Seats available":
                            # If an image is found, append 'Open' to indicate open seats
                            row_data.append("OPEN")
                        elif div_tag and div_tag.find('img') and div_tag.img.get('title') == "Reserve Capacity" and div_tag.img.get('width') == "55":
                            row_data.append('RESERVED SEATS')
                        elif div_tag and div_tag.find('img') and div_tag.img.get('title') == "Reserve Capacity":
                            row_data.append('OPEN (RESERVED)')
                        elif cell.text.strip() == '':
                            # If the cell is empty, replace it with 'NONE'
                            row_data.append("NONE")
                        else:
                            # Otherwise, extract and append the text from the cell
                            row_data.append(cell.text.strip())
                    # Write the row data into the file with comma-separated values
                    if len(row_data) > 3:
                        file.write(', '.join(row_data) + '\n')


def main():
    subject = input("Subject abbreviation: ").upper()
    url = 'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/' + subject + '.html'
    response = requests.get(url)

    # Check if response was successful
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        course_blocks = soup.find_all('div', class_='courseBlock')
    else:
        print("Error: This subject does not exist. Make sure the abbreviation is typed correctly.\n"
              "Example: CECS, MATH, or BIOL")
        return

    write_data_to_file(subject, course_blocks)


if __name__ == "__main__":
    main()
