import pyttsx3
txt_sp=pyttsx3.init() #init is a class
text=input("Enter the text: ")
# say
txt_sp.say(text) #conversion of text in to audio
txt_sp.setProperty('rate', 50) 
txt_sp.runAndWait() #wait untill it is converted

# property change

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
