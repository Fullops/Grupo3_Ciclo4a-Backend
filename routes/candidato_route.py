from flask import jsonify, request, Blueprint
from controllers.candidato_controller import CandidatoController

#lo establecemos como app de blue print (coleccion de rutas)
candidato_Module = Blueprint('candidato',__name__)

#establecemos el controlador
controller = CandidatoController()

@candidato_Module.get('/') #aca tenemos el listar
def get_candidato():
    return jsonify(controller.get())

@candidato_Module.post('/') #Crear
def create_candidato():
    result = controller.create(request.get_json())
    return jsonify(result), 201


@candidato_Module.get('/<string:id>') #listar por ID
def show_candidato(id):
    return jsonify(controller.getById(id))


@candidato_Module.put('/<string:id>')#actualizar
def update_candidato(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


@candidato_Module.delete('/<string:id>')#eliminar
def del_candidato(id):
    controller.delete(id)
    return jsonify({}), 204