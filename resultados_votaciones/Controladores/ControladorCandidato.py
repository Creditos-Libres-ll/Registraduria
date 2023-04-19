from resultados_votaciones.Repositorios.RepositorioCandidato import RepositorioCandidato
from resultados_votaciones.Modelos.ModeloCandidato import Candidato
from resultados_votaciones.Repositorios.RepositorioPartido import RepositorioPartido
from resultados_votaciones.Modelos.ModeloPartido import Partido



class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido =RepositorioPartido();
        print("Creando controlador Candidato")

    def index(self):
        print("Listar todos los candidatos")
        return self.repositorioCandidato.findAll()

    def create(self, elCandidato):
        print("Crear un Candidato")
        nuevoCandidato = Candidato(elCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, elCandidato):
        print("Actualizando candidato con id ", id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = elCandidato["cedula"]
        candidatoActual.numero_resolucion = elCandidato["numero_resolucion"]
        candidatoActual.nombre = elCandidato["nombre"]
        candidatoActual.apellido = elCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)

    def asignarPartido(self, id, id_partido):
        CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        CandidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(CandidatoActual)