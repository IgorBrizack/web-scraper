from tech_news.database import search_news
from datetime import datetime as d


# Requisito 7
def search_by_title(title):
    news = search_news({})
    result = []

    for content in news:
        if title.lower() in content['title'].lower():
            result.append((content['title'], content['url']))

    return result


# Requisito 8
def search_by_date(date):
    try:
        converted_data = (d.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y"))
    except ValueError:
        raise ValueError('Data inválida')

    news = search_news({'timestamp': converted_data})
    result = []

    if len(news) == 0:
        return []

    for content in news:
        result.append((content['title'], content['url']))

    return result
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
