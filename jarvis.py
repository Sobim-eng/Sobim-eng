import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import time
import pyautogui
import google.generativeai as ai

# ------------------ INITIAL SETUP ------------------
r = sr.Recognizer()
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 180) # Faster, more natural speed

def speak(text):
    print(f"Jarvis: {text}") # See it in console too
    engine.say(text)

# Google AI Gemini setup
# AI SETUP
import os
ai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = ai.GenerativeModel('gemini-1.5-flash')

def ask_jarvis(prompt):
    try:
        # We add a short instruction so Jarvis doesn't talk too much
        response = model.generate_content(f"Answer briefly in 1-2 sentences: {prompt}")
        return response.text
    except Exception as e:
        # This will now help you see the EXACT error in your terminal
        print(f"API Error: {e}")
        return "I'm sorry sir, I'm having trouble accessing my database."
    
# COMMAND PROCESSOR
def processCommand(cmd):
    cmd = cmd.lower()
    
    if "open youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")

    elif "open Chat" in cmd:
        speak("Opening Chat GPT")
        webbrowser.open("https://chatgpt.com/")

    elif "instagram" in cmd:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")

    elif "screenshot" in cmd:
        speak("Taking screenshot")
        take_screenshot()

    elif cmd.startswith("play"):
        song = cmd.replace("play ", "")
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak(f"I don't have {song} in my local library, searching YouTube...")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    # If it's not a specific command Gemini will handle it!
    else:
        print("Consulting Gemini...")
        ai_response = ask_jarvis(cmd)
        speak(ai_response)

#pyautogui task
def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    speak(f"Screenshot taken and saved as {filename}")

# MAIN LOOP 
speak("Jarvis is online and ready.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening for 'Jarvis'...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=None) # Wait indefinitely for wake word

        command = r.recognize_google(audio).lower()
        
        if "jarvis" in command:
            speak("Yes?")
            
            with sr.Microphone() as source:
                # Add a try-except here to prevent crash if you don't speak
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    user_command = r.recognize_google(audio)
                    print(f"You said: {user_command}")
                    processCommand(user_command)
                except sr.WaitTimeoutError:
                    print("No command heard.")
                except sr.UnknownValueError:
                    speak("I didn't catch that.")
        elif "exit" in command or "quit" in command:
            speak("Shutting down. Goodbye!")
            break

    except Exception as e:
        print(f"Error in main loop: {e}")