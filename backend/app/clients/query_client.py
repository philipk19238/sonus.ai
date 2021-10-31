import numpy as np

from abc import abstractmethod

from ..model.user import User

class QueryClient:

    @abstractmethod
    def create_output(self):
        pass


class QueryPhoneNumberClient(QueryClient):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    @property 
    def user(self):
        return User.objects(phone_number=self.phone_number)

    def create_output(self):
        res = {}
        res['data'] = None if not self.user else self.user.to_json()
        return res


class QueryAllClient(QueryClient):

    def __init__(self, user_daos):
        self.users = user_daos

    @property
    def average_sentiment(self):
        sentiments = []
        for user in self.users:
            curr = [call.sentiment for call in user.calls]
            sentiments.append(np.mean(curr))
        return np.mean(sentiments)

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
        return [user.phone_number for user in self.user]

    def create_output(self):
        data {
            'average_sentiment': self.average_sentiment,
            'average_time': self.average_time,
            'total_calls': self.total_calls,
            'phone_numbers': self.all_phone_numbers
        }
        return {
            'data': data
        }
        
            