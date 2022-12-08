# Mark Swift
# Pipeline Research
import time

print()
print(' *ROBOT PIPELINE MOVEMENT* ')
print()

# Receive user input for time of robot travel; Convert strings to integers for later use
cycles = int(input('Number of cycles:  '))
seconds_moving = int(input('Seconds of robot moving:  '))
pinging_between = int(input('Pinging period: '))
print()

# 5, 4, 3, 2, 1 BEGIN !
spaces = ' ' * 30
print('\r The robot will start to move in: 5  ', end='')
for n in reversed(range(0, 5)):
    time.sleep(1)
    if n > 0:
        print('\rGet ready, the timer will start in: {}  '.format(n), end='')
    else:
        print('\rBEGIN !' + spaces, end='')

# With number of cycles decided by user, from 0 to "x" go through the range
for cycle in range(cycles):
    print('\rMoving: 0' + spaces, end='')
    for n in range(seconds_moving):
        time.sleep(1)
        print('\rMoving: {}  '.format(n + 1), end='')

# Check if it is the last cycle first, then ping
    if cycle == cycles - 1:
        print('\rMOVEMENT COMPLETE !' + spaces, end='')
        break
    else:
        print('\rPing: 0' + spaces, end='')
        for n in range(pinging_between):
            time.sleep(1)
            print('\rPing: {}  '.format(n + 1), end='')