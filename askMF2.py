nip_extractor = NIPExtractor()

nip_extractor.check_nip('nip') #return slownik: nr nip, komunikat, printscreen
nip_extractor.check_list_of_nips(['nips']) #retern: tupla(nr nip, komunikat, printcreen)


class NIPExtractor():
    def __init__(self):
        self._browser = Browser('chrome', headless=True)
        #scraped_data = []
        url = 'https://ppuslugi.mf.gov.pl/'
        self._browser.driver.set_window_size(940, 580)
        self._browser.visit(url)

        # link with NIPfinder - going around not loggin
        findNIP_xpath = '//*[@id="SidebarActions_WebUMn"]/li[3]/a'
        findNIP = browser.find_by_xpath(findNIP_xpath)[0]
        findNIP.click()

    def check_nip(self, nip):
        pass
    def check_list_of_nips(self, nips):
        pass

