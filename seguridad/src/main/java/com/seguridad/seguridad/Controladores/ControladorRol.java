package com.seguridad.seguridad.Controladores;
import com.seguridad.seguridad.Modelos.Rol;
import com.seguridad.seguridad.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class ControladorRol{

    @Autowired
    private RepositorioRol miRepositorioRol;

    //Crear usuario

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping()
    public Rol create(@RequestBody Rol infoRol){
        return  this.miRepositorioRol.save(infoRol);
    }

    //Actualizar Rol
    @PutMapping("{id}")
    public Rol update(@PathVariable String id,@RequestBody Rol
            infoRol){
        Rol RolActual=this.miRepositorioRol
                .findById(id)
                .orElse(null);
        if (RolActual!=null){
            RolActual.setNombre(infoRol.getNombre());
            return this.miRepositorioRol.save(RolActual);
        }else{
            return null;
        }
    }

}