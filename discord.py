import pyautogui as pag
import time
from rich.console import Console
from rich.panel import Panel
console = Console()

# Đường dẫn hình ảnh
inboxIcon_img = "./img/discord/inbox-icon.png"
nikkeServer_img = "./img/discord/nikke-server.png"
startPoint_img = "./img/discord/start-point.png"
endPoint_img = "./img/discord/end-point.png"
signInChannel_img = "./img/discord/sign-in-channel.png"
signInButton_img = "./img/discord/sign-in-btn.png"
signInLog_img = "./img/discord/sign-in-log.png"
cdKeyChannel_img = "./img/discord/cd-key.png"

# Delay 0.5s cho mỗi lần làm xong 1 'pyautogui'  
pag.PAUSE = 0.5

# Mở Discord
def open(website):
    with console.status("[bold bright_magenta]Opening Discord..."):
        # Mở thông ô tìm kiếm trên Windows
        pag.press("win")

        # Web hoặc App?
        if website == False:
            pag.write("Discord", interval = 0.1)
        else:
            pag.write("https://discord.com/channels/@me", interval = 0.1)
            
        # Nhấn 'Enter'
        pag.press("enter")

        # Đợi cho Discord load thông qua icon
        while True:
            # Nếu tìm thấy ==> Thoát khỏi vòng lặp
            try:
                pag.locateOnScreen(inboxIcon_img, confidence = 0.9)
                console.print("[bold bright_green]✅ Opened and loaded [bright_magenta]Discord")
                break
            # Nếu không, tạm ngừng cho đến khi tìm thấy
            except pag.ImageNotFoundException:
                time.sleep(0.5)

# Di chuyển qua các Server
def navigateToServer(name, img_path):
    # Đè 2 phím 'Ctrl' và 'Alt'
    pag.keyDown("ctrl")
    pag.keyDown("alt")

    # Tìm bằng tên Server thông qua hình ảnh
    while True:
        with console.status(f"[bold bright_magenta]Finding {name} Server..."):
            # Nếu tìm được ==> Thoát khỏi vòng lặp
            try:
                pag.locateOnScreen(img_path, confidence = 0.9)
                console.print(f"[bold bright_green]✅ Entered [bright_magenta]{name} Server")
                break
            # Nếu không, cứ tiếp tục nhấn phím 'Mũi tên Xuống'
            except pag.ImageNotFoundException:
                pag.press("down")
                # Delay cho server load
                time.sleep(1)
            
    # Thả 2 phím 'Ctrl' và 'Alt'
    pag.keyUp("ctrl")
    pag.keyUp("alt")

# Di chuyển qua các Channel
def navigateToChannel(name, target_img_path, startPoint_img_path, endPoint_img_path):
    # Đè phím 'Alt' 
    pag.keyDown("alt")

    # Các biến với giá trị mặc định
    key = "down"
    downCounter = 0
    findStartPoint = False
    findEndPoint = False

    # Tìm 'target' channel thông qua tên của channel đó
    while True:
        with console.status(f"[bold bright_magenta]Finding {name} channel..."):
            # Nếu tìm thấy ==> Thoát khỏi vòng lặp
            try:
                pag.locateOnScreen(target_img_path, confidence=0.9)
                console.print(f"[bold bright_green]✅ Navigated to [bright_magenta]{name} channel")
                break
            # Nếu không thì
            except pag.ImageNotFoundException:
                # Tìm theo hướng dựa vào 'key'
                pag.press(key)
                time.sleep(0.5)

                # Trường hợp nằm dưới 'target'
                if findEndPoint == False:
                    # Nếu tìm được
                    try:
                        pag.locateOnScreen(endPoint_img_path, confidence=0.9)
                        console.print(f"[bright_black]❗ The {name} channel is located at the top")

                        # Cập nhật là đã tìm thấy 'endPoint' và đổi hướng tìm
                        findEndPoint = True
                        key = "up"

                    # Nếu không thì
                    except pag.ImageNotFoundException:
                        # Cập nhật số lần tìm 'downCounter'
                        downCounter += 1
                        # Cập nhật hướng tìm (để đảm bảo luôn là hướng xuống)
                        key = "down"

                        # Nếu tìm tới lần thứ 5 mà không thấy 'endPoint'
                        if downCounter == 5:
                            console.print(f"[bright_black]❗ The {name} channel is located at the top")
                            # Cập nhật là đã tìm thấy 'endPoint' (mặc dù không phải) và đổi hướng tìm
                            findEndPoint = True

                # Trường hợp nằm trên 'target' (chỉ khi đã tìm thấy 'endPoint')
                if findStartPoint == False and findEndPoint == True:
                    # Nếu tìm được
                    try:
                        pag.locateOnScreen(startPoint_img_path, confidence=0.9)
                        console.print(f"[bright_black]❗ The {name} channel is located at the bottom")

                        # Cập nhật là đã tìm thấy 'startPoint' và đổi hướng tìm
                        findStartPoint = True
                        key = "down"

                    # Nếu không thì
                    except pag.ImageNotFoundException:
                        # Cập nhật hướng tìm (để đảm bảo luôn là hướng lên)
                        key = "up"

    # Thả phím 'Alt' 
    pag.keyUp("alt")

# Đăng nhập sự kiện
def signInEvent():
    findChannelName = False

    # Tìm nút 'Sign In'
    while True:
        with console.status("[bold bright_magenta]Siging In..."):
            # Nếu tìm thấy ==> Nhấn nút và Thoát khỏi vòng lặp
            try:
                signInButton_location = pag.locateOnScreen(signInButton_img, confidence=0.9)
                pag.moveTo(signInButton_location, duration=0.2)
                pag.leftClick()
                break

            # Nếu không thì
            except pag.ImageNotFoundException:
                # Đưa con trỏ chuột vào trong vùng có thể cuộn xuống được
                signInChannel_location = pag.locateOnScreen(signInChannel_img, confidence=0.9)
                if findChannelName == False:
                    pag.moveTo(signInChannel_location, duration=0.2)
                    pag.moveRel(0, 50, duration=0.2)
                    findChannelName = True

                # Cuộn xuống cho đến khi tìm thấy
                pag.scroll(-150)  

    # Đợi kết quả đăng nhập xuất hiện
    while True:
        with console.status("[bold bright_magenta]Confirming..."):
            # Nếu tìm thấy ==> Thoát khỏi vòng lặp
            try:
                pag.locateOnScreen(signInLog_img, confidence=0.9)
                console.print("[bold bright_green]✅ [bright_magenta]Sign In[/bright_magenta] completed")
                break

            # Nếu không thì
            except pag.ImageNotFoundException:
                # Cuộn xuống cho đến khi tìm thấy
                pag.scroll(-150)  
            

def checkingCDKeys():
    # Đè phím 'Alt' 
    pag.keyDown("alt")

    # Tìm 'cd-keys' channel
    while True:
        with console.status("[bold bright_magenta]Finding cd-keys channel..."):
            # Nếu tìm thấy ==> Thoát khỏi vòng lặp
            try:
                pag.locateOnScreen(cdKeyChannel_img, confidence = 0.9)
                console.print("[bold bright_green]✅ Navigated to [bright_magenta]cd-keys channel")
                break

            # Nếu không, cứ tiếp tục nhấn phím 'Mũi tên Xuống'
            except pag.ImageNotFoundException:
                pag.press("down")
                # Delay cho channel load
                time.sleep(0.5)

    # Thả phím 'Alt' 
    pag.keyUp("alt")

def tasks(web):
    console.print("[bold bright_white]--------------------")
    console.print(Panel.fit("[bold bright_magenta]Discord"))
    open(web)
    navigateToServer("NIKKE", nikkeServer_img)
    navigateToChannel("sign-in-event", signInChannel_img, startPoint_img, endPoint_img)
    signInEvent()
    checkingCDKeys()
    console.print("[bold bright_white][Result][/bold bright_white]")
    console.print("[bold bright_green]✅ Completed [bright_magenta]Discord")
    console.print("[bold bright_white]--------------------")

if __name__ == "__main__":
    open(True)
    navigateToServer("NIKKE", nikkeServer_img)
    navigateToChannel("sign-in-event", signInChannel_img, startPoint_img, endPoint_img)
    signInEvent()
    checkingCDKeys()