import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("[!] Error: API Key not found. Please set OPENWEATHER_API_KEY in your .env file.")
    sys.exit(1)
base_url = "https://api.openweathermap.org/data/2.5/weather"
my_cities = []

def get_data(city):
    # Get weather from web
    try:
        url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 401:
            print(f"[!] API Key not yet active. Using MOCK data for '{city}'.")
            return {
                "name": city,
                "main": {"temp": 25.5},
                "weather": [{"description": "sunny (mock)"}]
            }
        else:
            print(f"[!] API Error {res.status_code}: {res.text}")
            print("Something went wrong or city not found")
            return None
    except Exception as e:
        print(f"[!] Exception occurred: {e}")
        return None

# Main program
while True:
    print("\n1. Search City")
    print("2. Add to Favourites")
    print("3. Show Favourites")
    print("4. Quit")
    
    choice = input("Pick a number: ")
    
    if choice == "1":
        c = input("City name: ").strip()
        if not c:
            print("City name cannot be empty.")
            continue
        print(f"Searching for '{c}'...")
        w = get_data(c)
        if w:
            print(f"Weather in {w['name']}:")
            print(f"Temp: {w['main']['temp']} C")
            print(f"Desc: {w['weather'][0]['description']}")

    elif choice == "2":
        c = input("City to add: ")
        my_cities.append(c)
        print("Added!")

    elif choice == "3":
        print("My Cities:")
        for c in my_cities:
            w = get_data(c)
            if w:
                print(f"{c}: {w['main']['temp']} C")
            else:
                print(f"{c}: Error")

    elif choice == "4":
        print("Bye!")
        break