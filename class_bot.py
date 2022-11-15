import speech_recognition as sr
import datetime
import pyttsx3
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def gpt3(texts):
    openai.api_key = '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'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt = 'you are a professor at angadi instute of technology and management from AI department '+ texts,
    temperature=0.7,
    max_tokens=256, 
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    return response.choices[0].text



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am your virtual professor. please tell me how may i help you')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print('Say that again please...')
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    wishMe()
    
    while True:
        query = takecommand().lower()
        response = gpt3(query)
        speak(response)
        print(response)