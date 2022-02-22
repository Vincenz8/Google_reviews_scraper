# config parameter
from selenium.webdriver.chrome.service import Service

SCRAPE_CONF = {"chrome_driver": Service("data/chromedriver.exe"),
               "link": "https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TCopSS9MSo83YLRSNagwMbcwSzZMMjVISjZNSksxtTKosEwyNTc3MUu2SDMzsUg0tfSSKkgtTU_NL1FIy8xLzEvOTMxRKE4tKstMTi0GAPPcGfI&q=peugeot+financial+services&rlz=1C1CHBF_itIT925IT925&oq=peugeot+financial+servic&aqs=chrome.1.69i57j46i175i199i512j0i22i30i457j0i22i30l5.17383j0j7&sourceid=chrome&ie=UTF-8#lrd=0x4786c1b50bc5bfd5:0x9b57746c8f648a59,1,,,",
               "id_review_form": "reviewSort",
               "scrollable_div_class_name": "review-dialog-list",
               "n_reviews_class_name": "z5jxId",
               "reviews_class_names": ["Jtu6Td", "review-snippet"],
               "reviews_file": "data/reviews/BANCA_PSA_RECENSIONI.txt"}
