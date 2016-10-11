from __future__ import unicode_literals
import xml.sax


AuthorDict = dict()
PubAuthDict = dict()
publicationDict = dict()
articleDict = dict()
inproceedingsDict = dict()
bookDict = dict()
incollectionDict = dict()


class docHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.pubCount = 0
        self.authorCount = 0
        self.inauthor = False
        self.intitle = False
        self.inpages = False
        self.inyear = False    
        self.involume = False
        self.injournal = False
        self.inbooktitle = False
        self.inseries = False
        self.inpublisher = False
        self.inisbn = False
    
    def startElement(self, name, attrs):
        if name == "article" or name == "proceedings" or name == "inproceedings" or name == "book" or name == "incollection":
            self.pubCount += 1
            if self.pubCount == 100000:
                return
            print(self.pubCount)
            PubAuthDict[self.pubCount] = []
            self.key = attrs.get('key', "")
            self.authorArray = []
            self.title = ""
            self.pages = ""
            self.year = ""
            self.volume = "" 
            self.journal = ""      
            self.series = ""
            self.publisher = ""
            self.isbn = ""
            self.inpublication = True

        elif name == "author" or name == "editor":
            self.inauthor = True
            self.author = ""
        elif name == "title":
            self.intitle = True
            self.title = ""
        elif name == "year":
            self.inyear = True
            self.year = ""
        elif name == "volume":
            self.involume = True
            self.volume = ""
        elif name == "journal":
            self.injournal = True
            self.journal = ""
        elif name == "booktitle":
            self.inbooktitle = True
            self.booktitle = ""
        elif name == "series":
            self.inseries = True
            self.series = ""
        elif name == "publisher":
            self.inpublisher = True
            self.publisher = ""
        elif name == "isbn":
            self.inisbn = True
            self.isbn = ""
   
    def UpdatePublicationDict(self):
        pub = {}
        pub['pubkey'] = self.key
        pub['title'] = self.title
        pub['year'] = self.year
        publicationDict[self.pubCount] = pub
        return

    def characters(self, ch):
        if self.inauthor:
            self.author += ch
        elif self.intitle:
            self.title += ch
        elif self.inyear:
            self.year += ch
        elif self.involume:
            self.volume += ch 
        elif self.injournal:
            self.journal += ch
        elif self.inbooktitle:
            self.booktitle += ch
        elif self.inisbn:
            self.isbn += ch
        elif self.inpublisher:
            self.publisher += ch

    def endElement(self, name):

        if name == "article":
            pub = {}
            pub["journal"] = self.journal
            pub["volume"] = self.volume
            articleDict[self.pubCount] = pub
            self.UpdatePublicationDict()
            self.inpublication = False
            

        elif name == "incollection":
            pub = {}
            pub["booktitle"] = self.booktitle
            pub["publisher"] = self.publisher
            pub["isbn"] = self.isbn
            incollectionDict[self.pubCount] = pub
            self.UpdatePublicationDict()
            self.inpublication = False

        elif name == "inproceedings" or name == "proceedings":
            pub = {}
            pub["booktitle"] = self.booktitle
            inproceedingsDict[self.pubCount] = pub
            self.UpdatePublicationDict()
            self.inpublication = False

        elif name == "book":
            pub = {}
            pub["publisher"] = self.publisher
            pub["isbn"] = self.isbn
            bookDict[self.pubCount] = pub
            self.UpdatePublicationDict()
            self.inpublication = False

        elif name == "author" and self.inpublication:
            self.inauthor = False
            if not(self.author in AuthorDict):
                self.authorCount += 1
                AuthorDict[self.author] = self.authorCount
            
            PubAuthDict[self.pubCount].append(AuthorDict[self.author])
            
        elif name == "title":
            self.intitle = False
        elif name == "year":
            self.inyear = False
        elif name == "volume":
            self.involume = False
        elif name == "journal":
            self.injournal = False
        elif name == "number":
            self.innumber = False
        elif name == "booktitle":
            self.inbooktitle = False
        elif name == "isbn":
            self.inisbn = False
        elif name == "publisher":
            self.inpublisher = False
        


parser = xml.sax.make_parser()
parser.setContentHandler(docHandler())
parser.parse(open("dblp.xml"))
