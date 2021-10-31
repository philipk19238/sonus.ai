import json
import traceback
import numpy as np
import os

from flask_restx import Namespace, Resource
from flask import current_app, request
from werkzeug.datastructures import FileStorage

from ..clients import TranscribeClient, BucketClient, SentimentClient, CallClient
from ..models.user import User

audio_controller = Namespace('Audio', 'Audio endpoint', '/audio')
upload_parser = audio_controller.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@audio_controller.route('/<string:phone_number>')
@audio_controller.expect(upload_parser)
@audio_controller.doc(security=None)
class UploadAudioController(Resource):

    @audio_controller.response(201, 'Successfully uploaded audio!')
    def post(self, phone_number):
        try:
            call_client = CallClient(request.form)
            sent_client = SentimentClient()
            sent_client.tearup(call_client.get_audio_stream())
            all_sents = sent_client.get_all_sentiments()
            curr_user = User.objects(phone_number=phone_number)
            if not curr_user:
                curr_user = User.create(phone_number=phone_number)
            else:
                curr_user = curr_user[0]
            sent = sent_client.classify_sentiments(np.mean(all_sents))
            print(sent, all_sents, flush=True)
            call = call_client.create_call()
            call.sentiment = sent
            call_arr = curr_user.calls
            call_arr.append(call)
            curr_user.update(calls=call_arr)
            curr_user.reload()
            curr_user.save()
        except:
            traceback.print_exc()
            for filename in os.listdir(os.getcwd()):
                if filename.endswith('.wav') or filename.endswith('.png'):
                    os.remove(filename)
