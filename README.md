# ReadTXT

ReadTXT is a Python program that converts the content of a text file into speech using Google Text-to-Speech (gTTS) and plays the generated MP3 file on your operating system (Windows, Linux, or macOS). Simply provide a text file, and ReadTXT will read it aloud for you.

## Features

- Converts text from a file to speech using gTTS
- Saves the speech as an MP3 file
- Plays the MP3 file automatically based on your operating system:
  - Windows: Uses the `start` command
  - Linux: Uses `xdg-open`
  - macOS: Uses `afplay`

## Requirements

- Python 3.x
- gTTS (`pip install gtts`)

## Usage

1. Clone or download this repository.
2. Install the required dependency:
   ```
   pip install gtts
   ```
3. Place the text file you want to convert in the same directory as the Python script.
4. Run the Python program:
   ```
   python readtxt.py
   ```
5. When prompted, enter the name of the text file (without the `.txt` extension).
6. The program will convert the text in the file to speech, save it as an MP3 file (`speech.mp3`), and play the file.

## Example

If you have a file named `example.txt` containing the text:

```
Hello, welcome to the ReadTXT converter.
```

When you run the program and input `example`, the program will convert the text to speech, save it as `speech.mp3`, and play the file.

## Error Handling

- If the file does not exist, the program will notify you with an error message.
- If the text file is empty, the program will inform you and terminate without generating an MP3 file.
- If the OS is unsupported, it will print an error message.

## Platform Compatibility

- Windows
- Linux
- macOS

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software as needed.
