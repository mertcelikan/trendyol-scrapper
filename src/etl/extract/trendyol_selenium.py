#!/usr/bin/env python3
"""
This class is not used in the project. It is just an example of how to use Selenium for web scraping.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TrendyolSelenium:
    def __init__(self):
        self.url = "https://www.trendyol.com/gida-ve-icecek-x-c103946"
        self.__category = "Gıda ve İçecek"

    def __driver_init(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(50)
        return driver

    def __get_products(self, driver, num_products=100):
        driver.get(self.url)
        time.sleep(15)
        products = []
        while len(products) < num_products:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(2)
            product_containers = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")
            for container in product_containers:
                if len(products) >= num_products:
                    break

                    name = container.find_element(
                        By.CLASS_NAME, "prdct-desc-cntnr-name"
                    ).text
                    price = container.find_element(By.CLASS_NAME, "prc-box-dscntd").text

                try:
                    description = container.find_element(
                        By.CLASS_NAME, "product-desc-sub-text"
                    ).text
                except:
                    print("Description not found")
                    description = None

                try:
                    rating = container.find_element(By.CLASS_NAME, "ratingCount").text
                except:
                    print("Rating not found")
                    rating = None

                try:
                    review_count = container.find_element(
                        By.CLASS_NAME, "ratingCount"
                    ).text
                except:
                    print("Review count not found")
                    review_count = None

                product_info = {
                    "Ürün Adı": name,
                    "Fiyat": price,
                    "Ürün Açıklaması": description,
                    "Ürün Kategorisi": self.__category,
                    "Değerlendirme Puanı": rating,
                    "Yorum Sayısı": review_count,
                }

                products.append(product_info)
        return products

    def extract(self):
        try:
            driver = self.__driver_init()
            products = self.__get_products(driver)
            return products
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if driver:
                driver.quit()
