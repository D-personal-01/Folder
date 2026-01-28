import time
h=int(time.strftime('%H'))
if h<12 and h<0:
    print ("Guten Morgan")
elif h>12 and h<15:
    print("Guten Tag")
else :
    print("Guten Abend")
