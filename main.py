import tkinter as tk
import threading
import time
import speech_recognition as sr
import pyttsx3

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Create the main window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x400")

# Output box
output_box = tk.Text(root, wrap='word', height=15, width=55)
output_box.pack(pady=10)
output_box.insert(tk.END, "Welcome! Press the 'Speak' button and give a command.\n")

# Function to add text to the output box
def display_text(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)

# Basic text-to-speech function
def speak(text):
    display_text("Assistant: " + text)
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        display_text("You: " + command)
        return command
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, there seems to be an issue with the service."

# GUI button function to activate the assistant
def start_listening():
    def task():
        speak("Listening now...")
        command = listen()
        handle_command(command)
    threading.Thread(target=task).start()

# Speak button
speak_button = tk.Button(root, text="Speak", command=start_listening)
speak_button.pack(pady=10)

### Step 2: Define the Command Handling Logic ###
def handle_command(command):
    if "weather" in command:
        speak("Weather feature will be added soon!")
    elif "news" in command:
        speak("News feature will be added soon!")
    elif "reminder" in command:
        speak("Reminder feature will be added soon!")
    else:
        speak("I'm here to assist with your commands.")

root.mainloop()
