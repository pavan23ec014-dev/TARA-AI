import json
import os
from rapidfuzz import fuzz

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


while True:
    query = input("Search: ")

    if query.lower() == "exit":
        break

    result, score = search_item(query)

    if result:
        print(f"\nFound: {result['name']}")
        print(f"Path: {result['path']}")
        print(f"Match Score: {score}")

        open_now = input("\nOpen it? (y/n): ")

        if open_now.lower() == "y":
            os.startfile(result["path"])
    else:
        print("No match found.")