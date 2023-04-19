from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

"""importando"""

from  Repositorios.InterfaceRepositorio import InterfaceRepositorio





app = Flask(__name__)

"""
Los cors permiten que se puedan hacer pruebas al
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

miInterfaceRepositorio= InterfaceRepositorio()
















if __name__ == '__main__':
    dataConfig = miInterfaceRepositorio.loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
   Se crea la instancia del servidor con la url del backend y puerto especificado
   en el archivo de configuración.
   """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
