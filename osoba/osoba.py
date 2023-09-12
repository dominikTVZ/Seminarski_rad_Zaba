
from racun import Racun


class Osoba:

    def __init__(self, racun=None):
        self.__osoba_id = 0
        self.__ime = ""
        self.__prezime = ""
        self.__adresa = ""
        self.__OIB = 0
        self.__racun = racun
        self.__insert_osoba_sql = '''INSERT INTO osoba (ime, prezime, adresa, OIB, racun_id) VALUES (?,?,?,?,?); '''
        self.__select_osoba_sql = '''SELECT id_osoba, adresa, OIB, racun_id FROM osoba WHERE ime = ? AND prezime = ?; '''

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def adresa(self):
        return self.__adresa

    @adresa.setter
    def adresa(self, adresa):
        self.__adresa = adresa

    @property
    def OIB(self):
        return self.__OIB

    @OIB.setter
    def OIB(self, OIB):
        self.__OIB = OIB

    @property
    def osoba_id(self):
        return self.__osoba_id

    @osoba_id.setter
    def osoba_id(self, id_osoba):
        self.__osoba_id = id_osoba

    @property
    def racun(self):
        return self.__racun

    @racun.setter
    def racun(self, racun):
        self.__racun = racun

    def print(self):
        print(f'\tIme: {self.__ime}, Prezime: {self.__prezime}, Adresa: {self.__adresa}, OIB: {self.__OIB}, '
              f'key/id_osoba: {self.__osoba_id}')
        if (self.__racun is not None):
            print(f'racun_id: {self.racun.id}')
        return

    def insertDataToDB(self, cur):
        osoba_tapl1 = (self.ime, self.prezime, self.adresa, self.OIB, self.racun.id)
        cur.execute(self.__insert_osoba_sql, osoba_tapl1)
        return

    def fetchDatafromDB(self, ime, prezime, cur):
        found = True
        osoba_tapl1 = (ime, prezime)
        res = cur.execute(self.__select_osoba_sql, osoba_tapl1)
        redak = res.fetchone()
        if redak is None:
            found = False
        else:
            self.ime = ime
            self.prezime = prezime
            self.__osoba_id = redak[0]
            self.adresa = redak[1]
            self.OIB = redak[2]
            racun_id = redak[3]
            self.racun = Racun(racun_id)
            found = self.racun.fetchDatafromDB(cur)
        return found
