
package com.seguridad.seguridad.Repositorios;

import com.seguridad.seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends
        MongoRepository<Usuario,String> {
}
