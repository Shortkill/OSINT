#!/bin/bash

echo "===== OSINT Tools Menu ====="
echo "Pilih metode pencarian:"
echo "1. cari berdasarkan nama "
echo "2. Cari username sosial media"
echo "3. Cari berdasarkan nomor telepon"
echo "4. Keluar"
echo -n "Masukkan pilihan (1/2/3/4): "
read choice

case $choice in
    1)
        echo -n "Masukkan nama untuk pencarian: "
        read name
        python3 name_search.py "$name"
        ;;
    2)
        echo -n "Masukkan username sosial media untuk pencarian: "
        read username
        python3 check_username.py "$username"
        ;;
    3)
        echo -n "Masukkan nomor telepon untuk pencarian: "
        read number
        python3 lookup_phone.py "$number"
        ;;
    4)
        echo "Keluar dari OSINT Tools."
        exit 0
        ;;
    *)
        echo "Pilihan tidak valid!"
        ;;
esac
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
