"""
weather.py - Python script to find current temperature of any city that user enters. Developed using TkInter Python GUI

Name : Vaibhav Vikas Kambli
"""

##------------------------------------------------------------------------------------------------------------------------------------------
#imports

from tkinter import *
from tkinter import messagebox
import pyowm

##------------------------------------------------------------------------------------------------------------------------------------------

#function to find weather of any city using openweathermap api 
def tell_weather() :

    #Api key
    owm = pyowm.OWM('#insert your api key here')     #get your own API key by registering with Openweather API and insert here to make your key work

    #Degree symbol to be used later for formatting
    degree_sign = u'\N{DEGREE SIGN}'

    
    # take a city name from city_field entry box 
    city_name = city_field.get()
    

    #get weather of the place entered by the user
    observation = owm.weather_at_place(city_name)
    w = observation.get_weather()
   
    #get temperature in celsius
    celsius_temperature = w.get_temperature('celsius')['temp']

    #get temperature in fahrenheit
    temperature = w.get_temperature('fahrenheit')['temp']

   
    #insert fahrenheit temperature in fahrenheit field
    temp_field_feh.insert(15, str((f'{int(temperature)}{degree_sign}F')))

    #insert celsius symbol in temperature celsius field
    temp_field.insert(15, str((f'{int(celsius_temperature)}{degree_sign}C')))


        
##---------------------------------------------------------------------------------------------------------------------------------------------------

# Function for clearing the contents of all text entry boxes 
def clear_all() : 
    city_field.delete(0, END) 
    temp_field.delete(0, END)
    temp_field_feh.delete(0, END)
    

    # set focus on the city_field entry box 
    city_field.focus_set() 


##----------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__" : 

    # Create a GUI window 
    window = Tk() 

    # name of tkinter GUI window 
    window.title("Tkinter weather app")

   
    # Create city name label 
    label1 = Label(window, text = "City name : ")
    
    # Create temperature label 
    label2 = Label(window, text = "Temperature in Celsius:" )

    #Create temperature label
    label3 = Label(window, text= "Temperature in Fahrenheit ")

    # label position
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 3, column = 0, sticky ="E")
    label3.grid(row = 4, column = 0, sticky ="E")


    # Create text entry box  
    city_field = Entry(window) 
    temp_field = Entry(window)
    temp_field_feh = Entry(window)
    

    # entry box position
    city_field.grid(row = 1, column = 1, ipadx ="100") 
    temp_field.grid(row = 3, column = 1, ipadx ="100")
    temp_field_feh.grid(row = 4, column = 1, ipadx ="100")


    # Create Submit Button
    button1 = Button(window, text = "Get temperature", command = tell_weather) 

    # Create Clear Button
    button2 = Button(window, text = "Clear", command = clear_all) 

    # button positions
    button1.grid(row = 2, column = 1) 
    button2.grid(row = 7, column = 1) 
    
    window.mainloop() 
