import keyboard
import psutil
import time
import random

def circle_strafe():
    try:
        keys = ['a', 'd']
        for _ in range(55):
            try:
                random_key = random.choice(keys)
                duration = random.uniform(0.05, 0.3)
                keyboard.press(random_key)
                time.sleep(duration)
                keyboard.release(random_key)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def escape_danger():
    try:    
        stem = "q"
        forward = "w"
        jump_pad = "z"
        ctrl = "ctrl"
        space = "space"
        run_duration = 0.3 
        jump_delay = 1
        stem_delay = 0.4
        keyboard.press(forward)
        time.sleep(run_duration)
        keyboard.press(stem)
        time.sleep(stem_delay)
        keyboard.release(stem)
        keyboard.press(forward)
        keyboard.press(jump_pad)
        time.sleep(jump_delay)
        keyboard.release(jump_pad)
        keyboard.press(ctrl)
        time.sleep(0.1)
        keyboard.release(ctrl)
        keyboard.press(forward)
        keyboard.press(space)
        keyboard.press(forward)
        time.sleep(3)
        keyboard.release(space)
        keyboard.release(forward)
    except:
        return    

def auto_run():
    stem = "q"
    forward = "w"
    ctrl = "ctrl"
    space = "space"
    slide_reset = 0.1
    stem_delay = 0.4
    loop_reset = 0.30
    jump_delay = 0.01
    keyboard.press(forward)
    keyboard.press(stem)
    time.sleep(stem_delay)
    keyboard.release(stem)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)
    keyboard.release(forward)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)
    keyboard.release(forward)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)

    time.sleep(loop_reset)
    keyboard.press(forward)
    keyboard.press(ctrl)
    time.sleep(jump_delay)
    keyboard.press(space)
    time.sleep(slide_reset)
    keyboard.release(ctrl)
    keyboard.release(forward)


def bypass_easy_anti_shit():
    for proc in psutil.process_iter():
        if proc.name() == "EACefSubProcess.exe":
            try:
                proc.kill()
                print("Terminated EasyAntiCheat process :p")
            except psutil.AccessDenied:
                print("Access denied to terminate EasyAntiCheat")               

def on_key_press(event):
    if event.name == '1':
        print("Strafing")
        circle_strafe()
    if event.name == '2': 
        print("Escapeing") 
        escape_danger()
    if event.name == '3':
        print("Auto Running")  
        auto_run()

def main():
    keyboard.on_press(on_key_press)
    bypass_easy_anti_shit()
    print("Press 1 to circle strafe, Press 2 to escape danger, press 3 to auto run (with stem)")
    keyboard.wait('esc') 

if __name__ == "__main__":
    main()
