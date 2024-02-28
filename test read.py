import time
import firebase_admin
import serial


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
                #print(oneByteTime*250)
            except Exception as e:
                print("-- error in onReceived callback:", e)
            buffer = b''
    except Exception as e:
       
            try:
                ser.close()
            except Exception:
                pass
