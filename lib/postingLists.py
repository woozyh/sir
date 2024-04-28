from os             import listdir
from sys            import getsizeof
from reader         import Reader
from lists          import InvertedList
from nltk.tokenize  import word_tokenize

class InvertedIndex(object):
    
    def __init__(self) -> None:
        self.dictionary = dict()

    def buildIndex(self, path: str):
        for doc in listdir(path):
            lines = Reader(path+doc).read()
            while True:
                try:       
                    line = word_tokenize(next(lines))
                    for term in line:
                        if term not in self.dictionary:
                            self.dictionary[term] = InvertedList()
                            self.dictionary[term].addToTail(listdir(path).index(doc))
                        elif (term in self.dictionary) and (self.dictionary[term].tail.docId != listdir(path).index(doc)):
                            self.dictionary[term].addToTail(listdir(path).index(doc))
                except StopIteration:
                    break
        print()

class PositionalIndex(object):

    def __init__(self) -> None:
        self.dictionary = dict()

    def buildIndex(self, path: str):
        pass

ins = InvertedIndex()
ins.buildIndex("/home/woozy/mine/sir/docs/")
print(getsizeof(ins.dictionary))