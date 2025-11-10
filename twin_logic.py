import firebase_admin
from firebase_admin import credentials, db
import time, random

cred = credentials.Certificate("your-service-account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOUR_APP.firebaseio.com/'
})

print("Virtual Sensors Active... Uploading Data...\n")

while True:
    temp = round(random.uniform(25, 35), 1)
    humidity = round(random.uniform(40, 70), 1)
    db.reference('environment').set({
        'temperature': temp,
        'humidity': humidity
    })
    print(f"Updated → Temp: {temp}°C | Humidity: {humidity}%")
    time.sleep(5)
