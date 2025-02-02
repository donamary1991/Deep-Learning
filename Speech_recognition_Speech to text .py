# # pip install pyaudio
# # pip install SpeechRecognition

# import speech_recognition as sr
# def speech_txt():
    
#     r=sr.Recognizer() #To recognise voice
#     # m=sr.Microphone() #To readvoice
    
#     while True:
#         with sr.Microphone() as source:
#             print("Speak.....")
#             audio=r.listen(source)
#             try:
#                 text=r.recognize_google(audio) #google api
#                 if text.lower()=='stop':
#                     break
#                 print("You said",text)
#             except:
#                 print("Did not hear anything pls repeat")
# speech_txt()


#or


import speech_recognition as sr

def speech_txt():
    r = sr.Recognizer()  # To recognize voice

    while True:
        with sr.Microphone() as source: #sr.Microphone() captures audio from the default microphone.
# The with statement ensures the microphone is properly opened and closed after use.
            print("Speak.....")
            r.adjust_for_ambient_noise(source)  # Helps with background noise
            audio = r.listen(source) #The listen() method captures the audio input and stores it in the audio variable.

            try:
                text = r.recognize_google(audio)  # Google API
                print("You said:", text)

                if text.lower() == 'stop':  # Corrected lower() usage
                    print("Stopping...")
                    break

            except sr.UnknownValueError:
                print("Could not understand the audio, please repeat.")
            except sr.RequestError:
                print("API request error. Check your internet connection.")

speech_txt()
