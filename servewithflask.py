# Kaimapanekuks kaivita hoopis runserver programm kasurealt
# See runserver kaivitab Flaski serveri ja ytleb, et kasutagu siinset programmi

# Brauserist katsetamiseks ava 
# http://localhost:5000/getdata

# kasutame neid teeke: Flask tuleb eelnevalt installeerida,
# teised on pythonisse sisse ehitatud standardteegi osad

from flask import Flask, request
import sqlite3
import json 

# nii tuleb Flaskile oelda
app = Flask(__name__)

# see jargmine rida ytleb, mis urli ja mis http meetodi
# jaoks jargmine programm kaivitub

@app.route('/getdata', methods=['POST', 'GET'])

# sinu programm, mis pannakse paringu peale kaima

def getdata():
   	
  # vaata, kas urlil anti key, op ja val parameetrid
  key=request.args.get("key",'')
  op=request.args.get("op",'')
  val=request.args.get("val",'') 
  
  # vota baasiga yhendust, valmista ette paring
  conn = sqlite3.connect('data.db')
  cur = conn.cursor()
  
  # hakka kokku panema paringu-sqli, alustades standardosast
  sql="""select id,nimi,
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
                teabesysteemi_link from maintable """
  
  # kui olid olemas key, op ja val, siis ehita where tingimus
  if key and val:
    if not op: # vaikimisi olgu op =
      op = "="
    # kontrollime, kas parameetrid ok  
    if (not (key in ["id","nimi","cariregistri_kood","kmkr_nr","ettevotja_staatus","Tegutsev_ettevote","ettevotja_staatus_tekstina",
    "ettevotja_esmakande_kpv","ettevotja_esmakande_kuupaev","ettevotja_esmakande_kuu","ettevotja_esmakande_aasta",
    "asukoha_ehak_kood","indeks_ettevotja_aadressis","ads_adr_id","maakond","Linnvald","Linnaosa","aadress","teabesysteemi_link"]) 
        or
        not (op in ["=","<",">","!="])):
      # valed parameetrid, sulge yhendus
      cur.close()
      conn.close()
      # anna veateade ja lopeta
      return('"error"')
    # siin koik ok
    where = " where " + key + op + "?"
    args = [val]
  else:
    where=""
    args=None
    
  # liida where tingimus sql standardosale
  sql = sql + where
  
  # liida sql lausele sorteering
  sql = sql + " order by id asc"
  
  # tryki debugimiseks sql lause ja args valja
  print(sql,args)
  
  # tee paring baasi
  if args:
    cur.execute(sql,args)
  else:
    cur.execute(sql)
    
  # loe koik read sisse, mis paringuga klapivad
  res=cur.fetchall()
  # sulge yhendus
  cur.close()
  conn.close()
  
  # teisenda saadud tulemus json formaati ja anna vastuseks
  return json.dumps(res)

# see paneb tegelikult sinu serverirakenduse kaima,
# pordil 5000 ja igaltpoolt kattesaadav 

app.run(debug=True, port=5000, host='0.0.0.0')
