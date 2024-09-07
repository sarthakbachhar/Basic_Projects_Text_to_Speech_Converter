from gtts import gTTS

# Set language 
language = "en"

# Set a text to convert
text = "Hello, It was raining all day. What about your place?"

# Convert to speech using along with British accent
speech = gTTS(text=text, lang=language, slow=False, tld="co.uk")

# Sace the audio in an MP3 file
speech.save("C:\\Users\\Acer\\Desktop\\Project 14\\final.mp3")