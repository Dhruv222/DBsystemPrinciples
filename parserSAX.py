import xml.sax

class docHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        if name == "article":
            for (k,v) in attrs.items():
                print k + " " + v
        elif name == "author":
            print 
            

parser = xml.sax.make_parser()
parser.setContentHandler(docHandler())
parser.parse(open("dblp.xml","r"))