from os             import listdir
from sys            import getsizeof
from reader         import Reader
from lists          import InvertedList
from hashlib        import md5
from nltk.tokenize  import word_tokenize
from stopWords      import words

class InvertedIndex(object):

    """
        Basic implementation for inverted index posting lists.
        __init__: it just produces a dict for storing inveted index lists and list of available
                 words.
        removeJunks: this function simply remove white spaces and do some normalization
                (ignore coments).
        buildMatrix: this function is the core function for producing the inverted index
                matrix.
    """

    def __init__(self) -> None:
        self.dictionary = dict()
        self.stopWords = words
        self.sizeInByte = 0

    def removeJunks(self, lineIn):
        lineInLower=lineIn.lower()
        lineInRmdSplChars = lineInLower.replace('.',' ').replace(';',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(':',' ')
        # rmdStopWordsLn = ' '.join(w for w in lineInRmdSplChars.split() if w.lower() not in self.stopWords)
        return lineInRmdSplChars

    def buildIndex(self, path: str):
        for doc in listdir(path):
            lines = Reader(path+doc).read()
            while True:
                try:       
                    line = word_tokenize(self.removeJunks(next(lines)))
                    for term in line:
                        if term not in self.dictionary and term not in self.stopWords:
                            self.dictionary[term] = InvertedList()
                            self.dictionary[term].addToTail(listdir(path).index(doc))
                        elif term in self.dictionary and term not in self.stopWords and self.dictionary[term].tail.docId != listdir(path).index(doc):
                            self.dictionary[term].addToTail(listdir(path).index(doc))
                except StopIteration:
                    break

    def size(self):
        s = [getsizeof(self.dictionary[_]) for _ in self.dictionary]
        print()
        return sum(s)


class PositionalIndex(object):

    """
        Basic implementation for positional inverted index posting lists.
        __init__: it just produces a dict for storing inveted index lists and list of available
                stop words.
        removeJunks: this function simply remove white spaces and do some normalization
                (ignore coments).
        buildMatrix: this function is the core function for producing the postional inverted index 
                matrix.
    """

    def __init__(self) -> None:
        self.dictionary = dict()
        self.stopWords = words
        self.sizeInByte = 0

    def removeJunks(self, lineIn):
        lineInLower = lineIn.lower()
        lineInRmdSplChars = lineInLower.replace('.',' ').replace(';',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(':',' ')
        # rmdStopWordsLn = ' '.join(w for w in lineInRmdSplChars.split() if w.lower() not in self.stopWords)
        return lineInRmdSplChars
    
    def buildIndex(self, path: str):
        lineNo = 0
        noDocs = 1
        for doc in listdir(path):
            lines = Reader(path+doc).read()
            while True:
                try:       
                    lineNo += 1
                    line = word_tokenize(self.removeJunks(next(lines)))
                    for term in line:
                        if term not in self.dictionary and term not in self.stopWords:
                            self.dictionary[term] = {"noDocs": noDocs, "docs": [(doc, lineNo, line.index(term)+1), ]}
                            line[line.index(term)] = md5(f"{term}".encode('utf-8')).hexdigest()
                        elif term in self.dictionary and term not in self.stopWords:
                            self.dictionary[term]["noDocs"] = noDocs
                            self.dictionary[term]["docs"].append((doc, lineNo, line.index(term)+1))
                except StopIteration:
                    noDocs += 1
                    lineNo = 0
                    break

    def size(self):
        s = [getsizeof(self.dictionary[_]) for _ in self.dictionary]
        return sum(s)

inv = InvertedIndex()
inv.buildIndex("/home/woozy/mine/sir/docs/")

pos = PositionalIndex()
pos.buildIndex("/home/woozy/mine/sir/docs/")

print(f"InvertedIndexSize: {inv.size()}-Byte (real: {getsizeof(inv.dictionary)}-Byte) \nPositionalIndexSize: {pos.size()}-Byte (real {getsizeof(pos.dictionary)}-Byte)")
