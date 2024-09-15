# ReadTXT

ReadTXT is a Python program that converts the content of a text file into speech using Google Text-to-Speech (gTTS) and plays the generated MP3 file on your operating system (Windows, Linux, or macOS). Additionally, you can now speed up the generated audio using `speed_up.py`.

## Features

- Converts text from a file to speech using gTTS
- Saves the speech as an MP3 file
- Plays the MP3 file automatically based on your operating system:
  - Windows: Uses the `start` command
  - Linux: Uses `xdg-open`
  - macOS: Uses `afplay`
- **New:** Speed up audio files using the `speed_up.py` script:
  - Speed up the audio by a specified factor (default is 1.2x)

## Requirements

- Python 3.x
- gTTS (`pip install gtts`)
- Pydub (`pip install pydub`)
- FFMPEG (for Pydub, installation instructions [here](https://github.com/jiaaro/pydub#dependencies))

## Usage

### For `main.py`:
1. Clone or download this repository.
2. Install the required dependencies:
   ```
   pip install gtts pydub
   ```
3. Ensure that FFMPEG is installed and available in your system's PATH.
4. Place the text file you want to convert in the same directory as the Python script.
5. Run the Python program:
   ```
   python main.py
   ```
6. When prompted, enter the name of the text file (without the `.txt` extension).
7. The program will convert the text in the file to speech, save it as an MP3 file (`speech.mp3`), and play the file.

### For `speed_up.py`:
1. After generating an MP3 file using `main.py` (or any other MP3 file), run the `speed_up.py` script:
   ```
   python speed_up.py
   ```
2. When prompted, enter the name of the MP3 file (without the `.mp3` extension) that you want to speed up.
3. The program will create a sped-up version of the file (default speed increase of 1.2x) and save it as `sped_up_audio.mp3`.

## Example

### Using `readtxt.py`:
If you have a file named `example.txt` containing the text:

```
Hello, welcome to the ReadTXT converter.
```

When you run the program and input `example`, the program will convert the text to speech, save it as `speech.mp3`, and play the file.

### Using `speed_up.py`:
If you want to speed up the `speech.mp3` file, simply run the `speed_up.py` script, enter `speech` when prompted, and the sped-up version (`sped_up_audio.mp3`) will be created.

## Error Handling

- If the file does not exist, the program will notify you with an error message.
- If the text file is empty, the program will inform you and terminate without generating an MP3 file.
- If the OS is unsupported, it will print an error message.
- `speed_up.py` will inform you if the specified MP3 file cannot be found.

## Platform Compatibility

- Windows
- Linux
- macOS

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software as needed.
