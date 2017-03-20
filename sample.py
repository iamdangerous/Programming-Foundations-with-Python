import webbrowser
import time

timeCount = 3
print("This program starts on: "+time.ctime())
while(timeCount>0):
    time.sleep(2)
    webbrowser.open("https://jsonformatter.curiousconcept.com/")
    timeCount = timeCount-1

    
