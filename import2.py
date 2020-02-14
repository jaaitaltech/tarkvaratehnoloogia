#!/usr/bin/python

# esimene rida on spetsiaalne rida linuxis, mis ytleb, 
#et linux kaivitagu python ja andku see programm ette

"""
See programm eeldab, et sul on juba olemas andmebaas data.db
tabeliga maintable kus yksteist tulpa
id,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10

Programm loeb etteantud failinime, eeldab, et failis on csv
kujul andmed ja siis loeb need andmed baasi sisse.
"""

# kasutame sqlite andmebaasi teeki, 
# csv lugemise teeki ja systeemiabivahendeid
import sqlite3, csv, sys

# vota viimane failinimi kasurealt
filename = sys.argv[-1]

# vota yhendust baasiga
conn = sqlite3.connect("data.db") 

# ava csv fail lugemiseks: eri viisidel python3 ja python2 jaoks
try:
  csvfile = open(filename, encoding="iso-8859-1") # python3 variant
except: # jargmine haru taidetakse, kui eelmine ebaonnestus
  csvfile = open(filename, "rb") # python2 variant

# ytle, kuidas csv failist aru saada:
# kasutusel mitu varianti delimiteri ja quotechari jaoks
myreader = csv.reader(csvfile, delimiter=';', quotechar='"')

# loe rida realt csv failist andmed, ehita iga rea jaoks
# lisamise-sql ja lisa see rida baasi

for row in myreader:
  print(row)
  # tyhi data list (et kui pole niipalju andmeid csv real)
  data = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
  # kopeeri loetud andmed realt data listi
  n = 0
  while n<len(row):
    data[n]=row[n]
    # jalle eraldi python2 ja python3 variandid tapitahtede jaoks
    try:
      data[n]=row[n].decode('utf-8') # python2
    except:
      data[n]=row[n]  #python3	    
    n=n+1
  # tee insert-sql-lause, kus kysimargid ? asendatakse data listi elementidega  
  sql_insert= """insert into maintable (nimi,
                ariregistri_kood,
                kmkr_nr,
                ettevotja_staatus,
                Tegutsev_ettevote,
                ettevotja_staatus_tekstina,
                ettevotja_esmakande_kpv,
                ettevotja_esmakande_kuupaev,
                ettevotja_esmakande_kuu,
                ettevotja_esmakande_aasta,
                asukoha_ehak_kood,
                indeks_ettevotja_aadressis,
                ads_adr_id,
                maakond,
                Linnvald,
                Linnaosa,
                aadress,
                teabesysteemi_link) 
                 values
                 (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
  # nyyd pane insert lause kaima ja anna data ette
  conn.execute(sql_insert,data)

# sulge csv fail  
csvfile.close()

# ytle baasile, et koik ok ja andmed jaagu alles
conn.commit()

# katkesta yhendus
conn.close() 
