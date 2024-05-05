from os             import listdir
from sys            import getsizeof
from reader         import Reader
from lists          import InvertedList
from nltk.tokenize  import word_tokenize
from hashlib        import md5

class InvertedIndex(object):
    
    def __init__(self) -> None:
        self.dictionary = dict()
        self.stopWords = ['i','i\'m', 'I\'m', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
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
        return sum(s)


class PositionalIndex(object):

    def __init__(self) -> None:
        self.dictionary = dict()
        self.stopWords = ['i','i\'m', 'I\'m', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
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
