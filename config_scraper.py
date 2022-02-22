# config parameter
from selenium.webdriver.chrome.service import Service

SCRAPE_CONF = {"chrome_driver": Service("data/chromedriver.exe"),
               "link": "https://www.google.com/search?gs_ssp=eJzj4tFP1zcsKCk3sSwsTzFgtFI1qDA0NjJNM0kzT7Y0M0k1TTW2MqgwMkwxTTYwTjQwMDY3tDC38BIoya_ML0lUSMvMS8xLzkzMAQDSKBT5&q=toyota+financial&rlz=1C1CHBF_itIT925IT925&oq=toyota+fin&aqs=chrome.1.0i355i433i512j46i175i199i433i512j69i57j69i59j0i512j69i60l3.8054j0j7&sourceid=chrome&ie=UTF-8#lrd=0x1325f4f7c964e5e3:0x21d5c03a00371878,1,,,",
               "id_review_form": "reviewSort",
               "scrollable_div_class_name": "review-dialog-list",
               "n_reviews_class_name": "z5jxId",
               "reviews_class_names": ["Jtu6Td", "review-snippet"],
               "reviews_file": "data/reviews/TOYOTA_RECENSIONI.txt"}
