package com.seguridad.seguridad.Repositorios;

import Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository

public interface RepositorioPermiso extends MongoRepository<Rol,String>{
}
