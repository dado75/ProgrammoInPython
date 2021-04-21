import tkinter as tk
#import requests
from funz_operaz import *

window = tk.Tk()
window.geometry("600x300")
window.title("Calcolatrice")
#window.resizable(False, False)
#window.configure(background="white")
window.grid_columnconfigure(0, weight=1)

def somma_print():
    if text_input.get() and text_input2.get():
        num1 = int(text_input.get())
        num2 = int(text_input2.get())
        text_response = (somma(num1, num2))
    else:
        text_response = "Inserisci gli addendi nei campi input!"

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
text_input2.grid(row=3, column=0, pady=10, padx=10)
somma_buttom = tk.Button(width=5, text="+", font=("Helvetica, 20"), command=somma_print)
somma_buttom.grid(row=2, column=0, pady=10, padx=10)

#def somma_print():
#    text="Il risultato della somma è: " + str(somma(5, 5))
#    text_output = tk.Label(window, text=text , fg="red", font=("Helvetica", 16) )
#    text_output.grid(row=0, column=1, padx=100, sticky="W")

#def sottrazione_print():
#    text = "Il risultato della sottrazione è: " + str(sottrazione(10, 5))
#    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16) )
#    text_output.grid(row=1, column=1, padx=100, sticky="W")

#first_button = tk.Button(text="Somma", command=somma_print)
#first_button.grid(row=0, column=0, sticky="W")

#second_button = tk.Button(text="Sottrazione", command=sottrazione_print)
#second_button.grid(row=1, column=0, pady=20, sticky="W")

if __name__ == "__main__":
    window.mainloop()