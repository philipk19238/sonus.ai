from flask_restx import Namespace, Resource, fields
from twilio.twiml.voice_response import Gather, VoiceResponse, Dial
from flask import jsonify, Response, request
import requests
import dropbox

import json

twilio_controller = Namespace('Twilio', 'Twilio endpoint', '/twilio')


@twilio_controller.route('/inbound')
@twilio_controller.doc(security=None)
class TwilioController(Resource):

    @twilio_controller.response(200, 'Successfully called endpoint')
    def post(self):
        response = VoiceResponse()
        # Access phone number
        phone_number = request.form['From']
        # response.say(
        #     'This call is going to be recorded for customer experience purposes. Please let us know what we can help you with after the tone. Press one when you are done.')
        response.record(recording_status_callback='/api/twilio/recording/callback',
                        recording_status_callback_event='completed')
        # gather = Gather(num_digits=1, action='/gather')
        return Response(str(response), mimetype='text/xml')

# @twilio_controller.route('/gather')
# @twilio_controller.doc(security=None)
# class TwilioController(Resource):

#     @twilio_controller.response(200, 'Successfully called endpoint')
#     def post(self):
#         recording_url = request.form['RecordingUrl']
#         # with requests.get(recording_url, stream=True) as r:

#         #     print('RecordingURL', flush=True)
#         #     print(recording_url, flush=True)
#         #     print(r, flush=True)


@twilio_controller.route('/recording/callback')
@twilio_controller.doc(security=None)
class TwilioController(Resource):

    @twilio_controller.response(200, 'Successfully called endpoint')
    def post(self):
        # URL to download .wav
        recording_url = request.form['RecordingUrl']
