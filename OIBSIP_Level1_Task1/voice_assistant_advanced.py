import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests
import time

# Put your API key here
WEATHER_API_KEY = "YOUR_API_KEY_HERE"

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, please repeat.")
        return ""

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")
    else:
        speak("City not found.")

def set_reminder():
    speak("After how many seconds?")
    seconds = int(listen())
    speak("What should I remind you?")
    message = listen()
    speak("Reminder set.")
    time.sleep(seconds)
    speak(f"Reminder: {message}")

def main():
    speak("Advanced voice assistant activated.")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you?")

        elif "time" in command:
            speak(datetime.datetime.now().strftime("The time is %H:%M"))

        elif "date" in command:
            speak(datetime.datetime.now().strftime("Today is %d %B %Y"))

        elif "search" in command:
            speak("What should I search?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "wikipedia" in command:
            speak("Tell me the topic.")
            topic = listen()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("No information found.")

        elif "weather" in command:
            speak("Which city?")
            city = listen()
            get_weather(city)

        elif "reminder" in command:
            set_reminder()

        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()