import datetime
import sched
import time
from play_music import set_alarm



# Define the alarm event
def play_alarm():
    set_alarm()

if __name__ == "__main__":
    # Set the alarm time
    alarm_time = datetime.datetime(2023, 3, 26, 6, 56, 0)


    # Create a scheduler object
    scheduler = sched.scheduler(time.time, time.sleep)

    # Schedule the alarm event
    scheduler.enterabs(alarm_time.timestamp(), 1, play_alarm)

    # Start the scheduler
    scheduler.run()
