import speech_recognition as sr
import time
import subprocess as sbp
import pyttsx3
import webbrowser
import datetime
import os
import pyautogui
import psutil
import pyjokes
import requests


def speak(audio):
    speak_assis = pyttsx3.init()
    speak_assis.setProperty("rate", 175)
    voices = speak_assis.getProperty("voices")
    speak_assis.setProperty("voice", voices[0].id)
    speak_assis.say(audio)
    speak_assis.runAndWait()


def recog():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        recog_resl = r.recognize_google(audio, language="en-in")
    except Exception as e:
        pass
    try:
        return recog_resl
    except UnboundLocalError:
        pass


def tell_jokes():
    speak(pyjokes.get_joke())


def created():
    speak("I was created by chandigarh university students")


def browse_net():
    speak("Which site you want to Browse")
    try:
        bs = recog().lower()
        speak("Do you want me to search on google or it is site.")
        try:
            gg = recog().lower()
        except Exception:
            pass
        if "google" in gg:
            speak("Opening " + bs)
            webbrowser.get(
                "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            ).open("https://www.google.com/search?q=" + bs)
            pass
        elif "site" in gg:
            speak("Opening " + bs)
            webbrowser.get(
                "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            ).open(bs+".com")
            pass
    except Exception:
        pass


def can_do():
    speak("Search anything on Internet, Just say browse")
    speak("Read your last book, just say Please read me the last book")
    speak("I can take screenshots and even switch window")
    speak("I can also launch prime music as well as prime video")
    speak("I can tell cpu usage and battery percentage")
    speak("I can Launch Netflix, Just say movie time")
    speak("And I am learning!")


def read_book():
    speak("Do you want me the read last book, which you were reading in chrome")

    try:
        dk = recog().lower()
    except Exception:
        speak("Sorry I can't hear you,")
        pass
    time.sleep(0.15)
    if "yes" in dk:
        sbp.call(["python", "pdf_read.py"])


def weather(city):
    r = requests.get(f"https://wttr.in/{city}?format=j1")
    weather = r.json()["current_condition"][0]["weatherDesc"][0]["value"]
    temp = r.json()["current_condition"][0]["temp_C"]
    speak("Today's weather in chandigarh: " + weather)
    speak("Current Temperature: " + temp + " degree celsius")


def cityName():
    city = "Chandigarh"
    return city


def greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon sir!")
    elif hour >= 16 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("advik at your service sir!")


def screenshot():
    pyautogui.hotkey("win", "prntscrn")


def power_cpu():
    usage = str(psutil.cpu_percent())
    speak("Current cpu usage is " + usage)

    battery = psutil.sensors_battery()
    speak("Current Battery percentage is")
    speak(battery.percent)


def switchwindow():
    pyautogui.hotkey("alt", "tab")


def cca():
    pyautogui.hotkey("alt", "f4")


def info():
    speak("Well, Hello I'm advik")
    speak("And I was created by Chandigarh university")
    speak("Currently my verison is 3.6")
    speak("And I am Learning")


def tasks_do(task):
    try:
        if "youtube" in task:
            speak("Opening youtube")
            webbrowser.get(
                "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            ).open("youtube.com")
        elif "logout" in task:
            os.system("shutdown -l")

        elif "shutdown" in task:
            os.system("shutdown /s /t 1")

        elif "restart" in task:
            os.system("shutdown /r /t 1")

        elif "created" in task:
            created()

        elif "battery" in task:
            power_cpu()

        elif "joke" in task:
            tell_jokes()

        elif "weather" in task:
            city = cityName()
            weather(city)

        elif "close" in task:
            cca()
        elif "screenshot" in task:
            screenshot()

        elif "about" in task:
            info()
        elif "switch" in task:
            switchwindow()
        elif "browse" in task:
            browse_net()
        elif "can do" or "Can you do" in task:
            can_do()
        elif "book" in task:
            read_book()
        elif "quit" in task:
            exit()
        else:
            speak("I'm afraid I can't do that right now, But I'm learning")
            pass
    except Exception:
        pass

if __name__ == '__main__':
    greet()
    try:
        print("\nListening....")
        query = recog()
        query = query.lower()
        print(query)
        tasks_do(query)
    except Exception:
        print("I can't hear you")
    
    
