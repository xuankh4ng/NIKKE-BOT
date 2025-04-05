import pyautogui as pag
import time

# Image Path
micro_icon_img = "./img/discord/micro-icon.png"
explore_img = "./img/discord/explore.png"
nikke_server_img = "./img/discord/nikke-server.png"
sign_in_event_img = "./img/discord/sign-in-event.png"
sign_in_event_active_img = "./img/discord/sign-in-event-active.png"
voice_channel_img = "./img/discord/voice-channel.png"
sign_in_btn_img = "./img/discord/sign-in-btn.png"
sign_in_log_img = "./img/discord/sign-in-log.png"
cd_key_img = "./img/discord/cd-key.png"

pag.PAUSE = 0.5

def open():
    # Discord
    pag.press("win")
    pag.write("Discord", interval = 0.1)
    pag.press("enter")

    # Wait for fully loaded
    while True:
        try:
            micro_icon_location = pag.locateOnScreen(micro_icon_img, confidence = 0.9)
            pag.moveTo(micro_icon_location, duration = 0.2)
            pag.moveRel(-160, -400, duration = 0.2)
            break
        except pag.ImageNotFoundException:
            time.sleep(1)

def nikkeServer():
    # Finding NIKKE Server
    scroll_value = -150
    explore = 0
    while True:
        try:
            nikke_server_location = pag.locateOnScreen(nikke_server_img, confidence = 0.9)
            pag.moveTo(nikke_server_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(scroll_value)
            if explore == 0:
                try:
                    explore_location = pag.locateOnScreen(explore_img, confidence = 0.9)
                    scroll_value *= -1
                    explore = 1
                except pag.ImageNotFoundException:
                    pass

def signInEvent():
    # Move to channel list
    micro_icon_location = pag.locateOnScreen(micro_icon_img, confidence = 0.9)
    pag.moveTo(micro_icon_location, duration = 0.2)
    pag.moveRel(0, -150, duration = 0.2)

    # Fiding 'sign-in-event' channel
    scroll = -150
    visited = 0

    while True:
        try:
            sign_in_event_location = pag.locateOnScreen(sign_in_event_img, confidence = 0.9)
            pag.moveTo(sign_in_event_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(scroll)

            if visited == 0:
                try:
                    pag.locateOnScreen(voice_channel_img, confidence = 0.9)    
                    scroll *= -1
                    visited = 1
                except pag.ImageNotFoundException:
                    pass

    # Sign In
    while True:
        try:
            sign_in_btn_location = pag.locateOnScreen(sign_in_btn_img, confidence = 0.9)
            pag.moveTo(sign_in_btn_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            time.sleep(1)

    # Wait for fully loaded
    while True:
        try:
            pag.locateOnScreen(sign_in_log_img, confidence = 0.9)
            break
        except pag.ImageNotFoundException:
            time.sleep(1)

def checkingCDKey():
    # Move to channel list
    sign_in_event_active_location = pag.locateOnScreen(sign_in_event_active_img, confidence = 0.9)
    pag.moveTo(sign_in_event_active_location, duration = 0.2)

    # Finding CD-Key Channel
    while True:
        try:
            cd_key_location = pag.locateOnScreen(cd_key_img, confidence = 0.9)
            pag.moveTo(cd_key_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(-150)