from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

"""importando"""

from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Controladores.ControladorMesa import ControladorMesa




app = Flask(__name__)

"""
Los cors permiten que se puedan hacer pruebas al
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

miInterfaceRepositorio = InterfaceRepositorio()
miControladorMesa = ControladorMesa()


""" SERVICIOS DE LA COLECION MESA"""

@app.route("/mesa", methods=['GET'])
def getMesa():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)












if __name__ == '__main__':
    dataConfig = miInterfaceRepositorio.loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
   Se crea la instancia del servidor con la url del backend y puerto especificado
   en el archivo de configuración.
   """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
