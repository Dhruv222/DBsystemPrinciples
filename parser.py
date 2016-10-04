import psycopg2 as psy
import password

conn_string = "host='localhost' dbname='dbsys' user='postgres' password='"+password.password+"'"

conn = psy.connect(conn_string)

cursor = conn.cursor()
