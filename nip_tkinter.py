from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from askMF_project.askMF2 import NIPExtractor
from askMF_project.data_provider import DataProvider


def nip_tkinter_checker():
    # root = Tk()
    # root.withdraw()

    def check_nip(*args):
        #nip = '7790001083'
        nip = str(niptobe.get())
        print(nip)
        nip_extractor = NIPExtractor()
        comment = nip_extractor.check_nip(nip)
        response_from_MF.set(comment)
        messagebox.showwarning('Alert', 'Informacje sa juz dostepne')
        #messagebox.showwarning('Alert', response_from_MF)

    def check_list_of_nips(*args):
        nip_extractor = NIPExtractor()
        source = DataProvider.factory('csv').get_nip_list()
        nip_extractor.check_list_of_nips(source)
        messagebox.showwarning('Alert', 'Informacje sa juz dostepne')

    root = Tk()
    root.title("NIP checker")
    #messagebox.showwarning('Alert', 'Po skonczeniu sprawdzania, poinformujemy Cie o tym')

    mainframe = ttk.Frame(root, padding="6 6 16 16")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    niptobe = StringVar()
    response_from_MF = StringVar()
    #path_csv = 'sciezka do pliku'

    niptobe_entry = ttk.Entry(mainframe, width=7, textvariable=niptobe)
    niptobe_entry.grid(column=3, row=2, sticky=W)
    #path_entry = ttk.Entry(mainframe, width=7, textvariable=path_csv)
    #path_entry.grid(column=3, row=4, sticky=W)
    ttk.Label(mainframe, textvariable=response_from_MF).grid(column=1, row=6, sticky=(W, E))


    ttk.Button(mainframe, text="check", command=check_nip).grid(column=4, row=2, sticky=W)
    ttk.Button(mainframe, text="check list", command=check_list_of_nips).grid(column=4, row=4, sticky=W)

    ttk.Label(mainframe, text="Wpisz NIP do sprawdzenia").grid(column=1, row=1, sticky=E)
    ttk.Label(mainframe, text="Sprawdz NIP").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Podaj sciezke do pliku .csv").grid(column=1, row=3, sticky=E)
    ttk.Label(mainframe, text="Sprawdz liste NIPow").grid(column=1, row=4, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    root.mainloop()



if __name__ == "__main__":
    nip_tkinter_checker()

