def main():
   print ('''
   Questo programma è una lista di funzioni
   che una volta importato come modulo,
   ci servono a fare le quattro operazioni.
   ''')

def somma(x,y):
   '''operazione somma'''
   piu = x + y
   return piu

def sottrazione(x,y):
   meno = x - y
   return meno

def moltiplicazione(x,y):
   per = x * y
   return per

def divisione(x,y):
   try:
      diviso = x / y
      return diviso
   except ZeroDivisionError:
      print('Divisione impossibile!!!')

if __name__ == "__main__":
   main()