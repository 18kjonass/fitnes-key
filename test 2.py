import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
from datetime import datetime

cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/fitnes-key-main/fitnes-key-main/computer-science-fitnes-firebase-adminsdk-lm0a4-65b841b747.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://computer-science-fitnes-default-rtdb.europe-west1.firebasedatabase.app/'})
user_name = input('enter your name')
ref = db.reference('/')
ref = ref.child('users/'+ user_name)

  
result = ref.get()
print(type(result))

x = []
y = []



for key, value in result.items():
   #print(value)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    print("date_time:",dt_obj)
    
    x.append(dt_obj)
    y.append(int(value['distance']))

'''
    print("type of dt:",type(dt_obj))
    print(timestamp_string)
    format_string = "%Y-%m-%d %H:%M:%S"
    datetime_object = datetime.strptime(timestamp_string, format_string)
    print(datetime_object)
'''




# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

plt.show()
