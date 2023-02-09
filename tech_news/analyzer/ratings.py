from tech_news.database import search_news


def sort_items(items):
    rank = sorted(items)
    rank = sorted(rank, key=lambda rank: -rank[1])

    result = []
    for items in rank:
        result.append(items[0])
    return result


# Requisito 10
def top_5_categories():
    news = search_news({})
    categories = []
    helper = 0
    counter = 0

    for content in news:
        categories.append(content['category'])

    only_categories = set(categories)

    rank = []

    for category in only_categories:
        while helper < len(categories):
            if category == categories[helper]:
                counter += 1
            helper += 1
        rank.append((category, counter))
        counter = 0
        helper = 0

    return sort_items(rank)
