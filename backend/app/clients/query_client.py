from ..models.user import User
from functools import lru_cache
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
        idx = len(buckets) - 2
        while idx > 1:
            key = buckets[idx]
            prev_key = buckets[idx - 1]
            if prev_key <= sentiment_score <= key:
                return dic[idx + 1]
            idx -= 1
        if sentiment_score <= buckets[0]:
            return dic[1]
        else:
            return dic[5]


class QueryPhoneNumberClient(QueryClient):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    @property
    @lru_cache()
    def user(self):
        user = User.objects(phone_number=self.phone_number)
        return None if not user else user[0]

    @property
    def average_length(self):
        res = []
        for call in self.user.calls:
            res.append(call.length)
        return int(np.mean(res))

    @property
    def average_sentiment(self):
        res = []
        for call in self.user.calls:
            res.append(call.sentiment)
        return self.classify_sentiment(np.mean(res))

    def create_output(self):
        user_data = self.user
        if user_data:
            user_data = json.loads(user_data.to_json())
            user_data['average_length'] = self.average_length
            user_data['average_sentiment'] = self.average_sentiment
            for idx, phone_call in enumerate(user_data['calls']):
                user_data['calls'][idx]['sentiment'] = self.classify_sentiment(
                    phone_call['sentiment'])
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
        return int(np.mean(times))

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
