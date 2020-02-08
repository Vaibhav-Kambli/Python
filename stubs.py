"""

Author : Vaibhav Vikas Kambli
Python script that demonstrates how you can use stubs to understand the logical flow of your program and break complex task into simple functions.
This code will help you better understand how functions in python can be used and how you can schedule events using schedule module (Python automation System).


"""
##----------------------------------------------------------------------------------
# Imports
  
import smtplib
import schedule
import times
import datetime
                            

##----------------------------------------------------------------------------------
# functions to implement specified task

def CheckServers():
    print("Check if the webservers are online")

def PlayFavouriteMusic():
    print("Play your favourite music")


def StartMachine():
          print("Start the washing machine")


def WakeUp():
          print("Time to wake up!")


def ClassReminder():
          print("You have a python class today")

def Bowling():
    print("Go to bowling!")


def SendQuote():
    print("Send an email to your favourite person with a quote from http://wisdomquotes.com/friendship-quotes/")



##----------------------------------------------------------------------------------
## schedule events

todayTime = datetime.datetime.now()

currentTime = (todayTime.strftime("%H:%M"))



schedule.every(10).minutes.do(CheckServers)

# if time between 22:00 to 07:00
if currentTime <= "22:00" <= "00:00":
    schedule.every().hour.do(PlayFavouriteMusic)


schedule.every().day.at("19:00").do(StartMachine)


schedule.every().day.at("07:30").do(WakeUp)


schedule.every().wednesday.at("08:00").do(ClassReminder)


schedule.every().friday.at("08:00").do(ClassReminder)


schedule.every().friday.at("18:00").do(Bowling)


schedule.every().day.at("07:00").do(SendQuote)

    

# loop
while True:
    schedule.run_pending()
    time.sleep(1)
