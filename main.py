import pymysql
from connection import Connection
import myconfig
from fileReader import MainFileHandler

password=myconfig.password
user=myconfig.user

class EnglishHelper():
    db_con = Connection(user=user, password=password, database='ENGLISH_HELPER')
    db_con.initial_connection()

    def menu(self):
        print ("A - add new word")
        choice = input()
        if choice=='A':
            print ("Write down your english word:")

    @classmethod
    def query(cls, queryString, fetchAll=False):
        result = cls.db_con.query_exec(queryString, fetchAll=fetchAll)
        return result

    @classmethod
    def checkIfExistsInDB(cls, word):
        print cls.query(word)



#print EnglishHelper.query("SELECT * FROM ENGLISH_HELPER.EnglishWords")
EnglishHelper.checkIfExistsInDB("help")