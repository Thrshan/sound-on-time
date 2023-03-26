import time
import multiprocessing
from smartlight_controller import Tuya_controller
from spotify_manager import Spotify


def sweep_light():
    light = Tuya_controller()
    light.sweep_brightness()


def play_song_in_loop():
    max_volume = 70
    spo = Spotify()
    # song_uri = "spotify:track:4qu63nuBpdn0qHUHuObEj1"
    song_uri = "spotify:track:18e3XXYCv4Tx8uUl1mP3CN"
    silence_uri = "spotify:track:5WQyF7t0tNomzABIYzxxSD"
    spo.play_song(silence_uri)
    spo.set_volume(1)
    spo.play_song(song_uri)
    for vol in range(10, max_volume+1, 2):
        spo.set_volume(vol)
        if not spo.is_playing():
            spo.resume() 
        time.sleep(1)
    start_time = time.time()
    current_time = 0
    while True:
        if spo.get_device_volume() < max_volume:
            spo.set_volume(max_volume)
        if not spo.is_playing():
            spo.resume() 
        time.sleep(4)
        current_time = time.time()
        if (current_time - start_time) > 3*60:
            break

# if __name__ == "__main__":
process1 = multiprocessing.Process(target=sweep_light)
process2 = multiprocessing.Process(target=play_song_in_loop)
def set_alarm():
    process1.start()
    process2.start()
