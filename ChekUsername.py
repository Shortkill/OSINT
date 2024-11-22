import requests
import sys

def check_username(username):
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}"
    }
    
    for platform, url in platforms.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{platform}: Username ditemukan ({url})")
        else:
            print(f"{platform}: Username tidak ditemukan")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Harap masukkan username untuk pencarian.")
    else:
        username = sys.argv[1]
        check_username(username)
