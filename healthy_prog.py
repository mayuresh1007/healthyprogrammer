import datetime
import time
from pygame import mixer

x = datetime.datetime.now()
print(x.strftime("%a"" ""%b"" ""%Y"))
print(x.strftime("%I"" ""%M"" ""%p"))
initial = time.time()

i=1
while  i<=1:
    f = open("heathy.txt", "a")
    f.write("You drank water at:-")
    f.write(x.strftime("%a"" ""%b"" ""%Y"'\n'))
    f.write(x.strftime("%I"":""%M"" ""%p"'\n'))
    f.close()
    i = i + 1
    continue
while True:
    print("Water Drinking time. Enter 'drank' to stop the alarm.")
    mixer.init()
    mixer.music.load("D:\water.ogg")
    mixer.music.play()
    query = input(" ")

    if query == 'drank':
        mixer.music.stop()
        break
i=1
while  i<=1:
    f = open("heathy.txt", "a")
    f.write("You done eye exercise at:-")
    f.write(x.strftime("%a"" ""%b"" ""%Y"'\n'))
    f.write(x.strftime("%I"":""%M"" ""%p"'\n'))
    f.close()
    i = i + 1

while True:
    print("time to eyes exercise. Enter 'eye' to stop the alarm.")
    mixer.init()
    mixer.music.load("D:\eyes.ogg")
    mixer.music.play()
    query=input(" ")


    if query == 'eye':
        mixer.music.stop()
        break
i = 1
while i <= 1:
    f = open("heathy.txt", "a")
    f.write("You done physical exercise at:-")
    f.write(x.strftime("%a"" ""%b"" ""%Y"'\n'))
    f.write(x.strftime("%I"":""%M"" ""%p"'\n'))
    f.close()
    i = i + 1

while True:
    print("time to physical activity. Enter 'ex' to stop the alarm.")
    mixer.init()
    mixer.music.load("D:\exercise.ogg")
    mixer.music.play()
    query = input(" ")

    if query == 'ex':
        mixer.music.stop()
        break






