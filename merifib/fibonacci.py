"""Modul implementira klasu koja predstavlja Fibonačijev niz i operacije sa/nad
njim.

"""
import math


class Fibonacci:
    """Klasa implementira Fibonačijev niz i metode za istraživanje niza.

    Metode ove klase ne funkcionišu za generalizaciju Fibonačijevog niza na
    negativne indekse.

    Atributi:
        phi: Zlatni presek, potreban u raznim formulama.

    Metode:
        sequence: Vraća niz željene dužine.

    """

    phi = 1.618033988749895

    def __init__(self, initial=0):
        """Inicijalizuj instancu niza sa početnom vrednošću.

        Instance klase se inicijalizuju početnom vrednošću (podrazumevano 0).
        Primer::

            >>> seq_0 = Fibonacci()  # Inicijalizuje podrazumevanom vrednošću.
            >>> seq_1 = Fibonacci(initial=13)  # Ili seq_1 = Fibonacci(13).

        Args:
            initial (int): Početna vrednost niza.

        """
        # TODO: Proveri da li je validan Fibonačijev broj.
        self.initial = initial

    def sequence(self, n):
        """Generiši Fibonačijev niz određene dužine.

        Metod generiše Fibonačijev niz zadate dužine i vraća ga kao listu
        celih brojeva::

            >>> seq = Fibonacci()
            >>> seq.sequence(10)
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        Args:
            n (int): Dužina željenog niza.

        Returns:
            (list): Niz željene dužine kao lista.

        """
        # Potrebno je imati prethodni broj u nizu jer se ne kreće nužno od 0.
        # Za brojeve veće od 1, on se dobija zaokruživanjem količnika početnog
        # broja i zlatnog preseka (na osnovu Bineove fomule).
        if self.initial > 1:
            prev = round(self.initial/self.phi)
        elif self.initial == 1:
            prev = 0
        elif self.initial == 0:
            prev = 1  # Matematički netačno, ali omogućava tačno pokretanje
                      # sabiranja od nule bez definisanja obe početne vrednosti.

        # TODO: Negativne dužine.
        a = self.initial
        b = self.initial + prev
        fseq = [a, b,]

        # S obzirom da smo već popunili prva dva mesta u listi, umanjujemo
        # brojač za toliko.
        for _ in range(n-2):
            a, b = b, a + b
            fseq.append(b)

        return fseq
