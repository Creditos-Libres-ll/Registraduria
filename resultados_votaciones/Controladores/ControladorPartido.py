from resultados_votaciones.Modelos.ModeloPartido import Partido
from resultados_votaciones.Repositorios.RepositorioPartido import RepositorioPartido

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorPartido():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los partidos")
        return self.repositorioPartido.findAll()

    def create(self, elPartido):
        print("Crear un Departamento")
        nuevoPartido = Partido(elPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elpartido = Partido(self.repositorioPartido.findById(id))
        return ellipsis.__dict__

    def update(self, id, elpartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = elpartido["nombre"]
        partidoActual.lema = elpartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        print("Elimiando partido con id ", id)
        return self.repositorioPartido.delete(id)