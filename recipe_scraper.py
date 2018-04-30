from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import numpy as np
import pandas as pd
import re

def websurf(browser):
    food_cat = ['Chinese', 'Thai']
    main_pages = [ 
                  'https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese',
                  'https://www.allrecipes.com/recipes/702/world-cuisine/asian/thai'
                 ]
    min_num = 100  # mininum number of recipes to extract from each category
    for i, cat in enumerate(food_cat):
        print("open allrecipe page on %s food..." % cat)
        browser.get(main_pages[i])
        recipe_lists(browser, cat, min_num)
        
def recipe_lists(br, cat, min_num):
    print("Getting recipes from %s food..." % cat)
    urls = []
    while True:
        shift = len(urls)
#        Rlist = br.find_elements_by_xpath(
#               "//section[@id='fixedGridSection'] \
#                //a[contains(@class,'favorite ng-isolate-scope') \
#                    or contains(@class,'favorite ng-scope ng-isolate-scope')]")
        Rlist = br.find_elements_by_xpath(
               "//div[@class='fixed-recipe-card__info']\
                /a[contains(@class,'ng-isolate-scope') \
                    or contains(@class,'ng-scope')]")
        print("# of recipes in the list:", len(Rlist))
        for i, url in enumerate(Rlist):
            if i < shift: 
                continue
            urls.append(url.get_attribute('href'))
        if (len(urls) >= min_num):
            break
        else: # scroll down to load more recipes
            br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            print("\nScroll down to load more recipes...\n")
    print("debug: ", len(urls))
    urls = np.unique(urls)
    print("debug: ", len(urls))
    
 #   for i, url in enumerate(urls):
 #       br.get(urls[i])
 #       time.sleep(3)
 #       extract_recipe(br, cat, data_id[i])
        
def extract_recipe(br, cat, id):
    print("Extracting %s food recipe id: %s" % (cat, id))
    try:
        Rname = br.find_element_by_tag_name('h1').text
    except:
        Rname = 'NA'
    print(Rname)    
        
        
if __name__ == '__main__':
    print("Scraping recipes from allrecipe.com")
    browser = webdriver.Firefox()
    websurf(browser)