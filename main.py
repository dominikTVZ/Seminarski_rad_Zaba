import sqlite3
from osoba import Osoba
from transakcija import Transakcija
from utilities import unos_iznosa

con = sqlite3.connect("Zaba.db")
cur = con.cursor()

#unos platitelja i primatelja
platitelj_string = input(f'Unesite <ime prezime> platitelja: ')
lista = platitelj_string.split()

platitelj = Osoba()
found = platitelj.fetchDatafromDB(lista[0], lista[1], cur)
if not found:
    print('\nNema platitelja/osobe')
    exit(1)

primatelj_string = input(f'Unesite <ime prezime> primatelja: ')
lista = primatelj_string.split()

primatelj = Osoba()
found = primatelj.fetchDatafromDB(lista[0], lista[1], cur)
if not found:
    print('\nNema primatelja/osobe')
    exit(1)

print('\n Stanje prije transakcije:')
platitelj.print()
platitelj.racun.print()
print(f'\t')
primatelj.print()
primatelj.racun.print()

# iz glavnog ekrana učitaj koliko se prebacuje sa računa na račun
iznos_transakcije = unos_iznosa("\tUnesite iznos transakcije u EUR: ")

transakcija = Transakcija(platitelj, primatelj)
transakcija.iznos = iznos_transakcije
transakcija.makeTransaction(cur)

print('\n Stanje poslije transakcije:')
platitelj.print()
platitelj.racun.print()
primatelj.print()
primatelj.racun.print()


con.commit()
con.close()

