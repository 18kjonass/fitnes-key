import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/18KJonass.ACC/Downloads/fitnes-key-main/fitnes-key-main/computer-science-fitnes-firebase-adminsdk-lm0a4-65b841b747.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://computer-science-fitnes-default-rtdb.europe-west1.firebasedatabase.app/'})
name = input('Enter your name')
ref = db.reference('/')
ref = ref.child('users/'+name)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.timeout = 0.002
ser.bytesize = 8
ser.stopbits = 1
ser.open()

oneByteTime = 1 / (ser.baudrate / (ser.bytesize + 2 + ser.stopbits)) # 1 byte u
buffer = b''
t = 0
firstdata= 0
seconddata= 1
thirddata= 2
fourthdata= 3
while True:
    try:
        length = max(1, ser.in_waiting)
        data = ser.read(length)
        if data:
            t = time.time()
            if length == 1 and not buffer: # just start receive
                buffer += data
                continue
            buffer += data
        if buffer and (time.time() - t > oneByteTime*250 ): # no new data in next frame
            try:
                print(buffer.decode())
                s = buffer.decode().strip()
                numbersdata = s.split('+')
                ref.update({str(int(time.time())):{
                                                'height':numbersdata[firstdata],
                                                'stride':numbersdata[seconddata],
                                                'distance':numbersdata[thirddata],
                                                'steps':numbersdata[fourthdata],
                                                }
                            })

                #print(oneByteTime*250)
            except Exception as e:
                print("-- error in buffer read:", e)
            buffer = b''
    except Exception as e:
       
            try:
                ser.close()
            except Exception:
                pass
