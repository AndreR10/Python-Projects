import speech_recognition as sr
import pyaudio
import DateTime
import Wikipedia


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alexa: Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try Again")


# Run the code and speak anything and it will printed on the screen
print(command())
