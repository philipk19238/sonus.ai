import json
import numpy as np

from flask_restx import Namespace, Resource
from flask import current_app, request
from werkzeug.datastructures import FileStorage

# from ..clients import TranscribeClient, BucketClient, SentimentClient
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
        # call_client = CallClient(request.form)
        # sent_client = SentimentClient()
        # sent_client.tearup(call_client.get_audio_stream())
        # scores = sent_client.get_all_sentiments()
        # curr_user = User.objects(phone_number=phone_number)
        # if not curr_user:
        #     curr_user = User.create(phone_number=phone_number)
        # else:
        #     curr_user = curr_user[0]
        # call = call_client.create_call()
        # call = np.mean(scores)
        # call_arr = curr_user.calls
        # call_arr.append(call)
        # curr_user.update(calls=call_arr)
        # curr_user.reload()
        # curr_user.save()

        pass
            






        # # # recording_url = request.form['RecordingUrl']
        # # # print(recording_url, flush=True)
        # # print(request, flush=True)
        # # print(request.args, flush=True)
        # # print(request.form, flush=True)
        # # # args = upload_parser.parse_args()
        # # # audio = args['file']
        # # # client = BucketClient()
        # # # client.upload_audio_file(audio, 'sample.mp3')
        # # # uri = client.generate_audio_uri('sample.mp3')
        # # # transcribe_client = TranscribeClient()
        # # # resp = transcribe_client.transcribe_from_uri(uri)
        # # # output = {'results':[]}
        # # # for res in resp.results:
        # # #     output['results'].append(res.alternatives[0].transcript)
        # # # return output
        # # return