import time, requests, pyperclip
import os
from dotenv import load_dotenv

load_dotenv()

QBIT_URL = os.getenv("QBIT_URL")
AUTH = {
    "username": os.getenv("QBIT_USER"),
    "password": os.getenv("QBIT_PASS")
	}


if not QBIT_URL or not AUTH["username"] or not AUTH["password"]:
	print("Error: Missing .env file or variables.")
	print("Please check your .env file in this directory.")
else:
	print(f"Connecting to {QBIT_URL} as {AUTH['username']}...")
	try:
		s = requests.Session()
		s.post(f"{QBIT_URL}/api/v2/auth/login", data=AUTH)
	except requests.exceptions.ConnectionError:
		print(f"Connection Error: Could not connect to {QBIT_URL}.")
        print("Is qBittorrent running and is the WebUI enabled?")