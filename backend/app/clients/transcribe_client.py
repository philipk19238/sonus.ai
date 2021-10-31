from google.cloud.speech import SpeechClient
from google.cloud import speech

from .gcp_client import GCPClient

class TranscribeClient(GCPClient):

    SAMPLE_RATE_HERTZ = 48000
    LANGUAGE_CODE = "en-US" 
    ENCODING = speech.RecognitionConfig.AudioEncoding.LINEAR16
    MODEL = "PHONE_CALL"

    def __init__(self):
        self.client = self.get_client(SpeechClient)
        
    def _get_speech_client(self):
        cred_file = '/app/app' + current_app.config.get('GOOGLE_APPLICATION_CREDENTIALS')
        client = SpeechClient.from_service_account_file(cred_file)
        return client

    def transcribe_from_uri(self, uri):
        audio = self._create_audio_object(uri=uri)
        config = self._create_config_object()
        resp = self.client.recognize(config=config, audio=audio)
        return resp

    def _create_audio_object(self, **kwargs):
        return speech.RecognitionAudio(**kwargs)

    def _create_config_object(self):
        return speech.RecognitionConfig(
            sample_rate_hertz=self.SAMPLE_RATE_HERTZ,
            encoding=self.ENCODING,
            language_code=self.LANGUAGE_CODE,
            model=self.MODEL
        )