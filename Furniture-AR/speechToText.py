import speech_recognition as sr
import os

# creating a speech recognition object
recognizer = sr.Recognizer()
microphone = sr.Microphone()

   # adjust recognizer sensitivity to ambient noise and record
   # from microphone
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    print("Recognizing...")

try:
    text = recognizer.recognize_google(audio)
except sr.UnknownValueError:
    # speech was unintelligible
    print("Unable to recognize speech")
except sr.RequestError:
    # API was unreachable or unresponsive
    print("API unavailable")
