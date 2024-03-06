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

'''
u need now to set goals for yours asking steps and if they need more or less
'''

avgsteps = 0
avgdistance = 0
count = 0

for key, value in result.items():
    timestamp_string = key
    dt_obj = datetime.fromtimestamp(int(timestamp_string))
    print("date_time:",dt_obj.strftime('%m-%d'))
    
    if int(value['steps']) > 0 :
        x1.append(dt_obj.strftime('%m-%d'))
        y1.append(int(value['steps']))
        
        avgsteps = avgsteps + int(value['steps']) 
        count += 1

avgsteps = avgsteps/count   
        
plt.plot(x1,y1)
plt.title("Steps " + str(round(avgsteps)))   
plt.suptitle("Step Counter")
plt.show()
    
user_input = int(input("do you want to see your distance travel if yes press 1.if you want time press 2 and if both press 3"))

for key, value in result.items():
    if user_input == 1:
        timestamp_string = key
        dt_obj = datetime.fromtimestamp(int(timestamp_string))
        print("date_time:",dt_obj.strftime('%m-%d'))
        
        if int(value['distance']) > 0 :
            x2.append(dt_obj.strftime('%m-%d'))
            y2.append(int(value['distance']))
                
            avgdistance = avgdistance + int(value['distance'])
            
        print(avgdistance)
        print(count)
        #avgdistance = round(((avgdistance/count)/100), 2)
        
        plt.plot(x2,y2)
        plt.title("Distance " + str(avgdistance/count))
    elif user_input == 2:
        timestamp_string = key
        dt_obj = datetime.fromtimestamp(int(timestamp_string))
        print("date_time:",dt_obj)
         
        if int(value['steps']) > 0 :
            x3.append(str(dt_obj.time()))
            y3.append(int(value['steps']))
            
        plt.plot(x3,y3)
        plt.title("Time")
    elif user_input == 3:
        timestamp_string = key
        dt_obj = datetime.fromtimestamp(int(timestamp_string))
        print("date_time:",dt_obj.strftime('%m-%d'))
        
        if int(value['distance']) > 0 :
            x2.append(dt_obj.strftime('%m-%d'))
            y2.append(int(value['distance']))
            
            avgdistance = avgdistance + int(value['distance']) 
        
        avgdistance = avgdistance/count
        plt.subplot(2, 1, 1)
        plt.plot(x2,y2)
        plt.title("Distance " + str(avgdistance))
        
        dt_obj = datetime.fromtimestamp(int(timestamp_string))
        print("date_time:",dt_obj)
         
        if int(value['steps']) > 0 :
            x3.append(str(dt_obj.time()))
            y3.append(int(value['steps']))
            
        plt.subplot(2, 1, 2)
        plt.plot(x3,y3)
        plt.title("Time")
    
        
plt.suptitle("Step Counter")
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
