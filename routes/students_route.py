import json
from flask import jsonify, request, Blueprint
from controllers.student_controller import StudentController

student_module = Blueprint('students',__name__)
controller = StudentController()

@student_module.get('/')
def getStudents():
  return jsonify(controller.get())  

@student_module.post('/')
def createStudent():
  result = controller.create(request.get_json())
  return jsonify(result.__dict__), 201
  
@student_module.get('/<string:id>')
def showStudent(id):
  return jsonify(controller.getById(id).__dict__)

@student_module.put('/<string:id>')
def updateStudent(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@student_module.delete('/<string:id>')
def deleteStudent(id):
  controller.delete(id)
  return jsonify({}), 204

