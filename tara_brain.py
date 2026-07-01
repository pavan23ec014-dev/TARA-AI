import ollama
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", 170)

print("===== Tara =====")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        engine.say("Goodbye Pavan.")
        engine.runAndWait()
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system",
             "content": "Your name is Tara. You are Pavan's personal AI assistant. Your name is pronounced Taara. Reply in a friendly, concise manner."},
            {"role": "user",
             "content": user}
        ]
    )

    reply = response["message"]["content"]

    print("\nTara:", reply, "\n")

    engine.say(reply)
    engine.runAndWait()