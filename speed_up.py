from pydub import AudioSegment

# Load your audio file
file_name = input("Enter name of audio file to be sped up (w/o .mp3):")
file_name = file_name.strip() + ".mp3"
audio = AudioSegment.from_file(file_name)

# Function to change speed
def change_speed(audio, speed=1.5):
    # Increase or decrease speed by changing the frame rate
    sound_with_altered_frame_rate = audio._spawn(audio.raw_data, overrides={
         "frame_rate": int(audio.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(audio.frame_rate)

# Speed up by 1.2x (increase speed by 20%)
sped_up_audio = change_speed(audio, speed=1.2)

# Export the sped-up audio
sped_up_audio.export("sped_up_audio.mp3", format="mp3")