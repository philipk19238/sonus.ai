from google.cloud import storage

from .gcp_client import GCPClient

class BucketClient(GCPClient):

    DEFAULT_BUCKET = "sonus-audio"

    def __init__(self):
        self.client = self.get_client(storage.Client)

    def upload_file(self, file_obj, filename, prefix=None, bucket_name=None):
        bucket_name = bucket_name or self.DEFAULT_BUCKET
        bucket = self.client.bucket(bucket_name)
        destination_name = "/".join((prefix, filename))
        blob = bucket.blob(destination_name)
        blob.upload_from_string(file_obj.read())

    def upload_audio_file(self, file_obj, filename):
        self.upload_file(file_obj, filename, prefix='audio-files')

    def generate_uri(self, filename, prefix=None, bucket_name=None):
        bucket_name = bucket_name or self.DEFAULT_BUCKET
        destination_name = "/".join((prefix, filename))
        return "gs://" + bucket_name + "/" + destination_name

    def generate_audio_uri(self, filename):
        return self.generate_uri(filename, prefix='audio-files')