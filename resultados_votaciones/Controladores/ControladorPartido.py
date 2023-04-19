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
        print("Listar todos los partido")
        return self.repositorioPartido.findAll()

    def create(self, elPartido):
        print("Crear una Partido")
        nuevoPartido = Partido(elPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, elPartido):
        partidoactual = Partido(self.repositorioPartido.findById(id))
        partidoactual.numero = elPartido["nombre"]
        partidoactual.cantidad_inscritos = elPartido["lema"]

        return self.repositorioPartido.save(partidoactual)

    def delete(self, id):
        print("Eliminando partido con id ", id)
        return self.repositorioPartido.delete(id)

