import datetime
import sched
import time
from play_music import play_song_in_loop

# Set the alarm time
alarm_time = datetime.datetime(2023, 3, 22, 1, 32, 0)


# Create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

# Define the alarm event
def play_alarm():
    play_song_in_loop()

# Schedule the alarm event
scheduler.enterabs(alarm_time.timestamp(), 1, play_alarm)

# Start the scheduler
scheduler.run()
