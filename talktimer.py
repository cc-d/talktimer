import sys
import time
import threading
from datetime import timedelta
from pynput import keyboard

# Set the initial time
if len(sys.argv) > 1:
    try:
        initial_time = int(sys.argv[1])
    except ValueError:
        print("Invalid argument. Using default value of 5 minutes.")
        initial_time = 5
else:
    initial_time = 5

timer = initial_time * 60
talking = None
start_time = time.time()

print("Press Enter to start")


def on_press(key):
    global talking, start_time

    if key == keyboard.Key.enter:
        if talking is None:
            talking = "Cary"
            print("\nCary starts talking")
            start_time = time.time()
        else:
            if talking == "Cary":
                talking = "Mom"
                start_time = time.time()
            else:
                talking = "Cary"
                start_time = time.time()
        time.sleep(0.2)


def display_timer():
    global talking, timer, start_time
    while True:
        if talking:
            elapsed_time = time.time() - start_time
            if talking == "Cary":
                timer -= elapsed_time
                if timer <= 0:
                    print("\nTime's up!")
                    break
            else:
                timer += elapsed_time

            remaining_time = timedelta(seconds=round(timer))
            print(f"{talking} is talking | Time remaining: {remaining_time}", end="\r")
            start_time = time.time()
        time.sleep(1)


listener = keyboard.Listener(on_press=on_press)
listener.start()

display_timer_thread = threading.Thread(target=display_timer)
display_timer_thread.start()

