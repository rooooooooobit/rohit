import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import subprocess
import os
import pygame


recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()

def speak(text):

    engine.say(text)
    engine.runAndWait()

def listen():
   
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Could you repeat that?")
            return None
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return None

def search_wikipedia(query):
 
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(summary)
    except wikipedia.DisambiguationError as e:
        speak("The term is ambiguous. Please be more specific.")
    except wikipedia.PageError:
        speak("No matching results found on Wikipedia.")

def play_youtube(query):

    speak("Opening YouTube...")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def open_application(app_name):

    try:
        subprocess.Popen(app_name)
        speak(f"Opening {app_name}.")
    except FileNotFoundError:
        speak("Application not found.")

def assist_with_coding():

    speak("What coding problem can I help you with?")
    while True:
        code_query = listen()
        if code_query:
            if "exit" in code_query or "stop" in code_query:
                speak("Exiting coding assistance.")
                break
            else:
           
                speak(f"Here is some advice for: {code_query}")
                print(f"You asked about: {code_query}")

def main():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        query = listen()
        if query:
            if "wikipedia" in query:
                speak("What should I search on Wikipedia?")
                search_query = listen()
                if search_query:
                    search_wikipedia(search_query)
            elif "youtube" in query or "play music" in query:
                
               
                
                    play_youtube(query)
            elif "location of school" in query:
                speak("our school is located at butwal 15 mainapur")
            elif "tell about school" in query :
                speak("Siddhi Vinayak Secondary School is dedicated to providing quality education through innovative teaching techniques, a child-friendly environment, and fully digitalized classrooms. The school emphasizes a joyful, engaging, and stress-free learning journey, aiming to equip students with 21st-century skills and exceptional academic and intellectual creativityThe institution offers an enriched learning environment, helping students learn, develop, and grow. Its unparalleled curriculum and teaching methods assist students in confidently taking the next steps in their education. Siddhi Vinayak Secondary School provides an excellent academic environment, blending co-curricular and extra-curricular activities to foster holistic development. The school strives to inculcate traditional values in young minds, blended with modernity and wisdom, enabling students to learn complex concepts with ease. The school's mission is to empower students to acquire, demonstrate, articulate, and value knowledge and skills that will support them as lifelong learners. It encourages creativity, innovation, and social engagement, aiming to develop critically engaged citizens dedicated to solving problems and contributing to the public good.Siddhi Vinayak Secondary School offers various services and facilities, including digitalized well-furnished classrooms, quality bus service, hygienic and well-sanitized canteen, well-equipped computer and science labs, library and e-library, good playground, extracurricular activities, child-friendly environment, and more. The school is located in Butwal-15, Mainapur, Rupandehi, Nepal. For more information, you can contact them via email at info@svsschool.edu.np or call +977 071-504074")

            elif "exit" in query or "bye" in query:
                speak("Goodbye! Have a great day and see you soon")
                break
            else:
                speak("I didn't understand that. Could you try again?")

if __name__ == "__main__":
    main()
