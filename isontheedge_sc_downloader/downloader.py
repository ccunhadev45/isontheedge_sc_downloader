from .client import SoundCloudClient
from .utils import download_file, tag_file, validate_name, get_filename
from soundcloud import resource

class SoundcloudDownloader(object):

    def __init__(self, client, args=None):
        self.client = client
        self.args = args

    # Function to download top tracks
    def download_top_tracks(self, genre='all-music'):
        # Get top tracks
        tracks = self.client.get_tracks(genre=genre, limit=self.args.limit)
        # Download tracks
        for track in tracks:
            self.download_track(track)

    # Function to download new tracks
    def download_new_tracks(self):
        # Get new tracks
        tracks = self.client.get_new_tracks(limit=self.args.limit)
        # Download tracks
        for track in tracks:
            self.download_track(track)

    # Function to download tracks from a URL
    def download_tracks_from_url(self, url):
        # Resolve URL
        resolved_url = self.client.resolve_url(url)
        # Check if URL is valid
        if not resolved_url:
            print("Invalid URL")
            return
        # Handle different types of URLs
        if isinstance(resolved_url, resource.Track):
            self.download_track(resolved_url)
        elif isinstance(resolved_url, resource.Playlist):
            self.download_playlist(resolved_url)
        else:
            print("Unsupported URL type")

    # Function to download similar tracks
    def download_similar_tracks(self, url):
        # Resolve URL
        resolved_url = self.client.resolve_url(url)
        # Check if URL is valid
        if not resolved_url:
            print("Invalid URL")
            return
        # Get similar tracks
        if isinstance(resolved_url, resource.Track):
            similar_tracks = self.client.get_similar(resolved_url)
        elif isinstance(resolved_url, resource.Playlist):
            print("Similar tracks cannot be fetched for a playlist.")
            return
        else:
