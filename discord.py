import pyautogui as pag
import time

# Image Path
discord_icon_img = "./img/discord/discord-icon.png"
nikke_server_img = "./img/discord/nikke-server.png"
sign_in_event_img = "./img/discord/sign-in-event.png"
voice_channel_img = "./img/discord/voice-channel.png"
sign_in_btn_img = "./img/discord/sign-in-btn.png"
sign_in_log_img = "./img/discord/sign-in-log.png"
cd_key_img = "./img/discord/cd-key.png"

pag.PAUSE = 0.5

def open():
    # Discord
    pag.hotkey("ctrl", "l")
    pag.write("https://discord.com/channels/@me")
    pag.press("enter")

    # Wait for fully loaded
    while True:
        try:
            discord_icon_location = pag.locateOnScreen(discord_icon_img, confidence = 0.9)
            pag.moveTo(discord_icon_location, duration = 0.2)
            break
        except pag.ImageNotFoundException:
            time.sleep(1)

def nikkeServer():
    # Finding NIKKE Server
    while True:
        try:
            nikke_server_location = pag.locateOnScreen(nikke_server_img, confidence = 0.9)
            pag.moveTo(nikke_server_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(-150)

def signInEvent():
    # Move to channel list
    pag.moveRel(150, 0, duration = 0.2)

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
    pag.moveRel(-450, 0, duration = 0.2)

    # Finding CD-Key Channel
    while True:
        try:
            cd_key_location = pag.locateOnScreen(cd_key_img, confidence = 0.9)
            pag.moveTo(cd_key_location, duration = 0.2)
            pag.leftClick()
            break
        except pag.ImageNotFoundException:
            pag.scroll(-150)