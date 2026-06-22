#AI based chat bot in python-

import datetime #To tell the date
import time
name=input("Enter your name buddy:")
presentHour=datetime.datetime.now().hour

if 5<= presentHour <=11:
    print(f"Good Morning {name}") 
elif 11< presentHour <=17:
    print(f"Good AfterNooon {name}") 
elif 17< presentHour <20:
    print(f"Good Good Evening {name}")     
else:
    print(f"Good Night {name}") 



print("--------------------------------")
print("===Welcome To Rule Based AI ChatBot🤖===")
print("--------------------------------")
print("=='Ask whatever you want, I'm here to help you out😉'==")
print("==='Write 'bye' to end the chat☺️'===")

response={
    "hello":"Hii, Whats Up😉",
    "who are you":"I'm your personal AI chatbot👾",
    "how are you":"I'm fine, what about you?",
    "happy":"Feeling great to hear that😍"
}

def getResponse(userQuestion):
    user= userQuestion.lower()
    for key in response:
        if key in user:
            return response[key]
        
    return "'SORRY😣' I am not able to answer that, I'm in my learning stage till now"    

while True:
    userInput=input("Plase ask your question: " ,)
    reply=getResponse(userInput)
    print("ChatBot🤖: ", reply)

    if "bye" in userInput.lower():
        print("ChatBot🤖: See You soon Buddy😉")
        break


