# -*- coding: utf-8 -*-

import mysql.connector as connector

conn = connector.connect(user="root", password = "CZ4031", host="127.0.0.1", database="cz4031")

cursor = conn.cursor()

def createTables():
	authorCreate = "create table Author(id int not null, name varchar(150) not null);"
	pubauthCreate = "create table PubAuth(aid int not null, pid int not null);"
	publicationCreate = "create table Publication(pid int not null, pubkey varchar(500) not null, title varchar(750) Null, year int Null, lowest_pages int null, highest_pages int null);"
	articleCreate = "create table Article(pid int not null, journal varchar(500) null, volume int null);"
	bookCreate = "create table Book(pid int not null, publisher varchar(200) null, isbn varchar(200) null);"
	incollectionCreate = "create table Incollection(pid int not null, booktitle varchar(750) null, publisher varchar(200) null, isbn varchar(200) null);"
	inproceedingsCreate = "create table Inproceedings(pid int not null, booktitle varchar(750) null);"

	cursor.execute(authorCreate)
	cursor.execute(pubauthCreate)
	cursor.execute(publicationCreate)
	cursor.execute(articleCreate)
	cursor.execute(bookCreate)
	cursor.execute(incollectionCreate)
	cursor.execute(inproceedingsCreate)

def dropTables():
	cursor.execute("DROP TABLE IF EXISTS Author;")
	cursor.execute("DROP TABLE IF EXISTS PubAuth;")
	cursor.execute("DROP TABLE IF EXISTS Publication;")
	cursor.execute("DROP TABLE IF EXISTS Article;")
	cursor.execute("DROP TABLE IF EXISTS Incollection;")
	cursor.execute("DROP TABLE IF EXISTS Inproceedings;")
	cursor.execute("DROP TABLE IF EXISTS Book;")

def loadFiles():
	authorLoad = "LOAD DATA LOCAL INFILE \'author.csv\' INTO TABLE author FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	pubAuthLoad = "LOAD DATA LOCAL INFILE \'pubauth.csv\' INTO TABLE pubauth FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	publicationLoad = "LOAD DATA LOCAL INFILE \'publication.csv\' INTO TABLE publication FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	articleLoad = "LOAD DATA LOCAL INFILE \'article.csv\' INTO TABLE article FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	bookLoad = "LOAD DATA LOCAL INFILE \'book.csv\' INTO TABLE book FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	inproceedingsLoad = "LOAD DATA LOCAL INFILE \'inproceedings.csv\' INTO TABLE inproceedings FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"
	incollectionLoad = "LOAD DATA LOCAL INFILE \'incollection.csv\' INTO TABLE incollection FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY \'\"\' LINES TERMINATED BY \'\n\';"

	cursor.execute(authorLoad)
	cursor.execute(pubAuthLoad)
	cursor.execute(publicationLoad)
	cursor.execute(articleLoad)
	cursor.execute(bookLoad)
	cursor.execute(inproceedingsLoad)
	cursor.execute(incollectionLoad)

dropTables()
createTables()
loadFiles()
conn.commit()
conn.close()
