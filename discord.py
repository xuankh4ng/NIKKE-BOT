import pyautogui as pag
import time

# Image Path
inbox_icon_img = "./img/discord/inbox-icon.png"
nikke_server_img = "./img/discord/nikke-server.png"
main_channel_img = "./img/discord/main-channel.png"
sign_in_event_img = "./img/discord/sign-in-event.png"
sign_in_btn_img = "./img/discord/sign-in-btn.png"
sign_in_log_img = "./img/discord/sign-in-log.png"
cd_key_img = "./img/discord/cd-key.png"

# Each pyautogui function will take 0.5s delay to excuse (for stability)
pag.PAUSE = 0.5

def open():
    # Open through Windows Search
    pag.press("win")
    pag.write("Discord", interval = 0.1)
    pag.press("enter")

    # Wait for fully loaded
    while True:
        # If find 'inbox-icon' === app fully loaded -> Break the loop
        try:
            pag.locateOnScreen(inbox_icon_img, confidence = 0.9)
            break
        # If not, sleep the script for 1s then repeat the loop
        except pag.ImageNotFoundException:
            time.sleep(0.5)

# In Discord, we can navigate through server by keyboard shortcut: 'Ctrl' + 'Alt' + 'Down_Arrow || Up_Arrow'
def nikkeServer():
    # Hold both 'Ctrl' and 'Alt' keys
    pag.keyDown("ctrl")
    pag.keyDown("alt")

    # Finding NIKKE SERVER by the name
    while True:
        # If find it, break the loop
        try:
            pag.locateOnScreen(nikke_server_img, confidence = 0.9)
            break
        # If not, keep press 'Down_Arrow' key to find
        except pag.ImageNotFoundException:
            pag.press("down")
            time.sleep(1) # Delay for the server load
            
    # Release both 'Ctrl' and 'Alt' keys
    pag.keyUp("ctrl")
    pag.keyUp("alt")


# Navigate channel by using keyboard shortcut: 'Alt' + 'Down_Arrow'
def signInEvent():
    # Hold 'Alt' key 
    pag.keyDown("alt")

    # Finding 'sign-in-event' channel by looking for 'sign-in-event' image
    key = "down"
    finding_main_channel = False
    steps = 0
    while True:
        # If find it, move inside 'sign-in-event' channel
        try:
            sign_in_event_location = pag.locateOnScreen(sign_in_event_img, confidence = 0.9)
            pag.moveTo(sign_in_event_location, duration = 0.2)
            pag.moveRel(0, 100, duration = 0.2)
            break
        # If not, keep pressing 'Down_Arrow' key 10 times
        except pag.ImageNotFoundException:
            pag.press(key)
            time.sleep(0.5) # Delay for the channel load
            
            # Fiding 'main' channel (to know that we pass by 'sign-in-event' channel)
            if finding_main_channel == False:
                while True:
                    # If find it, find upward
                    try:
                        pag.locateOnScreen(main_channel_img, confidence = 0.9)
                        key = "up"
                        finding_main_channel = True
                        break
                    # If not, keep find for 10 more times then find upward
                    except pag.ImageNotFoundException:
                        steps += 1 # Update each step to press 'Down_Arrow' key
                        if steps == 10:
                            key = "up"
                            finding_main_channel = True
                        break

    # Release 'Alt' key 
    pag.keyUp("alt")

    # Sign In
    while True:
        try:
            sign_in_btn_location = pag.locateOnScreen(sign_in_btn_img, confidence = 0.9)
            pag.moveTo(sign_in_btn_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(-150)

    # Wait for the message appear after click the 'Sign In' Button
    while True:
        try:
            pag.locateOnScreen(sign_in_log_img, confidence = 0.9)
            break
        # If not, delay for 1s
        except pag.ImageNotFoundException:
            time.sleep(1)

def checkingCDKey():
    # Hold 'Alt' key 
    pag.keyDown("alt")

    # Finding 'cd-key' channel
    while True:
        try:
            pag.locateOnScreen(cd_key_img, confidence = 0.9)
            break
        except pag.ImageNotFoundException:
            pag.press("down")
            time.sleep(0.5)

    # Release 'Alt' key 
    pag.keyUp("alt")