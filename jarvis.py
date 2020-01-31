import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr 
import wikipedia
import wolframalpha
import os
from selenium import webdriver
import datetime
import time
import sys
music =[]



engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('QX8979-3LEU6U6AV7')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

def speak(audio):
    print('Computer:'+ audio)
    engine.say(audio)
    engine.runAndWait()

def greetme():
    currentH = int (datetime.datetime.now().hour)
    if currentH>=0 and currentH<12:
        speak('Good Morning..!Mr Sahu')
    if currentH>=12 and currentH<18:
        speak('Good AfterNoon.. Mr Sahu')
    if currentH>=18 and currentH !=0:
        speak('Good Evening..!Mr Sahu') 

greetme()

speak("I M Jarvis,Your Assistant.... How Can I Help You Sir")



def myCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        query=r.recognize_google(audio, language='en-in')
        print('User: '+ query + "\n")
    except sr.UnknownValueError:
        speak(" Sorry Sir Can't Recognise What You Just Said,Try Typing the commands") 
        query=str(input('Command  ')) 
    return query 
if __name__ =="__main__":
    pass   
    while True:    
        query=  myCommands();
        query= query.lower()
        if 'hello jarvis how are you' in query:
            speak("I Am Always fine, What About you")
        elif 'i am good' in query:
            speak('Well I Am Glad')
        elif 'whats up jarvis, how you doing'in query:
            msg=['I am fine','Just doing my A-I Stuffs','In good mood',]
            speak(random.choice(msg))
        elif "how's the josh"in query:
            speak("Highh ,Sir")
        elif "open whatsapp" in query:
            speak("Opening whatsapp   sir!")
            driver=webdriver.Firefox()
            driver.get("https://web.whatsapp.com")
            time.sleep(20)
            speak("Please Tell the name of the person or group  sir?")
            name = myCommands();
            speak("Whats your message  sir!")
            msg= myCommands();
            user= driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            msgbox = driver.find_element_by_class_name('_3u328')
            msgbox.send_keys(msg)
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()   

           
        elif 'bye'in query:
            speak("Bye   Sir,  Have a Good Day")
            sys.exit()            
        else:
            
            try:
                try:
                    res =client.query(query)
                    results= next(res.results).text
                    
                    speak('There You Go')
                    speak(results)
                except:
                    results=wikipedia.summary(query,sentences=2)
                    speak("Got It")
                    speak('Wikipedia Says....\n')
                    speak(results)    
            except:
                webbrowser.open("www.google.com")
