import time, requests, pyperclip
import os
from dotenv import load_dotenv
from media_directory import find_media_dirs

load_dotenv() 

# Directories
# MOVIE_SAVE_PATH, TV_SAVE_PATH = find_media_dirs()

ITS_A_PRANK = r"C:\Users\Andrei Mayor\Documents\Films"

TV_KEYWORDS = [
    "Season", "season", "S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08",
    "s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08",
    "E01", "E02", "E03", "e01", "e02", "e03", "Complete Series"
]


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
	# print(f"Movies will be saved to: {MOVIE_SAVE_PATH}")
	# print(f"TV Shows will be saved to: {TV_SAVE_PATH}")
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
					magnet = clip.split("&dn=")[0]
					print(f"Adding: {clip[:60]}")
					s.post(f"{QBIT_URL}/api/v2/torrents/add", data={"urls": magnet, "savepath": ITS_A_PRANK})
					if s.post != 200:
						clip_prev = clip

				time.sleep(1)

	except requests.exceptions.ConnectionError:
		print(f"Connection Error: Could not connect to {QBIT_URL}.")
		print("Is qBittorrent running and is the WebUI enabled?")
	