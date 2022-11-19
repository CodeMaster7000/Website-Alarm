import time 
import webbrowser 

Set_Alarm = input("Set the website alarm in the form of H:M:S: ") 
url = input("Enter the link of the website you wish to open: ") 
Actual_Time = time.strftime("%I:%M:%S") 

while (Actual_Time != Set_Alarm): 
    print ("The time is " + Actual_Time) 
    Actual_Time = time.strftime("%I:%M:%S") 
    time.sleep(1) 
   
if (Actual_Time == Set_Alarm): 
    print ("You can see your webpage now.")
    webbrowser.open(url)
