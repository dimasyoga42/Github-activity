import requests
import json
import os
import sys
from collections import Counter
def structure(nama):
    url = f"https://api.github.com/users/{nama}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        repo_names = []

        for event in data:
            if event["type"] == "PushEvent":
                repo = event["repo"]["name"]
                waktu = event["created_at"]
                repo_names.append(repo)

        if repo_names:
            print("\nJumlah push per repository:")
            count = Counter(repo_names)
            for repo, jumlah in count.items():
                print(f"{repo}: {jumlah} push")
        else:
            print("Tidak ada PushEvent yang ditemukan.")
    else:
        print("User tidak ditemukan atau API limit tercapai.")

