

class MainFileHandler:
    # TODO: add file scanning for new files, log etc, add the iterator
    file=None

    @staticmethod
    def readFile(fileSource, directory="files/",method="r"):
        MainFileHandler.file = open(str(directory+fileSource), method)




MainFileHandler.readFile("words1.txt")
print MainFileHandler.file


