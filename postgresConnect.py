import psycopg2 as psy
import password

conn_string = "host='localhost' dbname='dbsys' user='postgres' password='"+password.password+"'"

conn = psy.connect(conn_string)

cursor = conn.cursor()

def createTables():
	createAuthor = "Create Table author( name varchar(255), authid int);"
	createPublications = "Create Table publication( pubid int, pubkey varchar(255), title varchar(500), year int, type varchar(255), lowest_pages int, highest_pages int);"
	createArticles = "Create Table article(pubid int, journal varchar(255), volume varchar(255), number varchar(255));"
	createBooks = "Create Table book(pubid int, publisher varchar(255), isbn varchar(255));"
	createIncollection = "Create Table incollection(pubid int, booktitle varchar(255), publisher varchar(255), isbn varchar(255));"
	createInproceeding = "Create Table inproceedings(pubid int, booktitle varchar(255));"
	createPubAuthor = "Create Table pubauth(pubid int, authid int);"


	cursor.execute(createInproceeding)
	cursor.execute(createIncollection)
	cursor.execute(createBooks)
	cursor.execute(createArticles)
	cursor.execute(createPublications)
	cursor.execute(createAuthor)
	cursor.execute(createPubAuthor)

	conn.commit()

def CheckAuthor(author):
	query = "Select authid from author where name=%s;"
	args = [author]
	cursor.execute(query, args)
	return cursor.fetchall()

def CheckPub(pubkey):
	query = "Select pubid from publication where pubkey=%s;"
	args = [pubkey]
	cursor.execute(query, args)
	return cursor.fetchall()

def getMaxAuthid():
	query = "Select max(authid) from author;"
	cursor.execute(query)
	return cursor.fetchall()[0][0]

def getMaxPubid():
	query = "Select max(pubid) from publication;"
	cursor.execute(query)
	return cursor.fetchall()[0][0]

def addAuthor(author):
	checkedAuthor = CheckAuthor(author)
	if not(CheckAuthor(author)):
		newAuthid = 0
		if type(getMaxAuthid()) != type(None):
			newAuthid = getMaxAuthid() + 1
			print "if"
		else:
			newAuthid = 1
			print "else"
		print "Author:",author, "AuthID:",newAuthid
		query = "Insert into author VALUES (%s,%s);"
		args = [unicode(author), str(newAuthid)]
		try:
			print query, args
			cursor.execute(query, args)
			return str(newAuthid)
		except:
			print "Could not add author!"
			exit()
	else:
		return str(checkedAuthor[0][0])


def addArticle(pub, pubid):
	query = "Insert into article VALUES (%s,%s,%s);"
	args = [str(pubid),pub["journal"],pub["volume"]]
	try:
		print query,args
		cursor.execute(query, args)
	except:
		print "Could not add Article!"
		exit()
	return

def addInproceeding(pub, pubid):
	query = "Insert into inproceedings VALUES (%s,%s);"
	args = [str(pubid), pub["booktitle"]]
	print query, args
	try:
		cursor.execute(query, args)
	except:
		print "Could not add Inproceeding!"
		exit()
	return

def addIncollection(pub, pubid):
	query = "Insert into incollection VALUES (%s,%s,%s,%s);"
	args = [str(pubid), pub["booktitle"], pub["publisher"], pub["isbn"]]
	print query, args
	try:
		cursor.execute(query, args)
	except:
		print "incollection insert failed!"
		exit()
	return

def addBooks(pub, pubid):
	query = "Insert into book VALUES (%s, %s, %s);"
	args = [str(pubid), pub["publisher"], pub["isbn"]]
	print query, args
	try:
		cursor.execute(query, args)
	except:
		print "Book insert failed!"
		exit()
	return

def addPubAuth(pubid, authid):
	print authid
	query = "Insert into pubauth VALUES (%s, %s);"
	args = [str(pubid), authid]
	print query, args
	try:
		cursor.execute(query, args)
	except:
		print "PubAuth Insert Failed!"
		exit()


def addPublication(pub, count, type):
	print pub
	if not(CheckPub(pub["pubkey"])):
		query = "Insert into publication VALUES (%s, %s, %s, %s, %s, %s, %s);"
		args = [str(count), pub["pubkey"], pub["title"], pub["year"], pub["pubkey"].split("/")[0], pub["lowest_pages"], pub["highest_pages"]]
		if type == "book":
			addBooks(pub, count)
		elif type == "inproceedings":
			addInproceeding(pub, count)
		elif type == "incollection":
			addIncollection(pub, count)
		elif type == "article":
			addArticle(pub, count)

		for author in pub["author"]:
			print author
			authorid = addAuthor(author)
			addPubAuth(count,authorid)
			conn.commit()

		try:
			print query, args
			cursor.execute(query, args)
		except:
			print "Publication Insert Failed!"
			exit()
	else:
		print "Added already"


if __name__  == "__main__":
	cursor.execute("DROP TABLE publication")
	cursor.execute("DROP TABLE author")
	cursor.execute("DROP TABLE article")
	cursor.execute("DROP TABLE inproceedings")
	cursor.execute("DROP TABLE incollection")
	cursor.execute("DROP TABLE pubauth")
	cursor.execute("DROP TABLE book")
	createTables()