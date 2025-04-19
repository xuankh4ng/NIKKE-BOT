import pyautogui as pag
import time
from rich.console import Console
from rich.panel import Panel
console = Console()

pag.PAUSE = 0.5

# Image Path
sign_in_btn_img = "./img/blablalink/sign-in-btn.png"
close_sign_in_img = "./img/blablalink/close-sign-in.png"
nikkeart_img = "./img/blablalink/nikkeart.png"
filter_img = "./img/blablalink/filter.png"
recent_tag_img = "./img/blablalink/recent-tag.png"
unlike_img = "./img/blablalink/unlike.png"
comment_box_img = "./img/blablalink/comment-box.png"
sticker_tab_img = "./img/blablalink/sticker-tab.png"
sticker_img = "./img/blablalink/sticker.png"
send_btn_img = "./img/blablalink/send-btn.png"
close_post_img = "./img/blablalink/close-post.png"
outpost_img = "./img/blablalink/outpost.png"
quest_img = "./img/blablalink/quest.png"


def open(web):
    with console.status("[bold bright_cyan]Opening Blablalink..."):
        # Blablalink
        pag.press("win")
        if web == False:
            pag.write("Blablalink", interval = 0.1)
        else:
            pag.write("https://www.blablalink.com/", interval = 0.1)

        pag.press("enter")

        # Wait for fully loaded
        while True:
            try:
                pag.locateOnScreen(filter_img, confidence = 0.9)
                console.print("[bold bright_green]✅ Opened and loaded [bright_cyan]Blablalink")
                break
            except pag.ImageNotFoundException:
                time.sleep(1)

def signIn():
    wait_time = 0
    while True:
        with console.status("[bold bright_cyan]Signing In..."):
            try:
                sign_in_btn_location = pag.locateOnScreen(sign_in_btn_img, confidence = 0.9)
                pag.moveTo(sign_in_btn_location, duration = 0.2)
                pag.leftClick()
                
                while True:
                    try:
                        close_sign_in_location = pag.locateOnScreen(close_sign_in_img, confidence = 0.9)
                        pag.moveTo(close_sign_in_location, duration = 0.2)
                        console.print("[bold bright_green]✅ [bright_cyan]Sign In[/bright_cyan] completed")
                        pag.leftClick()
                        break
                    except pag.ImageNotFoundException:
                        time.sleep(1)
                break
            except pag.ImageNotFoundException:
                wait_time += 1
                time.sleep(1)
                if wait_time == 3:
                    console.print("[bold bright_red]❗ Already signed in")
                    break

def mission():
    with console.status("[bold bright_cyan]Finding NIKKEART with RECENT tag..."):
        # Go to NIKKEART
        nikkeart_location = pag.locateOnScreen(nikkeart_img, confidence = 0.9)
        pag.moveTo(nikkeart_location, duration = 0.2)
        pag.leftClick()

        # Filter to RECENT Tag
        filter_location = pag.locateOnScreen(filter_img, confidence = 0.9)
        pag.moveTo(filter_location, duration = 0.2)
        pag.leftClick()

        recent_tag_location = pag.locateOnScreen(recent_tag_img, confidence = 0.9)
        pag.moveTo(recent_tag_location, duration = 0.2)
        console.print("[bold bright_green]✅ Navigated to [bright_cyan]NIKKEART (RECENT tag)")
        pag.leftClick()

    # 5 Likes, 3 Browse posts, 1 Comment
    comment = 0
    like = 0
    while True:
        with console.status("[bold bright_cyan]Doing all Daily Missions..."):
            try:
                # Like
                unlike_location = pag.locateOnScreen(unlike_img, confidence = 0.9)
                pag.moveTo(unlike_location, duration = 0.2)
                like += 1
                pag.leftClick()

                # Browse
                if like <= 3:
                    pag.moveRel(-100, -40, duration = 0.2)
                    pag.leftClick()

                # Comment
                if comment != 1:
                    try:
                        # Open comment box
                        comment_box_location = pag.locateOnScreen(comment_box_img, confidence = 0.9)
                        pag.moveTo(comment_box_location, duration = 0.2)
                        pag.leftClick()

                        # Go to sticker tab
                        sticker_tab_location = pag.locateOnScreen(sticker_tab_img, confidence = 0.9)
                        pag.moveTo(sticker_tab_location, duration = 0.2)
                        pag.leftClick()

                        # Pick a sticker
                        sticker_location = pag.locateOnScreen(sticker_img, confidence = 0.9)
                        pag.moveTo(sticker_location, duration = 0.2)
                        pag.leftClick()

                        # Send comment
                        send_btn_location = pag.locateOnScreen(send_btn_img, confidence = 0.9)
                        pag.moveTo(send_btn_location, duration = 0.2)
                        console.print("[bold bright_green]✅ [bright_cyan]Sent 1 comment[/bright_cyan] completed")
                        pag.leftClick()
                        
                        # Update "comment"
                        comment = 1 
                    except pag.ImageNotFoundException:
                        time.sleep(2)
                        console.print("[bright_black] # Cannot find the 'comment box'")
                
                # Complete 5 like ==> Break the loop
                if like == 5:
                    console.print("[bold bright_green]✅ [bright_cyan]Liked 5 posts[/bright_cyan] completed")
                    console.print("[bold bright_green]✅ [bright_cyan]Browsed 3 posts[/bright_cyan] completed")
                    break

                # Exit a post
                close_post_location = pag.locateOnScreen(close_post_img, confidence = 0.9)
                pag.moveTo(close_post_location, duration = 0.2)
                pag.leftClick()

            except pag.ImageNotFoundException:
                pag.scroll(-150)

def viewAllMissions():
    with console.status("[bold bright_cyan]Go to PERKS QUEST..."):
        # Go to OUTPOST tab
        outpost_location = pag.locateOnScreen(outpost_img, confidence = 0.9)
        pag.moveTo(outpost_location, duration = 0.2)
        pag.leftClick()

        # Open PERKS QUEST
        while True:
            try:
                quest_location = pag.locateOnScreen(quest_img, confidence = 0.9)
                pag.moveTo(quest_location, duration = 0.2)
                console.print("[bold bright_green]✅ Navigated to [bright_cyan]PERKS QUEST")
                pag.leftClick()
                break
            except pag.ImageNotFoundException:
                time.sleep(1)

def tasks(web):
    console.print("[bold bright_white]--------------------")
    console.print(Panel.fit("[bold bright_cyan]Blablalink"))
    open(web)
    signIn()
    mission()
    viewAllMissions()
    console.print("[bold bright_white][Result][/bold bright_white]")
    console.print("[bold bright_green]✅ Completed [bright_cyan]Blablalink")
    console.print("[bold bright_white]--------------------")

if __name__ == "__main__":
    open(True)
    signIn()
    mission()
    viewAllMissions()