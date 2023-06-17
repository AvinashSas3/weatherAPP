from tkinter import *
from configparser import ConfigParser
import requests
from tkinter import messagebox

'''
tkinter is a module for developing GUI in python
configparser is a module that is meant to read and write config files
requests is a module, that has to be installed using pip and is used to call and use API from other websites

API has been used from https://openweathermap.org/current, while calling the API to better understand the funtion used, refer the JSON file
'''


'''CALLING APIs'''
apiURL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}' #API call URL
apiKey = 'weather.key' #Assigning the key file to a variable
apiFile = ConfigParser() #Assigning this configparser to a variable as well
apiFile.read(apiKey) #We used config parser to read the file with our api key
api_key = apiFile['api_key']['key'] #Using the text file


'''CREATING A FUNCTION TO RETRIEVE INFORMATION AND ASSIGN VALUES'''
def weatherFind(city):
    final = requests.get(apiURL.format(city, api_key)) #If you notice the apiurl, it requires both city and apikey inorder to work and hence, we used those arguments
    if final:
        jsonFile = final.json() #retrieved the json file from the final variables api call
        city = jsonFile['name'] #if u look at the json file, the name of the city is written under the key: name
        countryName = jsonFile['sys']['country'] #Same as city
        kelvinTemp = jsonFile['main']['temp'] #The temperature in the JSON file is noted as Kelvin
        celsiusTemp = kelvinTemp - 273.15 #Temp COnversion
        farenheitTemp = (kelvinTemp-273.15) * 9/5 + 32 #Temp Conversion
        weatherEntry = jsonFile['weather'][0]['main']
        result = (city, countryName, celsiusTemp, farenheitTemp, weatherEntry)

        return result
    else:
        return messagebox.showerror('Emi ra balaraju')

'''CREATING FUNCTION TO PRINT'''
def printWeather():
    city = searchCity.get()
    weather = weatherFind(city)
    if weather:
        locationEntry['text'] = '{}, {}'.format(weather[0], weather[1]) #We are assigning values to the location, and as we can see we are using weather[0] and weather[1], which is basically 0, 1 indexs of result
        temperatureEntry['text'] = '{:.2f} C, {:.2f} F'.format(weather[2], weather[3])
        weatherEntry['text'] = weather[4]
    else:
        messagebox.showerror('Error'.format(city))

'''CREATING THE SCREEN'''
root = Tk() #assigning the module to a variable
root.title('Weather App')
root.config(background="Light Blue")
root.geometry("1280x720")

'''CREATING THE ENTRY BOX WHERE WE WOULD ADD THE PLACE'''
searchCity = StringVar() #This is to take a string as the input
enterCity = Entry(root, text= searchCity, fg="Dark Blue", font=("Ayuthaya", 30), bg="White", justify=CENTER) #Entry is used to create a box and add it  into the root variable and design everything added to the box
enterCity.place(relx=0.5, rely=0.3, anchor=CENTER) #This is used to add the enterCity to the entire project
#enterCity.pack()

'''CREATING SEARCH BUTTON'''
searchButton = Button(root, text="Click for weather", bg="Grey", font=("Ayuthaya", 20), fg="Blue", command= printWeather)
searchButton.place(relx=0.5, rely=0.4, anchor=CENTER) #Same as creating entry box
#searchButton.pack()

'''CREATING LOCATION, TEMPERATURE AND WEATHER'''
locationEntry = Label(root, text='', font=("Ayuthaya", 25, 'bold'), bg="Light Blue", fg="Blue")
locationEntry.place(relx=0.5, rely=0.5, anchor=CENTER)
temperatureEntry = Label(root, text='', font=("Ayuthaya", 25, 'bold'), bg="Light Blue", fg="Blue")
temperatureEntry.place(relx=0.5, rely=0.55, anchor=CENTER)
weatherEntry = Label(root, text='', font=("Ayuthaya", 25, 'bold'), bg="Light Blue", fg="Blue")
weatherEntry.place(relx=0.5, rely=0.6, anchor=CENTER)




root.mainloop() #this is to launch or run the variable/screen

