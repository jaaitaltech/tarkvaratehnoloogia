#!/usr/bin/python

# esimene rida on spetsiaalne rida linuxis, mis ytleb, 
#et linux kaivitagu python ja andku see programm ette

"""
See programm trykib valja andmebaasi data.db sisu
"""

# kasutame sqlite andmebaasi teeki
import sqlite3

# vota yhendust
conn = sqlite3.connect("data.db") 

# tee paring, loe koik tulemused ja tryki valja
sql_query = """ select * from maintable """
cur = conn.cursor()
cur.execute(sql_query)
rows = cur.fetchall()
print(rows)

# katkesta yhendus
conn.close() 