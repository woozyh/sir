from lists import list
from os    import listdir

class InvertedIndex(object):
    
    def __init__(self) -> None:
        self.dictionary = dict()
        self.my_list    = list()

    def readDocs(self, path: str):
        for doc in listdir(path):
            file = open(f"{path}{doc}", "r")
            lines = (line.strip().split() for line in file.readlines())
            while True:
                try:       
                    pass
                    # line = next(lines)
                    # for term in line:
                    #     if term not in self.dictionary:
                    #         self.dictionary[term] = list()
                    #     elif (term in self.dictionary) and (self.dictionary[term].size != listdir(path).index(doc)):
                    #         self.dictionary[term].addToTail(listdir(path).index(doc))
                    #     else:
                    #         pass

                except StopIteration:
                    file.close()
                    break

class PositionalIndex():

    def __init__(self) -> None:
        
        pass

