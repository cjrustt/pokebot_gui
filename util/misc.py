import os
import datetime
import json
import re
import requests

import pytz
from lxml.html import fromstring


def append_timestamp(timezone, message):
    try:
        # Get current time in the given timezone
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        timestamp = now.strftime('%m-%d-%Y %H:%M:%S %Z')

        # Separate by newline, print separately
        split_message = message.split(sep='\\n')

        for line in split_message:
            return f"[{timestamp}]  {line}"

    except Exception as e:
        return f"append_timestamp Error: {e}\n  Original message: {message}"


def read_config(default=False):
    if default:
        file = 'util/default_config.json'
    else:
        file = 'util/config.json'

    with open(file, 'r') as f:
        return json.load(f)


def write_config(data: dict):
    with open('util/config.json', 'w') as f:
        json.dump(data, f, indent=4)
        return None


def parse_target_url(url) -> dict:
    """ 1. Cleans trailing information from URL
        2. Parses product ID from URL
        3. Extracts product name from HTML
        4. Extracts product image and saves to local project directory
        5. Returns dictionary containing product information
    """
    # Removes trailing information from url
    clean_url = url.split('#')[0]

    # Gathers product ID from URL
    product_id = clean_url.split('/A-')[1]

    # Gathers HTML elements from given URL
    response = requests.get(clean_url)
    html_content = response.text
    soup = fromstring(html_content)

    # Gathers the product name
    raw_product_name = soup.xpath("//title/text()")[0]
    product_name = raw_product_name.split(': Target')[0].strip()

    # Gathers all image elements, selects the main product image
    # & extracts the direct image URL
    match = re.search(r'https://target\.scene7\.com/is/image/Target/[^" ]+', html_content)
    img_url = match.group(0)

    # Downloads the image file and saves in the project
    # images/ directory, under the name '<product_id>.jpg'
    image_file_path = f'images/{product_id}.jpg'

    # Checks if the file already exists locally before downloading the image
    if os.path.exists(image_file_path):
        pass
    else:
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            with open(image_file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
        else:
            print("Failed to download image.")

    product_information = {
        'name': product_name,
        'url': clean_url,
        'id': product_id,
        'image_file_path': image_file_path
    }

    return product_information


def parse_refresh_time(value):
    # Returns a string if passed an integer, returns an integer if passed a string
    str_dict = {
        '1 second': 1,
        '2 seconds': 2,
        '3 seconds': 3,
        '4 seconds': 4,
        '5 seconds': 5,
        '6 seconds': 6,
        '7 seconds': 7,
        '8 seconds': 8,
        '9 seconds': 9,
        '10 seconds': 10,
        '11 seconds': 11,
        '12 seconds': 12,
        '13 seconds': 13,
        '14 seconds': 14,
        '15 seconds': 15,
        '20 seconds': 20,
        '30 seconds': 30,
        '1 minute': 60,
        '2 minutes': 120,
        '5 minutes': 300
    }
    int_dict = {
        1: '1 second',
        2: '2 seconds',
        3: '3 seconds',
        4: '4 seconds',
        5: '5 seconds',
        6: '6 seconds',
        7: '7 seconds',
        8: '8 seconds',
        9: '9 seconds',
        10: '10 seconds',
        11: '11 seconds',
        12: '12 seconds',
        13: '13 seconds',
        14: '14 seconds',
        15: '15 seconds',
        20: '20 seconds',
        30: '30 seconds',
        60: '1 minute',
        120: '2 minutes',
        300: '5 minutes'
    }

    if type(value) == int:
        return int_dict[value]
    else:
        return str_dict[value]

