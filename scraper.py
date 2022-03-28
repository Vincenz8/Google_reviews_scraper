# third party libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# standard libraries
import time
import json
import pickle

CONFIG_FILE = "data/config_scraper.json"


def set_config(file: str) -> dict:
    """Importing Json with parameters for web scraper.

    Args:
        file (str): Json file

    Returns:
        dict: parameters
    """
    with open(file, "r") as config_file:
        config_scraper = json.load(config_file)
    return config_scraper


def get_number_reviews(html_source: str, class_name: str) -> float:
    """Get number of reviews from web page

    Args:
        html_source:
        class_name (_type_): value of html class

    Returns:
        float: number of reviews
    """
    soup = BeautifulSoup(html_source, "html.parser")
    n_reviews = soup.find("span", {"class": class_name}).get_text(strip=True)

    return float(n_reviews.split(" ")[0])


def scroll_div(sec: float, driver: WebDriver, scrollable_div: WebElement, tot_reviews: float) -> None:
    """Scroll reviews

    Args:
        sec (float): scrolling rate
        driver (WebDriver): web driver
        scrollable_div (WebElement): scrollable element of webpage
        tot_reviews (int): total number of reviews
    """
    for i in range(0, (round(tot_reviews / 10 - sec))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',
                              scrollable_div)
        time.sleep(sec)


def get_reviews(*class_name: str, html_source: str) -> list[str]:
    """Return a list of reviews

    Args:
        html_source: html source code
        *class_name: value/values of html tag
        
    Returns:
        list[str]: _description_
    """
    soup = BeautifulSoup(html_source, "html.parser")
    reviews = soup.find_all("div", {"class": class_name[1]})
    reviews_text = []

    for rev in reviews:
        rev2 = rev.find("span", {"class": class_name[0]})
        if rev2:
            reviews_text.append(rev2.get_text())
        else:
            reviews_text.append((rev.get_text()))

    return reviews_text


def review_to_file(file: str, reviews: WebElement) -> None:
    with open(file=file, mode="wb") as rev_file:
        pickle.dump(obj=reviews, file=rev_file)


def main():
    # set configuration
    scrape_conf = set_config(file=CONFIG_FILE)

    driver = webdriver.Chrome(service=Service("data/chromedriver.exe"))
    driver.get(scrape_conf["link"])

    # agree cookies
    xpath_accept_button = '//*[@id="L2AGLb"]/div'
    driver.find_element(by="xpath", value=xpath_accept_button).click()
    time.sleep(2)

    html_source = driver.page_source

    n_reviews = get_number_reviews(html_source=html_source, class_name=scrape_conf["n_reviews_class_name"])
    print(n_reviews)

    # loading all reviews
    scrollable_div = driver.find_element(by="class name", value=scrape_conf["scrollable_div_class_name"])
    scroll_div(1, driver, scrollable_div, n_reviews)

    html_source = driver.page_source

    # collect all reviews
    reviews = get_reviews(*scrape_conf["reviews_class_names"], html_source=html_source)

    # pickle raw reviews
    review_to_file(scrape_conf["reviews_file"], reviews)

    print("FINISHED")

    driver.quit()


if __name__ == "__main__":
    main()
