import datetime
from time import sleep
from icmplib import ping
import telegram

TG_TOKEN = "5857992954:AAEXOiADgCI5LkBd5CpnWrasDjhNkH75j3I"
bot = telegram.Bot(TG_TOKEN)

lastOnTime = ""
lastOffTime = ""
currentStatus = "ON"

def checkConncetion():
    global currentStatus
    global bot
    # response = ping("91.227.183.197", 5, 0.2, privileged=True)
    # response = ping("195.189.227.49", 5, 0.2, privileged=True)
    response = ping("10.8.3", 5, 0.2, privileged=True)
    # print(f"Respone: {response}")
    if response.is_alive:
        if currentStatus == "OFF":
            lastOnTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            bot.sendMessage("@dtek_salutna_kyiv", "Електроживлення відновленно")
            print(f"+ {lastOnTime}")
            currentStatus = "ON"
        sleep(5)
        checkConncetion()
    else:
        if currentStatus == "ON":
            lastOffTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            bot.sendMessage("@dtek_salutna_kyiv", "Електроживлення відключено")
            print(f"- {lastOffTime}")
            currentStatus = "OFF"
        sleep(5)
        checkConncetion()
    return response.is_alive

if __name__ == '__main__':
    checkConncetion()

