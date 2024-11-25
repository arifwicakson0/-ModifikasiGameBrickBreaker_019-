import sqlite3
con = sqlite3.connect("DB1.db")
cor = con.cursor()
a=input('masukan nomor: ')
b=input('masukan nama: ')
cor.execute("""
        INSERT INTO TBL1 VALUES
            ({}, '{}')
""".format(a.b))
con.commit()
