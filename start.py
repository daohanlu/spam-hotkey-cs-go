from glob import glob
from pynput.keyboard import Controller, Key, Listener
from time import sleep
import threading
import random
import upsidedown
import requests

k = Controller()
text_files = glob('texts/*.txt')
text_files.sort()
print("loaded text files:\n{}".format(text_files))
currentline = ''
evt = threading.Event()
alt_held = False
quit_next = False

def listen_keyboard_on_press(key):
    print(key)
    global alt_held
    # type message when 'y' is pressed on the keyboard
    try:
        if (key.char == 'y' or key.char == 'Y' or key.char == 'u' or key.char == 'U'):
            evt.set()
        elif (key.char == 'q' or key.char == 'Q') and alt_held:
            print('quitting')
            global quit_next
            quit_next = True
            evt.set()
    except AttributeError:
        if key == Key.alt_l:
            alt_held = True
        elif key == Key.alt_gr:
            k.release(Key.alt_gr)
            evt.set()

def listen_keyboard_on_release(key):
    global alt_held
    if key == Key.alt_l:
        alt_held= False

def get_dad_joke():
    header = {'Accept': 'application/json'}
    ret_json = requests.get(url = "https://icanhazdadjoke.com/", headers=header).json()
    joke = ret_json['joke']
    return joke

listener = Listener(
    on_press=listen_keyboard_on_press,
    on_release=listen_keyboard_on_release)
listener.start()

for text_file in text_files:
    dad_jokes = False
    text = open(text_file, 'r')
    lines = text.read().split('\n')
    if lines[0] == '#https://icanhazdadjoke.com/':
        while True:
            evt.wait()
            dad_jokes = True
            line = get_dad_joke()
            if quit_next:
                evt.clear()
                exit()
            sleep(0.03)
            k.type(line)
            
            k.press(Key.enter)
            k.release(Key.enter)
            evt.clear()
    lines = list(filter(lambda x: x.strip() != "", lines))
    text.close()
    total_lines = len(lines)
    
    for i, line in enumerate(lines):
        if line.strip() == '':
            continue
        else:
            # random upper case or scramble case event
            if random.random() < 0.333:
                if random.random() < 0.5:
                    line = line.upper()
                else:
                    newline = ""
                    for char in line:
                        if random.random() < 0.5:
                            newline += char.upper()
                        else:
                            newline += char.lower()
                    line = newline
            # random upside down event
            if random.random() < 0.05:
                line = upsidedown.transform(line)
            evt.wait()
            if quit_next:
                evt.clear()
                exit()
            sleep(0.03)
            line = line + " ({}/{})".format(i+1, total_lines)
            k.type(line)
            
            k.press(Key.enter)
            k.release(Key.enter)
            evt.clear()
            
