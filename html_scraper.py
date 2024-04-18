from bs4 import BeautifulSoup
import requests

url = 'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/CECS.html'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(response.text, 'html.parser')

course_blocks = soup.find_all('div', class_='courseBlock')
with open('scraped_data.txt', 'w') as file:
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
                    if cell.find('img'):
                        # If an image is found, append 'Open' to indicate open seats
                        row_data.append("Open")
                    elif cell.text.strip() == '':
                        # If the cell is empty, replace it with 'NONE'
                        row_data.append("NONE")
                    else:
                        # Otherwise, extract and append the text from the cell
                        row_data.append(cell.text.strip())
                # Write the row data into the file with comma-separated values
                if len(row_data) > 3:
                    file.write(', '.join(row_data) + '\n')