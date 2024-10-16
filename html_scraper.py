# Copyright 2024 Angie Tran, Diego Cid
#
# This file is part of Beach Buddy.
# Beach Buddy is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Free Software Foundation, either version 1 of the License, or
# (at your option) any later version.
#
# Beach Buddy is distributed in the hope that it will be useful,
# but WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# See the MIT License for more details.
#
# You should have received a copy of the MIT License
# along with Beach Buddy. If not, see <https://mit-license.org/>.

from bs4 import BeautifulSoup
import requests
import os


def delete_csv_file(csv_file_name):
    if os.path.isfile(csv_file_name):
        os.remove(csv_file_name)
    else:
        return


def write_data_to_file(csv_file_path, url):
    response = requests.get(url)
    course_blocks = ""
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        course_blocks = soup.find_all('div', class_='courseBlock')
    else:
        print("Error: This subject does not exist. Make sure the abbreviation is typed correctly.\n"
              "Example: CECS, MATH, or BIOL")
        return

    with open(csv_file_path, 'a') as file:
        for course_block in course_blocks:
            course_code = course_block.find('span', class_='courseCode').text
            course_title = course_block.find('span', class_='courseTitle').text
            course_title = course_title.replace(',', '')
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
                        elif div_tag and div_tag.find('img') and div_tag.img.get('title') == "Reserve Capacity" and \
                                div_tag.img.get('width') == "55":
                            row_data.append('RESERVED SEATS')
                        elif div_tag and div_tag.find('img') and div_tag.img.get('title') == "Reserve Capacity":
                            row_data.append('OPEN (RESERVED)')
                        elif cell.text.strip() == '':
                            # If the cell is empty, replace it with 'NONE'
                            row_data.append("NONE")
                        else:
                            # Otherwise, extract and append the text from the cell
                            full_text = ""
                            text = cell.contents
                            for item in text:
                                item_string = str(item)
                                if "href=" in item_string:
                                    text_replaced = cell.text.replace(',', ' ')
                                    full_text += text_replaced.strip()
                                elif "<br/>" not in item_string:
                                    text_stripped = item_string.strip()
                                    text_replaced = text_stripped.replace('\n', ' ')
                                    text_replaced = text_replaced.replace(',', ' ')
                                    full_text += f" {text_replaced}"
                                    full_text = full_text[1:]
                            row_data.append(full_text)
                    # Write the row data into the file with comma-separated values
                    if len(row_data) > 3:
                        file.write(', '.join(row_data) + '\n')


def main():
    # subject = input("Subject abbreviation: ").upper()
    return


if __name__ == "__main__":
    main()
