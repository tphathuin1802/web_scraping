# %% - Import Lib
import json
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

url = "https://cellphones.com.vn/laptop/mac.html"
driver = webdriver.Chrome()
driver.get(url)

time_out = 20
try:
    WebDriverWait(driver, time_out).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "block-product-list-filter"))
    )
except TimeoutException:
    print("Time out waiting for page too load")
    driver.quit()

try:
    while True:
        btn = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Xem thêm')]"))
        )
        btn.click()
        time.sleep(2)
except:
    print("Fully loaded page!.")

cmt_list = []
products = driver.find_element(By.CLASS_NAME, "block-product-list-filter")
product_lists = products.find_elements(
    By.CSS_SELECTOR, ".product-info-container.product-item"
)

for product in product_lists:
    try:
        name = product.find_element(By.CLASS_NAME, "product__name").text
        image = product.find_element(
            By.CSS_SELECTOR, "div.product__image img.product__img"
        ).get_attribute("src")
        price = product.find_element(By.CSS_SELECTOR, "p.product__price--show").text
        promotion = product.find_element(By.CLASS_NAME, "product__promotions").text

        price = price.replace(".", "").replace("đ", "")

        cmt_list.append(
            {
                "product_name": name,
                "img": image,
                "product_price": price,
                "promotion": promotion,
            }
        )
    except Exception as e:
        print(f"Error when finding products: {e}")

with open("mac.json", "w", encoding="utf-8") as f:
    json.dump(cmt_list, f, indent=3, ensure_ascii=False)
