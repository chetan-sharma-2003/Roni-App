from tkinter import *
from PIL import ImageTk,Image
import pyttsx3, speech_recognition as sr, datetime,pywhatkit,webbrowser,wikipedia,pyjokes
import random
	
window = Tk()

window.title("Roni Assistant")
# window.configure(bg='#F25D37')
window.geometry("450x580+500+100")
window.resizable(False,False)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 145)

# Love Messages-----------------------

love_messages = ["I need some time",
           "I will tell you later",
           "sorry I don't",
           "what do you mean By that?",
           "that's Not Good",
           "it's not possible",
           "you are not good",
           ]

def love_response():
    return love_messages[random.randint(0,7)]

# love messages -----------------------------
# Hello messages------------------

hello_messages1 = ["Hello. How may I Help you?",
             "Hello..what can I do for you?",
             "Hello..you are looking nice",
             "Namaste..",
             "Hello.",
             "Hello. I am your Roni"]

hello_messages2 = ["Hello. are you okay",
             "Hi..what can I do for you?",
             "Hello..Anything else",
             "Hi, what you want",
             "Hello. Everything okay",
             "Hi, what Happen to you?"]


def hello(has_said_hello):
    if has_said_hello == False:
        has_said_hello = True
        return hello_messages1[random.randint(0,5)]
    else:
        return hello_messages2[random.randint(0,5)]


# hello messages-----------------

def speak(text):
    engine.say(text)
    engine.runAndWait()

def change_message(mess):
    label_text.set(mess)
    window.update()

def wish():
    time = datetime.datetime.now().hour
    if time>=0 and time<12:
        change_message('Good Morning')
        speak('Good Morning')
    elif time>=12 and time<18:
        change_message("Good Afternoon")
        speak("Good Afternoon")
    else:
        change_message("Good Evening")
        speak("Good Evening")
    change_message("I am Your Roni! How may I Help you")
    speak("I am Your Roni! How may I Help you")
    print("I am Your Roni! How may I Help you")
    



def takeCommand():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            change_message("Listening to you...")
            print("Listening to you...")
            audio = listener.listen(source)
        change_message("Understanding...")
        print('Understanding...')
        
        query = listener.recognize_google(audio)
    except Exception as e:
        query = "None"
        print(e)
        # speak("I am Not Getting You")
        
    return query



        
def main():
    wish()
    has_said_hello = False
    while True:
        query = takeCommand().lower()
        if 'play' in query:
            query = query.replace('play','')
            change_message(f"playing:{query}")
            print(f"playing:{query}")
            speak(f"playing:{query}")
            pywhatkit.playonyt(query) 
        elif 'search' and 'youtube' in query:
            word_list = ['search','youtube','on'," "]
            for x in word_list:
                query = query.replace(x,"")
            change_message("okay wait!")
            speak("okay wait!")
            query = query.replace(' ','+')
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "the time" in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            change_message(f"its {time}")
            speak(f"its {time}")
            print(f"its {time}")
        elif 'joke' in query:
            change_message(pyjokes.get_joke())
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif 'love me' in query:
            love_mess_response = love_response()
            change_message(love_mess_response)
            print(love_mess_response)
            speak(love_mess_response)
        elif 'hello' in query:
            hello_response = hello(has_said_hello)
            has_said_hello = True
            change_message(hello_response)
            speak(hello_response)
            print(hello_response)
        elif 'wikipedia' in query:
            speak('searching...')
            print('searching...')
            words = ['what is','who is','tell','me','about','wikipedia'," "]
            for x in words:
                query = query.replace(x,'')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            change_message(results)
            print(results)
            speak(results)
        elif 'sleep' in query:
            change_message("Okay Bye!")
            speak("okay bye!")
            break
        elif 'none' in query:
            change_message("I am Not Getting You")
            speak("I am Not Getting You")
            print("I am Not Getting You")
    print('Say Hello to Start Again')
    change_message("Say Hello To Start Again")


# Girl Image
resized_girl_img = Image.open('girls.png').resize((380,380))
girl = ImageTk.PhotoImage(resized_girl_img)
girl_image = Label(image=girl).pack(pady=5)
# girl image

label_text = StringVar()

label_text.set("...")

message_label = Label(window,textvariable=label_text,font=('arial',12,'bold')).pack()
#btn image
resized_btn_img = Image.open('roundbtn2.png').resize((300,290))
btn = ImageTk.PhotoImage(resized_btn_img)
btn_image = Button(window,image=btn,borderwidth=0,cursor='hand2',command=main).pack(pady=10,side='bottom')

signature = Label(window,text="Made By Chetan Sharma",font=('arial',8,'bold'),fg='grey').place(x=150,y=550)


window.mainloop()