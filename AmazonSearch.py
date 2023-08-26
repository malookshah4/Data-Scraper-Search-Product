import time

import pandas as pd
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_item_details(item):
    title = item.find_element(By.CLASS_NAME, "search-card-e-title").text
    price = item.find_element(By.CLASS_NAME, "search-card-e-price-main").text
    min_order = item.find_element(By.CLASS_NAME, "search-card-m-sale-features__item").text
    link = item.find_element(By.CSS_SELECTOR,
                             '#root > div > div.app-organic-search__main-body > div.app-organic-search__content '
                             '> div >  div > div > div:nth-child(2) > div.card-info.list-card-layout__info > h2 > '
                             'a').get_attribute('href')
    return {
        'title': title,
        'price': price,
        'min_order': min_order,
        'link': link
    }


class Search:

    def __init__(self):
        self.option = wb.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.driver = wb.Chrome(options=self.option)

    def search_input(self, link, search_item_name):
        item_list = []

        self.driver.get(link)
        time.sleep(2)

        input_search = self.driver.find_element(By.XPATH,
                                                '//*[@id="J_SC_header"]/header/div[3]/div/div/div[2]/div/div[1]/div/input')

        input_search.send_keys(search_item_name)
        input_search.send_keys(Keys.ENTER)
        time.sleep(1)

        items = self.driver.find_elements(By.CLASS_NAME, "card-info")
        print(len(items))
        for i in items:
            title = i.find_element(By.CLASS_NAME, "search-card-e-title").text
            price = i.find_element(By.CLASS_NAME, "search-card-e-price-main").text
            link = i.find_element(By.TAG_NAME, "a").get_attribute("href")

            product = {
                "title": title,
                "price": price,
                "link": link
            }

            print(product)
            item_list.append(product)
        print(len(item_list))
        data = pd.DataFrame(item_list)
        data.to_csv(f"{search_item_name}.csv")
        self.driver.close()




