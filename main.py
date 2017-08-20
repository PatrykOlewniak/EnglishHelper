# -*- coding: utf-8 -*-

import random
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
            if not EnglishHelper._checkIfExistsInDB("english_word","EnglishWords", "english_word", word):
                cls.query("INSERT INTO EnglishWords (english_word) values ('%s')" % word)
                print ("New word '%s' added" % word)

    @classmethod
    def harvestPolishMeaning(cls):

        for id_eng, word in EnglishHelper.query("SELECT id_eng, english_word FROM EnglishWords",fetchAll=True):
            if not EnglishHelper._checkIfExistsInDB("id_eng","translations","id_eng",id_eng):
                polishWord = dikiTranslator.searchWordPolishMeaning(word)
                if polishWord:
                    print "ID_ENG:",id_eng," WORD:", word
                    if not EnglishHelper._checkIfExistsInDB("polish_word", "PolishWords", "polish_word", polishWord):
                        EnglishHelper.query("INSERT INTO PolishWords (polish_word) values ('%s')" % (polishWord))
                        newPolishWord_id = EnglishHelper.query("SELECT id_pl FROM PolishWords WHERE polish_word='%s'" %polishWord)
                        print "ID_PL:",newPolishWord_id[0],"connected in transactions table"
                        EnglishHelper.query("INSERT INTO translations (id_eng,id_pl) values ('%s','%s')" %(id_eng,newPolishWord_id[0]))
                else: print (word,"sorry, there was a problem with translations")


    @classmethod
    def showTranslatedWithoutJoin(cls):
        """
        only for select query training
        """
        print ("ALL WORDS WITH TRANSLATIONS STORED IN DATABASE:")
        for word1 in EnglishHelper.query("SELECT english_word FROM EnglishWords", fetchAll=True):
            try:
                print word1[0]," - ", (EnglishHelper.query("select polish_word from PolishWords where "
                                           " id_pl=(select id_pl from translations where "
                                           "id_eng = (select id_eng from EnglishWords "
                                           "where english_word = '%s'))"%word1))[0].encode('utf-8')
            except:
                print "There is no translation, sorry :("

    @classmethod
    def shuffleForEngWord(cls):
        englishWordsWithID= dict(EnglishHelper.query("SELECT id_eng, english_word FROM EnglishWords",fetchAll=True))
        listOfEnglishWordsId = englishWordsWithID.keys()
        shuffledElementID = listOfEnglishWordsId[random.randint(0, len(listOfEnglishWordsId)-1)]
        polishTranslations = dict(EnglishHelper.query("SELECT id_eng, id_pl FROM translations", fetchAll=True))
        shuffledPLID = polishTranslations[shuffledElementID]
        shuffledPLWord = (EnglishHelper.query("SELECT polish_word FROM PolishWords WHERE id_pl=%s"%shuffledPLID))
        return shuffledPLWord[0]

    @classmethod
    def shuffleForPLWord(cls):
        polishWordsWithID= dict(EnglishHelper.query("SELECT id_pl, polish_word FROM PolishWords",fetchAll=True))
        listOfPolishWordsId = polishWordsWithID.keys()
        shuffledElementID = listOfPolishWordsId[random.randint(0, len(listOfPolishWordsId)-1)]
        englishTranslations = dict(EnglishHelper.query("SELECT id_pl, id_eng FROM translations", fetchAll=True))
        shuffledEngID = englishTranslations[shuffledElementID]
        shuffledEngWord = (EnglishHelper.query("SELECT english_word FROM EnglishWords WHERE id_eng=%s"%shuffledEngID))
        return shuffledEngWord[0]

    @classmethod
    def askForWordAndCheck(cls):
        searchingWord = EnglishHelper.shuffleForEngWord()
        print "Tell me english word that means in polish : %s"%searchingWord
        answer = raw_input()
        if answer == searchingWord:
            print "GOOD JOB ! %s = %s"%(answer,searchingWord)
        else:
            print "sorry, I asked about %s"%searchingWord



if __name__ == "__main__":
    #EnglishHelper.addNewWordsFromFile("words1.txt")
    #EnglishHelper.harvestPolishMeaning()
    #EnglishHelper.showTranslatedWithoutJoin()
    #print EnglishHelper.query("SELECT * FROM ENGLISH_HELPER.PolishWords;")
    #print EnglishHelper.shuffleForEngWord()
    #print EnglishHelper.shuffleForPLWord()
    EnglishHelper.askForWordAndCheck()



