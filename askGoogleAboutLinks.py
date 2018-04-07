from splinter import Browser
import  pandas as pd

# open a brower
browser = Browser('chrome')
browser.driver.set_window_size(640, 480)
browser.visit('https://www.google.com')

#control the website
search_bar_xpath = '//*[@id="lst-ib"]'

# select first element
search_bar = browser.find_by_xpath(search_bar_xpath)[0]

#fill
search_bar.fill("eurosport.pl")

#click
search_button = browser.find_by_value('Szukaj w Google')[0]
search_button.click()

#scrape
search_results_xpath = '//h3[@class="r"]/a' # h3 element with class r
search_results = browser.find_by_xpath(search_results_xpath)
scraped_data = []
for search_result in search_results:
    title  = search_result.text.encode('utf8')
    link = search_result['href']
    scraped_data.append((title, link)) #in tuples

# csv
df = pd.DataFrame(data = scraped_data, columns=['Title', "Link"])
df.to_csv("links.csv")
