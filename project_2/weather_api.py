
import requests    
key="df6c3f0ecdcf83a6a28775d9b3cc996a"
choice="https://api.openweathermap.org/data/2.5/weather?q="
user_input=input("Enter Your City Name:")
cloudy=choice+user_input+"&appid="+key
response=requests.get(cloudy)    
if(response.status_code==200):
    use=(response.json())
    use1=use['main']['temp']
    temp=use1-273.15
    temp1=format(temp,".2f")
    print("Temperature in "+user_input+" is "+temp1+chr(176)+"c")
    print("Everyting print well")
else:
    print("Please put the correct city name!")
    

