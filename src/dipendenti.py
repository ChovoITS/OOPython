import datetime

class Dipendente(object):

    def __init__(self, nome, cognome, data_di_nascita, matricola):
        self.__nome = nome
        self.__cognome = cognome
        self.__data_di_nascita = data_di_nascita
        self.__matricola = matricola
    
    def __str__(self):
        return f"Nome: {self.__nome} {self.__cognome}, Matricola: {self.__matricola}"
    
    def __repr__(self):
        return f"Nome: {self.__nome}\nCognome: {self.__cognome}\nData di Nascita: {self.__data_di_nascita}\nMatricola: {self.__matricola}"

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getCognome(self):
        return self.__cognome
    
    def setCognome(self, cognome):
        self.__cognome = cognome

    def getDataDiNascita(self):
        return self.__data_di_nascita
    
    def setDataDiNascita(self, data_di_nascita):
        self.__data_di_nascita = data_di_nascita
    
    def getMatricola(self):
        return self.__matricola

    def setMatricola(self, matricola):
        self.__matricola = matricola
    
    def getEta(self):
        return int((datetime.date.today() - datetime.date.fromisoformat(self.__data_di_nascita)).days / 365)