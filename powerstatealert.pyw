import psutil
import winsound
import time
import ctypes

keepGoing = True

from infi.systray import SysTrayIcon
def about_app(systray):
    ctypes.windll.user32.MessageBoxW(None, u"This is Miguel's Battery Charge Alert.\nIt alerts you whenever the charger is unplugged.", u"About", 0)
def quit_callback(systray):
    global keepGoing
    keepGoing = False
menu_options = (("About", None, about_app),)
systray = SysTrayIcon("attention.ico", "Miguel's Battery Charge Alert", menu_options, on_quit=quit_callback)
systray.start()

while True and keepGoing == True:
    if psutil.sensors_battery().power_plugged == False:
        winsound.PlaySound("Alarm Clock.wav", winsound.SND_FILENAME)
    else:
        time.sleep(5)
