# third party libraries
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service

# standard libraries
import time
import pickle
import json

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

def get_number_reviews(driver: WebDriver, by, value) -> float:
    """Get number of reviews from web page

    Args:
        driver (WebDriver): web driver object
        by (_type_): html tag
        value (_type_): value of html tag

    Returns:
        float: number of reviews
    """
    try:
        n_reviews = WebDriverWait(driver, 15).until(EC.presence_of_element_located((by, value)))
    except Exception as e:
        print(e)
        driver.quit()
        
    n_reviews = n_reviews.text.strip()
    n_reviews = n_reviews.split(" ")[0]
    
    return float(n_reviews)

def get_reviews_div(driver: WebDriver, by: str, value: str) -> WebElement:
    """Get reviews's box from web page

    Args:
        driver (WebDriver): web driver
        by (str): html tag
        value (str): value of html tag

    Returns:
        WebElement: reviews'box
    """
    try:
        review_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))
    except Exception as e:
        print(e)
        driver.quit()
        
    return review_div

def scroll_div(sec: float, driver: WebDriver, scrollable_div: WebElement, tot_reviews: float) -> None:
    """Scroll reviews

    Args:
        sec (float): scrolling rate
        driver (WebDriver): web driver
        scrollable_div (WebElement): scrollable element of webpage
        tot_reviews (int): total number of reviews
    """
    for i in range(0,(round(tot_reviews/10 - sec))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                              scrollable_div)
        time.sleep(sec)

def get_reviews(*values: str, reviews_form: WebElement, by: str) -> list[str]:
    """Return a list of reviews

    Args:
        *values: value/values of html tag
        reviews_form (WebElement): reviews form
        by (str): html tag
        
    Returns:
        list[str]: _description_
    """
    tot_reviews = []
    for value in values:
        reviews = reviews_form.find_elements(by=by, value= value)
        tot_reviews += [review.text for review in reviews]
        
    return tot_reviews

def review_to_file(file: str, reviews: WebElement) -> None:
    
    with open(file= file, mode="wb") as rev_file:
        pickle.dump(obj=reviews, file=rev_file)       

def main():
    # set configuration
    scrape_conf = set_config(file=CONFIG_FILE)
    
    driver = webdriver.Chrome(service=Service("data/chromedriver.exe"))
    driver.get(scrape_conf["link"])
    
    # agree cookies
    xpath_accept_button = '//*[@id="L2AGLb"]/div'
    driver.find_element(by="xpath",value= xpath_accept_button).click()
    
    # waiting for id to show up
    review_div = get_reviews_div(driver=driver, by="id", value=scrape_conf["id_review_form"])
    n_reviews = get_number_reviews(driver=driver, by="class name", value=scrape_conf["n_reviews_class_name"])
    
    # loading all reviews
    scrollable_div = driver.find_element(by="class name", value=scrape_conf["scrollable_div_class_name"])
    scroll_div(1,driver, scrollable_div, n_reviews)
    
    # collect all reviews  
    reviews = get_reviews(*scrape_conf["reviews_class_names"], reviews_form=review_div, by="class name")
    
    # pickle raw reviews
    review_to_file(scrape_conf["reviews_file"], reviews)
     
    print("FINISHED")
    
    driver.quit()
       
if __name__ == "__main__":
    main()