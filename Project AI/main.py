from email.mime import audio
import os
import sys as s
import time as t
import logging as log
import webbrowser
import speech_recognition as sr
import pyttsx3 as tts
import pyaudio as pa
from openai import OpenAI
import anthropic
recoginer = sr.Recognizer()
engine = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Aiprocesscommand(command):
    client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    completion = client.chat.completions.create(
        model="Your-Model-Name",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def Aiprocesscommand2(command):
    response = anthropic.Anthropic().messages.create(
        model="Your-Model-Name",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content

def processcommand(command):
        with sr.Microphone() as source:
            print("processing command...")
            recoginer.pause_threshold = 1
            recoginer.energy_threshold = 300  
            recoginer.adjust_for_ambient_noise(source)
            audio = recoginer.listen(source, timeout=2, phrase_time_limit=2)
        if 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open facebook' in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif 'open linkedin' in command:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
        elif command.lower().startswith("search for"):
            query = command[11:].strip()
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            
        elif "anthropic" in command:
            output = Aiprocesscommand2(command)   # Anthropic API
            speak(output)
        elif "openai" in command:
            output = Aiprocesscommand(command)    # OpenAI API
            speak(output)
        else:
            speak("Please choose OpenAI or Anthropic")   
        



if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recoginer.pause_threshold = 1
            recoginer.energy_threshold = 300  
            recoginer.adjust_for_ambient_noise(source)
            audio = recoginer.listen(source, timeout=2, phrase_time_limit=2)

        try:
            command = recoginer.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")
            
            if "ali" in command.lower():
                speak("Yes, how can I help you?")
                processcommand(command)
            elif "exit" in command.lower():
                speak("Goodbye!")
                break
            else:
                speak(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            

        