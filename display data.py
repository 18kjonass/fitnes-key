import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db
import matplotlib.pyplot as plt
#import datetime
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


'''
u need now to set goals for yours asking steps and if they need more or less
'''

avgsteps = 0
avgdistance = 0
count = 0
Dtime = []
individualtimes = []
timehms = []
avgtime = 0

for key, value in result.items():
  #puts the times in a list
    Dtime.append(key)
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    #cheaks if the key is a start or end time and adds the values to a list
    if int(value['steps']) > 0 :
        x.append(dt_obj.strftime('%m-%d'))
        y1.append(int(value['steps']))
        y2.append(int(value['distance']))
        avgdistance = avgdistance + int(value['distance'])
        avgsteps = avgsteps + int(value['steps']) 
        count += 1

timecount = len(Dtime)
avgsteps = avgsteps/count
#gets the individualtimes and sorts them
for i in range(0,timecount-1,2):
    individualtimes.append(int(Dtime[i+1])-int(Dtime[i]))
print(individualtimes)

individualtimes = [60,180,120,600] 
   
'''
avgtime = avgtime + individualtimes[seconds]
avgtime = avgtime/timecount
print(avgtime)
'''           
#puts the keys to times
realtime = []
m = 0
while m < len(individualtimes):
    realtime.append((int(individualtimes[m])/60))
    print(realtime)
    m += 1
for seconds in individualtimes:
    timehms.append(str(timedelta(seconds=seconds)))

 
            

plt.plot(x,y1)
plt.title("Steps " + str(round(avgsteps)))   
plt.suptitle("Step Counter")
plt.show()
    
user_input = int(input("do you want to see your distance travel if yes press 1.if you want time press 2 and if both press 3"))
#cheacks if they want to display time or distance or both
if user_input == 1:
    plt.plot(x,y2)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))  
elif user_input == 2: 
    plt.plot(x,realtimeb)
    plt.title("Time")
elif user_input == 3:
    plt.subplot(2, 1, 1)
    plt.plot(x,y2)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))
     
    plt.subplot(2, 1, 2)
    plt.plot(x,individualtimes)
    plt.title("Time")
      
plt.show()




