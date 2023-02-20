from tkinter import Tk
from tkinter import ttk 
from googletrans import Translator
import ttkbootstrap
from ttkbootstrap.constants import *


class Translate(Tk):
    def __init__(self):
        super().__init__()
        
        self.sethings()
        self.labels_and_entries()

    def sethings(self):
        self.geometry('400x400')
        self.title('Tradutor')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 14))
        self.style.configure('TButton', background='#3CB371')

        ttkbootstrap.Style('darkly')

        self.bind('<Return>', self.translate)
    def labels_and_entries(self):
        self.label1 = ttk.Label(text='Digite a frase')
        self.label1.place(relx=0.4, rely=0.05)

        self.entry1 = ttk.Entry(justify='center')
        self.entry1.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.3)

        self.label2 = ttk.Label(text='Tradução')
        self.label2.place(relx=0.4, rely=0.45)

        self.entry2 = ttk.Entry(justify='center')
        self.entry2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.3)

        self.btntranslate = ttk.Button(text='traduzir', command=self.translate)
        self.btntranslate.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1)
        
    def translate(self, event=None):
        self.frase = self.entry1.get()

        if self.frase != '':
            translate_ = Translator()
            phrase = translate_.translate(self.frase, src='pt', dest='en')
            
            self.entry2.insert(0, phrase.text)
        else:
            print('nada para traduzir')


app = Translate()
app.mainloop()
