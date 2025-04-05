import pyautogui as pag
import blablalink, discord

pag.PAUSE = 0.5

# Blablalink
blablalink.open()
blablalink.signIn()
blablalink.mission()
blablalink.viewAllMissions()
print("✅ Blablalink")

# Discord
discord.open()
discord.nikkeServer()
discord.signInEvent()
discord.checkingCDKey()
print("✅ Discord")