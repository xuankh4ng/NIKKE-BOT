import pyautogui as pag
import time
import blablalink, discord

pag.PAUSE = 0.5

# User Input
browser = input("❓ Which web browser do you use? |> ")
print(f"✅ Confirm {browser}")
time.sleep(1)

# Open Web
pag.press("win")
pag.write(f"{browser}")
pag.press("enter")
print("✅ Open Edge")

# Blablalink
blablalink.open()
blablalink.signIn()
blablalink.mission()
print("✅ Blablalink")
# Open new tab
pag.hotkey("ctrl", "t")

# Discord
discord.open()
discord.nikkeServer()
discord.signInEvent()
discord.checkingCDKey()
print("✅ Discord")