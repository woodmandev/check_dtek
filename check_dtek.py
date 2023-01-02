import datetime
from time import sleep
import telegram
from icmplib import ping
from importlib import resources

bot = telegram.Bot(TG_TOKEN)

lastOnTime = ""
lastOffTime = ""
currentStatus = "OFF"

def checkConncetion():
    global currentStatus
    global bot
    response = ping("your ip", 5, 0.2, privileged=True)
    print(f"Time: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}")
    if response.is_alive:
        if currentStatus == "OFF":
            lastOnTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            bot.sendMessage("@dtek_salutna_kyiv", "Електроживлення відновленно")
            print(f"+ {lastOnTime}")
            currentStatus = "ON"
        sleep(5)
    else:
        if currentStatus == "ON":
            lastOffTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            bot.sendMessage("@dtek_salutna_kyiv", "Електроживлення відключено")
            print(f"- {lastOffTime}")
            currentStatus = "OFF"
        sleep(5)
    return response.is_alive

if __name__ == '__main__':
    global TG_TOKEN
    with resources.open_text("resources", "secret.properties") as secret:
        lines = secret.readlines()
        for line in lines:
            line = line.strip()
            if line.split(":")[0] == "TG_TOKEN":
                TG_TOKEN = line.replace(f"{line.split(':')[0]}:", "")
    print(TG_TOKEN)

    while True:
        checkConncetion()

