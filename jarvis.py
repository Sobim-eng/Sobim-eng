import speech_recognition as sr
import pyttsx3
import os
import time
import pyautogui
import google.generativeai as ai
from commands import register_commands

# Initial setup
r = sr.Recognizer()
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 180)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Gemini AI setup
ai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = ai.GenerativeModel("gemini-1.5-flash")

def ask_jarvis(prompt):
    try:
        response = model.generate_content(
            f"Answer briefly in 1-2 sentences: {prompt}"
        )
        return response.text
    except Exception as e:
        print(f"API Error: {e}")
        return "I'm having trouble accessing my database."

def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(filename)
    speak(f"Screenshot saved as {filename}")

# Register commands ONCE
COMMANDS = register_commands(speak, take_screenshot)
def process_command(user_command):
    user_command = user_command.lower()

    for trigger, action in COMMANDS.items():
        if trigger in user_command:
            action()
            return

    speak(ask_jarvis(user_command))

#Listen command
def listen_command(timeout=5, limit=7):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source, timeout=timeout, phrase_time_limit=limit)
        return r.recognize_google(audio).lower()

# Main loop
speak("Jarvis is online and ready.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening for 'Jarvis'...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        command = r.recognize_google(audio).lower()

        if "jarvis" in command:
            speak("Yes?")
            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=10)
                    user_command = r.recognize_google(audio)
                    print(f"You said: {user_command}")
                    process_command(user_command)
                except sr.WaitTimeoutError:
                    speak("Are you still there? I am still listening.")
                except sr.UnknownValueError:
                    speak("I didn't catch that.")

        elif "exit" in command:
            speak("Shutting down. Goodbye!")
            break

    except Exception as e:
        print(f"Error in main loop: {e}")
