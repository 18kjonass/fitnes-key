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

date = []
steps = []
distance = []



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
        date.append(dt_obj.strftime('%m-%d'))
        steps.append(int(value['steps']))
        distance.append((int(value['distance'])/100))
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
    
age = int(input("what is your age ?"))



if age < 18:
    if 6000 > round(avgsteps):
        if 6000 > steps[-1]:
            print("The model indicates you are under preforming in your average daily steps and need to put in more steps for your age.\nAt this rate you will only average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing will suffer. if you were to do more steps you will begin to see an improvment.")
        elif 6000 <= steps[-1]:
            print("The model indicates that your average steps is under preforming but if you keep going as your going incressing your steps you will reach " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing is suffering but you are impoving. If you were to do more steps you will begin to see an improvment.")
    elif 6000 < round(avgsteps):
        if 6000 > steps[-1]:
            print("The model indicates you are doing very well in your steps but your are slowly droping this maybe that you may need a break if you keep going like this you will reach on average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well but may need a few days of rest to improve your wellbeing.")
        elif 6000 <= steps[-1]:
            print("The model indicates you are doing very well and if you keep going like this you average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well and if you keep this up you will end up doing a lot better keep it up.")

elif age >= 18 and age < 65:    
    if 10000 > round(avgsteps):
        if 10000 > steps[-1]:
            print("The model indicates you are under preforming in your average daily steps and need to put in more steps for your age.\nAt this rate you will only average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing will suffer. if you were to do more steps you will begin to see an improvment.")
        elif 10000 <= steps[-1]:
            print("The model indicates that your average steps is under preforming but if you keep going as your going incressing your steps you will reach " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing is suffering but you are impoving. If you were to do more steps you will begin to see an improvment.")
    elif 10000 < round(avgsteps):
        if 10000 > steps[-1]:
            print("The model indicates you are doing very well in your steps but your are slowly droping this maybe that you may need a break if you keep going like this you will reach on average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well but may need a few days of rest to improve your wellbeing.")
        elif 10000 <= steps[-1]:
            print("The model indicates you are doing very well and if you keep going like this you average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well and if you keep this up you will end up doing a lot better keep it up.")

elif age >= 65:
    
    if 3000 > round(avgsteps):
        if 3000 > steps[-1]:
            print("The model indicates you are under preforming in your average daily steps and need to put in more steps for your age.\nAt this rate you will only average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing will suffer. if you were to do more steps you will begin to see an improvment.")
        elif 3000 <= steps[-1]:
            print("The model indicates that your average steps is under preforming but if you keep going as your going incressing your steps you will reach " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nOver all your physical wellbeing is suffering but you are impoving. If you were to do more steps you will begin to see an improvment.")
    elif 3000 < round(avgsteps):
        if 3000 > steps[-1]:
            print("The model indicates you are doing very well in your steps but your are slowly droping this maybe that you may need a break if you keep going like this you will reach on average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well but may need a few days of rest to improve your wellbeing.")
        elif 3000 <= steps[-1]:
            print("The model indicates you are doing very well and if you keep going like this you average " + str(round(((round(avgsteps))+(steps[-1]*30)/count)/30)) + " in the next 30 days.\nYou are doing physical well and if you keep this up you will end up doing a lot better keep it up.")
    
plt.plot(date,steps)
plt.title("Steps " + str(round(avgsteps)))   
plt.suptitle("Step Counter")
plt.show()
    
user_input = int(input("If you want to see your average distance travel press 1.\nIf you want to see your average time press 2.\nIf you want to see both press 3."))
#cheacks if they want to display time or distance or both
if user_input == 1:
    plt.plot(date,distance)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))
    print("The model indicatesif you want to want to incress your distance travel it would be reocmmended to run a set time like 1 hour and try to run as far as you can.\nYour average distance is " + str(round(((avgdistance/count)/100), 2)) +" meters which can always improve if you go out everyday and try to run more than the average which will improve your physical wellbeing.")
elif user_input == 2: 
    plt.bar(date,minute)
    plt.title("Time " + str(round((avgtime/len(individualtimes))/60,3)))
    print("The model indicates if you want to want to decress your time travel it would be reocmmended to run a set distance like 1 km and try to run as fast as you can.\nYour average time is " + str(round((avgtime/len(individualtimes))/60,3)) +" minutes which can always improve if you go out everyday and try to run less than the average which will improve your physical wellbeing.")
elif user_input == 3:
    plt.subplot(2, 1, 1)
    plt.plot(date,distance)
    plt.title("Distance " + str(round(((avgdistance/count)/100), 2)))
     
    plt.subplot(2, 1, 2)
    plt.bar(date,minute)
    plt.title("Time " + str(round((avgtime/len(individualtimes))/60,3)))
    print("The model indicates this is where you compare the 2 data sets to see if your improveing.\nIf you want distance try to keep the time chart as equal as possible but if your trying to improve time try to keep the distance chat as stright as possible to get good results.\nYou should see a great impovement over a large peroid of time in your physical wellbeing.")
      
plt.show()
