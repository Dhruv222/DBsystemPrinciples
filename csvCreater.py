from __future__ import unicode_literals	
import parserSAX as parser


authorFile = open("author.csv", "w")
for key in parser.AuthorDict.keys():
	line = "{0},{1}\n".format(key, parser.AuthorDict[key])
	authorFile.write(line)
authorFile.close()


pubauthFile = open("pubauth.csv", "w")
for key in parser.PubAuthDict.keys():
	line = "{0},{1}\n".format(key,parser.PubAuthDict[key])
	pubauthFile.write(line)
pubauthFile.close()


publicationFile = open("publication.csv", "w")
for key in parser.publicationDict.keys():
	line = "{0},\"{p[pubkey]}\",\"{p[title]}\",{p[year]},{p[lowest_pages]},{p[highest_pages]}\n".format(key, p=parser.publicationDict[key])
	publicationFile.write(line)
publicationFile.close()


articleFile = open("article.csv", "w")
for key in parser.articleDict.keys():
	line = "{0},\"{p[journal]}\",{p[volume]}\n".format(key, p = parser.articleDict[key])
	articleFile.write(line)
articleFile.close()
bookFile = open("book.csv", "w")
for key in parser.bookDict.keys():
	line = "{0},\"{p[publisher]}\",\"{p[isbn]}\"\n".format(key, p = parser.bookDict[key])
	bookFile.write(line)
bookFile.close()
inproceedingsFile = open("inproceedings.csv", "w")
for key in parser.inproceedingsDict.keys():
	line = "{0},\"{p[booktitle]}\"\n".format(key, p = parser.inproceedingsDict[key])
	inproceedingsFile.write(line)
inproceedingsFile.close()
incollectionFile = open("incollection.csv", "w")
for key in parser.incollectionDict.keys():
	line = "{0},\"{p[booktitle]}\",\"{p[publisher]}\",\"{p[isbn]}\"\n".format(key, p = parser.incollectionDict[key])
	incollectionFile.write(line)
incollectionFile.close()