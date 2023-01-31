import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
'''
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
'''
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        take_command()
        return command

def yes_no():
    print()
    print("RHS: Wanna ask something else?")
    abc = input("Yes(y/Y) or No(n/N)- ")
    abc = abc.lower()
    if abc == 'y':
        run_rhs()
    elif abc == 'n':
        print("RHS: It was nice talking with you!")
    else:
        print("RHS: Answer in y or n only.")
        yes_no()

def run_rhs():
    command = take_command()
    print("User:", command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        talk("You can come back later when you are done listening. I am waiting for you.")
        yes_no()
        
    elif 'gaana' in command:
        webbrowser.open("https://gaana.com/")
        talk("Opening Gaana website")
        talk("YOu can come back later when you are done listening to songs. I am waiting for you!")
        yes_no()

    elif 'hello' in command:
        greet = ['Nice to meet you','Heya mate!','Hello! Sup?','Hey dude','Hallo!','Hola!','Lumela','Salam']
        b = random.choice(greet)
        print("RHS:", b)
        talk(b)
        run_rhs()
    elif 'how are you' in command:
        a = ['Feeling happy that you asked me!','I am great. Thanks.','I am good, What about you?']
        f = random.choice(a)
        print("RHS:", f)
        talk(f)
        run_rhs()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("RHS: Current time is " + time)
        talk("Current time is " + time)
        run_rhs()
    elif 'who' in command:
        talk("Are you asking for someone?")
        ask = input("Yes(Y/y) or No(N/n)- ")
        ask = ask.lower()
        if ask == 'y':
            talk("Enter the name you are asking for")
            person = input("RHS: Enter the name here: ")
            webbrowser.open("https://en.wikipedia.org/wiki/" + person)
            talk("I found this on Wikipedia")
            talk("You can come back later when you are done surfing. I am waiting for you!")
            yes_no()
        elif ask == 'n':
            print("RHS: Okay, No Problem. Try asking again.")
            talk("Okay, No Problem. Try asking again.")
            run_rhs()
        else:
            print("RHS: I don't get it.")
            talk("I don't get it.")
            run_rhs()
    elif 'i am good' in command:
        print("RHS: Glad to hear that! How can I help you today?")
        talk("Glad to hear that! How can I help you today?")
        run_rhs()
    elif 'search' in command:
        result = command.replace('search','')
        pywhatkit.search(result)
        print("RHS: I found this on google.")
        talk("I found this on Google")
        talk("Youc an come back later when you are done surfing. I am waiting for you!")
        yes_no()
    elif 'date' in command:
        date = str(datetime.date.today())
        print("RHS: Today's date is " + date)
        talk("Today's date is " + date)
        run_rhs()
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print("RHS:", joke)
        talk(joke)
        run_rhs()
    elif 'leave' in command:
        print("RHS: Are you sure you wanna quit?")
        talk("RHS: Are you sure you wanna quit?")
        abc = input("Yes(y/Y) or No(n/N)- ")
        abc = abc.lower()
        if abc == 'y':
            print("RHS: Okay! You are ready to leave the assistant. See you soon again.")
            talk("Okay! You are ready to leave the assistant. See you soon again.")
        elif abc == 'n':
            print("RHS: Okay! Let's talk more.")
            talk("Okay! Let's talk more.")
            run_rhs()
        else:
            print("RHS: Answer in y or n only.")
            talk("Answer in y or n only.")
            run_rhs()
    elif 'what can you do' in command:
        print("")
    else:
        print("RHS: I didn't get you, Please repeat the command.")
        talk("I didn't get you, Please repeat the command.")
        run_rhs()
def login():
    print("Hello there!")
    talk("Hello there!")
    talk("Enter the username")
    name = input("Enter the username- ")
    if name.lower() == 'hiral':
        print("RHS:Welcome back Hiral!")
        talk("Welcome back Hiral!")
        run_rhs()
    else:
        print("Sorry, You are not a valid user.")
        talk("Sorry, You are not a valid user.")
        login()
login()
