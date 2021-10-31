from ..models.user import User
from abc import abstractmethod
import numpy as np
import json


class QueryClient:

    @abstractmethod
    def create_output(self):
        pass

    def classify_sentiment(self, sentiment_score):
        dic = {
            1: 'satisfied',
            2: 'happy',
            3: 'agitated',
            4: 'frustrated',
            5: 'angry'
        }
        buckets = [1.6]
        while len(buckets) < 5:
            buckets.append(buckets[-1] + 1.6)
        for idx, key in enumerate(buckets):
            if sentiment_score <= key:
                return dic[idx + 1]


class QueryPhoneNumberClient(QueryClient):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    @property
    def user(self):
        user = User.objects(phone_number=self.phone_number)
        return None if not user else user[0].to_json()

    def create_output(self):
        user_data = self.user
        if user_data:
            user_data = json.loads(user_data)
            for idx, call in enumerate(user_data['calls']):
                user_data['calls'][idx]['sentiment'] = self.classify_sentiment(
                    user_data['calls'][idx]['sentiment'])
        return {'data': user_data}


class QueryAllClient(QueryClient):

    def __init__(self, user_daos):
        self.users = user_daos

    @property
    def average_sentiment(self):
        sentiments = []
        for user in self.users:
            curr = [call.sentiment for call in user.calls]
            sentiments.append(np.mean(curr))
        return self.classify_sentiment(np.mean(sentiments))

    @property
    def average_time(self):
        times = []
        for user in self.users:
            curr = [call.length for call in user.calls]
            times.append(np.mean(curr))
        return np.mean(times)

    @property
    def total_calls(self):
        total = 0
        for user in self.users:
            total += len(user.calls)
        return total

    @property
    def all_phone_numbers(self):
        return [user.phone_number for user in self.users]

    def create_output(self):
        data = {
            'average_sentiment': self.average_sentiment,
            'average_time': self.average_time,
            'total_calls': self.total_calls,
            'phone_numbers': self.all_phone_numbers
        }
        return {
            'data': data
        }
