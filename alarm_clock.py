import datetime
import os
import random
import webbrowser

if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt"...')
    favourite_song = input('Wake up with your favorite song. Please add the YouTube link here: ')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write(favourite_song)

am_pm = str(input('Do you prefer AM or PM? ')).lower()
alarm_hour = int(input('What hour do you want your alarm to be set at? '))
alarm_minute = int(input('What minute do you want your alarm to be set at? '))

if am_pm != 'am' and am_pm != 'pm':
    print('Your time period is invalid. Try again!')

if not 12 > alarm_hour >= 0 and 60 > alarm_minute >= 0:
    print('Your time is invalid. Try again!')

if alarm_minute < 10:
    alarm_minute = '0' + str(alarm_minute)

print(f'Alarm is successful for {alarm_hour}:{alarm_minute} {am_pm.upper()}!')

if am_pm == 'pm':
    alarm_hour += 12

while True:
    current_hour = datetime.datetime.now().hour
    current_minute = datetime.datetime.now().minute

    if alarm_hour == current_hour and alarm_minute == current_minute:
        with open("youtube_alarm_videos.txt", "r") as alarm_file:
            videos = alarm_file.readlines()

        webbrowser.open(random.choice(videos))
        break
