from models.candidato_model import CandidatoModel
from db.candidato_repository import CandidatoRepository

class CandidatoController():
    
    def __init__(self):
        self.repo = CandidatoRepository()
    
    def get(self): 
            return self.repo.get_all()

    def getById(self,id):
        return self.repo.get_by_id(id)
    
    def create(self,data):
        candidato = CandidatoModel(data) #creamos Mesa
        return {
            "id":self.repo.save(candidato) #llamamos al repo en el metodo Save
        }
    def update(self, id,  data):
        candidato = CandidatoModel(data) #cremos mesa
        self.repo.update(id, candidato)#llamamos update y pasamos los valores
    
    def delete(self,id):
        return self.repo.delete(id) #llamamos Delete y pasamos ID
        