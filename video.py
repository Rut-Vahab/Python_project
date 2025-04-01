import os
from pygame import mixer

try:
    mixer.init()
    file_path = os.path.join(os.path.dirname(__file__), 'alarms.mp3')
    play_music=lambda:(mixer.music.load(file_path),mixer.music.play())
except Exception as e:
    print(f"Error: השמע שהכנסת הוא לא מסוג mp3. Exception: {e}")