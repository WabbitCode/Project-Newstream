import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=False)
    page = browser.new_page()
    page.goto('https://www.koknystrom.se/')
    page.wait_for_selector('.dish')
    dish_elements = page.query_selector_all('.dish')

    menu_items = [{"Category": dish.query_selector('.category').inner_text().strip().replace("\xa0", " "),
                   'Dish': dish.query_selector('.dish-name').inner_text().strip().replace("\xa0", " ")}
                  for dish in dish_elements]

    with open("outcome.json", "w", encoding="utf-8") as file:
        json.dump(menu_items, file, ensure_ascii=False, indent=4)

    browser.close()
