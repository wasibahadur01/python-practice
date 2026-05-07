
# FULL AI ASSISTANT - ALL FEATURES

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
import psutil
import shutil
import zipfile
import glob
import subprocess
import ctypes
import requests
import smtplib
import imaplib
import email
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import json
import base64
import schedule
import threading
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp
#import face_recognition
import pynput
from pynput import keyboard as kb, mouse as ms
import pygame
import tweepy
import pywhatkit
from twilio.rest import Client as TwilioClient
import openpyxl
import pdfplumber
from deep_translator import GoogleTranslator
from textblob import TextBlob
import language_tool_python
import notifypy
import pygetwindow as gw
import win32api
import win32con
import hashlib
from cryptography.fernet import Fernet

# ============================================================
# SETUP
# ============================================================
recoginer = sr.Recognizer()
engine = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ============================================================
# ORIGINAL: AI COMMANDS
# ============================================================
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
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": command}]
    )
    return response.content[0].text

# ============================================================
# ORIGINAL: CHAT ROAST FEATURES
# ============================================================
def get_chat_history():
    print("Getting chat history...")
    pyautogui.click(x=800, y=600)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)
    chat_text = pyperclip.paste()
    return chat_text

def check_last_sender(chat_history, target_user="Ali Bushar"):
    lines = chat_history.strip().split('\n')
    for line in reversed(lines):
        line = line.strip()
        if line == "":
            continue
        if target_user.lower() in line.lower():
            return True
        else:
            return False
    return False

def generate_roast(chat_history):
    client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    prompt = f"Here is a chat:\n{chat_history}\nGenerate a funny roast reply to Ali Bushar. Keep it short and friendly."
    completion = client.chat.completions.create(
        model="Your-Model-Name",
        messages=[
            {"role": "system", "content": "You are a funny comedian."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def send_reply_in_chat(reply_text):
    pyperclip.copy(reply_text)
    time.sleep(0.3)
    pyautogui.click(x=800, y=900)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')
    speak("Reply sent!")

def auto_chat_roast():
    speak("Starting automated chat interaction")
    chat_history = get_chat_history()
    if not chat_history:
        speak("Could not get chat history.")
        return
    is_ali = check_last_sender(chat_history, target_user="Ali Bushar")
    if is_ali:
        speak("Generating roast reply...")
        roast = generate_roast(chat_history)
        speak(f"Sending: {roast}")
        send_reply_in_chat(roast)
    else:
        speak("Last message is not from Ali Bushar.")

# ============================================================
# NEW: DESKTOP & SYSTEM CONTROL
# ============================================================

# Control mouse and keyboard automatically
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    speak(f"Mouse moved to {x}, {y}")

def click_mouse(x, y):
    pyautogui.click(x, y)
    speak("Clicked!")

def type_text(text):
    pyautogui.typewrite(text, interval=0.05)
    speak("Text typed!")

# Take and analyze screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    path = "screenshot.png"
    screenshot.save(path)
    speak("Screenshot taken! Analyzing now...")
    
    # Analyze screenshot using Claude Vision
    with open(path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": image_data}},
                {"type": "text", "text": "Describe what is on this screen in detail."}
            ]
        }]
    )
    result = response.content[0].text
    speak(result)
    print(result)

# Open any application
def open_application(app_name):
    speak(f"Opening {app_name}")
    os.startfile(app_name) if os.path.exists(app_name) else subprocess.Popen(app_name)

# Close any application
def close_application(app_name):
    speak(f"Closing {app_name}")
    os.system(f"taskkill /f /im {app_name}.exe")

# Monitor CPU, RAM, disk usage
def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    result = f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%"
    speak(result)
    print(result)

# Auto-organize files in a folder
def organize_files(folder_path):
    speak("Organizing files...")
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z"],
        "Code": [".py", ".js", ".html", ".css", ".java"]
    }
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, exts in extensions.items():
                if ext in exts:
                    dest = os.path.join(folder_path, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, file))
                    break
    speak("Files organized successfully!")

# Rename bulk files
def rename_bulk_files(folder_path, prefix="file"):
    speak("Renaming files...")
    files = os.listdir(folder_path)
    for i, file in enumerate(files):
        ext = os.path.splitext(file)[1]
        old = os.path.join(folder_path, file)
        new = os.path.join(folder_path, f"{prefix}_{i+1}{ext}")
        os.rename(old, new)
    speak(f"Renamed {len(files)} files!")

# Zip files by voice
def zip_files(folder_path, zip_name="output.zip"):
    speak("Zipping files...")
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in glob.glob(f"{folder_path}/*"):
            zipf.write(file, os.path.basename(file))
    speak("Files zipped successfully!")

# Unzip files by voice
def unzip_files(zip_path, extract_to="."):
    speak("Unzipping files...")
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    speak("Files unzipped successfully!")

# Lock PC by voice
def lock_pc():
    speak("Locking PC...")
    ctypes.windll.user32.LockWorkStation()

# Unlock PC — just wake screen (actual unlock needs password)
def unlock_pc():
    speak("Waking screen...")
    pyautogui.press('enter')

# Set wallpaper by voice
def set_wallpaper(image_path):
    speak("Setting wallpaper...")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    speak("Wallpaper set!")

# ============================================================
# NEW: AI & SMART FEATURES
# ============================================================

# Claude Computer Use — AI sees screen and controls it
def claude_computer_use(task):
    speak("Activating Claude Computer Use...")
    screenshot = pyautogui.screenshot()
    path = "screen_for_claude.png"
    screenshot.save(path)
    
    with open(path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": image_data}},
                {"type": "text", "text": f"Look at this screen and help me: {task}. Tell me exactly what to click or type."}
            ]
        }]
    )
    result = response.content[0].text
    speak(result)
    print(result)

# Read and summarize any webpage
def summarize_webpage(url):
    speak("Reading webpage...")
    response = requests.get(url)
    text = response.text[:3000]
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": f"Summarize this webpage content:\n{text}"}]
    )
    summary = result.content[0].text
    speak(summary)
    print(summary)

# Analyze Excel/CSV report
def analyze_report(file_path):
    speak("Analyzing report...")
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    summary = df.describe().to_string()
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Analyze this data and give insights:\n{summary}"}]
    )
    analysis = result.content[0].text
    speak(analysis)
    print(analysis)

# Generate chart from data
def generate_chart(file_path):
    speak("Generating chart...")
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    df.plot(kind='bar', figsize=(10, 6))
    plt.title("Data Chart")
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()
    speak("Chart generated and saved!")

# Translate text to Urdu/English
def translate_text(text, target_lang="ur"):
    speak("Translating...")
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    speak(translated)
    print(f"Translation: {translated}")
    return translated

# Detect emotions in chat
def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        emotion = "Happy and positive!"
    elif polarity < -0.3:
        emotion = "Negative or angry!"
    else:
        emotion = "Neutral!"
    speak(f"Emotion detected: {emotion}")
    print(f"Emotion: {emotion}, Score: {polarity}")

# Auto-correct grammar
def autocorrect_grammar(text):
    speak("Checking grammar...")
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    speak(f"Corrected text: {corrected}")
    print(f"Corrected: {corrected}")
    return corrected

# Generate full report from raw data
def generate_report(file_path):
    speak("Generating full report...")
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    data_str = df.to_string()
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": f"Generate a full professional business report from this data:\n{data_str}"}]
    )
    report = result.content[0].text
    with open("generated_report.txt", "w") as f:
        f.write(report)
    speak("Report generated and saved!")
    print(report)

# ============================================================
# NEW: CHAT & SOCIAL MEDIA AUTOMATION
# ============================================================

# Auto-reply to WhatsApp
def whatsapp_auto_reply(phone_number, message):
    speak(f"Sending WhatsApp message...")
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    speak("WhatsApp message sent!")

# Monitor keywords in chat
def monitor_keywords(chat_text, keywords=["help", "urgent", "emergency"]):
    found = [kw for kw in keywords if kw.lower() in chat_text.lower()]
    if found:
        speak(f"Alert! Keywords found: {', '.join(found)}")
        print(f"Keywords detected: {found}")
    else:
        speak("No keywords found.")

# Generate viral social media caption
def generate_caption(topic):
    speak("Generating social media caption...")
    client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a viral social media expert."},
            {"role": "user", "content": f"Generate a viral caption for: {topic}. Include hashtags."}
        ]
    )
    caption = completion.choices[0].message.content
    speak("Caption generated!")
    print(caption)
    return caption

# Scrape and analyze Twitter/X posts
def analyze_twitter(query):
    speak(f"Searching Twitter for {query}...")
    # Note: Requires Twitter API v2 Bearer Token
    client = tweepy.Client(bearer_token="YOUR-TWITTER-BEARER-TOKEN")
    tweets = client.search_recent_tweets(query=query, max_results=10)
    tweet_texts = [tweet.text for tweet in tweets.data] if tweets.data else []
    combined = "\n".join(tweet_texts)
    
    ai_client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = ai_client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": f"Analyze these tweets and summarize:\n{combined}"}]
    )
    speak(result.content[0].text)
    print(result.content[0].text)

# ============================================================
# NEW: EMAIL AUTOMATION
# ============================================================

EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"   # Use Gmail App Password

# Send email by voice
def send_email(to, subject, body):
    speak(f"Sending email to {to}...")
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, EMAIL_PASSWORD)
    server.sendmail(EMAIL, to, msg.as_string())
    server.quit()
    speak("Email sent!")

# Read and summarize unread emails
def read_emails():
    speak("Reading unread emails...")
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL, EMAIL_PASSWORD)
    mail.select('inbox')
    
    _, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()[:5]   # Read last 5 unread
    
    summaries = []
    for eid in email_ids:
        _, msg_data = mail.fetch(eid, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        subject = msg['subject']
        from_addr = msg['from']
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()
        summaries.append(f"From: {from_addr}\nSubject: {subject}\nBody: {body[:200]}")
    
    combined = "\n\n".join(summaries)
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": f"Summarize these emails briefly:\n{combined}"}]
    )
    speak(result.content[0].text)
    print(result.content[0].text)

# ============================================================
# NEW: DATA & REPORT ANALYSIS
# ============================================================

# Read PDF and summarize
def read_pdf(pdf_path):
    speak("Reading PDF...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Summarize this PDF:\n{text[:4000]}"}]
    )
    speak(result.content[0].text)
    print(result.content[0].text)

# Real-time stock price alert
def stock_alert(symbol):
    speak(f"Checking stock price for {symbol}...")
    response = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}")
    data = response.json()
    price = data['chart']['result'][0]['meta']['regularMarketPrice']
    speak(f"{symbol} current price is {price} dollars")
    print(f"{symbol}: ${price}")

# Read news and summarize
def daily_news_briefing():
    speak("Getting daily news briefing...")
    response = requests.get("https://newsapi.org/v2/top-headlines?country=pk&apiKey=YOUR-NEWSAPI-KEY")
    articles = response.json().get('articles', [])[:5]
    headlines = "\n".join([a['title'] for a in articles])
    
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": f"Summarize these news headlines:\n{headlines}"}]
    )
    speak(result.content[0].text)

# ============================================================
# NEW: MEDIA & ENTERTAINMENT
# ============================================================

# Control Spotify by voice
def spotify_play(song_name):
    speak(f"Playing {song_name} on Spotify...")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="YOUR-SPOTIFY-CLIENT-ID",
        client_secret="YOUR-SPOTIFY-SECRET",
        redirect_uri="http://localhost:8888/callback",
        scope="user-read-playback-state,user-modify-playback-state"
    ))
    results = sp.search(q=song_name, type='track', limit=1)
    uri = results['tracks']['items'][0]['uri']
    devices = sp.devices()
    device_id = devices['devices'][0]['id']
    sp.start_playback(device_id=device_id, uris=[uri])
    speak(f"Now playing {song_name}!")

# Download YouTube video/audio
def download_youtube(url, audio_only=False):
    speak("Downloading from YouTube...")
    opts = {
        'format': 'bestaudio/best' if audio_only else 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    speak("Download complete!")

# Generate AI image by voice
def generate_image(prompt):
    speak(f"Generating image for: {prompt}")
    client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1
    )
    image_url = response.data[0].url
    speak("Image generated! Opening in browser...")
    webbrowser.open(image_url)
    print(f"Image URL: {image_url}")

# Play/pause media
def media_control(action):
    if action == "play" or action == "pause":
        pyautogui.press('playpause')
    elif action == "next":
        pyautogui.press('nexttrack')
    elif action == "previous":
        pyautogui.press('prevtrack')
    speak(f"Media {action}!")

# ============================================================
# NEW: WEB & BROWSER AUTOMATION
# ============================================================

# Auto Google search and summarize
def search_and_summarize(query):
    speak(f"Searching for {query}...")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}")
    if response.status_code == 200:
        summary = response.json().get('extract', 'No summary found')
        speak(summary[:500])
        print(summary)

# Monitor website for price changes
def monitor_price(url, check_text):
    speak(f"Monitoring {url} for price changes...")
    response = requests.get(url)
    if check_text in response.text:
        speak("Price alert! Target price found!")
        print("Price found!")
    else:
        speak("Price not yet reached.")

# ============================================================
# NEW: PHONE & NOTIFICATIONS
# ============================================================

# Send SMS by voice
def send_sms(to_number, message):
    speak(f"Sending SMS to {to_number}...")
    client = TwilioClient("YOUR-TWILIO-SID", "YOUR-TWILIO-TOKEN")
    client.messages.create(
        body=message,
        from_="+1XXXXXXXXXX",   # Your Twilio number
        to=to_number
    )
    speak("SMS sent!")

# Push notification on PC
def push_notification(title, message):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = message
    notification.send()
    speak(f"Notification sent: {title}")

# ============================================================
# NEW: SECURITY & PRIVACY
# ============================================================

# Face recognition login
# def face_login():
#     speak("Starting face recognition...")
#     known_image = face_recognition.load_image_file("my_face.jpg")   # Your photo
#     known_encoding = face_recognition.face_encodings(known_image)[0]
    
#     cam = cv2.VideoCapture(0)
#     ret, frame = cam.read()
#     cam.release()
    
#     unknown_encodings = face_recognition.face_encodings(frame)
#     if unknown_encodings:
#         match = face_recognition.compare_faces([known_encoding], unknown_encodings[0])
#         if match[0]:
#             speak("Face recognized! Access granted!")
#             return True
#         else:
#             speak("Face not recognized! Access denied!")
#             return False
#     else:
#         speak("No face detected!")
#         return False

# Alert when USB is plugged in
def monitor_usb():
    speak("Monitoring USB ports...")
    initial = set(psutil.disk_partitions())
    while True:
        current = set(psutil.disk_partitions())
        new = current - initial
        if new:
            speak("Alert! New USB device connected!")
            print(f"New device: {new}")
            push_notification("USB Alert", "New USB device plugged in!")
        initial = current
        time.sleep(2)
        

# Encrypt file
def encrypt_file(file_path):
    speak("Encrypting file...")
    key = Fernet.generate_key()
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(file_path + ".encrypted", 'wb') as file:
        file.write(encrypted)
    with open("encryption_key.key", 'wb') as key_file:
        key_file.write(key)
    speak("File encrypted! Key saved to encryption_key.key")

# Decrypt file
def decrypt_file(encrypted_path, key_path):
    speak("Decrypting file...")
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    f = Fernet(key)
    with open(encrypted_path, 'rb') as file:
        data = file.read()
    decrypted = f.decrypt(data)
    output_path = encrypted_path.replace(".encrypted", "_decrypted")
    with open(output_path, 'wb') as file:
        file.write(decrypted)
    speak("File decrypted successfully!")

# Auto-lock PC when idle
def auto_lock_on_idle(idle_minutes=5):
    speak(f"Auto-lock enabled. Will lock after {idle_minutes} minutes of idle.")
    while True:
        idle_time = (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000
        if idle_time >= idle_minutes * 60:
            speak("Idle detected. Locking PC.")
            lock_pc()
        time.sleep(30)

# ============================================================
# NEW: MEMORY & LEARNING
# ============================================================

MEMORY_FILE = "assistant_memory.json"

# Remember things
def remember(key, value):
    memory = {}
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
    memory[key] = value
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f)
    speak(f"I will remember that {key} is {value}")

# Recall things
def recall(key):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
        value = memory.get(key, "I don't remember that.")
        speak(f"{key} is {value}")
        return value
    speak("No memory found.")

# Keep diary by voice
def add_diary_entry(entry):
    timestamp = t.strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"\n[{timestamp}]\n{entry}\n")
    speak("Diary entry saved!")

# Smart todo list
def add_todo(task):
    with open("todo.txt", "a") as f:
        f.write(f"[ ] {task}\n")
    speak(f"Added to todo list: {task}")

def read_todos():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            todos = f.read()
        speak("Here are your tasks:")
        print(todos)
        speak(todos)
    else:
        speak("No tasks found.")

# ============================================================
# NEW: LANGUAGE & COMMUNICATION
# ============================================================

# Translate and speak in Urdu
def speak_urdu(text):
    urdu = translate_text(text, target_lang="ur")
    engine.say(urdu)
    engine.runAndWait()

# Summarize Urdu news
def urdu_news():
    speak("Getting Urdu news...")
    response = requests.get("https://newsapi.org/v2/top-headlines?country=pk&language=ur&apiKey=YOUR-NEWSAPI-KEY")
    articles = response.json().get('articles', [])[:3]
    for article in articles:
        title = article.get('title', '')
        speak(title)
        print(title)

# Generate Urdu social media post
def generate_urdu_post(topic):
    speak("Generating Urdu social media post...")
    client = anthropic.Anthropic(api_key="YOUR-ANTHROPIC-KEY")
    result = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": f"Write a viral Urdu social media post about: {topic}. Include hashtags in Urdu and English."}]
    )
    post = result.content[0].text
    speak("Post generated!")
    print(post)
    return post

# ============================================================
# UPDATED: PROCESS COMMAND (All voice triggers)
# ============================================================
def processcommand(command):
    with sr.Microphone() as source:
        print("processing command...")
        recoginer.pause_threshold = 1
        recoginer.energy_threshold = 300
        recoginer.adjust_for_ambient_noise(source)
        audio = recoginer.listen(source, timeout=2, phrase_time_limit=2)

    # --- ORIGINAL FEATURES ---
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
        output = Aiprocesscommand2(command)
        speak(output)
    elif "openai" in command:
        output = Aiprocesscommand(command)
        speak(output)
    elif "roast ali" in command or "roast chat" in command:
        auto_chat_roast()

    # --- DESKTOP CONTROL ---
    elif "take screenshot" in command:
        take_screenshot()
    elif "lock pc" in command or "lock computer" in command:
        lock_pc()
    elif "monitor system" in command or "system status" in command:
        monitor_system()
    elif "organize files" in command:
        organize_files("C:/Users/YourName/Downloads")   # Change path
    elif "zip files" in command:
        zip_files("C:/Users/YourName/Downloads")        # Change path
    elif "set wallpaper" in command:
        set_wallpaper("C:/Users/YourName/wallpaper.jpg")  # Change path

    # --- AI FEATURES ---
    elif "analyze screen" in command or "what's on screen" in command:
        claude_computer_use(command)
    elif "summarize webpage" in command:
        speak("Which URL should I summarize?")
        # You can add URL input logic here
    elif "analyze report" in command:
        analyze_report("report.csv")   # Change file path
    elif "generate chart" in command:
        generate_chart("report.csv")   # Change file path
    elif "translate to urdu" in command:
        text = command.replace("translate to urdu", "").strip()
        translate_text(text, target_lang="ur")
    elif "translate to english" in command:
        text = command.replace("translate to english", "").strip()
        translate_text(text, target_lang="en")
    elif "check emotion" in command:
        text = command.replace("check emotion", "").strip()
        detect_emotion(text)
    elif "correct grammar" in command:
        text = command.replace("correct grammar", "").strip()
        autocorrect_grammar(text)
    elif "generate report" in command:
        generate_report("data.csv")   # Change file path

    # --- SOCIAL MEDIA ---
    elif "generate caption" in command:
        topic = command.replace("generate caption", "").strip()
        generate_caption(topic)
    elif "urdu post" in command:
        topic = command.replace("urdu post", "").strip()
        generate_urdu_post(topic)

    # --- EMAIL ---
    elif "read emails" in command:
        read_emails()
    elif "send email" in command:
        send_email("recipient@gmail.com", "Voice Email", "This email was sent by voice!")

    # --- DATA & REPORTS ---
    elif "read pdf" in command:
        read_pdf("document.pdf")   # Change file path
    elif "stock price" in command:
        symbol = command.replace("stock price", "").strip().upper()
        stock_alert(symbol)
    elif "daily news" in command or "news briefing" in command:
        daily_news_briefing()

    # --- MEDIA ---
    elif "play on spotify" in command:
        song = command.replace("play on spotify", "").strip()
        spotify_play(song)
    elif "download youtube" in command:
        speak("Please say the YouTube URL")
        # Add URL capture logic
    elif "generate image" in command:
        prompt = command.replace("generate image", "").strip()
        generate_image(prompt)
    elif "pause music" in command:
        media_control("pause")
    elif "next song" in command:
        media_control("next")

    # --- SECURITY ---
    #elif "face login" in command:
    #    face_login()
    elif "encrypt file" in command:
        encrypt_file("important.txt")   # Change file path
    elif "decrypt file" in command:
        decrypt_file("important.txt.encrypted", "encryption_key.key")

    # --- MEMORY ---
    elif "remember that" in command:
        parts = command.replace("remember that", "").strip().split(" is ")
        if len(parts) == 2:
            remember(parts[0].strip(), parts[1].strip())
    elif "what is" in command and "recall" in command:
        key = command.replace("recall what is", "").strip()
        recall(key)
    elif "add diary" in command:
        entry = command.replace("add diary", "").strip()
        add_diary_entry(entry)
    elif "add todo" in command:
        task = command.replace("add todo", "").strip()
        add_todo(task)
    elif "read todos" in command or "my tasks" in command:
        read_todos()

    # --- NOTIFICATIONS ---
    elif "send sms" in command:
        send_sms("+92XXXXXXXXXX", "Hello from your AI assistant!")

    # --- NEWS ---
    elif "urdu news" in command:
        urdu_news()

    else:
        speak("Please choose a valid command or say OpenAI or Anthropic")


# ============================================================
# MAIN LOOP (Same as original)
# ============================================================
if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you?")
    
    # Start USB monitor in background thread
    usb_thread = threading.Thread(target=monitor_usb, daemon=True)
    usb_thread.start()
    
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



            