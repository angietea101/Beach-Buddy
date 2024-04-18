from bs4 import BeautifulSoup
import requests
url = 'http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/CECS.html'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(response.text, 'html.parser')
course_blocks = soup.find_all('div', class_='courseBlock')
for course_block in course_blocks:
    course_code = course_block.find('span', class_='courseCode').text
    course_title = course_block.find('span', class_='courseTitle').text
    units = course_block.find('span', class_='units').text
    print("Course Code:", course_code)
    print("Course Title:", course_title)
    print("Units:", units)

    # Find all tables within the current course block
    tables = course_block.find_all('table', class_='sectionTable')
    for table in tables:
        rows = table.find_all('tr')
        for i, row in enumerate(rows):
            if i == 0:
                continue
            cells = row.find_all(['td', 'th'])
            # Extract and organize data from each row
            row_data = [cell.text.strip() for cell in cells]
            # Print the row data in the specified format
            print('\t'.join(row_data))
        print()  # Print an extra line between tables
    print()  # Print an extra line between course blocks from bs4 import BeautifulSoup
