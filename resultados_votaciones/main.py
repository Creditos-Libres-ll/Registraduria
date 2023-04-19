import flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

"""importando"""

from resultados_votaciones.Repositorios.InterfaceRepositorio import InterfaceRepositorio
from resultados_votaciones.Controladores.ControladorMesa import ControladorMesa
from resultados_votaciones.Controladores.ControladorPartido import ControladorPartido



app = flask.Flask(__name__)

"""
Los cors permiten que se puedan hacer pruebas al
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

miInterfaceRepositorio = InterfaceRepositorio()
miControladorMesa = ControladorMesa()
miControladorPartido = ControladorPartido()


""" SERVICIOS DE LA COLECION MESA"""

@app.route("/mesa", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['GET'])
def getmesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


""" SERVICIOS DE LA COLECION PARTIDO"""

@app.route("/partido", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['GET'])
def getpartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)







if __name__ == '__main__':
    dataConfig = miInterfaceRepositorio.loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
   Se crea la instancia del servidor con la url del backend y puerto especificado
   en el archivo de configuración.
   """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
