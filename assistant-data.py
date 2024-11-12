import json
import os
from datetime import datetime
# Path for local storage file
DATA_FILE = "assistant_data.json"

# Initialize the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump({"reminders": []}, file)

# Function to load data
def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Function to save data
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Save a reminder
def add_reminder(reminder_text):
    data = load_data()
    data["reminders"].append(reminder_text)
    save_data(data)
    speak(f"Reminder added: {reminder_text}")

# Display reminders
def show_reminders():
    data = load_data()
    if data["reminders"]:
        reminders = "\n".join(data["reminders"])
        speak("Here are your reminders: " + reminders)
    else:
        speak("You have no reminders.")
def handle_command(command):
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "reminder" in command:
        reminder_text = command.replace("reminder", "").strip()
        add_reminder(reminder_text)
    elif "show reminders" in command:
        show_reminders()
    else:
        speak("I'm here to assist with your commands.")