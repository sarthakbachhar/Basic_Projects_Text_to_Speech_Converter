# Basic Text to Speech Converter

This script converts text to speech using Google's Text-to-Speech API via the `gTTS` library. The output is saved as an MP3 file with a customizable accent and speech rate.

## Requirements

- Python 3.x
- gTTS (`pip install gtts`)

## Usage

1. **Set the Text**: Update the `text` variable in the script with the text you want to convert to speech.
2. **Choose Language and Accent**: The script uses English with a British accent by default (`tld="co.uk"`), but you can adjust it as needed.
3. **Run the Script**:

   ```bash
   python your_script_name.py

3. **Output**: The speech is saved as an MP3 file at the specified path.

## Example
    
    Text: Hello, It was raining all day. What about your place?

The output audio will be saved as final.mp3.

## License

MIT License
