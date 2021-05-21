import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')

engine.setProperty("voice",voices[2].id)
def speak(audio):
     engine.say(audio)
     engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good moring prabesh!")
    elif hour>=12 and hour<18:
        speak("Good evening prabesh!")
    else:
        speak("good evening prabesh!")
    speak("I am anup,Please tell me how may I help you")
def take_cmd():
    """it takes microphone input from user and returns string as output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language="en-us")
        print(f"User said:{query}\n")
    except Exception as E:
        #print(E)


        print("Say that again..")
        return "None"
    return query






if __name__=='__main__':
    wishme()
    while True:
        query=take_cmd().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to me")
            speak(results)
        elif "open youtube" in query:
            speak("opening youtube....")
            webbrowser.open("youtube.com")
        elif "time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {time}')









