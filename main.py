import pyautogui as pag
import blablalink, discord
import time
import tkinter as tk
from tkinter import messagebox
from rich.panel import Panel
from rich.console import Console

pag.PAUSE = 0.5
console = Console()

def styleText(mess, fontStyle, color):
    return f"[{fontStyle} {color}]{mess}[/{fontStyle} {color}]"

def show_notification():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Notification", "The command has completed. You may continue in your Terminal!")
    root.destroy()

message = [
    # "? Blablalink or Discord or All? (b/d/a) |> " 
    styleText("❓ ", "bold", "bright_red") + 
    styleText("Blablalink ", "bold", "bright_cyan") + "or " + 
    styleText("Discord ", "bold", "bright_magenta") + "or " + 
    styleText("All ", "bold", "bright_green") + "? (" + 
    styleText("b", "bold", "bright_cyan") + "/" + 
    styleText("d", "bold", "bright_magenta") + "/" + 
    styleText("a", "bold", "bright_green") + ") |> ",
    # "! Are you sure? (y/n) |> "
    styleText("❗ Are you sure? (", "bold", "bright_red") + 
    styleText("y", "bold", "bright_green") +    
    styleText("/", "bold", "bright_red") + 
    styleText("n", "bold", "bright_yellow") +    
    styleText(") |> ", "bold", "bright_red"),
    # "? App or Web version? |> "
    styleText("❓ ", "bold", "bright_red") +
    styleText("App ", "bold", "bright_cyan") + 
    styleText("or ", "bold", "bright_red") +
    styleText("Web ", "bold", "bright_yellow") +    
    styleText("version? (", "bold", "bright_red") +
    styleText("a", "bold", "bright_cyan") + 
    styleText("/", "bold", "bright_red") +
    styleText("w", "bold", "bright_yellow") +    
    styleText(") |> ", "bold", "bright_red"),
]

def main():
    console.print(Panel.fit("[bold bright_yellow]NIKKE BOT"))
    console.print("[bold bright_white][Choices][/bold bright_white]")
    user_input = console.input(message[0])

    while user_input:
        # Both Blablalink and Discord
        if user_input == "a":
            # "! Are you sure? (y/n) |> "
            user_confirm = console.input(message[1])

            if user_confirm == "y":
                console.print("[bold bright_white]--------------------")
                console.print("[bold bright_white]🆗 Confirm [bright_green]All")

                # "? App or Web version? (a/w) |> "
                web_input = console.input(message[2])

                if web_input == "w":
                    console.print("[bold bright_white]🆗 Confirm [bright_yellow]Web version")
                    time.sleep(0.5)
                    blablalink.tasks(True)
                    discord.tasks(True)
                else:
                    console.print("[bold bright_white]🆗 Confirm [bright_cyan]App version")
                    time.sleep(0.5)
                    blablalink.tasks(False)
                    discord.tasks(False)

                show_notification()
            elif user_confirm == "n":
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")
            else:
                console.print(styleText("❌ Wrong Input. Please try again!", "bold", "bright_red"))
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")

        # Blablalink
        elif user_input == "b":
            # "! Are you sure? (y/n) |> "
            user_confirm = console.input(message[1])
            
            if user_confirm == "y":
                console.print("[bold bright_white]--------------------")
                console.print("[bold bright_white]🆗 Confirm [bright_cyan]Blablalink")

                # "? App or Web version? (a/w) |> "
                web_input = console.input(message[2])
                
                if web_input == "w":
                    console.print("[bold bright_white]🆗 Confirm [bright_yellow]Web version")
                    time.sleep(0.5)
                    blablalink.tasks(True)
                else:
                    console.print("[bold bright_white]🆗 Confirm [bright_cyan]App version")
                    time.sleep(0.5)
                    blablalink.tasks(False)

                show_notification()
            elif user_confirm == "n":
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")
            else:
                console.print(styleText("❌ Wrong Input. Please try again!", "bold", "bright_red"))
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")

        # Discord
        elif user_input == "d":
            # "! Are you sure? (y/n) |> "
            user_confirm = console.input(message[1])

            if user_confirm == "y":
                console.print("[bold bright_white]--------------------")
                console.print("[bold bright_white]🆗 Confirm [bright_magenta]Discord")

                # "? App or Web version? (a/w) |> "
                web_input = console.input(message[2])

                if web_input == "w":
                    console.print("[bold bright_white]🆗 Confirm [bright_yellow]Web version")
                    time.sleep(0.5)
                    discord.tasks(True)
                else:
                    console.print("[bold bright_white]🆗 Confirm [bright_cyan]App version")
                    time.sleep(0.5)
                    discord.tasks(False)
                
                show_notification()
            elif user_confirm == "n":
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")
            else:
                console.print(styleText("❌ Wrong Input. Please try again!", "bold", "bright_red"))
                time.sleep(0.5)
                console.print("[bold bright_white]--------------------")

        else:
            console.print(styleText("❌ Wrong Input. Please try again!", "bold", "bright_red"))
            time.sleep(0.5)
            console.print("[bold bright_white]--------------------")

        # Update user input
        console.print("[bold bright_white][Choices][/bold bright_white]")
        user_input = console.input(message[0])

if __name__ == "__main__":
    main()
