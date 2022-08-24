from models.student_model import StudentModel
from db.student_repository import StudentRepository
class StudentController():
  
  def __init__(self) -> None:
    self.repo = StudentRepository()
  
  def get(self):
    return self.repo.get_all()
  
  def get_by_id(self,id):
    return self.repo.get_by_id(id)
  
  # def create(self,data):
  #   self.students[data['id']] = StudentModel(data)
  #   return self.students[data['id']]
  
  # def update(self,id, data):
  #   student = self.students[id]
  #   for key, value in data.items():
  #     setattr(student, key, value)
  #     # student[key] = value
  
  # def delete(self,id):
  #   del self.students[id]