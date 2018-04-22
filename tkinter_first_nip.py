from tkinter import *
from tkinter import ttk
from askMF_project.askMF import check_nip




def nip_tkinter():

    def calculate(*args):
        try:
            value = niptobe.get()
            print(value)
            list_of_nips = []
            list_of_nips.append(value)
            response_from_MF.check_nip((list_of_nips))
            print(list_of_nips)
        except ValueError:
            pass


    root = Tk()
    root.title("Check NIP")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    niptobe = StringVar()
    response_from_MF = StringVar()

    niptobe_entry = ttk.Entry(mainframe, width=7, textvariable=niptobe)
    niptobe_entry.grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe, textvariable=response_from_MF).grid(column=2, row=2, sticky=(W, E))
    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="NIP").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="wynik z z MF").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe).grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    #niptobe_entry.focus()
    #root.bind('<Return>', calculate)

    root.mainloop()

nip_tkinter()
