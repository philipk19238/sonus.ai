from flask_restx import Namespace, Resource, fields
from ..models.user import User
search_controller = Namespace(
    'Search', 'Search endpoint', '/search'
)
from ..clients import QueryPhoneNumberClient, QueryAllClient

@search_controller.route('/<string:phone_number>')
@search_controller.doc(security=None)
class QueryPhoneNumberController(Resource):

    @search_controller.response(200, 'Successfully called endpoint')
    def get(self, phone_number):
        query_client = QueryPhoneNumberClient(phone_number)
        return query_client.create_output()

@search_controller.route('/all')
@search_controller.doc(security=None)
class QueryPhoneNumberController(Resource):

    @search_controller.response(200, 'Successfully called endpoint')
    def get(self):
        query_client = QueryAllClient(User.objects)
        return query_client.create_output()