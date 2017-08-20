# -*- coding: utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup


class dikiTranslator:
    url = "https://www.diki.pl"
    searchingSuffix= "/slownik-angielskiego?q="

    @staticmethod
    def searchWordPartOfSpeech(word):
        html = urlopen((dikiTranslator.url+dikiTranslator.searchingSuffix+word))
        bsObj = BeautifulSoup(html.read(), "html5lib")
        nameList = bsObj.findAll("span", {"class": "partOfSpeech"})
        return nameList[0].get_text()

    @staticmethod
    def searchWordPolishMeaning(word):
        html = urlopen((dikiTranslator.url+dikiTranslator.searchingSuffix+word))
        bsObj = BeautifulSoup(html.read(), "html5lib")
        nameList = bsObj.findAll("span", {"class": "hw"})
        #strip for removing spaces and tabs before
        return (nameList[1].get_text()).strip()




#print dikiTranslator.searchWordPartOfSpeech("alter")


#print dikiTranslator.searchWordPolishMeaning("alter")
