import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print(f"\nTara: {text}\n")
    engine.say(text)
    engine.runAndWait()