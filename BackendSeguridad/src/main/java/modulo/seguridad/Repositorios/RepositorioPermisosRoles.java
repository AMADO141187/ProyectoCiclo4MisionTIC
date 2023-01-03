package modulo.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import modulo.seguridad.Modelos.PermisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}
