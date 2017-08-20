# -*- coding: utf-8 -*-

import pymysql
from connection import Connection
import myconfig
from fileReader import MainFileHandler
from wordHarvester import dikiTranslator

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
    def _checkIfExistsInDB(cls,column,table, columnToSearch, word):
        if EnglishHelper.query("SELECT %s FROM %s WHERE %s='%s'"%(column, table, columnToSearch,word, )):
             return True
        else:
            return False

    @classmethod
    def _getNewWordsFromFile(cls, file):
        FileHandler = MainFileHandler(file)
        return FileHandler.wordsToList()

    @classmethod
    def addNewWordsFromFile(cls, file):
        for word in EnglishHelper._getNewWordsFromFile(file):
            print EnglishHelper._checkIfExistsInDB("english_word","EnglishWords", "english_word", word)
            if not EnglishHelper._checkIfExistsInDB("english_word","EnglishWords", "english_word", word):
                cls.query("INSERT INTO EnglishWords (english_word) values ('%s')" % word)

    @classmethod
    def harvestPolishMeaning(cls):
        for word in EnglishHelper.query("SELECT english_word FROM EnglishWords"):
            polishWord = dikiTranslator.searchWordPolishMeaning(word)
            print polishWord
            if not EnglishHelper._checkIfExistsInDB("polish_word", "PolishWords", "polish_word", polishWord):
                EnglishHelper.query("INSERT INTO PolishWords (polish_word) values ('%s')" % (polishWord))








if __name__ == "__main__":
    EnglishHelper.addNewWordsFromFile("words1.txt")
    #EnglishHelper.harvestPolishMeaning()
    #print EnglishHelper.query("SELECT * FROM ENGLISH_HELPER.PolishWords;")


