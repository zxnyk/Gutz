import subprocess
from pathlib import Path

## Running on WSL2

def get_windows_user_home():
    try:
        username_bytes = subprocess.check_output("cmd.exe /c echo %USERNAME%", shell=True)
        windows_user = username_bytes.decode('utf-8').strip()

        windows_home = Path(f"/mnt/c/Users/{windows_user}")

        return windows_home
    
    except Exception as e:
        print("Error: Could not run 'cmd.exe'. Are you running this script inside WSL?")
        return None



def find_media_dirs():
        windows_home = get_windows_user_home()
        if not windows_home:
            print("Error: Could not find Windows home directory.")
            return None, None
        
        movie_dir = windows_home / "Documents" / "Films"
        movie_dir.mkdir(parents=True, exist_ok=True)

        tv_dir = windows_home / "Documents" / "TV Shows"
        tv_dir.mkdir(parents=True, exist_ok=True)

        return movie_dir, tv_dir


def list_file(file_path):
    print(f"\nContents of {file_path}:")
    for item in file_path.iterdir():
        if item.is_file():
            print(f"  [File] {item.name}")
        elif item.is_dir():
            print(f"  [Dir]  {item.name}")
    return

if __name__ == "__main__":
    
    saved_file_path = find_media_dirs()
    if saved_file_path:
        directory_to_list = saved_file_path.parent
        list_file(directory_to_list)
