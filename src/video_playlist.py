"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self, playlist_name):
        self._name = playlist_name
        self._video_ids = []
        
    def add_video(self, video_id):
        self._video_ids.append(video_id)
    
    def remove_video(self, video_id):
        self._video_ids.remove(video_id)
        
    def clear_videos(self):
        self._video_ids.clear()
    
    def get_all_videos(self):
        return tuple(self._video_ids)
    
    def get_name(self):
        return self._name
    
    def contains(self, video_id):
        return video_id in self._video_ids
    
    def __str__(self):
        return f"({', '.join(self._video_ids)})"      
