"""Modul implementira klasu koja predstavlja Fibonačijev niz i operacije sa/nad
njim.

"""

import decimal
import json


# Podešavanje preciznosti za artimetiku sa Decimal objektima (u tekućoj niti).
# Vrednost je izabrana donekle arbitrarno: povećavana je za 100 dok 301.
# Fibonačijev broj nije izračunat tačno pomoću Bineove fomule (što se pokazalo
# dovoljnim za bar do 501. broja).
decimal.getcontext().prec = 300


class Fibonacci:
    """Klasa implementira Fibonačijev niz i metode za istraživanje niza.

    Metode ove klase ne funkcionišu za generalizaciju Fibonačijevog niza na
    negativne indekse.  Za izračunavanje se koriste Pythonovi Decimal objekti
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
        length: Dužina željenog niza.
        seed: Početna vrednost niza u odnosu na koju se obavljaju operacije.

    Metode:
        sequence: Vraća niz željene dužine počevši od zadatog broja u oba smera.
        nth: Vraća broj na željenom mestu po redu u nizu (od 0).
        json: Vraća reprezentaciju niza u JSON formatu sa određenim dodatnim
            informacijama o nizu.


    .. __: https://sites.google.com/site/theagogs/fibonacci-number

    """

    D = decimal.Decimal  # Preimenujemo da bi skratili.

    # Zlatni presek računamo kao Decimal objekat velike preciznosti.
    _phi = (D(1) + D(5).sqrt()) / D(2)

    def __init__(self, length=None, seed=0):
        """Inicijalizuj instancu niza sa početnom vrednošću i dužinom.

        Instance klase se inicijalizuju početnom vrednošću (podrazumevano 0) i
        dužinom niza.  Podrazumevana dužina je None, i u tom slučaju niz je
        beskonačni generator Fibonačijevih brojeva.  Primer inicijalizacije::

            >>> seq0 = Fibonacci()  # Inicijalizuje podrazumevanim vrednostima.
            >>> seq1 = Fibonacci(length=10, seed=13)  # Ili seq1 = Fibonacci(10, 13).

        Args:
            length (int or None): Dužina niza, mora biti različit od 0.
                Podrazumevana vrednost je None, i u tom slučaju niz je
                beskonačan.
            seed (int): Početna vrednost niza.  Podrazumevana vrednost je 0.
                Mora biti validan Fibonačijev broj.

        Raises:
            ValueError: Izuzetak se podiže ukoliko argument ``seed`` nije
                broj Fibonačijevog niza.  Takođe ukoliko je dužina niza 0.

        """
        # Proveravamo da li je argument seed validan Fibonačijev broj pomoću
        # svojstva da bar jedan od brojeva 5*seed^2 +/- 4 mora biti potpuni
        # kvadrat.  Broj takođe mora biti nenegativan jer ne radimo sa
        # generalizacijom na negativne brojeve.
        D = decimal.Decimal
        sq1 = D(5) * D(seed)**D(2) + D(4)
        sq2 = D(5) * D(seed)**D(2) - D(4)

        if (round(sq1.sqrt())**D(2) == sq1 or
                round(sq2.sqrt())**D(2) == sq2) and seed >= 0:
            self.seed = seed
        else:
            raise ValueError("Broj ne pripada Fibonačijevom nizu.")

        if length == 0:
            raise ValueError("Dužina mora biti različita od 0.")
        else:
            self.length = length

    @staticmethod
    def _generator_seq(a, b):
        # Pomoćni metod, odnosno generator koji vraća beskonačni niz
        # Fibonačijevih brojeva.  Nije potrebno da bude vezan bilo za klasu,
        # bilo za instancu, te je statičan metod.
        #
        # Argumenti:
        #   a (int): Prva vrednost niza.
        #   b (int): Druga vrednost niza.

        # Vraća:
        #   int: Sledeći Fibonačijev broj u nizu.
        while True:
            yield a
            a, b = b, a + b

    def sequence(self):
        """Generiši Fibonačijev niz određene dužine.

        Metod generiše inicijalizovan Fibonačijev niz i vraća ga kao listu
        Fibonačijevih brojeva (u slučaju inicijalizovane dužine), ili kao
        beskonačni generator Fibonačijevih brojeva (u slučaju podrazumevane
        vrednosti, ``None``)::

            >>> seq0 = Fibonacci(10)
            >>> seq0.sequence()
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            >>> f = Fibonacci()
            >>> seq1 = f.sequence()
            >>> i = 0
            >>> while i < 300:
                    print(next(seq1))
                    i += 1
            0
            1
            1
            .
            .
            .
            137347080577163115432025771710279131845700275212767467264610201

        Ovaj metod je izuzetak po pitanju generalizacije na negativne indekse,
        tj. brojeve.  Pošto prirodno radi za slučaj brojeva „levo“ od 0, nije
        veštački ograničavana ta mogućnost.  Na ovaj slučaj se može naići
        ukoliko se zada dovoljno mali negativan broj za dužinu niza::

            >>> f = Fibonacci(length=-10, seed=5)
            >>> f.sequence()
            [-3, 2, -1, 1, 0, 1, 1, 2, 3, 5]

        Returns:
            list or generator: Niz željene dužine, kao lista, ili generator
                Fibonačijevih brojeva ukoliko nije inicijalizovana dužina.

        """
        # Potrebno je imati prethodni broj u nizu jer se ne kreće nužno od 0,
        # pa ni nužno rastućim nizom.  Za brojeve veće od 1, on se dobija
        # zaokruživanjem količnika početnog broja i zlatnog preseka budući da
        # je phi limes količnika dva susedna Fibonačijeva broja.
        if self.seed > 1:
            prev = round(self.seed/Fibonacci._phi)
        elif self.seed == 1:
            prev = 0
        elif self.seed == 0:
            prev = 1  # Matematički netačno, ali omogućava tačno pokretanje
                      # sabiranja od nule bez definisanja obe početne vrednosti.

        a = self.seed
        b = self.seed + prev

        if self.length == None:
            return Fibonacci._generator_seq(a, b)

        # Ukoliko je tražena dužina 1, jednostavno vraćamo početnu vrednost.
        elif abs(self.length) == 1:
            return [a]

        # Ukoliko je dužina broj veći ili jednak 2.
        elif self.length >= 2:
            fseq = [a, b]

            # S obzirom da smo već popunili prva dva mesta u listi, umanjujemo
            # brojač za toliko.
            for _ in range(self.length-2):
                a, b = b, a + b
                fseq.append(b)
            return fseq

        # Slučaj sa negativnim dužinama, tj. brojanjem unazad.  Slično kao u
        # slučaju sa length >= 2, s tim što za b umesto sledeće uzimamo
        # prethodnu (``prev``) vrednost, i umesto sabiranja oduzimamo.
        elif self.length <= -2:
            b = prev
            fseq = [b, a]

            # Pošto je sada ``self.length`` negativan, neophodno je uzeti
            # njegovu apsolutnu vrednost.
            for _ in range(abs(self.length)-2):
                a, b = b, a - b

                # insert metod liste je prihvatljiv u slučaju malih listi, što
                # je ovde slučaj.  U suprotnom collections.deque iz standardne
                # biblioteke pruža O(1) vremenske performanse za ubacivanje
                # elementa na prvo mesto.
                fseq.insert(0, b)
            return fseq

    @classmethod
    def nth(cls, position):
        """Vrati n-ti broj Fibonačijevog niza.

        Metod vraća n-ti broj Fibonačijevog niza po definiciji, od n_0 = 0,
        dakle bez obzira kojom vrednošću je instanca niza inicijalizovana.  S
        obzirom da ovaj metod ne zavisi od instance, klasni je metod.  Pozicija
        mora biti pozitivna vrednost.

        Primer::

            >>> f = Fibonacci(8)
            >>> f.nth(20)
            4181

        Args:
            position (int): Redni broj željenog Fibonačijevog broja.  Pošto
                indeks niza (n) počinje od 0 u definiciji, važi
                position = n + 1.

        Returns:
            int: Fibonačijev broj na poziciji zadatoj argumentom position.

        Raises:
            ValueError: Ukoliko je pozicija manja od 1, podiže se izuzetak.

        """
        if position <= 0:
            raise ValueError("Pozicija mora biti pozitivna vrednost.")

        D = decimal.Decimal

        # Indeks niza u definiciji i Bineovoj formuli, počinje od 0.
        n = position - 1

        # Bineova formula za izračunavanje n-tog Fibonačijevog broja.
        return round((cls._phi**D(n) - (-cls._phi)**D(-n)) / D(5).sqrt())

    def json(self):
        """Vrati JSON reprezentaciju niza sa dodatnim informacijama.

        Metod vraća u JSON formatu traženi Fibonačijev niz, zbir svih brojeva u
        nizu, broj parnih, i broj neparnih brojeva u nizu.  Ukoliko dužina niza
        nije definisana, diže ``ValueError`` izuzetak.  Primer::

            >>> f = Fibonacci(10)  # Niz dužine 10, od 0.
            >>> f.json()
            '{"sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "sum": 88, "evens": 4, "odds": 6}'

        Returns:
            str: JSON objekat sa nizom (JSON array celih brojeva), zbirom
                brojeva u nizu, brojem parnih i neparnih brojeva u nizu:
                ``{"sequence": [<niz>], "sum": <suma>, "evens": <broj parnih>,
                "odds": <broj neparnih>}``.

        Raises:
            ValueError: Ukoliko je dužina niza nije definisana, tj. ukoliko je
                ``None``, podiže ValueError izuzetak.

        """
        # Pošto self.sequence() vraća generator u slučaju da nije definisana
        # dužina niza, ovde se to proverava, ukoliko je nedefinisana diže se
        # izuzetak.
        if self.length == None:
            raise ValueError("Niz mora imati dužinu.")

        seq = self.sequence()   # Traženi niz brojeva.
        seq_sum = sum(seq)      # Zbir svih brojeva u nizu.

        # Broj parnih brojeva u nizu.  Izračunat kao dužina liste brojeva iz
        # niza deljivih sa 2.  Lista je dobijena filtriranjem pomoću anonimne
        # funkcije koja ispituje vrednost ostatka celobrojnog deljenja.  Drugo
        # rešenje bi mogla biti for petlja kroz niz i uvećanje brojača za 1
        # svaki put kada tekuća vrednost iz niza zadovoljava isti uslov.
        evens = len(list(filter(lambda x: x % 2 == 0, seq)))

        # Broj neparnih brojeva, razlika dužine niza i broja parnih brojeva u
        # nizu.
        odds = len(seq) - evens

        # Formiramo dictionary koji odgovara traženom JSON objektu i vraćamo
        # ispravno formatiran JSON objekat kao string.
        return json.dumps(
            {
                "sequence": seq,
                "sum": seq_sum,
                "evens": evens,
                "odds": odds
            }
        )
