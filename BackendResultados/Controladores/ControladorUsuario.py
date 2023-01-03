from Repositorios.RepositorioUsuario import RepositorioUsuario
from Modelos.Usuario import Usuario
class ControladorUsuario():

    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()

    def index(self):
        return self.repositorioUsuario.findAll()

    def create(self,infoUsuario):
        nuevoUsuario=Usuario(infoUsuario)
        return self.repositorioUsuario.save(nuevoUsuario)

    def show(self,id):
        elUsuario=Usuario(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__

    def update(self,id,infoUsuario):
        UsuarioActual=Usuario(self.repositorioUsuario.findById(id))
        UsuarioActual.id = infoUsuario["id"]
        UsuarioActual.seudonimo=infoUsuario["seudonimo"]
        UsuarioActual.correo = infoUsuario["correo"]
        UsuarioActual.contraseña = infoContraseña["contraseña"]
        return self.repositorioUsuario.save(UsuarioActual)

    def delete(self,id):
        return self.repositorioUsuario.delete(id)