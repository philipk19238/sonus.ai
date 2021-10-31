from flask import current_app
from google.oauth2 import service_account

class GCPClient: 

    WORKING_DIR = "/app/app"

    def get_client(self, gcp_instance, *args, **kwargs):
        cred_file = self.WORKING_DIR + current_app.config.get('GOOGLE_APPLICATION_CREDENTIALS')
        creds = service_account.Credentials.from_service_account_file(cred_file)
        return gcp_instance(credentials=creds, *args, **kwargs)