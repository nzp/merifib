"""Modul implementira klasu koja predstavlja Fibonačijev niz i operacije sa/nad
njim.

"""

import decimal


# Podešavanje preciznosti za artimetiku sa Decimal objektima (u tekućoj niti).
# Vrednost je izabrana donekle arbitrarno: povećavana je za 100 dok 301.
# Fibonačijev broj nije izračunat tačno pomoću Bineove fomule (što se pokazalo
# dovoljnim za bar do 501. broja).
decimal.getcontext().prec = 300


class Fibonacci:
    """Klasa implementira Fibonačijev niz i metode za istraživanje niza.

    Metode ove klase ne funkcionišu za generalizaciju Fibonačijevog niza na
    negativne indekse.  Za izračunavanje se koristi Pythonovi Decimal objekti
    koji predstavljaju egzaktnu reprezentaciju realnih brojeva i omogućavaju
    artimetiku sa arbitrarno velikom preciznošću.  Alternativa, u nekim
    slučajevima, je bila korišćenje matričnog računa, ali za to bi bilo
    neophodno koristiti NumPy biblioteku, koja nije deo standardne
    biblioteke, što uvodi komplikaciju u pokretanju ovakvog jednostavnog demo
    programa, a pritom su analitička rešenja poput Bineove formule svakako
    manje prostorne i vremenske kompleksnosti (nalaženje n-tog broja pomoću
    matrične eksponencijacije ima `vremensku O(log(n)) i prostornu O(log(n)) ili
    O(1)`__).  Tačnost rešenja dobijenih aritmetikom pomoću Decimal objekata sa
    tačnošću od 300 decimalnih mesta su proverena do F(500) (501. Fibonačijevog
    broja) u slučaju nalaženja određenog broja Bineovom formulom.

    Atributi:
        initial: Početna vrednost niza u odnosu na koju se obavljaju operacije.

    Atributi klase:
        phi: Zlatni presek, potreban u raznim formulama.

    Metode:
        sequence: Vraća niz željene dužine.


    .. __: https://sites.google.com/site/theagogs/fibonacci-number

    """

    D = decimal.Decimal  # Preimenujemo da bi skratili.

    # Zlatni presek računamo kao Decimal objekat velike preciznosti.
    phi = (D(1) + D(5).sqrt()) / D(2)

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

    def sequence(self, length):
        """Generiši Fibonačijev niz određene dužine.

        Metod generiše Fibonačijev niz zadate dužine i vraća ga kao listu
        celih brojeva::

            >>> seq = Fibonacci()
            >>> seq.sequence(10)
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        Args:
            length (int): Dužina željenog niza.

        Returns:
            list: Niz željene dužine kao lista.

        """
        # Potrebno je imati prethodni broj u nizu jer se ne kreće nužno od 0.
        # Za brojeve veće od 1, on se dobija zaokruživanjem količnika početnog
        # broja i zlatnog preseka budući da je phi limes količnika dva susedna
        # Fibonačijeva broja.
        if self.initial > 1:
            prev = round(self.initial/Fibonacci.phi)
        elif self.initial == 1:
            prev = 0
        elif self.initial == 0:
            prev = 1  # Matematički netačno, ali omogućava tačno pokretanje
                      # sabiranja od nule bez definisanja obe početne vrednosti.

        # TODO: Negativne dužine.
        a = self.initial
        b = self.initial + prev
        fseq = [a, b]

        # S obzirom da smo već popunili prva dva mesta u listi, umanjujemo
        # brojač za toliko.
        for _ in range(length-2):
            a, b = b, a + b
            fseq.append(b)

        return fseq

    def nth(self, position):
        """Vrati n-ti broj Fibonačijevog niza.

        Metod vraća n-ti broj Fibonačijevog niza po definiciji, od n_0 = 0,
        dakle bez obzira kojom vrednošću je instanca niza inicijalizovana.

        Args:
            position (int): Redni broj željenog Fibonačijevog broja.  Pošto
            indeks niza (n) počinje od 0 u definiciji, važi position = n + 1.

        Returns:
            int: Fibonačijev broj na poziciji zadatoj argumentom position.

        """
        D = decimal.Decimal
        phi = Fibonacci.phi

        # Indeks niza u definiciji i Bineovoj formuli, počinje od 0.
        n = position - 1

        # Bineova formula za izračunavanje n-tog Fibonačijevog broja.
        return round((phi**D(n) - (-phi)**D(-n)) / D(5).sqrt())
