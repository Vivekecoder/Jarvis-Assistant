import pyttsx3      # is a text-to-speech conversion library and support two voice male and female.
import speech_recognition as sr  # use speech to text to take input from the microphone and convert it into text.
import datetime
import wikipedia  # allows us to search a query supplied as an argument using the search() method.
import webbrowser # provides a high-level interface to allow displaying web-based documents to users.
import requests   # The request() method returns a response object which contains various types data such as the webpage text, status code and the reason for that response.
from bs4 import BeautifulSoup
import os
# import smtplib  # SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def GreetMe():
    print("Hello sir,I am Jarvis. Please tell me how may I help you")
    speak("Hello sir,I am Jarvis. Please tell me how may I help you")


def takeCommand():  # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening --->  ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing --->  ")
        User_Input = r.recognize_google(audio)
        print(f"Jarvis think you said:" + " " + User_Input)

    except Exception as e:
        print("Jarvis didn't understand please, Say again...")
        return "None"
    return User_Input


if __name__ == "__main__":
    GreetMe()
    while True:
        User_Input = takeCommand().lower()


        if 'hello jarvis' in User_Input:
            print(f"Hello sir, How are you sir ?")
            speak(f"Hello sir, How are you sir ?")
        elif 'i am good' in User_Input:
            print(f"that's great sir, How may I help you sir")
            speak(f"that's great sir, How may I help you sir")
        elif 'how are you' in User_Input:
            print("I am good sir ")
            speak("I am good sir ")


        elif 'wikipedia' in User_Input:
            speak('Searching Wikipedia...')
            User_Input = User_Input.replace("wikipedia", "")
            results = wikipedia.summary(User_Input, sentences=2)
            speak("According to Wikipedia")
            print("According to Wikipedia" + " " + results)
            speak(results)

        elif 'youtube' in User_Input:
            if User_Input == 'open youtube':
                webbrowser.open("youtube.com")
            else:
                f_text = "https://www.youtube.com/results?search_query=" + User_Input
                webbrowser.get(chrome_path).open(f_text)

        elif 'google' in User_Input:
            if User_Input == 'open google':
                webbrowser.open("google.com")
            else:
                f_text = "https://www.google.com/search?q=" + User_Input
                (webbrowser.get(chrome_path).open(f_text))

        elif 'play offline music ' in User_Input:
            music_dir = 'E:\\Ducat\\computer vision\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in User_Input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is : ---> " + strTime)
            speak(f"Sir, the time is {strTime}")

        elif "set an alarm" in User_Input:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "temperature" in User_Input:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ ="BNeawe").text
            print(f"current{search} is {temp}")
            speak(f"current{search} is {temp}")

        elif "weather" in User_Input:
            search = "Weather in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(f"current{search} is {temp}")
            speak(f"current{search} is {temp}")

        elif "shutdown the system" in User_Input:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                exit()



