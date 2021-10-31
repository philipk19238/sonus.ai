from flask_restx import Namespace, Resource
from twilio.twiml.voice_response import VoiceResponse
from flask import Response

twilio_controller = Namespace("Twilio", "Twilio endpoint", '/twilio')


@twilio_controller.route('/inbound')
@twilio_controller.doc(security=None)
class ReceiveInboundController(Resource):

    @twilio_controller.response(201, 'Successfully recorded call!')
    def post(self):
        resp = VoiceResponse()
        resp.record(recording_status_callback='/api/audio',
                    recording_status_callback_event='completed')
        return Response(str(resp), mimetype='text/xml')
