# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:37:14 2019

@author: Icarpio
"""

import speech_recognition as sr
import webbrowser as web

def main():
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something....")
        
        audio = r.listen(source)
        
        print("Reconizing now....")
        
        try:
            dest = r.recognize_google(audio)
            print("You have said: " + dest)
            
            web.get(path).open(dest)
            
        except Exception as e:
            print("Error" + str(e))
            
if __name__ == "__main__":
    main()