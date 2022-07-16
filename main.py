import schedule
import subprocess
import time

def job():
    subprocess.call(['vlc "music/8 Letters.mp3"'], shell=True)

schedule.every().day.at('17:30').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)