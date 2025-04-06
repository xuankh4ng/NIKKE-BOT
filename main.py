import pyautogui as pag
import blablalink, discord
import time
import tkinter as tk
from tkinter import messagebox

pag.PAUSE = 0.5

def show_notification():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Notification", "✅ The command has completed. You may continue.")
    root.destroy()

user_input = input("❓ Blablalink or Discord or All or Exit? (b/d/a/e) |> ")

while user_input:
    if user_input == "a":
        user_confirm = input("❗ Are you sure? (y/n) |> ")

        if user_confirm == "y":
            print("✅ Confirm All")
            # Blablalink
            time.sleep(1)
            blablalink.open()
            blablalink.signIn()
            blablalink.mission()
            blablalink.viewAllMissions()
            print("✅ Blablalink")

            # Discord
            time.sleep(1)
            discord.open()
            discord.nikkeServer()
            discord.signInEvent()
            discord.checkingCDKey()
            print("✅ Discord")
            print("--------------------")
            show_notification()
        elif user_confirm == "n":
            time.sleep(1)
            print("--------------------")

    elif user_input == "b":
        # Blablalink
        time.sleep(1)
        blablalink.open()
        blablalink.signIn()
        blablalink.mission()
        blablalink.viewAllMissions()
        print("✅ Blablalink")
        print("--------------------")
        show_notification()

    elif user_input == "d":
        # Discord
        time.sleep(1)
        discord.open()
        discord.nikkeServer()
        discord.signInEvent()
        discord.checkingCDKey()
        print("✅ Discord")
        print("--------------------")
        show_notification()

    elif user_input == "e":
        user_confirm = input("❗ Are you sure? (y/n) |> ")

        if user_confirm == "y":
            print("--------------------")
            for x in range(5, 0, -1):
                print(f"🟨 Closing app in {x}")
                time.sleep(1)
                if x == 1:
                    pag.hotkey("alt", "f4")

        elif user_confirm == "n":
            time.sleep(1)
            print("--------------------")

    else:
        print("❌ Wrong Input. Please try again!")
        time.sleep(1)
        print("--------------------")

    # Update user input
    user_input = input("❓ Blablalink or Discord or All or Exit? (b/d/a/e) |> ")