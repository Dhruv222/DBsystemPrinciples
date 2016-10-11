# -*- coding: utf-8 -*-

import mysql.connector as connector

conn = connector.connect(user="root", password = "CZ4031", host="127.0.0.1", database="cz4031")

cursor = conn.cursor()

def createTables():
	authorCreate = ("create table authors("
					"authID int not null,"
					"authName varchar(150) not null,"
					"Primary Key (authID)"
					");")
	authoredCreate = ("create table authored("
					"authID int not null,"
					"pubID int not null"
					");")
	publicationCreate = ("create table publication("
						"pubID int not null Primary Key,"
						"pubkey varchar(500) not null Unique,"
						"title varchar(750) Null,"
						"year int null"
						");")
	articleCreate = ("create table article("
					"pubID int not null Primary Key,"
					"journal varchar(500) null,"
					"volume int null"
					");")
	bookCreate = ("create table book("
				 "pubID int not null Primary Key,"
				 "publisher varchar(200) null,"
				 "ISBN varchar(200) null"
				 ");")
	incollectionCreate = ("create table incollection("
						 "pubID int not null Primary Key,"
						 "bookTitle varchar(750) null,"
						 "publisher varchar(200) null,"
						 "isbn varchar(200) null"
						 ");")
	inproceedingsCreate = ("create table inproceeding("
						  "pubID int not null Primary Key,"
						  "bookTitle varchar(750) null"
						  ");")

	cursor.execute(authorCreate)
	cursor.execute(authoredCreate)
	cursor.execute(publicationCreate)
	cursor.execute(articleCreate)
	cursor.execute(bookCreate)
	cursor.execute(incollectionCreate)
	cursor.execute(inproceedingsCreate)

def dropTables():
	cursor.execute("DROP TABLE IF EXISTS authored;")
	cursor.execute("DROP TABLE IF EXISTS authors;")
	cursor.execute("DROP TABLE IF EXISTS article;")
	cursor.execute("DROP TABLE IF EXISTS incollection;")
	cursor.execute("DROP TABLE IF EXISTS inproceeding;")
	cursor.execute("DROP TABLE IF EXISTS book;")
	cursor.execute("DROP TABLE IF EXISTS publication;")


def loadFiles():
	authorLoad = "LOAD DATA LOCAL INFILE \'author.csv\' INTO TABLE authors FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	pubAuthLoad = "LOAD DATA LOCAL INFILE \'pubauth.csv\' INTO TABLE authored FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	publicationLoad = "LOAD DATA LOCAL INFILE \'publication.csv\' INTO TABLE publication FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	articleLoad = "LOAD DATA LOCAL INFILE \'article.csv\' INTO TABLE article FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	bookLoad = "LOAD DATA LOCAL INFILE \'book.csv\' INTO TABLE book FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	inproceedingsLoad = "LOAD DATA LOCAL INFILE \'inproceedings.csv\' INTO TABLE inproceeding FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	incollectionLoad = "LOAD DATA LOCAL INFILE \'incollection.csv\' INTO TABLE incollection FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"

	cursor.execute(authorLoad)
	cursor.execute(pubAuthLoad)
	cursor.execute(publicationLoad)
	cursor.execute(articleLoad)
	cursor.execute(bookLoad)
	cursor.execute(inproceedingsLoad)
	cursor.execute(incollectionLoad)

def alterTables():
	articleAlter = ("Alter Table article "
					"Add Foreign Key(pubID) "
					"REFERENCES publication(pubID) ON UPDATE CASCADE ON DELETE CASCADE;"
					)
	bookAlter = ("Alter Table book "
					"Add Foreign Key(pubID) "
					"REFERENCES publication(pubID) ON UPDATE CASCADE ON DELETE CASCADE;"
					)
	incollectionAlter = ("Alter Table incollection "
					"Add Foreign Key(pubID) "
					"REFERENCES publication(pubID) ON UPDATE CASCADE ON DELETE CASCADE;"
					)
	inproceedingAlter = ("Alter Table inproceeding "
					"Add Foreign Key(pubID) "
					"REFERENCES publication(pubID) ON UPDATE CASCADE ON DELETE CASCADE;"
					)
	authoredAlter = ("Alter Table authored "
					"ADD Constraint pk_authoredID PRIMARY KEY(authID, pubID),"
					"Add Foreign Key(pubID) "
					"REFERENCES publication(pubID) ON UPDATE CASCADE ON DELETE CASCADE,"
					"Add Foreign Key(authID) "
					"REFERENCES authors(authID) ON UPDATE CASCADE ON DELETE CASCADE;"
					)
	cursor.execute(articleAlter)
	cursor.execute(bookAlter)
	cursor.execute(authoredAlter)
	cursor.execute(inproceedingAlter)
	cursor.execute(incollectionAlter)
if __name__ == "__main__":
        dropTables()
        createTables()
        #cursor.execute("ALTER DATABASE cz4031 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;")
        #cursor.execute("ALTER TABLE publication CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        loadFiles()
        #alterTables()
        conn.commit()
        conn.close()
