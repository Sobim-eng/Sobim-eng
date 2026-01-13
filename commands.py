# commands.py
import webbrowser
import pyautogui
import time
import speech_recognition as sr

pyautogui.FAILSAFE = True
volume_step = 5
r = sr.Recognizer()

def open_browser(speak):
    speak("Opening browser")
    webbrowser.open("https://www.google.com")

def open_youtube(speak):
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

def take_screenshot_cmd(speak, screenshot_func):
    speak("Taking screenshot")
    screenshot_func()

def close_app(speak):  
    speak("Are you sure? ")
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            user_command = r.recognize_google(audio)
            if "yes" in user_command.lower():
                speak("Closing the application")
                pyautogui.hotkey("alt", "f4")
            else:
                speak("Close application command cancelled.")
        except sr.UnknownValueError:
            speak("I didn't catch that.")
            
    
    pyautogui.hotkey("alt", "f4")
        
        
def register_commands(speak, screenshot_func):
    return {
        "open browser" or "start browser": lambda: open_browser(speak),
        "open youtube": lambda: open_youtube(speak),
        "volume up": lambda: volume_up(speak),
        "volume down": lambda: volume_down(speak),
        "mute": lambda: mute_volume(speak),
        "screenshot": lambda: take_screenshot_cmd(speak, screenshot_func),
        "close app" or "close application": lambda: close_app(speak)
    }
