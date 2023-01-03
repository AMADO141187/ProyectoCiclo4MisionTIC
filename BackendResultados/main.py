from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import requests
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

#========Conexion a la Base de Datos ====================
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://administrador:NandO551299*@cluster0.3252ll4.mongodb.net/bd-registraduria?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["bd-registraduria"]
print(baseDatos.list_collection_names())
#=========================================================

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario=ControladorUsuario()
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato=ControladorCandidato()
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()
from Controladores.ControladorResultado import ControladorResultado
miControladorResultado=ControladorResultado()


@app.route("/",methods=['GET'])
def test():
   json = {}
   json["message"]="Server running ..."
   return jsonify(json)

#=========  Servicio Usuario  ===============

@app.route("/usuario",methods=['GET'])
def getUsuarios():
    json=miControladorUsuario.index()
    return jsonify(json)

@app.route("/usuario",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)
@app.route("/usuario/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)
@app.route("/usuario/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json=miControladorUsuario.update(id, data)
    return jsonify(json)

@app.route("/usuario/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)
#========= Servicios Mesa ==========
@app.route("/mesa",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

#=========  Servicio Candidato  ===============

@app.route("/candidato",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

#========= Servicios Partido ==========

@app.route("/partido",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['GET'])
def getpartidos(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

#=========  Servicio Resultado  ===============

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=miControladorResultado.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorResultado.delete(id)
    return jsonify(json)

#=========  Fin Servicios  ===============

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
