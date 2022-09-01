from models.resultado_model import ResultadoModel
from db.resultado_repository import ResultadoRepository
from db.mesa_repository import MesaRepository

class ResultadoController():
    
    def __init__(self):
        self.repo = ResultadoRepository()
        self.repo_mesa = MesaRepository()
    
    def get(self): 
            return self.repo.get_all()

    def getById(self,id):
        return self.repo.get_by_id(id)
    
    def create(self,data,numero_mesa):
        resultado = ResultadoModel(data) #creamos Mesa
        mesa = self.repo_mesa.get_by_id(numero_mesa)
        resultado.mesa = mesa

        return{
            self.repo.save(resultado) #llamamos al repo en el metodo Save
        }

    def update(self, id,  data):
        resultado = ResultadoModel(data) #cremos mesa
        self.repo.update(id, resultado)#llamamos update y pasamos los valores
    
    def delete(self,id):
        return self.repo.delete(id) #llamamos Delete y pasamos ID
        