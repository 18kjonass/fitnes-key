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

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []


for key, value in result.items():
   #print(value)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    print("date_time:",dt_obj.strftime('%m-%d'))
    
    x1.append(dt_obj.strftime('%m-%d'))
    y1.append(int(value['steps']))
    
    plt.subplot(3, 1, 1)
    plt.plot(x1,y1)
    plt.title("Step Counter")
   
'''
  
for key, value in result.items():
   #print(value)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    print("date_time:",dt_obj)
    
    x2.append(dt_obj)
    y2.append(int(value['distance']))
    
    plt.subplot(3, 1, 2)
    plt.plot(x2,y2)

for key, value in result.items():
   #print(value)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    print("date_time:",dt_obj)
    
    x3.append(str(dt_obj.time()))
    y3.append(int(value['steps']))
    
    plt.subplot(3, 1, 3)
    plt.plot(x3,y3)
'''

plt.show()

'''
    print("type of dt:",type(dt_obj))
    print(timestamp_string)
    format_string = "%Y-%m-%d %H:%M:%S"
    datetime_object = datetime.strptime(timestamp_string, format_string)
    print(datetime_object)
'''



'''
# plot
fig, ax = plt.subplots()
fig, bx = plt.subplots()
fig, cx = plt.subplots()

plt.title("Step Counter")

plt.x1label("Dates")
plt.y1label("Steps")

plt.x2label("Dates")
plt.y2label("Distance")

plt.x3label("Time")
plt.y3label("Steps")



ax.plot(x1, y1, linewidth=2.0)
bx.plot(x2, y2, linewidth=2.0)
cx.plot(x3, y3, linewidth=2.0)

plt.show()
'''