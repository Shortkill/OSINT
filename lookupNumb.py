import requests
import sys

def lookup_phone(number):
    api_key = "78b2142e2d6dd8c449cf0840bc206c9a"
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={number}"
    response = requests.get(url)
    data = response.json()
    
    if data['valid']:
        print(f"Nomor Telepon: {data['number']}")
        print(f"Negara: {data['country_name']}")
        print(f"Provider: {data['carrier']}")
    else:
        print("Nomor telepon tidak valid.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Harap masukkan nomor telepon untuk pencarian.")
    else:
        number = sys.argv[1]
        lookup_phone(number)
