from machine import Pin, UART
# For serial output from SR04-M2 waterproof ultrasonic sensor
#Converted from C prog by:
# https://wolles-elektronikkiste.de/hc-sr04-und-jsn-sr04t-2-0-abstandssensoren
#in his article there is a 4k7 resistor at the jumper near the two electrolytics

uart = UART(0,baudrate = 9600,rx = Pin(17),tx = Pin(16))


def getDistance():

    buf = uart.read()
    if buf[0]  != 255:
        return
        print('ok32')

        h_data = buf[0]
        l_data = buf[1]
        c_sum = buf[2]
        distance = (h_data<<8) + l_data

      # if(((startByte + h_data + l_data)&0xFF) != c_sum):
     #   print("Invalid result")    
      #  else:
        print("Distance [mm]: ",distance)
       # else:
    return

def simple():

    buf = uart.read()
    if buf[0]  != 255:
        return
    c_sum = buf[3]
    calc_csum = (buf[1] + buf[2] + 255) & 255
    if c_sum == calc_csum:
        distance = (buf[1] <<8) + buf[2]
        if distance != 6000:
            print('Distance',distance)
    
        #print(buf,c_sum,calc_csum)

    
while True:
  if uart.any():
    simple()


