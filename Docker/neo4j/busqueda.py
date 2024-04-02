
from flask import Flask,render_template,request
from pymongo import MongoClient


def conectar():
    client = MongoClient('mongodb://root:root1@localhost:27017/')
    return client["mflix"]

app=Flask("EEAE")                    


@app.route("/")
def saludo():
    db=conectar()
    busqueda=db["movies"].distinct("genres")
    return render_template("busqueda.html",busqueda=busqueda) 



@app.route("/ver_genero/<variable>")
def pyton(variable):
    client=conectar()
    filter={'genres': variable}
    projection={'title':1}
    result=client['movies'].find(filter=filter,projection=projection)
    return render_template("ver_generos.html",result=result)

from bson.objectid import ObjectId


@app.route("/ver_titulo/sinopsis")
def verpeli(sinopsis):
    client=conectar()
    filter={'_fullplot': ObjectId(sinopsis)}
    result=client['movies'].find(filter=filter)
    return render_template("ver_titulo.html",result=result)
    
    
    
"""  
@app.route("/formulario",method=['GET','POST'])
def miformulario():
    if request.method == 'GET':
        recibido=(request.args.get('nombre','Valor por defecto', type=str))
        return recibido
    
    elif request.method == 'POST':
        return "Hola" + request.form.get('Manuel')
        
"""     

app.run(debug=True)