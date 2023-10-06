# Exercise

import time

localtime = int(time.strftime("%H"))
localAMPM = time.strftime(": %M %p" )

if (6<=localtime<12):
    print("Good Morning, Sir.")
elif (12<=localtime<17):
    print("Good AfterNoon, Sir.")
elif (17<=localtime<20):
    print("Good Evening, Sir.")
else:
    print("Good Night, Sir.")

print("It's" ,localtime,localAMPM)