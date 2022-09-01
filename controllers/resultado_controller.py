from models.mesa_model import MesaModel
from models.resultado_model import ResultadoModel
from db.resultado_repository import ResultadoRepository
from db.mesa_repository import MesaRepository
from db.partido_repository import PartidoRepository

class ResultadoController():
    
    def __init__(self):
        self.repo = ResultadoRepository()
        self.repo_mesa = MesaRepository()
        #self.repo_partido = PartidoRepository()
    
    def get(self): 
            return self.repo.get_all()

    def getById(self,id):
        return self.repo.get_by_id(id)
    
    def create(self,data,mesa_id):
        resultado = ResultadoModel(data) #creamos Mesa
        mesa = self.repo_mesa.get_by_id(mesa_id)
        #partido = self.repo_partido.get_by_id(partido_id)
        resultado.mesa = MesaModel(mesa)
        #resultado.partido = resultado.mesa + partido

        return{
            "id":self.repo.save(resultado) #llamamos al repo en el metodo Save
        }

    def update(self, id,  data):
        resultado = ResultadoModel(data) #cremos mesa
        self.repo.update(id, resultado)#llamamos update y pasamos los valores
    
    def delete(self,id):
        return self.repo.delete(id) #llamamos Delete y pasamos ID
        