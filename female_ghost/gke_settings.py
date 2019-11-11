import os
from google.oauth2 import service_account

# “SB” is Storage Bucket
# “SA” is Service Account
# File will be generated through Cloud Deployment Manager
SB_SA_FILE = os.environ.get('STORAGE_BUCKETS_FILE',
                            'credentials.json')
DEFAULT_FILE_STORAGE = 'female_ghost.lib.storages.GoogleMediaFilesStorage'  # media
GS_DEFAULT_ACL = 'publicRead'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    f'/gs/{SB_SA_FILE}'
)
GS_BUCKET_NAME = os.environ.get('GS_BUCKET_NAME')
GS_LOCATION = os.environ.get('GS_LOCATION', '')
