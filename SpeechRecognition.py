"""
Created on Fri Oct 18 07:05:14 2019

@author: Icarpio
"""


import speech_recognition as sr
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio = r.listen(source)
        print("Recognizing now...")
        
        try:
            #r.recognize_google(audio, language="fr-FR") French
            #r.recognize_google(audio, language="es-ES") Spanish
            print("You have said: \n" + r.recognize_google(audio))
            print("Audio Recorder Successfully \n")
        except Exception as e:
            print("Error: " + str(e))
        
        with open("recorderaudio.wav", "wb") as f:

                f.write(audio.get_wav_data())
            
            
            
if __name__ == "__main__":
    main()