import requests
from bs4 import BeautifulSoup

url = 'https://commeventshub.onrender.com/'

try:
    response = requests.get(url)
    # make sure the status is 200
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'html.parser')

    badge_element = soup.find('span', class_='badge bg-primary')

    # check whether finded the element
    if badge_element:
        # If found, take the context (.text)
        count_text = badge_element.text
        
        print(f"The number of activities displayed on the webpage is: {count_text}")
    else:
        # If not found
        print("Error: The <span class='badge bg-primary'> element was not found on the page.")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")