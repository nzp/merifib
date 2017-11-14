# Merifib

Program za istraživanje nekih aspekata Fibonačijevog niza.

## Funkcionalnost

*  Ispisivanje Fibonačijevog niza zadate dužine.
*  Prikaz dobijenog niza u JSON formatu sa sumom brojeva, te brojem parnih i
   neparnih u nizu.
*  Nalaženje određenog Fibonačijevog broja zadavanjem njegovog mesta u nizu.
*  Definisanje novog niza zadavanjem početne vrednosti i dužine (koja može biti
   negativna).

## Pokretanje

Za pokretanje programa potreban je Python 3.  Nakon raspakivanja arhive,
program se pokreće komandom
```
$ python3 merifib/merifib.py
```
U početnom prozoru su tasteri koji otvaraju prozore namenjene prethodno
navedenim funkcijama.

### Testovi

Za pokretanje unit testova potrebno je instalirati Python biblioteku Pytest.
Nakon toga, dovoljno je izvršiti skriptu ``test.sh`` u glavnom direktorijumu
arhive:
```
$ ./test.sh
```
Ili, direktno komandom:
```
$ PYTHONPATH=. pytest
```
## Napomene u vezi sa komentarima i sl.

Funkcionalnost vezana za zadatke iz testa se nalazi u modulu
`merifib.fibonacci` (tj. u fajlu `merifib/fibonacci.py`).  Komentari su
mešavina običnih komentara i docstringova u skladu sa preporukama iz standarda
PEP 8 i PEP 257.  Docstringovi su formatirani u skladu sa pomenutim standardima
kao i konvencijama za [Sphinx](http://www.sphinx-doc.org/en/stable/) sistem
dokumentacije i [Google style format za
docstringove](http://www.sphinx-doc.org/en/stable/ext/example_google.html) u u
meri u kojoj je to bilo pogodno za ovaj projekat.  Stil izvornog koda se trudi
da prati PEP 8.  Van docstringova, budući da je napomenuto da je potrebno dobro
iskomentarisati kod, obični komentari su možda detaljniji nego što je
uobičajeno ukoliko se prati pravilo „komentarisati zašto radi, a ne šta radi“,
tj. ponegde možda prelaze u opisivanje „šta radi“.

Što se tiče `merifib/merifib.py` gde je implementiran interfejs, pošto je deo
programa, komentari takođe prate PEP 8 i PEP 257, ali nisu detaljni kao u
`fibonacci.py` budući da implementacija samog interfejsa nije deo zadataka, a
i kod je po svojoj prirodi mahom deklarativan pa bi se komentarisanje svelo
na prevođenje TKInter API-ja na srpski.

Testovi nisu komentarisani skoro uopšte, kako zbog toga što su veoma jednostavni
i očigledni (za programera), tako i zbog uštede vremena i činjenice da ni oni
nisu bili deo samog zadatka.
