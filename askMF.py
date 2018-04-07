from splinter import Browser
import shutil
import pandas as pd
import time
from input_data import InputData

# open a brower
browser = Browser('chrome')
url = 'https://ppuslugi.mf.gov.pl/'
browser.driver.set_window_size(940, 580)
browser.visit(url)
#TODO headless spr jak zrobic bez pokazania przegladarki


# link with NIPfinder - going around not loggin
findNIP_xpath = '//*[@id="SidebarActions_WebUMn"]/li[3]/a'
findNIP = browser.find_by_xpath(findNIP_xpath)[0]
findNIP.click()



#valid & correct
nip0 = "7790001083"
#incorrect
nip1 = "7790001080"
#invalid
nip2 = '5851326431'
#fill
#TODO warunki na nipy z plikow zrodlowych
nips = [nip0, nip1, nip2]

def click_by_id(button_id):
    button = browser.find_by_id(button_id)[0]
    button.click()


def esc(table): #wyjscie ze strony, wejscie na startowa
    if len(table) > 0:
        esc_button_id = 'b-9'
        click_by_id(esc_button_id)
    else:
        pass

def fill_search_bar(a): #znajduje i wypelnia search_bar
    while browser.is_element_not_present_by_xpath("//input[@id='b-7' and @name='b-7']"):
        time.sleep(0.5)
    search_bar = browser.find_by_xpath("//input[@id='b-7' and @name='b-7']")
    search_bar.fill(a)

def scrape(): #szuka informacji i zbiera do zmiennej
    search_results_xpath = '//*[@id="caption2_b-3"]'
    while browser.is_element_not_present_by_xpath(search_results_xpath):
        time.sleep(0.5)
    search_results = browser.find_by_xpath(search_results_xpath).first
    search_results_text = search_results.text
    return search_results_text

def screenshot_saver(): #robi i zapisuje screenshot
    imageMF = browser.screenshot(name=nip, suffix='.png')
    save_path = '/home/izabela/workspace/askMF/{}.png'.format(nip)
    shutil.copyfile(imageMF, save_path)


scraped_data = []


for nip in nips:
    search_button_id = 'b-8'
    tab = []

    fill_search_bar(nip)
    click_by_id(search_button_id)
    scrape()

    for line in scrape().splitlines():
        tab.append(line)

    if len(tab) > 0:
        comment = tab[0]
    else:
        comment = "nie sprawdzono, prawdopodobnie bledny NIP"
    print(comment)

    screenshot_saver()
    scraped_data.append((comment))  # in tuples
    esc(tab)


# csv
df = pd.DataFrame(data = scraped_data, columns=["comment"])
df.to_csv("nipMF.csv")












