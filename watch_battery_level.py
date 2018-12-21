import os
import subprocess
import pyglet

command = "upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep 'percentage'"

while True:
    status = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
    battery_percent = status.communicate()[0].decode("utf-8").replace("\n", "").split(" ")[-1:][0].split("%")[0]
    while int(battery_percent) == 7:
        print(battery_percent)
        sound = pyglet.media.load('robot1.wav')
        sound.play()
        pyglet.app.run()

