from splinter import Browser
import shutil
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox

from data_provider import DataProvider




#browser = Browser('chrome', headless=True)
browser = Browser('chrome')


def click_by_id(button_id):
    button = browser.find_by_id(button_id)[0]
    button.click()


def esc(table): #wyjscie ze strony, wejscie na startowa
    if len(table) > 0:
        esc_button_id = 'b-9'
        click_by_id(esc_button_id)


def fill_search_bar(a): #znajduje i wypelnia search_bar
    search_bar_path = "//input[@id='b-7' and @name='b-7']"
    while browser.is_element_not_present_by_xpath(search_bar_path):
        time.sleep(0.5)
    search_bar = browser.find_by_xpath(search_bar_path)
    search_bar.fill(a)


def scrape(): #szuka informacji i zbiera do zmiennej
    search_results_xpath = '//*[@id="caption2_b-3"]'
    while browser.is_element_not_present_by_xpath(search_results_xpath):
        time.sleep(0.5)
    search_results = browser.find_by_xpath(search_results_xpath).first
    search_results_text = search_results.text
    return search_results_text


def screenshot_saver(nip): #robi i zapisuje screenshot
    imageMF = browser.screenshot(name=nip, suffix='.png')
    save_path = '/home/izabela/workspace/askMF/printscreens/{}.png'.format(nip)
    shutil.copyfile(imageMF, save_path)


def check_nip(nips):
    scraped_data = []
    url = 'https://ppuslugi.mf.gov.pl/'
    browser.driver.set_window_size(940, 580)
    browser.visit(url)

    # link with NIPfinder - going around not loggin
    findNIP_xpath = '//*[@id="SidebarActions_WebUMn"]/li[3]/a'
    findNIP = browser.find_by_xpath(findNIP_xpath)[0]
    findNIP.click()

    for nip in nips:
        nip = str(nip)
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

        screenshot_saver(nip)
        scraped_data.append((nip, comment))  # in tuples
        esc(tab)
    save_to_csv(scraped_data)
    browser.quit()
    return scraped_data


def save_to_csv(data_to_csv):
    df = pd.DataFrame(data = data_to_csv, columns=['nip', 'comment'])
    df.to_csv("nipMF.csv")



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    source = DataProvider.factory('csv').get_nip_list() #w faktur wybierasz typ dokumentu
    messagebox.showwarning('Alert', 'Po skonczeniu sprawdzania, poinformujemy Cie o tym')
    check_nip(source)
    messagebox.showwarning('Alert', 'Informacje sa juz dostepne')

# pythonrq ew.celery do zarzadzania zadaniami








