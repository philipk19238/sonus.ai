import json

from flask_restx import Namespace, Resource
from flask import current_app, request
from werkzeug.datastructures import FileStorage

from ..clients import TranscribeClient, BucketClient

audio_controller = Namespace('Audio', 'Audio endpoint', '/audio')
upload_parser = audio_controller.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

@audio_controller.route('')
@audio_controller.expect(upload_parser)
@audio_controller.doc(security=None)
class UploadAudioController(Resource):

    @audio_controller.response(201, 'Successfully uploaded audio!')
    def post(self):
        args = upload_parser.parse_args()
        audio = args['file']
        client = BucketClient()
        client.upload_audio_file(audio, 'sample.mp3')
        uri = client.generate_audio_uri('sample.mp3')
        transcribe_client = TranscribeClient()
        resp = transcribe_client.transcribe_from_uri(uri)
        output = {'results':[]}
        for res in resp.results:
            output['results'].append(res.alternatives[0].transcript)
        return output