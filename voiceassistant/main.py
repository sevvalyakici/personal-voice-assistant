import speech_recognition as sr
import venv 
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3


r = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def recognize_voice():
  text = ''
  
  with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)
    voice = r.listen(source)
    
    try:
      text = r.recognize_google(voice)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
      speak("Sorry, Unable to recognize your speech...")
  return text.lower()

def reply(text_version):
  
  
  if "hi" in text_version:
        speak ("Hi, nice to see you.")
  
  if "What is your name?" in text_version:
    speak("My name is JARVIS")
  
  
  if "Hello, how are you?" in text_version:
    speak("I am fine... Thank you.")
    
  
  if "date" in text_version:
    date = datetime.now().strftime("%-d %B %Y")
    speak("The date is " + date)
  
  
  if "time" in text_version:
    time = datetime.now().time().strftime("%H %M")
    speak("The time is " + time)
  
  
  if "search" in text_version:
    speak("What do you want me to search for?")
    keyword = recognize_voice()
    
    if keyword != '':
      url = "https://google.com/search?q=" + keyword
      
      speak("Here are the search results for " + keyword)
      webbrowser.open(url)
      sleep(3)
  
 
  if "quit" in text_version or "exit" in text_version:
    speak("Ok, I am going to take a nap.")
    exit()
    

sleep(1)
while True:
  speak("Start speaking...")
  text_version = recognize_voice()
  reply(text_version)