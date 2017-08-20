# -*- coding: utf-8 -*-

class MainFileHandler:
    def __init__(self, file):
        self.file = file
        self.readFile(self.file)

    def readFile(self,fileSource, directory="files/",method="r"):
        self.file = open(str(directory+fileSource), method)

    def wordsToList(self):
        wordsList = self.file.read().split(",")
        return wordsList

    def __str__(self):
        return ("Words in file: "+str(self.wordsToList()))



    #TODO: add file scanning for new files, log etc, add the iterator


