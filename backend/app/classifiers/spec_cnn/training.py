import os
import librosa
import numpy as np
import skimage.io
import pandas as pd
import pickle

from functools import lru_cache
from collections import defaultdict
from sklearn.model_selection import train_test_split
from PIL import Image

from tensorflow.keras import Sequential
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping


class SpectrogramConverter:

    HOP_LENGTH = 512
    N_MELS = 128
    TIME_STEPS = 384

    def __init__(self, path):
        self.path = path

    def load_file(self):
        return librosa.load(self.path, offset=1.0, duration=10.0, sr=22050)

    def scale_minmax(self, x, min_val=0.0, max_val=1.0):
        x_std = (x - x.min()) / (x.max() - x.min())
        x_scaled = x_std * (max_val - min_val) + min_val
        return x_scaled

    def spectrogram_image(self, y, sr, out, hop_length, n_mels):
        mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                              n_fft=hop_length*2, hop_length=hop_length)
        mels = np.log(mels + 1e-9)

        img = self.scale_minmax(mels, 0, 255).astype(np.uint8)
        img = np.flip(img, axis=0)
        img = 255-img

        skimage.io.imsave(out, img)

    def process_and_save(self, filename):
        y, sr = self.load_file()
        start_sample = 0
        length_samples = self.TIME_STEPS * self.HOP_LENGTH
        window = y[start_sample:start_sample+length_samples]
        self.spectrogram_image(window, sr=sr, out=filename,
                               hop_length=self.HOP_LENGTH, n_mels=self.N_MELS)


class Row:

    def __init__(self, file_name, path):
        self.file_name = file_name
        self.split_name = self.process_name(file_name)
        self.path = path

    def process_name(self, file_name):
        split_name = file_name.split('-')
        split_name.append(split_name.pop().split('.')[0])
        return [int(elem) for elem in split_name]

    @property
    def modality(self):
        dic = {
            1: 'audio_video',
            2: 'video',
            3: 'audio'
        }
        return dic[self.split_name[0]]

    @property
    def channel(self):
        dic = {
            1: 'speech',
            2: 'song'
        }
        return dic[self.split_name[1]]

    @property
    def emotion(self):
        return self.split_name[2]

    @property
    def emotion_string(self):
        dic = {
            1: 'neutral',
            2: 'calm',
            3: 'happy',
            4: 'sad',
            5: 'angry',
            6: 'fearful',
            7: 'disgust',
            8: 'surprised'
        }
        return dic[self.split_name[2]]

    @property
    def intensity(self):
        dic = {
            1: 'normal',
            2: 'intense'
        }
        return dic[self.split_name[3]]

    @property
    def statement(self):
        dic = {
            1: 'kids are talking by the door',
            2: 'dogs are sitting by the door'
        }
        return dic[self.split_name[4]]

    @property
    def repetition(self):
        return self.split_name[5]

    @property
    def gender(self):
        num = self.split_name[6]
        return 'female' if num % 2 == 0 else 'male'

    @property
    def path_to_file(self):
        return self.path + '/' + self.file_name

    @property
    def path_to_spec(self):
        return self.path + '/' + self.file_name.replace('.wav', '') + '-spec.png'

    def generate_spec(self):
        converter = SpectrogramConverter(self.path_to_file)
        converter.process_and_save(self.path_to_spec)

    def to_dic(self):
        return {
            'modality': self.modality,
            'channel': self.channel,
            'emotion': self.emotion,
            'intensity': self.intensity,
            'statement': self.statement,
            'repetition': self.repetition,
            'gender': self.gender,
            'path_to_file': self.path_to_file,
            'path_to_spec': self.path_to_spec,
            'emotion_string': self.emotion_string
        }


class ModelTrainer:

    def __init__(self, data_src_path, load_model=False, generate_specs=False):
        self.data_src_path = data_src_path
        self.generate_specs = generate_specs
        self.model = ModelTrainer._init_model(load_model)

    @classmethod
    def _init_model(cls, load_model):
        if load_model:
            return cls.load_model()
        else:
            return cls.create_model()

    @property
    @lru_cache()
    def df(self):
        path = self.data_src_path
        names = os.listdir(path)
        dic = defaultdict(list)
        for name in names:
            if name.startswith('.'):
                continue
            for file_name in os.listdir(path + '/' + name):
                if not file_name.endswith('.wav'):
                    continue
                row = Row(file_name, path + '/' + name)
                if self.generate_specs:
                    row.generate_spec()
                for k, v in row.to_dic().items():
                    dic[k].append(v)
        return pd.DataFrame(dic)

    @property
    def test_data(self):
        x_train, x_test, y_train, y_test = train_test_split(
            self.df['path_to_spec'].to_list(), self.df['emotion'])
        x_train = np.array(
            [np.array(Image.open(elem).resize((128, 128))) for elem in x_train])
        x_test = np.array(
            [np.array(Image.open(elem).resize((128, 128))) for elem in x_test])
        return (x_train, y_train), (x_test,  y_test)

    def train_model(self):
        training_data, _ = self.test_data
        x, y = training_data
        x = x.reshape((len(x), 128, 128, 1))
        es = EarlyStopping(patience=10, restore_best_weights=True)
        self.model.fit(x, y,
                       batch_size=32,
                       epochs=30,
                       callbacks=[es])

    def evaluate_model(self):
        _, testing_data = self.test_data
        x, y = testing_data
        x = x.reshape((len(x), 128, 128, 1))
        loss, acc = self.model.evaluate(x, y)
        return loss, acc

    def get_array_size(self, array):
        return array.shape()

    def save_model(self):
        self.model.save('model')

    @classmethod
    def load_model(cls):
        loaded_model = load_model('model')
        return cls.compile_model(loaded_model)

    @classmethod
    def create_model(cls):
        model = Sequential()
        model.add(layers.Conv2D(
            32, (4, 4), activation='relu', input_shape=(128, 128, 1)))
        model.add(layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
        model.add(layers.Conv2D(10, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
        model.add(layers.Flatten())
        model.add(layers.Dense(15, activation='relu'))
        model.add(layers.Dense(10, activation='relu'))
        return cls.compile_model(model)

    @classmethod
    def compile_model(cls, model):
        model.compile(optimizer='adam',
                      loss='mse',
                      metrics=['mae',
                               'accuracy'])
        return model


if __name__ == '__main__':
    path = os.getcwd() + '/data/Audio_Speech_Actors_01-24'
    # mt = ModelTrainer(path, load_model=True)
    # loss, mae, acc = mt.evaluate_model()
    # print('\nTesting loss: {}, mae: {}, acc: {}, \n'.format(loss, mae, acc))
    mt = ModelTrainer(path)
    mt.train_model()
    mt.save_model()
