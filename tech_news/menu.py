from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
import sys


# Requisitos 11 e 12
def zero_option():
    qty_news = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(int(qty_news))


def first_option():
    title = input("Digite o título:")
    return print(search_by_title(title))


def second_option():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return print(search_by_date(date))


def third_option():
    category = input("Digite a categoria:")
    return print(search_by_category(category))


def fourth_option():
    return print(top_5_categories())


def fifth_option():
    return print("Encerrando script")


def analyzer_menu():
    selected = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n 5 - Sair."
    )

    options = {
        "0": zero_option,
        "1": first_option,
        "2": second_option,
        "3": third_option,
        "4": fourth_option,
        "5": fifth_option
    }

    try:
        return options[selected]()
    except Exception:
        return sys.stderr.write("Opção inválida\n")
