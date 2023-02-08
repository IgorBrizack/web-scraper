import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError
import time


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        result = requests.get(url, headers={"user-agent": "Fake user-agent"})
        result.raise_for_status()
    except (ReadTimeout, ConnectionError, HTTPError):
        return None

    return result.text


# Requisito 2
def scrape_updates(html_content):
    bs_select = BeautifulSoup(html_content, 'html.parser')

    result = bs_select.find_all('a', class_='cs-overlay-link')

    refactored_result = []

    for a in result:
        refactored_result.append(str(a['href']))

    return refactored_result


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
