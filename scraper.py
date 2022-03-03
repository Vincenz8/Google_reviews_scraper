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

# local libraries
from config_scraper import SCRAPE_CONF

def get_number_reviews(driver: WebDriver, by, value) -> float:
    
    try:
        n_reviews = WebDriverWait(driver, 15).until(EC.presence_of_element_located((by, value)))
    except Exception as e:
        print(e)
        print("NON HO TROVATO IL NUMERO")
        driver.quit()
        
    n_reviews = n_reviews.text.strip()
    n_reviews = n_reviews.split(" ")[0]
    print(n_reviews)
    
    return float(n_reviews)

def get_reviews_div(driver: WebDriver, by: str, value: str) -> WebElement:
    
    try:
        review_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))
    except Exception as e:
        print("NON HO TROVATO IL FORM CON LE RECENSIONI")
        driver.quit()
    return review_div

def scroll_div(sec: float, driver: WebDriver, scrollable_div: WebElement, n_reviews: int) -> None:
    
    for i in range(0,(round(n_reviews/10 - sec))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                              scrollable_div)
        time.sleep(sec)

def get_reviews(*values: str, reviews_form: WebElement, by: str) -> list[str]:
    
    tot_reviews = []
    for value in values:
        reviews = reviews_form.find_elements(by=by, value= value)
        tot_reviews += [review.text for review in reviews]
        
    return tot_reviews

def review_to_file(file: str, reviews: WebElement) -> None:
    
    with open(file= file, mode="wb") as rev_file:
        pickle.dump(obj=reviews, file=rev_file)       

def main():
    
    driver = webdriver.Chrome(service=Service("data/chromedriver.exe"))
    driver.get(SCRAPE_CONF["link"])
    
    # agree cookies
    xpath_accept_button = '//*[@id="L2AGLb"]/div'
    driver.find_element(by="xpath",value= xpath_accept_button).click()
    
    # waiting for id to show up
    review_div = get_reviews_div(driver=driver, by="id", value=SCRAPE_CONF["id_review_form"])
    n_reviews = get_number_reviews(driver=driver, by="class name", value=SCRAPE_CONF["n_reviews_class_name"])
    
    # loading all reviews
    scrollable_div = driver.find_element(by="class name", value=SCRAPE_CONF["scrollable_div_class_name"])
    scroll_div(1,driver, scrollable_div, n_reviews)
    
    # collect all reviews  
    reviews = get_reviews(*SCRAPE_CONF["reviews_class_names"], reviews_form=review_div, by="class name")
    
    # pickle raw reviews
    review_to_file(SCRAPE_CONF["reviews_file"], reviews)
    # pickle.dump(obj=reviews, file=SCRAPE_CONF["reviews_file"])    
    print("FINISHED")
    
    driver.quit()
       
if __name__ == "__main__":
    main()