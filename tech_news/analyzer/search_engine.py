from tech_news.database import search_news
from datetime import datetime as d


# Requisito 7
def search_by_title(title):
    result = []
    news = search_news({})

    for content in news:
        if title.lower() in content['title'].lower():
            result.append((content['title'], content['url']))

    return result


# Requisito 8
def search_by_date(date):
    result = []
    try:
        converted_data = (d.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y"))
    except ValueError:
        raise ValueError('Data inválida')

    news = search_news({'timestamp': converted_data})

    if len(news) == 0:
        return []

    for content in news:
        result.append((content['title'], content['url']))

    return result


# Requisito 9
def search_by_category(category):
    result = []
    news = search_news({})

    if len(news) == 0:
        return []

    for content in news:
        if category.lower() in content['category'].lower():
            result.append((content['title'], content['url']))

    return result
