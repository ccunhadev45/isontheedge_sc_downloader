from django.conf import settings
import soundcloud

# ... (other imports)

class SoundCloudClient(object):

    def __init__(self, client_id=None):
        if not client_id:
            client_id = settings.SOUNDCLOUD_CLIENT_ID
        self.client = soundcloud.Client(client_id=client_id)

    # Function to get user information
    def get_user(self, user_id):
        return self.client.get_user(user_id)

    # Function to get a track
    def get_track(self, track_id):
        return self.client.get_track(track_id)

    # Function to resolve a URL
    def resolve_url(self, url):
        try:
            return self.client.get(url, resolve=True)
        except soundcloud.exceptions.NotFoundError:
            return None

    # Function to get tracks based on a query
    def get_tracks(self, query, limit=None, offset=0):
        return self.client.get_tracks(q=query, limit=limit, offset=offset)

    # Function to get playlists based on a query
    def get_playlists(self, query, limit=None, offset=0):
        return self.client.get_playlists(q=query, limit=limit, offset=offset)

    # Function to get a playlist
    def get_playlist(self, playlist_id):
        return self.client.get_playlist(playlist_id)

    # Function to get users liked tracks
    def get_users_liked_tracks(self, user_id, limit=None, offset=0):
        return self.client.get_user_favorites(user_id, limit=limit, offset=offset)
