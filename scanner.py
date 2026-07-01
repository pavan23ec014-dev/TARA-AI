import os
import json

database = []

# Folders to scan
paths_to_scan = [
    os.path.join(os.environ["USERPROFILE"], "Desktop"),
    os.path.join(os.environ["USERPROFILE"], "Documents"),
    os.path.join(os.environ["USERPROFILE"], "Downloads"),
    r"G:\dji",
    r"G:\insta 360"
]

def scan_folder(folder):
    if not os.path.exists(folder):
        print(f"Skipping missing folder: {folder}")
        return

    for root, dirs, files in os.walk(folder):
        for d in dirs:
            database.append({
                "name": d.lower(),
                "path": os.path.join(root, d),
                "type": "folder"
            })

        for f in files:
            database.append({
                "name": f.lower(),
                "path": os.path.join(root, f),
                "type": "file"
            })

for path in paths_to_scan:
    print(f"Scanning: {path}")
    scan_folder(path)

with open("database.json", "w", encoding="utf-8") as file:
    json.dump(database, file, indent=2)

print(f"Done! Indexed {len(database)} items.")