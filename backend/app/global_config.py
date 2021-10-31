import os


class Config:

    GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
        'GOOGLE_APPLICATION_CREDENTIALS')
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGO_HOST'),
    }
