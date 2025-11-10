import time, requests, pyperclip
import os
from dotenv import load_dotenv
from media_directory import find_dir

load_dotenv() 
film_directory = find_dir()

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
		login_response = s.post(f"{QBIT_URL}/api/v2/auth/login", data=AUTH)

		if login_response.status_code != 200:
			print("Login failed! Please check username/password in .env file.")
		else:
			print("Login sucessful! Watching clipboard")
			clip_prev = ""
			while True:
				clip = pyperclip.paste()
				if clip != clip_prev and clip.startswith("magnet:"):
					if clip.endswith("=Torrentio"):
						clip = clip.replace("=Torrentio", "")
					print(f"Adding: {clip[:60]}")
					s.post(f"{QBIT_URL}/api/v2/torrents/add", data={"urls": clip, "savepath":film_directory})
					clip_prev = clip
				time.sleep(1)

	except requests.exceptions.ConnectionError:
		print(f"Connection Error: Could not connect to {QBIT_URL}.")
		print("Is qBittorrent running and is the WebUI enabled?")
	