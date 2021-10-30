from flask_restx import Namespace, Resource, fields

class HelloWorldDTO: 

    response = {
        'message': fields.String()
    }

hello_world_controller = Namespace(
    'Hello World', 'Hello World endpoint', '/hello-world')
hello_world_response = hello_world_controller.model(
    'hello_world_response', HelloWorldDTO.response)

@hello_world_controller.route('')
@hello_world_controller.doc(security=None)
class HelloWorldController(Resource):

    @hello_world_controller.response(200, 'Successfully called endpoint', hello_world_response)
    def get(self):
        return {'message': 'Hello World!'}