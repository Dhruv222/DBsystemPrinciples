import xml.sax



#Format for WWW
'''
<www mdate="2005-10-06" key="persons/Ley2003">
<author>Michael Ley</author>
<title>ACM SIGMOD Contribution Award 2003 Acceptance Speech</title>
<year>2003</year>
<url>http://www.informatik.uni-trier.de/~ley/db/about/contributionaward03.html</url>
</www>
'''


class docHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.count = 0
        self.inauthor = False
        self.intitle = False
        self.inpages = False
        self.inyear = False    
        self.involume = False
        self.injournal = False
        self.innumber = False
        self.inurl = False
        self.inee = False
        self.incrossref = False
        self.inbooktitle = False
        self.inseries = False
        self.inpublisher = False
        self.inisbn = False
        self.inschool = False
    
    def startElement(self, name, attrs):
        if name == "article" or name == "proceedings" or name == "inproceedings" or name == "book" or name == "incollection":
            self.count += 1
            if self.count == 500:
                exit()
            self.mdate = attrs.get('mdate',"")
            self.key = attrs.get('key', "")
            self.authorArray = []
            self.title = ""
            self.pages = ""
            self.year = ""
            self.volume = "" 
            self.journal = ""
            self.number = "" 
            self.url = ""            
            self.ee = ""            
            self.crossref = ""        
            self.booktitle = ""
            self.series = ""
            self.publisher = ""
            self.isbn = ""
            self.school = ""

        elif name == "author" or name == "editor":
            self.inauthor = True
            self.author = ""
        elif name == "title":
            self.intitle = True
            self.title = ""
        elif name == "pages":
            self.inpages = True
            self.pages = ""
        elif name == "year":
            self.inyear = True
            self.year = ""
        elif name == "volume":
            self.involume = True
            self.volume = ""
        elif name == "journal":
            self.injournal = True
            self.journal = ""
        elif name == "number":
            self.innumber = True
            self.number = ""
        elif name == "url":
            self.inurl = True
            self.url = ""
        elif name == "ee":
            self.inee = True
            self.ee = ""
        elif name == "crossref":
            self.incrossref = True
            self.crossref = ""
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
        elif name == "school":
            self.inschool = True
            self.school = ""
    
    def characters(self, ch):
        if self.inauthor:
            self.author += ch
        elif self.intitle:
            self.title += ch
        elif self.inpages:
            self.pages += ch
        elif self.inyear:
            self.year += ch
        elif self.involume:
            self.volume += ch 
        elif self.injournal:
            self.journal += ch
        elif self.innumber:
            self.number += ch 
        elif self.inurl:
            self.url += ch
        elif self.inee:
            self.ee += ch
        elif self.incrossref:
            self.crossref += ch
        elif self.inbooktitle:
            self.booktitle += ch
        elif self.inseries:
            self.series += ch
        elif self.inisbn:
            self.isbn += ch
        elif self.inpublisher:
            self.publisher += ch
        elif self.inschool:
            self.school += ch

    def PrintAuthors(self):
        authorString = ""
        for i in range(len(self.authorArray)):
            authorString += self.authorArray[i]+", "
        authorString = authorString[:-2]
        return authorString

    def endElement(self, name):

        if name == "article":
            #Format for Article
            '''
            <article mdate="2012-04-14" key="journals/spe/Kearns91">
            <author>Steven M. Kearns</author>
            <title>Extending Regular Expressions with Context Operators and Parse Extraction.</title>
            <pages>787-804</pages>
            <year>1991</year>
            <volume>21</volume>
            <journal>Softw., Pract. Exper.</journal>
            <number>8</number>
            <url>db/journals/spe/spe21.html#Kearns91</url>
            <ee>http://dx.doi.org/10.1002/spe.4380210803</ee>
            </article>
            '''
            print "Article", self.count
            print "\tMdate:", self.mdate
            print "\tKEY:", self.key
            print "\tAuthor:", self.PrintAuthors()
            print "\tTitle:", self.title
            print "\tPages:", self.pages
            print "\tYear:", self.year
            print "\tVolume:", self.volume
            print "\tNumber:", self.number
            print "\tURL:", self.url
            print "\tEE:", self.ee

        elif name == "proceedings":
            #Format for Proceeding
            '''
            <proceedings mdate="2011-12-29" key="tr/trier/MI99-17" publtype="informal publication">
            <editor>Dieter Baum</editor>
            <editor>Norbert Th. M&uuml;ller</editor>
            <editor>Richard R&ouml;dler</editor>
            <title>MMB '99, Messung, Modellierung und Bewertung von Rechen- und Kommunikationssystemen, 10. GI/NTG-F
            achtagung, 22.-24. September 1999, Trier, Kurzbeitr&auml;ge und Toolbeschreibungen</title>
            <booktitle>MMB (Kurzvortr&auml;ge)</booktitle>
            <series>Universit&auml;t Trier, Mathematik/Informatik, Forschungsbericht</series>
            <volume>99-16</volume>
            <year>1999</year>
            <url>db/conf/mmb/mmb99k.html</url>
            </proceedings>
            '''
            print "Proceedings", self.count
            print "\tMdate:", self.mdate
            print "\tKEY:", self.key
            print "\tAuthor:", self.PrintAuthors()
            print "\tTitle:", self.title
            print "\tBook Title:", self.booktitle
            print "\tSeries:", self.series
            print "\tYear:", self.year
            print "\tVolume:", self.volume
            print "\tURL:", self.url

        elif name == "inproceedings" or name == "incollection":
            #Format for Inproceeding
            '''
            <inproceedings mdate="2011-06-14" key="journals/lncs/Ludewig91">
            <author>Petra Ludewig</author>
            <title>Incremental Vocabulary Extensions in Text Understanding Systems.</title>
            <pages>153-166</pages>
            <year>1991</year>
            <crossref>journals/lncs/1991-546</crossref>
            <booktitle>Text Understanding in LILOG</booktitle>
            <url>db/journals/lncs/lncs546.html#Ludewig91</url>
            <ee>http://dx.doi.org/10.1007/3-540-54594-8_59</ee>
            </inproceedings>
            '''

            #Format for Incollection
            '''
            <incollection mdate="2011-06-14" key="journals/lncs/AtzeniCCT93">
            <author>Paolo Atzeni</author>
            <author>Filippo Cacace</author>
            <author>Stefano Ceri</author>
            <author>Letizia Tanca</author>
            <title>The LOGIDATA+ Model.</title>
            <pages>20-29</pages>
            <year>1993</year>
            <crossref>books/sp/Atzeni93</crossref>
            <booktitle>LOGIDATA+: Deductive Databases with Complex Objects</booktitle>
            <url>db/journals/lncs/lncs701.html#AtzeniCCT93</url>
            <ee>http://dx.doi.org/10.1007/BFb0021887</ee>
            </incollection>
            '''
            print "Proceedings", self.count
            print "\tMdate:", self.mdate
            print "\tKEY:", self.key
            print "\tAuthor:", self.PrintAuthors()
            print "\tTitle:", self.title
            print "\tBook Title:", self.booktitle
            print "\tSeries:", self.series
            print "\tYear:", self.year
            print "\tVolume:", self.volume
            print "\tURL:", self.url
            print "\tCrossref:", self.crossref
            print "\tEE:", self.ee

        elif name == "book":
            #Format for Book
            '''
            <book mdate="2008-02-08" key="conf/ncs/2006membrane">
            <editor>Gabriel Ciobanu</editor>
            <editor>Mario J. P&eacute;rez-Jim&eacute;nez</editor>
            <editor>Gheorghe Paun</editor>
            <title>Applications of Membrane Computing</title>
            <booktitle>Applications of Membrane Computing</booktitle>
            <year>2006</year>
            <isbn>978-3-540-25017-3</isbn>
            <series href="db/series/ncs/index.html">Natural Computing Series</series>
            <publisher>Springer</publisher>
            <url>db/conf/ncs/membrane2006.html</url>
            </book>
            '''
            print "Book", self.count
            print "\tMdate:", self.mdate
            print "\tKEY:", self.key
            print "\tAuthor:", self.PrintAuthors()
            print "\tTitle:", self.title
            print "\tBook Title:", self.booktitle
            print "\tYear:", self.year
            print "\tISBN:", self.isbn
            print "\tSeries:", self.series
            print "\tPublisher:", self.publisher
            print "\tURL:", self.url

        elif name == "mastersthesis" or name == "phdthesis":
            #Format for PHD Thesis
            '''
            <phdthesis mdate="2011-03-23" key="books/daglib/0071011">
            <author>Jie-Ming J. Wang</author>
            <title>Visual logic - a visual source code animation system for teaching computer science at school.</ti
            tle>
            <pages>I-XI, 1-169</pages>
            <school>TH Darmstadt</school>
            <year>1993</year>
            </phdthesis>
            '''

            #Format for Masters Thesis
            '''
            <mastersthesis mdate="2006-04-06" key="ms/Vollmer2006">
            <author>Stephan Vollmer</author>
            <title>Portierung des DBLP-Systems auf ein relationales Datenbanksystem und Evaluation der Performance.<
            /title>
            <year>2006</year>
            <school>Diplomarbeit, Universit&auml;t Trier, FB IV, Informatik</school>
            <url>http://dbis.uni-trier.de/Diplomanden/Vollmer/vollmer.shtml</url>
            </mastersthesis>
            '''
            print "Thesis"
            print "\tMdate:", self.mdate
            print "\tKEY:", self.key
            print "\tAuthor:", self.PrintAuthors()
            print "\tTitle:", self.title
            print "\tYear:", self.year
            print "\tSchool:", self.school
            print "\tURL:", self.url
        elif name == "author":
            self.inauthor = False
            self.authorArray.append(self.author)
        elif name == "title":
            self.intitle = False
        elif name == "pages":
            self.inpages = False
        elif name == "year":
            self.inyear = False
        elif name == "volume":
            self.involume = False
        elif name == "journal":
            self.injournal = False
        elif name == "number":
            self.innumber = False
        elif name == "url":
            self.inurl = False
        elif name == "ee":
            self.inee = False
        elif name == "crossref":
            self.incrossref = False
        elif name == "booktitle":
            self.inbooktitle = False
        elif name == "series":
            self.inseries = False
        elif name == "isbn":
            self.inisbn = False
        elif name == "publisher":
            self.inpublisher = False
        


parser = xml.sax.make_parser()
parser.setContentHandler(docHandler())
parser.parse(open("dblp.xml","r"))