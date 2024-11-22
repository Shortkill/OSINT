import os
import requests
import sys
from time import sleep

# Banner function
def show_banner():
    os.system("clear")
    banner = """
    ███    ███ ██████  ██     ██ ██     ██ 
    ████  ████ ██   ██ ██     ██ ██     ██ 
    ██ ████ ██ ██████  ██  █  ██ ██  █  ██ 
    ██  ██  ██ ██   ██ ██ ███ ██ ██ ███ ██ 
    ██      ██ ██████   ███ ███   ███ ███  
                Mr.W - OSINT Script
    """
    print(banner)

# Function to perform OSINT tasks
def osint_menu():
    show_banner()
    print("\n[1] Check Website Status")
    print("[2] Get IP Info")
    print("[3] Find Subdomains")
    print("[4] Exit")
    choice = input("\nChoose an option: ")

    if choice == "1":
        check_website_status()
    elif choice == "2":
        get_ip_info()
    elif choice == "3":
        find_subdomains()
    elif choice == "4":
        sys.exit()
    else:
        print("\nInvalid option! Try again.")
        sleep(2)
        osint_menu()

# Option 1: Check website status
def check_website_status():
    url = input("\nEnter website URL (e.g., https://example.com): ")
    try:
        response = requests.get(url)
        print(f"\n[+] Status Code: {response.status_code}")
    except Exception as e:
        print(f"\n[-] Error: {e}")
    input("\nPress Enter to return to the menu...")
    osint_menu()

# Option 2: Get IP information
def get_ip_info():
    ip = input("\nEnter an IP address: ")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"\n[-] Error: {e}")
    input("\nPress Enter to return to the menu...")
    osint_menu()

# Option 3: Find subdomains
def find_subdomains():
    domain = input("\nEnter the domain (e.g., example.com): ")
    try:
        print("\n[+] Finding subdomains...")
        # This is just a placeholder logic. Add your actual subdomain finding logic here.
        subdomains = [f"sub1.{domain}", f"sub2.{domain}", f"sub3.{domain}"]
        for sub in subdomains:
            print(f" - {sub}")
    except Exception as e:
        print(f"\n[-] Error: {e}")
    input("\nPress Enter to return to the menu...")
    osint_menu()

# Main function
if __name__ == "__main__":
    osint_menu()