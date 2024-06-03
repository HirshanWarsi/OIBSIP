import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests

#Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet based on the time
def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good Afternoon!, How can I assist you?")
    else:
        speak("Good evening!, How can I assist you?")

# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

# Function to handle commands        
def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open amazon" in command:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
    elif "exit" in command or "stop" in command:
        speak("Thank you for using me!")
    else:
        speak("I'm not sure how to help with that.")
  
def main():
    greet()
    while True:
        command = listen()
        if "close" in command or "stop" in command:
            speak("Thank you for using me!")
            break
        else:
            handle_command(command)

if  __name__ == "__main__":
    main()

