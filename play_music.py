import time

from spotify_manager import Spotify


def play_song_in_loop():
    spo = Spotify()
    song_uri = "spotify:track:4qu63nuBpdn0qHUHuObEj1"
    spo.play_song(song_uri)
    # spo.set_volume(50)
    start_time = time.time()
    current_time = 0
    while True:
        if spo.get_device_volume() < 100:
            spo.set_volume(100)
        if not spo.is_playing():
            spo.resume() 
        time.sleep(5)
        current_time = time.time()
        if (current_time - start_time) > 1*60:
            break
