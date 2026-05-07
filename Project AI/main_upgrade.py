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
import pyautogui
import pyperclip
import time

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
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": command}
        ]
    )
    return response.content[0].text  # ✅ Fixed: was response.choices[0].message.content

# ─────────────────────────────────────────────
# NEW FEATURE 1: Copy Chat History from App
# ─────────────────────────────────────────────
def get_chat_history():
    """
    Clicks on the chat window, selects all text, copies it to clipboard,
    and returns the text as a string.
    """
    print("Getting chat history...")
    
    # Click on the chat window (you need to set correct X, Y coordinates)
    # To find coordinates: run pyautogui.position() while hovering over chat window
    pyautogui.click(x=800, y=600)   # <-- Change this to your chat window position
    time.sleep(0.5)
    
    # Select all text in the chat window
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)
    
    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)
    
    # Get text from clipboard
    chat_text = pyperclip.paste()
    print(f"Chat history copied! Length: {len(chat_text)} characters")
    
    return chat_text


# ─────────────────────────────────────────────
# NEW FEATURE 2: Check if Last Message is from Specific User
# ─────────────────────────────────────────────
def check_last_sender(chat_history, target_user="Ali Bushar"):
    """
    Checks if the last message in the chat was sent by target_user.
    Returns True if yes, False if no.
    """
    lines = chat_history.strip().split('\n')
    
    # Loop from the bottom to find the last non-empty line
    for line in reversed(lines):
        line = line.strip()
        if line == "":
            continue
        
        # Check if the line contains the target user's name
        if target_user.lower() in line.lower():
            print(f"Last message is from: {target_user}")
            return True
        else:
            print(f"Last message is NOT from {target_user}")
            return False
    
    return False


# ─────────────────────────────────────────────
# NEW FEATURE 3: Generate Funny Roast Response using AI
# ─────────────────────────────────────────────
def generate_roast(chat_history):
    """
    Sends the chat history to OpenAI GPT and asks it to generate
    a funny roast-style reply based on what was said.
    """
    client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
    prompt = f"""
    Here is a chat conversation:
    {chat_history}
    
    The last message was sent by Ali Bushar.
    Generate a funny, roast-style reply to tease Ali Bushar in a friendly way.
    Keep it short (1-2 sentences), funny, and not offensive.
    """
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",   # Good model for funny responses
        messages=[
            {"role": "system", "content": "You are a funny comedian who loves to roast people in a friendly way."},
            {"role": "user", "content": prompt}
        ]
    )
    
    roast_reply = completion.choices[0].message.content
    print(f"Generated roast: {roast_reply}")
    return roast_reply


# ─────────────────────────────────────────────
# NEW FEATURE 4: Type and Send the Reply in Chat App
# ─────────────────────────────────────────────
def send_reply_in_chat(reply_text):
    """
    Uses pyperclip to copy the reply, then uses pyautogui to
    click the chat input box and paste + send the message.
    """
    print("Sending reply in chat...")
    
    # Copy reply text to clipboard
    pyperclip.copy(reply_text)
    time.sleep(0.3)
    
    # Click on the chat input box (Change X, Y to your input box position)
    pyautogui.click(x=800, y=900)   # <-- Change this to your chat input box position
    time.sleep(0.5)
    
    # Paste the text from clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    
    # Press Enter to send the message
    pyautogui.press('enter')
    time.sleep(0.3)
    
    print("Reply sent successfully!")
    speak("Reply sent successfully!")


# ─────────────────────────────────────────────
# NEW FEATURE 5: Full Automated Chat Interaction (Combines all above)
# ─────────────────────────────────────────────
def auto_chat_roast():
    """
    Full automated flow:
    1. Get chat history
    2. Check if Ali Bushar sent the last message
    3. Generate a funny roast
    4. Send the roast reply automatically
    """
    speak("Starting automated chat interaction")
    
    # Step 1: Get chat history
    chat_history = get_chat_history()
    
    if not chat_history:
        speak("Could not get chat history. Please make sure the chat window is open.")
        return
    
    # Step 2: Check if last message is from Ali Bushar
    is_ali = check_last_sender(chat_history, target_user="Ali Bushar")
    
    if is_ali:
        speak("Last message is from Ali Bushar. Generating roast reply...")
        
        # Step 3: Generate funny roast
        roast = generate_roast(chat_history)
        speak(f"Generated reply: {roast}")
        
        # Step 4: Send the reply
        send_reply_in_chat(roast)
        
    else:
        speak("Last message is not from Ali Bushar. No roast needed.")
        print("Last message is not from Ali Bushar. Skipping roast.")


# ─────────────────────────────────────────────
# ORIGINAL processcommand (Updated with new voice trigger)
# ─────────────────────────────────────────────
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
        
        # ✅ NEW: Voice trigger for auto chat roast feature
        elif "roast ali" in command or "roast chat" in command:
            auto_chat_roast()
            
        else:
            speak("Please choose OpenAI or Anthropic")   


# ─────────────────────────────────────────────
# MAIN LOOP (Same as original, no changes)
# ─────────────────────────────────────────────
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