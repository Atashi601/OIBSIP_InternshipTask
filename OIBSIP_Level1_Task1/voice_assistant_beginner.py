import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

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
        speak("Sorry, I didn't understand.")
        return ""

def main():
    speak("Hello! I am your basic voice assistant.")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {current_date}")

        elif "search" in command:
            speak("What should I search?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("Here are the search results.")

        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()