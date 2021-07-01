"""A video playlist library class."""

from .video_playlist import Playlist


class PlaylistLibrary:
    """A class used to represent a playlist library."""
    
    def __init__(self):
        self._playlists = {}
        
    def create_playlist(self, playlist_name):
        self._playlists[playlist_name.lower()] = Playlist(playlist_name)

    def delete_playlist(self, playlist_name):
        self._playlists.pop(playlist_name)

    def contains(self, playlist_name):
        return playlist_name.lower() in self._playlists

    def get_playlist(self, playlist_name):
        if not self.contains(playlist_name):
            return None
        return self._playlists[playlist_name.lower()]

    def get_all_playlist_names(self):        
        return [playlist.get_name() for playlist in self._playlists.values()]
        

    # ~ def __str__(self):
        # ~ return str(self._playlists)
