import requests
import io

from ..models.phone_call import PhoneCall

class CallClient:

    def __init__(self, request_form):
        self.form = request_form

    @property
    def duration(self):
        return self.form.get('RecordingDuration')

    @property 
    def date(self):
        return self.form.get('RecordingStartTime')

    @property
    def audio_link(self):
        return self.form.get('RecordingUrl')

    def create_call(self):
        dic = {
            'length': self.duration,
            'link': self.audio_link,
            'date': self.date
        }
        call = PhoneCall.create(**dic)
        return call

    def get_audio_stream(self):
        bytes_stream = requests.get(self.audio_link).content
        return io.BytesIO(bytes_stream)

