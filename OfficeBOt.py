
import PySimpleGUI as sg
from tkinter.constants import TRUE
import datetime
import time
import requests
import json
import smtplib
import bs4
import wikipedia
import webbrowser
import nutrition
from tkinter import*
from random import choice
from random import randint

a = Tk()


def Weather(timeing):
    try:
        with open("Jarinfo.json") as f:
            contents = json.load(f)
            key = contents["OpenWeatherKey"]
            Place = contents["City"]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + Place + "&APPID=" + key + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temp = current_temperature
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(timeing + Place + ":")
            print(" Temperature (Celsius) = " + str(current_temp) +
                  "\n Humidity (Percentage) = " + str(current_humidiy) + "\n Description = " + str(weather_description))
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER GETS WEATHER REPORT!!!) \n")
            Audfile.close()
        else:
            print("BOT: Please check your city in the settings as this is invalid.")
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER'S CITY IS INVALID!!!) \n")
            Audfile.close()
    except:
        print("BOT: I am having a problem in getting live weather please check your internet-connection.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(CONNECTION FAILED WITH OPENWEATHERMAP.ORG!!!) \n")
        Audfile.close()


def stocks(tickers):
    # Apple, Microsoft and the S&P500 index.
    # tickers = ['AAPL', 'MSFT', '^GSPC']
    try:
        tickers = tickers.upper()
        link = 'https://finance.yahoo.com/quote/'+tickers+'?p='+tickers
        url = requests.get(link)
        soup = bs4.BeautifulSoup(url.text, features="html.parser")
        price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
            0].find('span').text
        print("Current pricing of Stock for "+tickers+" is: "+price)
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(USER GETS STOCK PRICES FOR "+ tickers +"!!!) \n")
        Audfile.close()
    except:
        print("BOT: I am having a problem in getting Stock Prices please check your internet-connection")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(CONNECTION FAILED TO GET STOCK PRICES!!!) \n")
        Audfile.close()



def send_an_email(from_address, to_address, subject, message_text, password):
    try:
        jarvis_mail = '\n \n \n \n                                                        ---This message was sent to you by BOT  :-)'
        full_message = "{0} {1}".format(message_text, jarvis_mail)
        email_message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (from_address, to_address, subject, full_message)
        # Use port 587 or 465 using SMTP_SSL
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()    # start TLS for security
        s.login(from_address, password)    # Authentication to your account
        s.sendmail(from_address, to_address,
                   email_message)    # sending the email
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(USER SUCCESSFULLY SENT AN EMAIL!!!) \n")
        Audfile.close()
        s.quit()    # terminating the session
    except:
        sg.popup("Please check your internet connection and have turned 'on' Less secure app access in 'security' section in your Google Account Settings.")
        Audfile = open("Jaraudit.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(
            querytime + "-(USER FAILED TO SEND AN EMAIL!!!) \n")
        Audfile.close()

def gmail():
    sg.theme('Dark')
    layout = [[sg.Text('Send an Email', font='Default 15')],
              [sg.T('From:', size=(8, 1)), sg.Input(
                  key='-EMAIL FROM-', size=(35, 1))],
              [sg.T('To:', size=(8, 1)), sg.Input(
                  key='-EMAIL TO-', size=(35, 1))],
              [sg.T('Subject:', size=(8, 1)), sg.Input(
                  key='-EMAIL SUBJECT-', size=(35, 1))],
              [sg.T('Mail login information', font='Default 14')],
              [sg.T('Password:', size=(8, 1)), sg.Input(
                  password_char='*', key='-PASSWORD-', size=(35, 1))],
              [sg.Multiline('Type your message here',
                            size=(44, 10), key='-EMAIL TEXT-')],
              [sg.Button('Send')]]
    window = sg.Window('Send An Email', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Discard'):
            break
        if event == 'Send':
            send_an_email(from_address=values['-EMAIL FROM-'],
                          to_address=values['-EMAIL TO-'],
                          subject=values['-EMAIL SUBJECT-'],
                          message_text=values['-EMAIL TEXT-'],
                          password=values['-PASSWORD-'])
            continue
        window.close()
        event = window.read()
        return event != 'OK'


with open("Jarinfo.json") as f:
    contents = json.load(f)
    LoadOutput = contents["Outputscreensize"]
    LoadInput = contents["Inputbarsize"]
sg.theme('DarkBlack')  # gives window a spiffy set of colors
sg.set_options(element_padding=(3,3))

layout = [
          [sg.Text('BOT', size=(135, 1))],
          [sg.Output(size=(LoadOutput, 40), font=('Times 14'))],
          [sg.Multiline(size=(LoadInput, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('ENTER',size=(11,2), bind_return_key=True)]]

window = sg.Window('BOT', layout, location=(10,10), font=(
    'Helvetica', ' 13'), default_button_element_size=(10, 4)).Finalize()
window.maximize()

print("BOT: Welcome")
Audfile = open("Jaraudit.txt", "a")
querytime = (datetime.datetime.now().ctime())
Audfile.writelines(querytime + "-(USER ACTIVATED BOT AND INITIALIZED RELATED PROCESSES!!!) \n")
Audfile.close()

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    timeing = "BOT: Good morning, here is the current weather in "
    Weather(timeing)
    #Breifing('Morning Briefing', 'Morning News Headlines')
elif hour >= 12 and hour < 18:
    timeing = "BOT: Good afternoon, here is the current weather in "
    Weather(timeing)
else:
    timeing = "BOT: Good evening, here is the current weather in "
    Weather(timeing)

if __name__ == '__main__':
    while True:     # The Infinity Event Loop
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # quit if exit button or X
            if hour>= 18:
                print("\n BOT: Office time is up! You should rest now!")
            
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(USER TERMINATED BOT AND ALL IT'S RELATED PROCESSES!!!) \n")
            Audfile.close()
            print("\nBOT: Goodby0:-)")
            time.sleep(4)
            break

        if event == 'ENTER':
            # THE START OF THE RENDER-WORD ENGINE (C) Epicalable
            que = value['-QUERY-'].rstrip()  # Your input here
            query = (que.upper())
            Audfile = open("Jaraudit.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            str = (querytime + ": " + que.capitalize() + "\n")
            Audfile.write(str)
            with open("Jarinfo.json") as f:
                contents = json.load(f)
                User = contents["User"]
                print("\n" + User + ": {}".format(que.capitalize()))
                with open("Jarintents.json") as f:
                    data = json.load(f)
                    for word in data['intents']:
                        if word['tags'] in query:
                            print(choice(word["response"]))
                            break
                    # THE END OF THE RENDER-WORD ENGINE (C) Epicalable
                    else:
                        if "DATE" in query or "TIME" in query:
                            x = datetime.datetime.now()
                            print("BOT: The Date and Time is ",x," respectively.")
                            continue

                        if "DAY" in query or "YEAR" in query:
                            x = datetime.datetime.now()
                            print("BOT: The Date and Time is ",x," respectively.")
                            continue

                        elif "WIKIPEDIA" in query or "WIKI" in query:
                            query = query.replace('WIKI', "")
                            query = query.replace('WIKIPEDIA', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "BOT: I am having a problem in getting wikipedia please check your internet-connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION FAILED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "WHAT IS" in query or "WHO IS" in query:
                            query = query.replace('WHAT', "")
                            query = query.replace('IS', "")

                            query = query.replace('WHO', "")
                            query = query.replace('IS', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "BOT: I am having a problem in getting wikipedia please check your internet-connection")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(CONNECTION FAILED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "NEWS ABOUT" in query or "NEWS ON" in query:
                            query = query.replace('NEWS ', "")
                            query = query.replace('ABOUT ', "")
                            query = query.replace('ON ', "")
                            try:
                                with open("Jarinfo.json") as f:
                                    contents = json.load(f)
                                    JNews = contents["NewsApiKey"]
                                headers = {'Authorization': JNews}
                                everything_news_url = 'https://newsapi.org/v2/everything'
                                everything_payload = {
                                    'q': query, 'language': 'en', 'sortBy': 'publishedAt'}
                                open_news_page = requests.get(
                                    url=everything_news_url, headers=headers, params=everything_payload).json()
                                article = open_news_page["articles"]
                                results = []
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                for ar in article:
                                    results.append(ar["title"])
                                for i in range(len(results)):
                                    print(i + 1,'.', results[i])
                            except:
                                print(
                                    "BOT: Something went wrong please check if you have a good internet connection.")
                                Audfile = open("Jaraudit.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(CONNECTION FAILED WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                continue

                
                        
                        elif "STOCKS" in query or "STOCK PRICE" in query:
                            query = query.replace('GET ME ', "")
                            query = query.replace('PRICE ', "")
                            query = query.replace('PRICES ', "")
                            query = query.replace('STOCK ', "")
                            query = query.replace('STOCKS ', "")
                            query = query.replace('FOR ', "")
                            query = query.replace('ON ', "")
                            stocks(tickers=query.upper())

                        elif "SEND AN EMAIL" in query or "SEND A EMAIL" in query or "SEND EMAIL" in query or "SEND MESSAGE" in query:
                            gmail()

                        elif query == "GOODBYE" or query == "BYE" or query =="BYE BYE":
                            Audfile = open("Jaraudit.txt", "a")
                            querytime = (datetime.datetime.now().ctime())
                            Audfile.writelines(querytime + "-(USER TERMINATED BOT AND ALL IT'S RELATED PROCESSES!!!) \n")
                            Audfile.close()
                            print("Have a great day ahead")
                            time.sleep(4)
                            break
                        # elif "DIET" in query or "NUTRITION" in query or "MEAL" in query:
                        #     print("Generate your nutrition plan!")
                        #     nutrition.nutritionwindow()
                        #     print("Completed!")

                        else:
                            print(
                                "BOT: I did not understand you, as you can see i am still evolving :-)")
                            Audfile = open("Jaraudit.txt", "a")  
                            Audfile.write("ERROR 404 (FALLBACK)!!! \n")
                            Audfile.close()


       


window.close()

