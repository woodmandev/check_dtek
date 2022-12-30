import datetime
from time import sleep
import telegram
from icmplib import ping

TG_TOKEN = "5857992954:AAEXOiADgCI5LkBd5CpnWrasDjhNkH75j3I"
bot = telegram.Bot(TG_TOKEN)

lastOnTime = ""
lastOffTime = ""
currentStatus = "OFF"

def checkConncetion():
    global currentStatus
    global bot
    # response = ping("91.227.183.197", 5, 0.2, privileged=True)
    # response = ping("195.189.227.49", 5, 0.2, privileged=True)
    # response = ping("10.8.0.3", 5, 0.2, privileged=True)
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
    while True:
        checkConncetion()

