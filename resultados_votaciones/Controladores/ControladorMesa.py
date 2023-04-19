from Modelos.ModeloMesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMesa():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioMesa = RepositorioMesa
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos las Mesas")
        return self.repositorioMesa.findAll()

    def create(self, laMesa):
        print("Crear una Mesa")
        nuevaMesa = Mesa(laMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, laMesa):
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero = laMesa["numero"]
        MesaActual.cantidad_inscritos = laMesa["cantidad_inscritos"]

        return self.repositorioMesa.save(MesaActual)

    def delete(self, id):
        print("Eliminando mesa con id ", id)
        return self.repositorioMesa.delete(id)
