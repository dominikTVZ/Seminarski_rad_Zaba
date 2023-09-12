class Transakcija:

    def __init__(self, platitelj=None, primatelj=None):
        self.__iznos = ""
        self.__valuta = 0
        self.__platitelj = platitelj
        self.__primatelj = primatelj
        self.__insert_transakcija_sql = '''INSERT INTO transakcija (iznos, platitelj_id, primatelj_id) VALUES (?,?,?); '''

    @property
    def iznos(self):
        return self.__iznos

    @iznos.setter
    def iznos(self, iznos):
        self.__iznos = iznos

    @property
    def platitelj(self):
        return self.__platitelj

    @platitelj.setter
    def platitelj(self, platitelj):
        self.__platitelj = platitelj

    @property
    def primatelj(self):
        return self.__primatelj

    @primatelj.setter
    def primatelj(self, primatelj):
        self.__primatelj = primatelj

    def makeTransaction(self, cur):
        # jednom skinemo iznos, a drugom dodamo iznos u njihovim objektima
        self.platitelj.racun.stanje = self.platitelj.racun.stanje - self.iznos
        self.primatelj.racun.stanje = self.primatelj.racun.stanje + self.iznos
        # azurirano stanje baze sa novim stanjem objekata
        self.platitelj.racun.updateStanjeinDB(cur)
        self.primatelj.racun.updateStanjeinDB(cur)
        # dodamo zapis u tablicu transakcija
        transakcija_tapl1 = (self.iznos, self.platitelj.osoba_id, self.primatelj.osoba_id)
        cur.execute(self.__insert_transakcija_sql, transakcija_tapl1)
        return