# links for completion:
# https://www.youtube.com/watch?v=SPM1tm2ZdK4
# https://docs.google.com/document/d/16igOIW5zv-JmH-wksDaQg1DAR4462LO4Pu4tnustZe0/edit


import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# import database.data_handlers

options = Options()
options.add_experimental_option("detach", True)  # if True - keep browser open after script is done (for debugging)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          )

catalogue_url = "https://shop.nag.ru/catalog/31418.setevoe-oborudovanie"



def parse_urls_on_page(catalogue_page) -> list:
    """
    Parse items links from the page
    :return: item links
    """
    item_links = []
    driver.get(catalogue_url + f"?page={catalogue_page}")
    item_title = driver.find_elements("xpath", "//*[@title='Нажмите, чтобы скопировать наименование']/../../a[@href]")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            "xpath", "//*[@title='Нажмите, чтобы скопировать наименование']"))
    except:
        print("Waiting for page to load...")
        time.sleep(3)

    for item in item_title:
        item_links.append(item.get_attribute("href"))
    return item_links


def page_counter() -> int:
    """
    Count pages in the category
    :return: number of pages
    """
    driver.get(catalogue_url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('xpath', '//a[contains(@href, "?page")]')))

    while True:
        try:
            paginators = []
            paginator_elements = driver.find_elements('xpath', '//a[contains(@href, "?page")]')
            for paginator in paginator_elements:
                paginators.append(paginator.text)
            break
        except:
            print("Waiting for page to load...")
            time.sleep(3)

    total_pages = int(paginators[-2])
    return total_pages





def item_urls_loop(item_links: list) -> dict:
    """
    Loop through all items in the category page
    :param item_links: list of links to items
    :return: dictionary with data for each url
    """
    cat_page_data = {}
    for item in item_links:
        driver.get(item)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(("xpath", "TODO: find element to wait for")))
        # cat_page_data[item] = parse_item_data(item)  # TODO: create function to parse item data
    return cat_page_data

# Example dictionary with item data
# cat_page_sample_data = {
#     "name": "Управляемый коммутатор уровня 2 SNR-S2985G-48T",
#     "partnumber": "SNR-S2985G-48T",
#     "short_description": "Управляемый гигабитный коммутатор",
#     "extended_description": "<p>Управляемый гигабитный коммутатор</p><strong>Основные особенности:</strong>",
#     "vendor": "SNR",
#     "link": "https://shop.nag.ru/catalog/00001.kommutatory/40213.fiksirovannye-kommutatory/17303.snr-s2985g-48t",
#     "image_url": "https://files-shop.nag.ru/files/new_shop/items/SNR-S2985G-48T/main/9d86f5ea794db17ea1c2627f63705e3a.webp"
#
# }


def cat_urls_loop(total_pages: int) -> dict:
    """
    Loop through all pages in the category
    :param total_pages:  number of pages in the category
    :return: dictionary with data for each url
    """

    # use tabs method to open new pages
    for page in range(1, total_pages):
        page_url = catalogue_url + f"?page={page}"

        driver.get(page_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(("xpath", "//*[@title='Нажмите, чтобы скопировать наименование']")))
        page_item_links = parse_urls_on_page(page)
        # TODO: loop through links on the page

        # TODO: return dict with data


def main():
    """
    Loop through all pages of the catalog
    :return:
    """
    start_time = time.time()

    # find number of pages in the category
    pages = page_counter()


    # total pages in the category
    print("--> Total pages: ", pages)
    # time for script to run
    print("--- %s minutes ---" % ((time.time() - start_time)/60))


if __name__ == "__main__":
    print(page_counter())