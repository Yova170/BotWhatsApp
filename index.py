import pyautogui, webbrowser, schedule, time

from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+') #Add the phone number to which you want to send the message with its country code after the + sign


def mensaje():
    sleep(5)
    pyautogui.typewrite('') #Add your Text
    pyautogui.press("Enter")


schedule.every().day.at("").do(mensaje) #Select the time you want to send a message in 24-hour military hours

while True:
    schedule.run_pending()
    time.sleep(1)