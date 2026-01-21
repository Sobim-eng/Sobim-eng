# commands.py
import webbrowser
import pyautogui
import random
import speech_recognition as sr

pyautogui.FAILSAFE = True
volume_step = 5
r = sr.Recognizer()

response = {
    "OK",
    "Right away",
    "Working"
    "Working on it"
}

def open_browser(speak):
    speak(random(response))
    speak("Opening Browser")
    webbrowser.open("https://www.google.com")

def open_youtube(speak):
    speak(random(response))
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def volume_up(speak):
    for _ in range(volume_step):
        pyautogui.press("volumeup")

def volume_down(speak):
    for _ in range(volume_step):
        pyautogui.press("volumedown")

def mute_volume(speak):
    pyautogui.press("volumemute")

volume_Settings = {
    "volume up": volume_up,
    "volume down": volume_down,
    "Silence": mute_volume
}
def take_screenshot_cmd(speak, screenshot_func):
    speak("Taking screenshot")
    screenshot_func()

def close_app(speak):
    confiramtion = speak("You sure? ")
    try:
        if "yes" in confiramtion:
            speak("Closing Application")
            pyautogui.hotkey("alt", 'f4')
        else:
            speak("Cancelling closing")
    
    except Exception as e:
        print (e)

def minimize_screen(speak):
    speak("Minimizing Screen")
    pyautogui.hotkey("win", "d")

def setting(speak):
    speak("Opening Settings")
    pyautogui.hotkey("win", "i")

def opened_window(speak):
    speak("Working on that")
    pyautogui.hotkey("win", "tab")

def search(speak):
    speak("Opening Search: ")
    pyautogui.hotkey("win", "s")

def register_commands(speak, screenshot_func):
    return {
        "open browser" or "start browser": lambda: open_browser(speak),
        "open youtube": lambda: open_youtube(speak),
        "volume up": lambda: volume_up(speak),
        "volume down": lambda: volume_down(speak),
        "mute": lambda: mute_volume(speak),
        "screenshot": lambda: take_screenshot_cmd(speak, screenshot_func),
        "close app" or "close application": lambda: close_app(speak),
        "minimize": lambda: minimize_screen(speak),
        "windows": lambda: opened_window(speak)
    }

