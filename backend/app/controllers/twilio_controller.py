from flask_restx import Namespace, Resource
from twilio.twiml.voice_response import VoiceResponse
from flask import Response, request
import requests

twilio_controller = Namespace("Twilio", "Twilio endpoint", '/twilio')


@twilio_controller.route('/inbound')
@twilio_controller.doc(security=None)
class ReceiveInboundController(Resource):

    @twilio_controller.response(201, 'Successfully recorded call!')
    def post(self):
        resp = VoiceResponse()
        phone_number = request.form['From']
        # resp.say(
            # 'This call is going to be recorded for customer experience purposes. Please let us know what we can help you with after the tone. Press the pound key when you are done.')
        resp.record(recording_status_callback='/api/audio/' + phone_number,
                    recording_status_callback_event='completed', finishOnKey='#')
        # evaluated_sentiment = requests.get(BACKEND_URL)
        # if evaluated_sentiment == 0:
        #     resp.say('I am transferring you to a live representative. Please hold.')

        # if evaluated_sentiment == 1:
        #     resp.say('We will get back to you as soon as possible. Thank you!')
        #     resp.hangup()
        return Response(str(resp), mimetype='text/xml')
