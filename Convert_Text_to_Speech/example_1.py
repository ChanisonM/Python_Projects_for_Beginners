from gtts import gTTS
import os

myText = "สวัสดีครับ"
language = "th"

myObj = gTTS(text=myText , lang=language , slow=False)

myObj.save("welcome.mp3")

os.system("start welcome.mp3")