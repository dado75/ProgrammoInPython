import tkinter as tk
from funz_operaz import *

window = tk.Tk()
window.geometry("600x300")
window.title("Calcolatrice")
#window.resizable(False, False)
#window.configure(background="white")
window.grid_columnconfigure(0,weight=1)

def somma_print():
    if text_input.get() and text_input2.get():
        num1 = int(text_input.get())
        num2 = int(text_input2.get())
        text_response = (somma(num1, num2))
    else:
        text_response = "Inserisci i valori nei campi input!"
    text = tk.Text()
    text.insert(tk.END, text_response)
    text.grid(row=5, column=0, sticky="N", padx=10)

def sottrazione_print():
    if text_input.get() and text_input2.get():
        num1 = int(text_input.get())
        num2 = int(text_input2.get())
        text_response = (sottrazione(num1, num2))
    else:
        text_response = "Inserisci i valori nei campi input!"
    text = tk.Text()
    text.insert(tk.END, text_response)
    text.grid(row=4, column=0, sticky="N", padx=10)

welcome_label = tk.Label(window,
                         text="Benvenuti nella calcolatrice di PYTHON!!!",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry(width=20)
text_input.grid(row=1, column=0, pady=10, padx=10)
text_input2 = tk.Entry(width=20)
text_input2.grid(row=2, column=0, pady=10, padx=10)
somma_buttom = tk.Button(width=5, text="+", font=("Helvetica, 20"), command=somma_print)
somma_buttom.grid(row=3, column=0, pady=10, padx=10)
sottrazione_buttom = tk.Button(width=5, text="-", font=("Helvetica, 20"), command=sottrazione_print)
sottrazione_buttom.grid(row=4, column=0, pady=10, padx=10)

if __name__ == "__main__":
    window.mainloop()