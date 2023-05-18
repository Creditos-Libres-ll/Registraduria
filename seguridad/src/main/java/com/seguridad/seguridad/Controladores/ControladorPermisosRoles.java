package com.seguridad.seguridad.Controladores;

import com.seguridad.seguridad.Modelos.Permiso;
import com.seguridad.seguridad.Modelos.PermisosRoles;
import com.seguridad.seguridad.Modelos.Rol;
import com.seguridad.seguridad.Repositorios.RepositorioPermiso;
import com.seguridad.seguridad.Repositorios.RepositorioPermisosRoles;
import com.seguridad.seguridad.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class ControladorPermisosRoles {

    @Autowired
    private RepositorioPermisosRoles miRepositoriopermisosRoles;
    @Autowired
    private RepositorioRol miRepositoriorol;
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @GetMapping("")
    public List<PermisosRoles> index(){
        return this.miRepositoriopermisosRoles.findAll();
    }
    /**
    * Asignación rol y permiso
* @param id_rol
* @param id_permiso
* @return
        */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles create(@PathVariable String id_rol,@PathVariable
    String id_permiso){
        PermisosRoles nuevo=new PermisosRoles();
        Rol elRol=this.miRepositoriorol.findById(id_rol).get();
        Permiso elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if (elRol!=null && elPermiso!=null){
            nuevo.setPermiso(elPermiso);
            nuevo.setRol(elRol);
            return this.miRepositoriopermisosRoles.save(nuevo);
        }else{
            return null;
        }
    }

    @GetMapping("{id}")
    public PermisosRoles show(@PathVariable String id){
        PermisosRoles permisosRolesActual=this.miRepositoriopermisosRoles
                .findById(id)
                .orElse(null);
        return permisosRolesActual;
    }


    /**
     * Modificación Rol y Permiso
     * @param id
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles update(@PathVariable String id,@PathVariable
    String id_rol,@PathVariable String id_permiso){
        PermisosRoles permisosRolesActual=this.miRepositoriopermisosRoles
                .findById(id)
                .orElse(null);

        Rol elRol=this.miRepositoriorol.findById(id_rol).get();
        Permiso
                elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if(permisosRolesActual!=null && elPermiso!=null && elRol!=null){
            permisosRolesActual.setPermiso(elPermiso);
            permisosRolesActual.setRol(elRol);
            return
                    this.miRepositoriopermisosRoles.save(permisosRolesActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")

    public void delete(@PathVariable String id){
        PermisosRoles permisosRolesActual=this.miRepositoriopermisosRoles
                .findById(id)
                .orElse(null);
        if (permisosRolesActual!=null){
            this.miRepositoriopermisosRoles.delete(permisosRolesActual);
        }
    }
}
