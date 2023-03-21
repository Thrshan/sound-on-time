import spotipy
import spotipy.oauth2 as oauth2
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRETc")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
DEVICE_NAME = os.environ.get("DEVICE_NAME")
scope = "user-read-playback-state,app-remote-control,user-library-read,user-modify-playback-state"

class Spotify:
    def __init__(self) -> None:
        self.token = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope)
        self.sp = spotipy.Spotify(auth_manager=self.token)
        self.device_id = None

    def set_device(self, device_name=DEVICE_NAME):
        devices = self.sp.devices()
        devices_list = devices["devices"]
        for device in devices_list:
                if device["name"] == device_name:
                    self.device_id = device["id"]
                    print("Device id is {}".format(self.device_id))
                    break
        else:
            print("No Devices found")

    def play_song(self, song_uri):
        if self.device_id == None:
            self.set_device()
        self.sp.start_playback(device_id=self.device_id, uris=[song_uri])

    def set_volume(self, volume):
        '''volume 0-100'''
        if self.device_id == None:
            self.set_device()
        # if self.is_playing():
        #     self.sp.volume(volume, device_id=self.device_id)
        # else:
        #     print("Please play any song to change to volume, If the song start request is send, wait for few seconds and change the volume")
        time.sleep(0.2)
        self.sp.volume(volume, device_id=self.device_id)

    def is_playing(self):
        play_staus = self.sp.currently_playing()
        return play_staus["is_playing"]
    
    def resume(self):
        if self.device_id == None:
            self.set_device()
        self.sp.start_playback(device_id=self.device_id)

    def get_device_volume(self):
        if self.device_id == None:
            self.set_device()
        devices = self.sp.devices()
        devices_list = devices["devices"]
        for device in devices_list:
            if device["id"] == self.device_id:
                return device["volume_percent"]
        else:
            return None

# except spotipy.exceptions.SpotifyException:
# spo = Spotify()
# song_uri = "spotify:track:4qu63nuBpdn0qHUHuObEj1"
# spo.play_song(song_uri)
# t1 = time.time()
# spo.set_volume(35)
# t2 = time.time()
