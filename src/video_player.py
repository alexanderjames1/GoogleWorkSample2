"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from .playlist_library import PlaylistLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist_library = PlaylistLibrary()
        self._current_video = None
        self._is_paused = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:")
        sorted_videos = self._video_library.get_all_videos()
        sorted_videos.sort()
        
        for video in sorted_videos:
            print(f"    {video}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
                
        video_to_play = self._video_library.get_video(video_id)        
        if not video_to_play:
            print("Cannot play video: Video does not exist")
            return
        
        if self._current_video:
            print(f"Stopping video: {self._current_video.title}")
        
        print(f"Playing video: {video_to_play.title}")
        self._current_video = video_to_play
        self._is_paused = False

    def stop_video(self):
        """Stops the current video."""

        if self._current_video:
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None
            self._is_paused = None                   
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        all_videos = self._video_library.get_all_videos()
        if all_videos:
            random_video = random.choice(all_videos)
            self.play_video(random_video.video_id)            
        else:
            print("No videos available")  

    def pause_video(self):
        """Pauses the current video."""
        
        if not self._current_video:
            print("Cannot pause video: No video is currently playing")    
        elif self._is_paused:
            print(f"Video already paused: {self._current_video.title}")
        else:            
            print(f"Pausing video: {self._current_video.title}")
            self._is_paused = True

    def continue_video(self):
        """Resumes playing the current video."""

        if not self._current_video:
            print("Cannot continue video: No video is currently playing")
        elif self._is_paused:
            print(f"Continuing video: {self._current_video.title}")
            self._is_paused = False      
        else:
            print("Cannot continue video: Video is not paused")    

    def show_playing(self):
        """Displays video currently playing."""

        if not self._current_video:
            print("No video is currently playing")
        else:
            print(f"Currently playing: {self._current_video} {'- PAUSED' if self._is_paused else ''}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self._playlist_library.contains(playlist_name):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist_library.create_playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """        
        playlist = self._playlist_library.get_playlist(playlist_name)
        video = self._video_library.get_video(video_id)
            
        if not playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif not video:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif playlist.contains(video_id):
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            playlist.add_video(video_id)
            print(f"Added video to {playlist_name}: {video.title}")          
            
    def show_all_playlists(self):
        """Display all playlists."""
        
        playlist_names = self._playlist_library.get_all_playlist_names()
        
        if not playlist_names:
            print("No playlists exist yet")
        else:
            playlist_names.sort()
            print("Showing all playlists: ")
            print("\n".join(playlist_names))

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if not playlist:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")   
            return
        
        print(f"Showing playlist: {playlist_name}")
        
        video_ids = playlist.get_all_videos()
        if not video_ids:
            print("No videos here yet")
        else:
            videos = [str(self._video_library.get_video(video_id)) for video_id in video_ids]
            print('\n'.join(videos))
            
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        video = self._video_library.get_video(video_id)
            
        if not playlist:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif not video:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif not playlist.contains(video_id):
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            playlist.remove_video(video_id)
            print(f"Removed video from {playlist_name}: {video.title}")       
            
    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
            
        if not playlist:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            playlist.clear_videos()
            print(f"Successfully removed all videos from {playlist_name}")               
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
    
        if not playlist:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self._playlist_library.delete_playlist(playlist_name)
            print(f"Deleted playlist: {playlist_name}")  
            
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
