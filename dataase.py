import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="Somapal@5201", database="parking")
from Main import *
var1 = licPlate.strChars
mycursor=mydb.cursor()

mycursor.execute("insert into licenseplate values('%s' ,1, '2011-03-13 02:53:50' )" , var1)
mydb.commit()




