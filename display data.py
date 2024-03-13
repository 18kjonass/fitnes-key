import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/fitnes-key-main (1)/fitnes-key-main/computer-science-fitnes-firebase-adminsdk-lm0a4-65b841b747.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://computer-science-fitnes-default-rtdb.europe-west1.firebasedatabase.app/'})
user_name = input('enter your name')
ref = db.reference('/')
ref = ref.child('users/'+ user_name)
  
result = ref.get()

x = []
y1 = []
y2 = []



avgsteps = 0
avgdistance = 0
count = 0
Dtime = []
individualtimes = []
timehms = []
avgtime = 0

age = input("what is your age ?")

agesteps = 0

if age > 18:
    

for key, value in result.items():
  #puts the times in a list
    Dtime.append(key)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    #cheaks if the key is a start or end time and adds the values to a list
    if int(value['steps']) > 0 :
        x.append(dt_obj.strftime('%m-%d'))
        y1.append(int(value['steps']))
        y2.append((int(value['distance'])/100))
        avgdistance = avgdistance + int(value['distance'])
        avgsteps = avgsteps + int(value['steps']) 
        count += 1

timecount = len(Dtime)
avgsteps = avgsteps/count
#gets the individualtimes and sorts them
for i in range(0,timecount-1,2):
    individualtimes.append(int(Dtime[i+1])-int(Dtime[i]))

t = 0
avgtime = 0
while t < len(individualtimes):
    avgtime = avgtime + individualtimes[t]
    t += 1   
    
#puts the keys to times
realtime = []
m = 0
minute = []
while m < len(individualtimes):
    realtime.append((int(individualtimes[m])/60))
    minute.append(round(realtime[m],3))
    m += 1

plt.plot(x,y1)
plt.title("Steps " + str(round(avgsteps)))   
plt.suptitle("Step Counter")
plt.show()
    
user_input = int(input("if you want to see your average distance travel press 1. if you want to see your average time press 2. if you want to see both press 3"))
#cheacks if they want to display time or distance or both
if user_input == 1:
    plt.plot(x,y2)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))  
elif user_input == 2: 
    plt.bar(x,minute)
    plt.title("Time" + str(round((avgtime/len(individualtimes))/60,3)))
elif user_input == 3:
    plt.subplot(2, 1, 1)
    plt.plot(x,y2)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))
     
    plt.subplot(2, 1, 2)
    plt.bar(x,minute)
    plt.title("Time" + str(round((avgtime/len(individualtimes))/60,3)))
      
plt.show()
