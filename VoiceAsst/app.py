import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said: " + query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


if __name__ == "__main__":
    speak("Hello! I'm Lionel Messi , your favourite voice assistant.")
    speak("How can I help you meri jaan?")

    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you today?")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = get_date()
                speak(f"Today's date is {current_date}")
                print(f"Today's date is {current_date}")
            elif "search" in command:
                search_query = command.replace("search", "").strip()
                speak(f"Searching the web for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif "exit" in command:
                speak("Goodbye have a nice day ahead!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")
