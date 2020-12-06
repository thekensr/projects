"""
Simple python scraper to get weekly menu from my favourite restaurant
in Brno.
"""

import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

URL = "https://padagali.cz/denni-menu/index.php"
PAGE = requests.get(URL)
PARSED_PAGE_CONTENT = bs(PAGE.content, "html.parser")


def group_target_items_by_class():
    """
    Gets first 20 elements with matching class
    for further processing
    """

    menu_name = PARSED_PAGE_CONTENT.find_all("h5", class_="glf-mor-restaurant-menu-item-name")[:20]
    menu_description = PARSED_PAGE_CONTENT.find_all(class_="glf-mor-restaurant-menu-item-description")[:20]
    menu_price = PARSED_PAGE_CONTENT.find_all(class_="glf-mor-restaurant-menu-item-price")[:20]

    return (menu_name, menu_description, menu_price)


def order_menu_items():
    """
    Orders menu items to triplets
    """
    ordered_menu = []

    menu, description, price = group_target_items_by_class()

    for i in range(len(menu)):
        menu_item = menu[i].get_text()
        matching_description = description[i].get_text()
        item_price = price[i].get_text()

        ordered_menu.append((menu_item, matching_description, item_price))

    return ordered_menu


def sort_items_by_days():
    """
    Sorts ordered triplets by days,
    every day gets 5 triplets
    """

    days = {
            "Pondelok": "",
            "Utorok": "",
            "Stvrtok": "",
            "Piatok": ""
            }

    ordered_menu = order_menu_items()

    for key in days:
        days[key] = ordered_menu[:5]
        ordered_menu = ordered_menu[5:]

    return days


def pretty_print():
    processed_strings = []
    days = sort_items_by_days()

    for key in days:
        processed_strings.append([' - '.join(array) for array in days[key]])

    return processed_strings


def format_to_write():
    DAY = datetime.today().weekday()
    PON, UT, STV, PIA = pretty_print()

    formated_daily_menus = {
                            0: '\n'.join(PON),
                            1: '\n'.join(UT),
                            3: '\n'.join(STV),
                            4: '\n'.join(PIA)
                            }
    try:
        return formated_daily_menus[DAY]
    except KeyError:
        return "No menu for today"

if __name__ == "__main__":
    print(format_to_write())

