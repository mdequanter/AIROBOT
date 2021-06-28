from pynput import keyboard
import urllib3
import time

http = urllib3.PoolManager()

robot = '192.168.0.18'
leftSpeed = 90
rightSpeed= 90

webUrl = http.request('GET', 'http://' + robot + '/?left=' + str(leftSpeed) + '&right=' + str(rightSpeed) + '')

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
def on_release(key):
    global leftSpeed
    global rightSpeed
    global robot

    try:
        if (key.char == 'z'):
            leftSpeed = leftSpeed - 5
        if (key.char == 's'):
            leftSpeed = leftSpeed + 5
        if (key.char == 'a'):
            rightSpeed = rightSpeed + 5
        if (key.char == 'q'):
            rightSpeed = rightSpeed -5
        print("Speed: L" + str(leftSpeed) + " R" + str(rightSpeed))
        webUrl = http.request('GET', 'http://' + robot + '/?left=' + str(leftSpeed) + '&right=' + str(rightSpeed) + '')
    except AttributeError:

        if (key == keyboard.Key.up):
            rightSpeed = rightSpeed + 5
            leftSpeed = leftSpeed - 5
        if ( key == keyboard.Key.down):
            rightSpeed = rightSpeed - 5
            leftSpeed = leftSpeed   + 5
        if (key == keyboard.Key.left):
            rightSpeed = rightSpeed - 5
            leftSpeed = leftSpeed -  5
        if (key == keyboard.Key.right):
            leftSpeed = leftSpeed + 5
            rightSpeed = rightSpeed + 5
        if (key == keyboard.Key.space):
            rightSpeed = 90
            leftSpeed= 90

        print ("Speed: L" + str(leftSpeed) + " R" + str(rightSpeed))
        webUrl = http.request('GET', 'http://' + robot + '/?left=' + str(leftSpeed) + '&right=' + str(rightSpeed) + '')


        if key == keyboard.Key.esc:
            # Stop listener
            return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()