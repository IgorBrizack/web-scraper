import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError
import time
from tech_news.database import create_news


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
    bs_select = BeautifulSoup(html_content, "html.parser")

    result = bs_select.find_all("a", class_="cs-overlay-link")

    refactored_result = []

    for a in result:
        refactored_result.append(str(a["href"]))

    return refactored_result


# Requisito 3
def scrape_next_page_link(html_content):
    bs_select_next = BeautifulSoup(html_content, "html.parser")

    try:
        result = bs_select_next.find_all("a", class_="next page-numbers")
        return str(result[0]["href"])
    except Exception:
        None


# Requisito 4
def scrape_news(html_content):
    bs_selec_page = BeautifulSoup(html_content, "html.parser")

    content = {
        "url": str(bs_selec_page.find_all("link", rel="canonical")[0]["href"]),
        "title": str(
            bs_selec_page.find_all("h1", class_="entry-title")[0].text.strip()
        ),
        "timestamp": str(
            bs_selec_page.find_all("li", class_="meta-date")[0].text
        ),
        "writer": str(bs_selec_page.find_all("a", class_="url fn n")[0].text),
        "reading_time": int(
            (
                (
                    bs_selec_page.find_all("li", class_="meta-reading-time")[
                        0
                    ].text
                ).split(" ")
            )[0]
        ),
        "summary": str(bs_selec_page.main.article.div.find("p").text.strip()),
        "category": str(
            bs_selec_page.find_all("span", class_="label")[0].text
        ),

    }

    return content


# Requisito 5
def get_tech_news(amount):
    url = fetch('https://blog.betrybe.com')
    data = scrape_updates(url)
    result = []

    while len(data) < amount:
        new_page_url = scrape_next_page_link(url)
        url = fetch(new_page_url)
        new_links = scrape_updates(url)
        data.extend(new_links)

    for link in data:
        if len(result) == amount:
            break
        html = fetch(link)
        result.append(scrape_news(html))

    create_news(result)
    return result
