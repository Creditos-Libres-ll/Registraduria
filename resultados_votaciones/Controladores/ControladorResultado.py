from resultados_votaciones.Modelos.ModeloResultado import Resultado
from resultados_votaciones.Modelos.ModeloMesa import Mesa
from  resultados_votaciones.Modelos.ModeloCandidato import Candidato

from resultados_votaciones.Repositorios.RepositoriResultado import RepositorioResultado
from resultados_votaciones.Repositorios.RepositorioMesa import RepositorioMesa
from resultados_votaciones.Repositorios.RepositorioCandidato import RepositorioCandidato


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""

class ControladorResultado():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       print("Creando ControladorResultado")
       self.repositorioResultado = RepositorioResultado();
       self.repositorioMesa = RepositorioMesa();
       self.repositorioCandidato = RepositorioCandidato();



   def index(self):
       print("Listar todos los resultados")
       return self.repositorioResultado.findAll()

   def create(self, infoResultado, id_mesa , id_candidato):
       print("Crear un resultado")

       nuevoResultado = Resultado(infoResultado)
       laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
       elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
       nuevoResultado.mesa = laMesa
       nuevoResultado.candidato= elCandidato
       return self.repositorioResultado.save(nuevoResultado)


   def show(self, id):
       print("Mostrando un resultado con id ", id)
       elResultado = Resultado(self.repositorioResultado.findById(id))
       return elResultado.__dict__


   def update(self, id, id_mesa , id_candidato):
       print("Actualizando Resultado con id ", id)
       ResultadoActual = Resultado(self.repositorioResultado.findById(id))

       laMesa= Mesa(self.repositorioMesa.findById(id_mesa))
       elCandidato= Candidato(self.repositorioCandidato.findById(id_candidato))
       ResultadoActual.mesa= laMesa
       ResultadoActual.candidato= elCandidato
       return self.repositorioResultado.save(ResultadoActual)


   def delete(self, id):
       print("Elimiando Resultado con id ", id)
       return self.repositorioResultado.delete(id)