from abc import ABCMeta, abstractmethod
import pandas as pd

file_nip_data_path = '/home/izabela/workspace/askMF/askMF_project/niplist'

class DataProvider(metaclass=ABCMeta):
    @abstractmethod
    def get_nip_list(self):
        pass
    @classmethod
    def factory(cls, type = None, *args, **kwargs):
        if type == 'csv':
            return CSVDataProvider()
        elif type == 'xls':
            pass
        return DummyDataProvider()



class DummyDataProvider(DataProvider):
    def get_nip_list(self):
        return ['7790001083', '790001080', '5851326431']


class CSVDataProvider(DataProvider):
    def get_nip_list(self):
        csv = pd.read_csv('{}.csv'.format(file_nip_data_path))
        csv1 = csv["NIPS"].tolist()
        return list(csv1)

class XLSDataProvider(DataProvider):
    #TODO czytanie z excela
    def get_nip_list(self):
        xls = pd.read_excel('{}.xls'.format(file_nip_data_path))
        xls1 = xls["NIPS"].tolist()
        return print(xls1)

#CSVDataProvider().get_nip_list()
#XLSDataProvider().get_nip_list()


# TODO warunki na nipy z plikow zrodlowych
