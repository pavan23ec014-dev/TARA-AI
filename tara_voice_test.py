import ollama
import pyttsx3

# Initialize voice
engine = pyttsx3.init()

# Try to use a female voice if available
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", 170)

# Ask Ollama
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Introduce yourself as Tara. Pronounce your name as Taara."
        }
    ]
)

reply = response["message"]["content"]

print("Tara:", reply)

# Speak it
engine.say(reply)
engine.runAndWait()