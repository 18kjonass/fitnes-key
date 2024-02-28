import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/fitnes-key-main/fitnes-key-main/computer-science-fitnes-firebase-adminsdk-lm0a4-65b841b747.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://computer-science-fitnes-default-rtdb.europe-west1.firebasedatabase.app/'})
user_name = input('enter your name')
ref = db.reference('/')
ref = ref.child('users/'+ user_name)

  
result = ref.get()
print(type(result))

for key, value in result.items():
    print(value)