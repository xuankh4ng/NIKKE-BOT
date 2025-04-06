import pyautogui as pag
import blablalink, discord
import time

pag.PAUSE = 0.5

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
            print("")

            # Discord
            time.sleep(1)
            discord.open()
            discord.nikkeServer()
            discord.signInEvent()
            discord.checkingCDKey()
            print("✅ Discord")

            pag.keyDown("alt")
            pag.press("tab")
            pag.press("tab")
            pag.keyUp("alt")

            time.sleep(1)
            print("")
        elif user_confirm == "n":
            time.sleep(1)
            print("")

    elif user_input == "b":
        # Blablalink
        time.sleep(1)
        blablalink.open()
        blablalink.signIn()
        blablalink.mission()
        blablalink.viewAllMissions()
        print("✅ Blablalink")

        pag.keyDown("alt")
        pag.press("tab")
        pag.keyUp("alt")

        time.sleep(1)
        print("")

    elif user_input == "d":
        # Discord
        time.sleep(1)
        discord.open()
        discord.nikkeServer()
        discord.signInEvent()
        discord.checkingCDKey()
        print("✅ Discord")

        pag.keyDown("alt")
        pag.press("tab")
        pag.keyUp("alt")

        time.sleep(1)
        print("")

    elif user_input == "e":
        user_confirm = input("❗ Are you sure? (y/n) |> ")

        if user_confirm == "y":
            for x in range(5, 0, -1):
                print(f"🟨 Closing app in {x}")
                time.sleep(1)
                if x == 1:
                    pag.hotkey("alt", "f4")

        elif user_confirm == "n":
            time.sleep(1)
            print("")

    else:
        print("❌ Wrong Input. Please try again!")
        time.sleep(1)
        print("")

    # Update user input
    user_input = input("❓ Blablalink or Discord or All or Exit? (b/d/a/e) |> ")