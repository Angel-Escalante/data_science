import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium_init import get_explorer
from selenium.webdriver.common.by import By

elements = {"title": [], "rating": [], "price": []}


def do_on_page_change(page):
    soup = BeautifulSoup(page, "html5lib")
    products = soup.findAll("div", attrs={"data-component-type": "s-search-result"})

    for product in products:
        title = product.find("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
        price = product.find("span", attrs={"class": "a-offscreen"})
        rating = product.find("span", attrs={"class": "a-size-base"})

        elements["title"].append(title.text)

        if price is not None:
            elements["price"].append(price.text)
        else:
            elements["price"].append("None")

        if rating is not None:
            elements["rating"].append(rating.text)
        else:
            elements["rating"].append("None")


def change_page(explorer, page):
    explorer.save_screenshot(f"page{page}.png")
    btn_next = explorer.find_element(By.XPATH, "//*[contains(text(), 'Siguiente')]")
    btn_next.click()


def main():
    options = ["--window-size = 1200, 1020"]
    explorer = get_explorer(options)
    explorer.get("https://www.amazon.com.mx/")

    text_search = explorer.find_element(By.ID, "twotabsearchtextbox")
    text_search.send_keys("laptop")
    text_search.submit()

    for x in range(3):
        time.sleep(1)
        do_on_page_change(explorer.page_source)
        change_page(explorer, x)

    data_frame = pd.DataFrame(elements)
    data_frame.to_csv("laptops_data.csv", encoding="utf-8")


main()
