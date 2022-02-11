import time

#the sound module
from pygame import mixer

#normal timer
def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1
    print('Blast off!')


t = int(input("In how many seconds do you want the timer to start?"))
countdown(int(t))

#pomodoro timer
def pomodoro():
    print("Pomodoro starts now!")
    #here 4 signifies the average pomodoro cycles = 4 ==25 mins of workktime 4 times ++ 5 mins of breaks 4 times
    for i in range(4):
        t = 1 * 60 #(n * seconds)
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -=1
        print("Break time!")
        mixer.init()
        mixer.music.load('C:/Users/AAXIM/Desktop/Python_FB/Pomodoro/Anime Sound.mp3')
        mixer.music.play()
        time.sleep(4)
        mixer.music.stop()

        #5 minute break starts here
        t = 5 * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -=1
            print("Work time!")
            mixer.init()
            mixer.music.load('C:/Users/AAXIM/Desktop/Python_FB/Pomodoro/Anime Sound.mp3')
            mixer.music.play()
            time.sleep(4)
            mixer.music.stop()
            break;
pomodoro()