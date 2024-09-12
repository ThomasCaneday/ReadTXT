from gtts import gTTS
import os
import platform

# Function to play the MP3 file based on the OS
def play_audio(file):
    os_type = platform.system()

    try:
        if os_type == "Windows":
            os.system(f"start {file}")
        elif os_type == "Linux":
            os.system(f"xdg-open {file}")
        elif os_type == "Darwin":  # macOS
            os.system(f"afplay {file}")  # Using afplay for macOS
        else:
            print(f"Unsupported OS: {os_type}")
    
    except Exception as e:
        print(f"Error playing the audio file: {e}")

# Function to read the text file and convert it to speech
def speak_text_from_file(file_path):
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            text = file.read()
        
        if not text.strip():
            print("The file is empty!")
            return
        
        # Convert text to speech
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save the speech as an mp3 file
        speech_file = 'speech.mp3'
        tts.save(speech_file)
        
        # Play the mp3 file
        print("Speaking the text...")
        play_audio(speech_file)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the file name from the user
file_name = input("Enter the name of the text file (w/o extension) to convert to speech: ")
file_name += ".txt"

# Call the function to speak the text
speak_text_from_file(file_name)
