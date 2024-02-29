import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt

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
    x.append(key)
    y.append(value['distance'])
    

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)


plt.show()
