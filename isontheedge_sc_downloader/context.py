from django.conf import settings

CLIENT_ID = settings.SOUNDCLOUD_CLIENT_ID  # Replace with your API key

DOWNLOAD_DIR = os.path.join(settings.BASE_DIR, 'downloads')  # Default download directory
MAX_CONCURRENT_DOWNLOADS