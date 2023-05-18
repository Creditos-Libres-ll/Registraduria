package com.seguridad.seguridad.Controladores;

import com.seguridad.seguridad.Modelos.Permiso;
import com.seguridad.seguridad.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class ControladorPermiso{

    //inyeccion de depenencia
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    //Listar todos los permisos
    @GetMapping("")
    public List<Permiso> index(){
        return this.miRepositorioPermiso.findAll();
    }

    //crer permiso
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Permiso create(@RequestBody Permiso infoPermiso){
        return this.miRepositorioPermiso.save(infoPermiso);
    }
    //listar permiso por id
    @GetMapping("{id}")
    public  Permiso show(@PathVariable String id){
        Permiso  permisoActual = this.miRepositorioPermiso.findById(id).orElse(null);
        return permisoActual;
    }
    //acrualizar un permiso
    @PutMapping("{id}")
    public Permiso update(@PathVariable String id, @RequestBody Permiso infoPermiso){
        Permiso permisoActual = this.miRepositorioPermiso.findById(id).orElse(null);
        if(permisoActual != null){
            permisoActual.setUrl(infoPermiso.getUrl());
            permisoActual.setMetodo(infoPermiso.getMetodo());
            return this.miRepositorioPermiso.save(infoPermiso);

        }else{
            return null;
        }
    }
    //Eliminar un permiso
    @ResponseStatus(HttpStatus.NO_CONTENT) // debuelve un 1 si elimina 0 si no
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Permiso permisoActual = this.miRepositorioPermiso.findById(id).orElse(null);
        if(permisoActual != null){
            this.miRepositorioPermiso.delete(permisoActual);
        }
    }

}