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
  sql="""select id,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45 from maintable """
  
  # kui olid olemas key, op ja val, siis ehita where tingimus
  if key and val:
    if not op: # vaikimisi olgu op =
      op = "like"
    # kontrollime, kas parameetrid ok  
    if (not (key in ["id","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15","c16","c17","c18","c19","c20","c21","c22","c23","c24","c25","c26","c27","c28","c29","c30","c31","c32","c33","c34","c35","c36","c37","c38","c39","c40","c41","c42","c43","c44","c45"]) 
        or
        not (op in ["like","=","<",">","!="])):
      # valed parameetrid, sulge yhendus
      cur.close()
      conn.close()
      # anna veateade ja lopeta
      return('"error"')
    # siin koik ok
    where = " where " + key + " " + op + " ?" 
    args = ["%" + val + "%"]
  else:
    where=""
    args=None
    
  # liida where tingimus sql standardosale
  sql = sql + where
  
  # liida sql lausele sorteering
  sql = sql + " order by id asc"
  
  # tryki debugimiseks sql lause ja args valja
  print(sql, args)
  
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