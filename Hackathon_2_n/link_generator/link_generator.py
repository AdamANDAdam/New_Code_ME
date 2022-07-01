import tkinter as tk
from tkinter import messagebox
import json
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        messagebox.askquestion("askquestion", "Choose one of the links from:\n https://github.com/ritaly/PythonCourse2022/blob/main/hackaton_2/04_generator_linkow/hints/test.md")
        self.contents.set("Enter link URL:")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
        temp_URL = self.contents.get()
        with open('URL_saver.json', mode='w') as plik:
            json.dump(temp_URL, plik)
        temp_URL = self.helloCallBack()
        with open('URL_saver.json', mode='w') as plik:
            json.dump(temp_URL, plik)
        print("Hi. The new link is saved in file and reads now:",
              temp_URL)
    def helloCallBack(self):
        # mi("Hello Python", "Hello World")
        try:
            with open('url_saver.json', mode='r') as plik:
                lista_numerow = json.load(plik)
                #print(f'Wczytano {len(lista_numerow)} wpisów.')
                if str(lista_numerow).find('/ksiazki/') == True:
                    last = str(lista_numerow).replace('/ksiazki/', '.pl/ksiazki/view/90023/')
                # last = str(lista_numerow).replace('.pl/','.pl/view/90023/')
                elif str(lista_numerow).find('ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d') == True:
                    last = str(lista_numerow.replace('ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d','view/90412/algoip'))
                elif str(lista_numerow).find('/ksiazki/') == True:
                    last = str(lista_numerow.replace('kategorie/promocja-2za1','page/90412/promocja/promocja-2za1'))
                elif str(lista_numerow).find('kategorie/programowanie') == True:
                    last = str(lista_numerow.replace('kategorie/programowanie', 'page/90412/kategorie/programowanie'))
                return last
        except FileNotFoundError:
            return []


root = tk.Tk()
root.geometry('500x500')
myapp = App(root)
myapp.mainloop()