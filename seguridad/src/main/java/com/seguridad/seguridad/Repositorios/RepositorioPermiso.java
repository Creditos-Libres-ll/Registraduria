package com.seguridad.seguridad.Repositorios;

import com.seguridad.seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Rol,String>{
}
