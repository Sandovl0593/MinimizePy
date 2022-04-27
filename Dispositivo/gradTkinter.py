import tkinter as tk
import idlelib.percolator as I
import idlelib.colorizer as ic

def grafics():

    def salir():
        import sys
        sys.exit()

    root = tk.Tk()
    texto = tk.Text(root, font="Calibri")
    texto.pack()
    I.Percolator(texto).insertfilter(ic.ColorDelegator())
    # etiqueta = tk.Label(root, text="Azucarado a mi serás").pack()

    boton1 = tk.Button(root, border=20, text="Salir...",
                activebackground="chocolate", highlightcolor="green",
                font=("Cascadia", 10), background="yellow",
                command=salir)
    boton1.pack()
    root.mainloop()

def jsonpokemon():
    import requests
    api = requests.get("https://pokeapi.co/api/v2/pokemon")
    archi = str(api.json()["results"])
    print(archi)
    
grafics()