import json
import os
from rapidfuzz import fuzz

# Load scanned database
with open("database.json", "r", encoding="utf-8") as file:
    database = json.load(file)


def search_item(query):
    best_match = None
    best_score = 0

    query = query.lower()

    for item in database:
        score = fuzz.partial_ratio(query, item["name"])

        if score > best_score:
            best_score = score
            best_match = item

    return best_match, best_score


def open_website(cmd):
    websites = {
        "gmail": "https://mail.google.com",
        "youtube": "https://youtube.com",
        "chatgpt": "https://chatgpt.com",
        "github": "https://github.com",
        "google": "https://google.com"
    }

    for name, url in websites.items():
        if name in cmd:
            print(f"Opening {name}...")
            os.system(f"start {url}")
            return True

    return False


while True:
    cmd = input("\nYou: ").lower()

    if cmd == "exit":
        print("Goodbye!")
        break

    # Website opening
    if open_website(cmd):
        continue

    # File/folder search
    if "open " in cmd:
        search_query = cmd.replace("open ", "")
    else:
        search_query = cmd

    result, score = search_item(search_query)

    if result and score > 60:
        print(f"Found: {result['name']}")
        print("Opening...")
        os.startfile(result["path"])
    else:
        print("I couldn't find that.")