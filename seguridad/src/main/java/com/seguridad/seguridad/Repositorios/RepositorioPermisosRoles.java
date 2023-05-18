package com.seguridad.seguridad.Repositorios;

import com.seguridad.seguridad.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String> {
}
