# third party libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# standard libraries
import time
from itertools import chain

CHROME_EXE = Service("data/chromedriver.exe")
TOYOTA_REVIEWS = "https://www.google.com/search?gs_ssp=eJzj4tFP1zcsKCk3sSwsTzFgtFI1qDA0NjJNM0kzT7Y0M0k1TTW2MqgwMkwxTTYwTjQwMDY3tDC38BIoya_ML0lUSMvMS8xLzkzMAQDSKBT5&q=toyota+financial&rlz=1C1CHBF_itIT925IT925&oq=toyota+fin&aqs=chrome.1.0i355i433i512j46i175i199i433i512j69i57j69i59j0i512j69i60l3.8054j0j7&sourceid=chrome&ie=UTF-8#lrd=0x1325f4f7c964e5e3:0x21d5c03a00371878,1,,,"
VOLKS_LINK = "https://www.google.com/search?q=volkswagen+financial+services&rlz=1C1CHBF_itIT925IT925&ei=kHIOYrbsN5-C9u8P0fGCsA0&gs_ssp=eJwFwcEJgDAMAED8Co4g-PFtQksjjuAWSYi1KhUsWMf3ru2mOCFqDkesdYdmGeHzNAdF2NCRBZtpgY-YhTw4UUIR0bV_7-sslaPlYUuZsya-hmLPm9TKDz8vG2Q&oq=volkswagen+finan&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyEQguEIAEELEDEIMBEMcBEK8BMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6DQguEMcBEKMCELADEEM6BwgAELADEEM6CggAEOQCELADGAA6EgguEMcBEKMCEMgDELADEEMYAToVCC4QxwEQowIQ1AIQyAMQsAMQQxgBOgcIABCxAxBDOgsIABCABBCxAxCDAToECAAQQzoICAAQgAQQsQM6CAgAEIAEEMkDOgsILhCABBDHARCvAUoECEEYAEoECEYYAVD2AVitGmCeKGgBcAF4AIABf4gB_gOSAQM1LjGYAQCgAQHIARPAAQHaAQYIABABGAnaAQYIARABGAg&sclient=gws-wiz#lrd=0x4786c10f137e6e87:0x7aab7403bc71bbbc,1,,,"
ID_REVIEW_FORM = "reviewSort"
REVIEW_CLASS = "Jtu6Td"
VOLKS_CLASS = "review-snippet"
FILENAME = "data/Recensioni_Volkswagen.txt"

def get_number_reviews(driver, by, value) -> int:
    driver.implicitly_wait(3)  
    n_reviews = driver.find_element(by=by, value=value)
    
    n_reviews = int(n_reviews.text.split(" ")[0])
    return n_reviews

def get_reviews_div(driver, locator:tuple):
    try:
        review_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    except:
        print("HAI SBAGLIATO QUALCOSA COMPA!")
        driver.quit()
    return review_div

def scroll_div(time, driver, scrollable_div, n_reviews):
    for i in range(0,(round(n_reviews/10 - 1))):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        time.sleep(1)
def review_to_file(file, reviews, n_reviews):
    with open(file= file, mode="w") as rev_file:
        rev_file.write(f"NUMERO DI RECENSIONI: {n_reviews}\n\n")
        for i, review in enumerate(reviews): 
            rev_file.write(f"{i+1})\n{review.text}\n")       
def main():
    driver = webdriver.Chrome(service=CHROME_EXE)
    driver.get(VOLKS_LINK)
    
    # agree cookies
    xpath_accept_button = '//*[@id="L2AGLb"]/div'
    driver.find_element(by="xpath",value= xpath_accept_button).click()
    
    # waiting for id to show up
    review_div = get_reviews_div(driver=driver, locator=(By.ID,ID_REVIEW_FORM ))
        
    n_reviews = get_number_reviews(driver=driver, by= "class name", value= "z5jxId")
    
    # loading all reviews
    scrollable_div = driver.find_element(by="class name", value="review-dialog-list")
    
    scroll_div(1,driver, scrollable_div, n_reviews)
    
       
    # collect all reviews  
    driver.implicitly_wait(3) 
    reviews = review_div.find_elements(by="class name", value= VOLKS_CLASS)

    # print all reviews to file
    review_to_file(FILENAME, reviews, n_reviews)
        
    print("TOMBOLA COMPA")
    driver.quit()  

       
if __name__ == "__main__":
    main()