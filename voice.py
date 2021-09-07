from gtts import gTTS 
import os 

mytext = 'Image Captured'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("hh.mp3") 
os.system("hh.mp3") 
