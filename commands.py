import pyautogui
import webbrowser
import time

def take_screenshot(speak):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

def open_browser(speak):
    webbrowser.get().open_new_tab("about:blank")

def volume_up(speak):
    pyautogui.press("volumeup")
    speak("Volume increased")

def volume_down(speak):
    pyautogui.press("volumedown")
    speak("Volume decreased")

Commands = {
    "open browser": open_browser,
    "screenshot": take_screenshot,
    "volume up": volume_up,
    "volume down": volume_down}