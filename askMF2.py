from splinter import Browser
import pandas as pd
import time
import shutil




class NIPExtractor():
    def __init__(self):
        self._browser = Browser('chrome')
        # self._browser = Browser('chrome', headless=True)
        self.scraped_data = []
        url = 'https://ppuslugi.mf.gov.pl/'
        self._browser.driver.set_window_size(940, 580)
        self._browser.visit(url)

        # link with NIPfinder - going around not loggin
        findNIP_xpath = '//*[@id="SidebarActions_WebUMn"]/li[3]/a'
        findNIP = self._browser.find_by_xpath(findNIP_xpath)[0]
        findNIP.click()


    def _fill_search_bar(self, a):  # znajduje i wypelnia search_bar
        search_bar_path = "//input[@id='b-7' and @name='b-7']"
        while self._browser.is_element_not_present_by_xpath(search_bar_path):
            time.sleep(0.5)
        search_bar = self._browser.find_by_xpath(search_bar_path)
        search_bar.fill(a)

    def _click_by_id(self, button_id):
        while self._browser.is_element_not_present_by_id(button_id):
            time.sleep(0.5)
        button = self._browser.find_by_id(button_id)[0]
        button.click()


    def _scrape(self):  # szuka informacji i zbiera do zmiennej
        search_results_xpath = '//*[@id="caption2_b-3"]'
        while self._browser.is_element_not_present_by_xpath(search_results_xpath):
            time.sleep(0.5)
        search_results = self._browser.find_by_xpath(search_results_xpath).first
        search_results_text = search_results.text
        return search_results_text

    def _quit(self):
        self._browser.quit()

    def _screenshot_saver(self, nip):  # robi i zapisuje screenshot
        imageMF = self._browser.screenshot(name=nip, suffix='.png')
        save_path = '/home/izabela/workspace/askMF/printscreens/{}.png'.format(nip)
        shutil.copyfile(imageMF, save_path)

    def _esc(self, table):  # wyjscie ze strony, wejscie na startowa
        if len(table) > 0:
            esc_button_id = 'b-9'
            self._click_by_id(esc_button_id)

    def _check(self, nip):
        nip = str(nip)
        search_button_id = 'b-8'
        tab = []

        self._fill_search_bar(nip)
        self._click_by_id(search_button_id)
        self._scrape()

        for line in self._scrape().splitlines():
            tab.append(line)

        if len(tab) > 0:
            comment = tab[0]
        else:
            comment = "nie sprawdzono, prawdopodobnie bledny NIP"
        print(comment)

        self._screenshot_saver(nip)
        self.scraped_data.append((nip, comment))  # in tuples
        self._esc(tab)
        return self.scraped_data


    def _save_to_csv(self, data_to_csv):
        df = pd.DataFrame(data=data_to_csv, columns=['nip', 'comment'])
        df.to_csv("nipMF.csv")

    def check_nip(self, nip):
        result = self._check(nip)
        self._save_to_csv(self.scraped_data)
        self._quit()
        return result


    def check_list_of_nips(self, nips):
        for nip in nips:
            nip = str(nip)
            result = self._check(nip)
        self._save_to_csv(result)
        self._quit()
        return result








