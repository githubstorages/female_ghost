from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage


class GoogleMediaFilesStorage(GoogleCloudStorage):
    def _save(self, name, content):
        name = f'{settings.MEDIA_URL[1:]}{name}'
        return super()._save(name, content)

    def url(self, name):
        """
        @brief      for implementation of CDN using image field url
        @return     Dynamic return of CDN or local URL
        """
        if settings.CDN_HOSTNAME:
            url = f'{settings.CDN_HOSTNAME}/{name}'
            return url
        return super().url(name)
