from pygame import mixer
import time


def sound():
    mixer.init()
    mixer.music.load("D:/Alaram/alaram.mp3")
    mixer.music.play()


def alarm():
    hour = int(input("Enter the hour : "))
    min = int(input("Enter the Min : "))
    sec = int(input("Enter the Sec : "))

    n = 5

    print('alaram Set For : ', str(hour) + ":" + str(min) + ":" + str(sec))
    while True:
        if time.localtime().tm_hour == hour and time.localtime().tm_min == min and time.localtime().tm_sec == sec:
            print(" Wake Up ")
            break
    sound ()
    while n > 0:
        mixer.music.play()
        time.sleep(2)


    opt = print("Snooze Alaram : ")
    if opt == 'Yes':
        n = 3
        time.sleep(1000)

        while n>0:
            mixer.music.play()
            time.sleep(2)
    else:
            exit()
alarm()