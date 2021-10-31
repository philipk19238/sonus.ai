from functools import lru_cache
from collections import defaultdict
from sklearn.model_selection import train_test_split
from PIL import Image

import os
import librosa
import numpy as np
import skimage.io
import pandas as pd

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
        self.spectrogram_image(window, sr=sr, out=filename, hop_length=self.HOP_LENGTH, n_mels=self.N_MELS)

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
            'path_to_spec': self.path_to_spec
        }

class ModelTrainer:
    
    def __init__(self, data_src_path, generate_specs=False):
        self.data_src_path = data_src_path
        self.generate_specs = generate_specs
        
    @lru_cache()
    def generate_data_set(self):
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
                    row.generate_pec()
                for k, v in row.to_dic().items():
                    dic[k].append(v)
        return pd.DataFrame(dic)
    
    def generate_test_data(self, df):
        x_train, x_test, y_train, y_test = train_test_split(df['path_to_spec'].to_list(), df['emotion'].to_list())
        x_train = [np.asarray(Image.open(elem)) for elem in x_train]
        x_test = [np.asarray(Image.open(elem)) for elem in x_test]
        return (x_train, x_test), (y_train,  y_test)

if __name__ == '__main__':
    mt = ModelTrainer(os.getcwd() + '/data/Audio_Speech_Actors_01-24', generate_specs=True)
    df = mt.generate_data_set()