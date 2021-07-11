import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import easyimap as e

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, None, 10)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def choice():
    talk('do you want to send email or read the latest mail')
    print('do you want to send email or read the latest mail')
    ch = get_info()
    if 'send' in ch:
        get_email_info()
    if 'read' in ch:
        recieve_email()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('saayush412@gmail.com', 'aayushsingh143')
    email = EmailMessage()
    email['From'] = 'saayush412@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'ashutosh': 'guptaashutosh208@gmail.com',
    'hardik': 'hardiklunial@gmail.com',
    'hridey': 'lunialhridey@gmail.com',
    'rahul': 'kushwahrahul320@gmail.com',
    'fluffy':'yogitasingh1866@gmail.com',
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    talk('please check ur msg once')
    talk(message)
    talk('do you want to proceed with this msg or change it')
    agree=get_info()
    if 'yes' in agree:
        send_email(receiver, subject, message)
    if 'no' in agree:
        get_email_info()


    talk('Hey Ayush. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    elif 'no' in send_more:
        talk("thank you!")


def recieve_email():
    password = "aayushsingh143"
    user = "saayush412@gmail.com"
    server = e.connect("imap.gmail.com", user, password)
    print(server.listids())
    email = server.mail(server.listids()[0])
    talk('you got a new email from')
    sender = email.from_addr
    print(sender)
    talk(sender)
    subject = email.title
    talk('Subject is........')
    print(subject)
    talk(subject)
    talk('The Mail is.....')
    message = email.body
    print(message)
    talk(message)


choice()
