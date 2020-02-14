#!/usr/bin/python

# esimene rida on spetsiaalne rida linuxis, mis ytleb, 
#et linux kaivitagu python ja andku see programm ette

"""
See programm teeb sqlite andmebaasi nimega data.db
ja ehitab sinna tyhja tabeli maintable yheteistkymne tulbaga
id,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10

Sa void kasutada endale arusaadavamaid sisulisi tulbanimesid,
siis pead neid kasutama ka teistes programmides, mis
seda baasi kasutavad. 

NB! id vali taidetakse edaspidi automaatselt.
"""

# kasutame sqlite andmebaasi teeki
import sqlite3

# vota yhendust: kui baasi pole, see tehakse
conn = sqlite3.connect("data.db") 

# kui baas ja tabel juba olemas, kustuta tabel
sql_drop = """drop table if exists maintable"""
conn.execute(sql_drop)

# tee andmebaasi schema yhe tabeliga
# kus id vali taidetakse edaspidi automaatselt
sql_create = """create table maintable(id integer primary key autoincrement,
                nimi,
                ariregistri_kood,
                kmkr_nr,ettevotja_staatus,
                Tegutsev_ettevote,
                ettevotja_staatus_tekstina,
                ettevotja_esmakande_kpv,
                ettevotja_esmakande_kuupaev,
                ettevotja_esmakande_kuu,
                ettevotja_esmakande_aasta,
                asukoha_ehak_kood,
                indeks_ettevotja_aadressis,
                ads_adr_id,maakond,
                Linnvald,
                Linnaosa,
                aadress,
                teabesysteemi_link)"""
conn.execute(sql_create)

# katkesta yhendus
conn.close() 