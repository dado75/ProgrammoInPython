import tkinter as tk
#import sqlite3 as sq
from autoclass import *

window = tk.Tk()
window.geometry("600x600")
window.title("Transport")
window.resizable(False, False)
window.configure(background="white")
window.grid_columnconfigure(0,weight=1)

def visualizza_scheda_auto():
    if text_input.get() and text_input2.get() and text_input3.get():
        a = text_input.get()
        b = int(text_input2.get())
        c = text_input3.get()
        mezzo = Mezzi_trasporto(a,b,c)
        text_response = (mezzo.scheda_mezzo_trasporto())
    else:
        text_response = "Inserisci i valori nei campi input!"
    text = tk.Text()
    text.insert(tk.END, text_response)
    text.grid(row=5, column=0, sticky="N", padx=10) 


welcome_label = tk.Label(window,
                         text= "Mezzo di trasporto",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry(width=20)
text_input.grid(row=1, column=0, pady=10, padx=10)
text_input2 = tk.Entry(width=20)
text_input2.grid(row=2, column=0, pady=10, padx=10)
text_input3 = tk.Entry(width=20)
text_input3.grid(row=3, column=0, pady=10, padx=10)
mezzi_buttom = tk.Button(width=20, text="Scheda Mezzo Trasporto", font=("Helvetica, 20"), command=visualizza_scheda_auto)
mezzi_buttom.grid(row=4, column=0, pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()