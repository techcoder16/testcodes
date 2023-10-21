# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # Set the user agent to avoid bot detection

# import time
# search_query = "agent Multi Purpose Amplifier MK"
# headers = {"User-Agent": "Mozilla/5.0"}
# cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}

# url = f"https://www.google.com/search?q={search_query}&tbm=shop"

# # Send a GET request with the headers
# response = requests.get(url, headers=headers, cookies=cookies)

# print(response.text)


# if response.status_code == 200:
#     # Check if the "Before continuing to Google" page is present
#     # Check if the "Before continuing to Google" page is present
#     if "Accept all" in response.text:
#         # Extract the URL for accepting cookies from the response
#         cookie_url = response.url

#         # Send a POST request to the consent API
#         consent_url = f"https://consent.google.com/{cookie_url.split('/')[4]}/consent"
#         payload = {
#             "continue": cookie_url,
#             "gl": "US",  # Adjust the location as needed
#             "m": "0",
#             "pc": "null",
#             "wp": "null",
#         }
#         response = requests.post(consent_url, data=payload)
        

#         if response.status_code == 200:
#             # Continue with your scraping code as before
#             soup = BeautifulSoup(response.text, 'html.parser')
#             print(soup)


#     else:
#         print("No 'Before continuing to Google' page. Proceeding with scraping.")
#         soup = BeautifulSoup(response.text, 'html.parser')
#         # Continue with your scraping code as before

# else:
#     print("Failed to retrieve the page.")


import requests
from bs4 import BeautifulSoup

import time
search_query = "agent Multi Purpose Amplifier MK"

url = f"https://www.google.com/search?q={search_query}&tbm=shop"


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"
}
cookies = {"CONSENT": "YES+cb.20220419-08-p0.cs+FX+111"}



cookies = {'CONSENT': 'PENDING+987', 'SOCS': 'CAESHAgBEhJnd3NfMjAyMzA4MTAtMF9SQzIaAmRlIAEaBgiAo_CmBg' }


r = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(r.content, "html.parser")
with open("output.html", "w", encoding="utf-8") as html_file:
    html_file.write(soup.prettify())  # This writes the HTML data with proper formatting




print(soup.prettify())