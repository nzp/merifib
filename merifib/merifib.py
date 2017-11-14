#!/usr/bin/env python3
"""Modul implementira korisnički interfejs programa i služi za pokretanje aplikacije."""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from fibonacci import Fibonacci


# Inicijalizacija glavnog prozora.
root = tk.Tk()
root.title("Istraživanje Fibonačijevog niza")
root.columnconfigure(0, weight=1)

# Glavni frejm.  Može i bez toga, ali onda pozadina prozora ne bi bila
# „temirana“ u skladu sa vidžetima.
mainframe = ttk.Frame(root, padding="10 10 10 10")

# Frejm popunjava čitav prostor glavnog prozora.
mainframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)

# Da bi se širina frejma menjala sa veličinom glavnog prozora.
mainframe.columnconfigure(0, weight=1)


#
# Globalne promenljive koje služe izračunavanju i prikazivanju niza.
#
fib_seed = tk.IntVar(value=0)               # Početna vrednost niza.
fib_sequence_length = tk.IntVar(value=1)    # Dužina niza.
fib_sequence = tk.StringVar()               # Niz.
json_fib_sequence = tk.StringVar()          # Niz u JSON formatu.
fib_ord = tk.IntVar()                       # Pozicija broja u nizu.
fib_ord_num = tk.IntVar()                   # Broj na zadatoj poziciji.


#
# Funkcije koje pozivaju metode Fibonacci klase i ažuriraju rezultate.
#
def set_sequence(length, seed, parent_win):
    """Setuj niz sa određenom dužinom i početnom vrednošću.

    Funkcija setuje globalnu promenljivu ``fib_sequence`` koja se ispisuje u
    korisničkom interfejsu.

    Args:
        length (int): Dužina niza.
        seed (int): Početna vrednost niza.
        parent_win (tk.Toplevel): Prozor iz kog se funkcija pokreće.  Služi za
            prosleđivanje te informacije dijalogu za izveštaj o grešci.

    """
    # Ukoliko je uneta nevalidna vrednost za dužinu ili početnu vrednost, to
    # hvatamo ovde i prikazujemo poruku u dijalogu.
    try:
        f = Fibonacci(length, seed)
        fib_sequence.set(str(f.sequence()))
    except ValueError:
        messagebox.showerror(
            "Pogrešna vrednost",
            "Dužina niza mora biti različita od 0, a početna vrednost mora "
            "biti validan Fibonačijev broj.",
            parent=parent_win)


def set_json(length, seed, parent_win):
    """Setuj JSON reprezentaciju niza zadate dužine i početne vrednosti.

    Funkcija setuje globalnu promenljivu ``json_sequence`` koja sadrži JSON
    prikaz niza sa dodatnim podacima koja se prikazuje u korisničkom interfejsu.

    Args:
        length (int): Dužina niza.
        seed (int): Početna vrednost niza.
        parent_win (tk.Toplevel): Prozor iz kog se funkcija pokreće.  Služi za
            prosleđivanje te informacije dijalogu za izveštaj o grešci.

    """
    # Ukoliko je uneta nevalidna vrednost za dužinu ili početnu vrednost, to
    # hvatamo ovde i prikazujemo poruku u dijalogu.
    try:
        f = Fibonacci(length, seed)
        json_fib_sequence.set(f.json())
    except ValueError:
        messagebox.showerror(
            "Pogrešna vrednost",
            "Dužina niza mora biti različita od 0, a početna vrednost mora "
            "biti validan Fibonačijev broj.",
            parent=parent_win)

def set_nth(position, parent_win):
    """Setuj vrednost Fibonačijevog broja na datoj poziciji.

    Funkcija setuje globalnu promenljivu ``fib_ord_num`` na vrednost
    Fibonačijevog broja na zadatoj poziciji.

    Args:
        position (int): Pozicija (redni broj) u Fibonačijevom nizu.
        parent_win (tk.Toplevel): Prozor iz kog se funkcija pokreće.  Služi za
            prosleđivanje te informacije dijalogu za izveštaj o grešci.

    """
    # Kao i u prethodnim funkcijama, hvatamo nevalidne vrednosti.
    try:
        fib_ord_num.set(Fibonacci.nth(position))
    except ValueError:
        messagebox.showerror(
            "Pogrešna vrednost",
            "Redni broj mora biti pozitivan.",
            parent=parent_win)


#
# Funkcije kojima se pozivaju prozori za izračunavanje raznih aspekata niza.
#
def sequence_of_length_win():
    """Vraća prozor za računanje niza određene dužine."""

    # Inicijalizacija prozora.
    win = tk.Toplevel()
    win.title("Računanje niza određene dužine")

    mainframe = ttk.Frame(win, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)

    # Polje za unošenje dužine niza.
    length_label = ttk.Label(mainframe, text="Dužina niza:")
    length_label.grid(column=0, row=0, sticky=tk.E)

    length_entry = ttk.Entry(mainframe, textvariable=fib_sequence_length)
    length_entry.grid(column=1, row=0, sticky=tk.W)

    ttk.Button(mainframe,
               text="Izračunaj",
               command=lambda: set_sequence(fib_sequence_length.get(),
                                            0,
                                            win)).grid(column=1, row=1, sticky=tk.E)

    # Prikaz izračunatog niza.
    sequence = ttk.Label(mainframe, textvariable=fib_sequence)
    sequence.grid(column=0, row=2, columnspan=2)

    # Prikaz niza u JSON formatu.
    ttk.Button(mainframe,
               text="Prikaži JSON",
               command=lambda: set_json(fib_sequence_length.get(),
                                        0,
                                        win)).grid(column=1, row=3, sticky=tk.E)

    ttk.Label(mainframe, textvariable=json_fib_sequence).grid(column=0,
                                                              row=4,
                                                              columnspan=2)


def nth_number_win():
    """Vraća prozor za računanje određenog Fibonačijevog broja."""

    # Inicijalizacija prozora.
    win = tk.Toplevel()
    win.title("Računanje određenog Fibonačijevog broja")

    mainframe = ttk.Frame(win, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)

    # Polje za unošenje rednog broja.
    order_label = ttk.Label(mainframe, text="Mesto broja u nizu:")
    order_label.grid(column=0, row=0, sticky=tk.E)

    order_entry = ttk.Entry(mainframe, textvariable=fib_ord)
    order_entry.grid(column=1, row=0, sticky=tk.W)

    ttk.Button(mainframe,
               text="Izračunaj",
               command=lambda: set_nth(fib_ord.get(), win)
               ).grid(column=1, row=1, sticky=tk.W)

    # Prikaz broja.
    ttk.Label(mainframe, textvariable=fib_ord_num).grid(column=0,
                                                        row=2,
                                                        columnspan=2)

def new_sequence_win():
    """Vraća prozor za računanje novog niza željene dužine."""

    # Inicijalizacija prozora.
    win = tk.Toplevel()
    win.title("Računanje novog niza određene dužine")

    mainframe = ttk.Frame(win, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)

    # Polje za unošenje početne vrednosti.
    seed_label = ttk.Label(mainframe, text="Početna vrednost:")
    seed_label.grid(column=0, row=0, sticky=tk.E)

    seed_entry = ttk.Entry(mainframe, textvariable=fib_seed)
    seed_entry.grid(column=1, row=0, sticky=tk.W)

    # Polje za unošenje dužine niza.
    length_label = ttk.Label(mainframe, text="Dužina niza:")
    length_label.grid(column=0, row=1, sticky=tk.E)

    length_entry = ttk.Entry(mainframe, textvariable=fib_sequence_length)
    length_entry.grid(column=1, row=1, sticky=tk.W)

    # Dugme za izračunavanje.
    ttk.Button(mainframe,
               text="Izračunaj",
               command=lambda: set_sequence(fib_sequence_length.get(),
                                            fib_seed.get(),
                                            win)).grid(column=1,
                                                       row=2,
                                                       sticky=tk.W)

    # Polje za prikaz.
    ttk.Label(mainframe, textvariable=fib_sequence).grid(column=0,
                                                         row=3,
                                                         columnspan=2)


#
# Glavne opcije programa.
#
ttk.Button(mainframe,
           text="Niz željene dužine",
           command=sequence_of_length_win).grid(column=0, row=0)
ttk.Button(mainframe,
           text="Određeni broj",
           command=nth_number_win).grid(column=0, row=1)
ttk.Button(mainframe,
           text="Novi niz",
           command=new_sequence_win).grid(column=0, row=2)


# Glavna petlja programa.
root.mainloop()
