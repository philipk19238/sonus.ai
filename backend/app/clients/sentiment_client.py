import librosa
import pydub
import numpy as np
import os

from tensorflow.keras.models import load_model
from PIL import Image

from .call_client import CallClient
from ..classifiers.spec_cnn.training import SpectrogramConverter


class SentimentClient:

    def tearup(self, stream):
        with open('temp.wav', mode='bx') as f:
            f.write(stream)

    def teardown(self):
        os.remove('temp.wav')

    def stream_audio_file(self):
        audio = pydub.AudioSegment.from_file('temp.wav', 'wav')
        chunk_size = 3 * 1000
        chunks = pydub.utils.make_chunks(audio, chunk_size)
        for idx, chunk in enumerate(chunks):
            chunk_name = f'chunk{idx}.wav'
            chunk.export(chunk_name, format='wav')
            yield chunk_name

    def get_sentiment_from_chunk(self, chunk_name, model):
        name, _ = chunk_name.split('.')
        image_name = name + '.png'
        converter = SpectrogramConverter(chunk_name)
        converter.process_and_save(image_name)
        img = np.asarray(Image.open(image_name).resize((28, 28)))
        img = img.reshape(1, 28, 28, 1)
        os.remove(image_name)
        os.remove(chunk_name)
        return model.predict(img)

    def get_all_sentiments(self):
        model = load_model("/app/app/classifiers/spec_cnn/model")
        scores = []
        for chunk_name in self.stream_audio_file():
            scores.append(self.get_sentiment_from_chunk(chunk_name, model))
        return scores
