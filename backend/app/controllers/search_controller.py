from flask_restx import Namespace, Resource, fields
from ..models.user import User
search_controller = Namespace(
    'Search', 'Search endpoint', '/search'
)

@search_controller.route('/<string:phone_number>')
@search_controller.doc(security=None)
class QueryPhoneNumberController(Resource):

    @search_controller.response(200, 'Successfully called endpoint', hello_world_response)
    def get(self, phone_number):
        user = User.objects(phone_number=phone_number)
        if user:
            return user[0].to_json()
        return {}