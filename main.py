import requests
import smtplib
import schedule
from bs4 import BeautifulSoup

def umbrella_reminder():
    city="Gurugram"
    #url created, instance requested
    url='https://google.com/search?q='+"weather"+city
    html=requests.get(url).content
    
    #retrieving raw data
    soup=BeautifulSoup(html,'html.parser')

    temperature=soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky=soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    #format
    sky = time_sky.split('\n')[1]

    if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy": 
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587) #Google SMTP Server
          
        # start TLS for security 
        smtp_object.starttls()

        # Authentication 
        smtp_object.login("YOUR EMAIL", "PASSWORD") 
        subject = "Umbrella Reminder!"
        body = f"Take an umbrella before leaving the house.\ 
        Weather condition for today is {sky} and temperature is\ 
        {temperature} in {city}." 
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nsimratanand".encode( 
            'utf-8') 
          
        # sending the mail 
        smtp_object.sendmail("FROM EMAIL", 
                             "TO EMAIL", msg) 
          
        # terminating the session 
        smtp_object.quit() 
        print("Email Sent!") 

# Every day at 08:00AM time umbrellaReminder() is called. 
schedule.every().day.at("08:00").do(umbrella_reminder) 

while True: 
    schedule.run_pending()