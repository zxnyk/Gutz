import subprocess
from pathlib import Path

## Running on WSL2

def find_dir():
    try:
        username_bytes = subprocess.check_output("cmd.exe /c echo %USERNAME%", shell=True)
        windows_user = username_bytes.decode('utf-8').strip()

        windows_home = Path(f"/mnt/c/Users/{windows_user}")
        save_dir = windows_home / "Documents" / "Films"
        save_dir.mkdir(parents=True, exist_ok=True)

        file_path = save_dir / "my_film_list.txt"
        file_path.write_text("This is a test file for my Film folder.")

        print(f"Success! File saved to your Windows folder:")
        print(file_path)
        return file_path

    except FileNotFoundError:
        print("Error: Could not run 'cmd.exe'. Are you running this script inside WSL?")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def list_file(save_dir):
    print(f"\nContents of {save_dir}:")
    for item in save_dir.iterdir():
        if item.is_file():
            print(f"  [File] {item.name}")
        elif item.is_dir():
            print(f"  [Dir]  {item.name}")
    return

if __name__ == "__main__":
    
    saved_file_path = find_dir

    if saved_file_path:
        directory_to_list = saved_file_path.parent
        list_file(directory_to_list)
