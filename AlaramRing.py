from pygame import mixer
import time


def sound():
    mixer.init()
    mixer.music.load("D:/Alaram/alaram.mp3")
    mixer.music.play(3)


hour = int(input("==>Enter The Hour : "))
min = int(input("==>Enter The Minute : "))
sec = int(input("==>Enter The Second : "))
mer = input("Enter Am/Pm : ")
print("Alaram Set To  ===> ", hour, ":", min, ":", sec, " ", mer)

if (mer == 'pm'):
    hour = int(hour + 12)

res = False

while True:
    if time.localtime().tm_sec == sec and time.localtime().tm_hour == hour and time.localtime().tm_min == min:
        print("Wake Up ")
        res = True
        break

while res:
    sound()

    op = input("Do U Wana Snooze  Or Stop (sn/st): ")
    if op == 'sn':
        time.sleep(5)
    elif op == 'st':
        print("*************** Alaram Stopped ***************")
        exit()
    else:
        sound()
