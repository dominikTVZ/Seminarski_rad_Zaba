
class Racun:
    def __init__(self, racun_id = 0):
        self.__IBAN = ""
        self.__stanje = 0.0
        self.__id = racun_id
        self.__insert_racun_sql = '''INSERT INTO racun (IBAN, stanje) VALUES (?,?); '''
        self.__update_racun_sql = '''UPDATE racun SET stanje = ? WHERE IBAN = ?; '''
        self.__select_racun_sql = '''SELECT IBAN, stanje FROM racun WHERE id_racun = ?; '''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def IBAN(self):
        return self.__IBAN

    @IBAN.setter
    def IBAN(self, IBAN):
        self.__IBAN = IBAN

    @property
    def stanje(self):
        return self.__stanje

    @stanje.setter
    def stanje(self, stanje):
        self.__stanje = stanje

    def insertDataToDB(self, cur):
        racun_tapl1 = (self.IBAN, self.stanje)
        cur.execute(self.__insert_racun_sql, racun_tapl1)
        self.id = cur.lastrowid
        return

    def print(self):
        print(f"\tIBAN: {self.IBAN}, Stanje: {self.stanje}")
        return

    def updateStanjeinDB(self, cur):
        racun_tapl1 = (self.stanje, self.IBAN)
        cur.execute(self.__update_racun_sql, racun_tapl1)
        return

    def fetchDatafromDB(self, cur):
        found = True
        tapl = (self.id, )
        res = cur.execute(self.__select_racun_sql, tapl)
        redak = res.fetchone()
        if redak is None:
            found = False
        else:
            self.IBAN = redak[0]
            self.stanje = redak[1]
        return found
