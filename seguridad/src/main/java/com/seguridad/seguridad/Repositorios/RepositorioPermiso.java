package com.seguridad.seguridad.Repositorios;

import com.seguridad.seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Permiso,String>{
}

