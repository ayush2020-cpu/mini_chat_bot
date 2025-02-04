import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import time

recognizer = sr.Recognizer()
speaker = pyttsx3.init()

speaker.setProperty('rate', 150)
speaker.setProperty('volume', 1)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        command = ""
        
        try:
            command = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        
        return command.lower()

def respond(command):
    if 'hello' in command:
        speak("Hello! How can I help you today?")
    
    elif 'wikipedia' in command:
        speak("What would you like to know about?")
        query = listen()
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    
    elif 'open' in command and 'website' in command:
        speak("Which website would you like me to open?")
        website = listen()
        url = f"https://{website}"
        webbrowser.open(url)
        speak(f"Opening {website} now.")
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    
    elif 'exit' in command or 'goodbye' in command:
        speak("Goodbye! Have a great day.")
        exit()
    
    else:
        speak("Sorry, I did not understand that.")

def run_assistant():
    speak("Hello! I am your personal assistant. How can I assist you today?")
    
    while True:
        command = listen()
        
        if command:
            respond(command)
        time.sleep(1)

if __name__ == "__main__":
    run_assistant()
