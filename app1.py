#!/usr/bin/python3

name = input('Enter the weekday')
if (name == 'Monday'or name == 'Tuesday' or name == 'wednesday' or name == 'Thursday' or name == 'Friday'):
    print ("9 to 5:30")
elif (name == "saturday"):
    print ("10 to 1")

else:
   print("Holiday")