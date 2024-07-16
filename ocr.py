from gtts import gTTS
import os
import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read('val.cfg')

class Ocr:

    def get_img(self, file="images/example.jpg", overlay=True, language='eng'):
        data = {
            'isOverlayRequired': overlay,
            'apikey': cfg["Api"]["key"],
            'language': language,
            'isCreateSearchablePdf': True,
            'OCREngine': 2

        }
        with open(file, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={file: f},
                              data=data,
                              )
        print(r.json()['ParsedResults'][0]['ParsedText'])
        with open("result.pdf", 'wb') as w:
            response = requests.get(r.json()['SearchablePDFURL'])
            w.write(response.content)
        return r.json()['ParsedResults'][0]['ParsedText']

    def speech(self):
        # Import the required module for text
        # to speech conversion(gtts)
        # This module is imported so that we can
        # play the converted audio
        # The text that you want to convert to audio

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        text = self.get_img()
        myobj = gTTS(text=text, lang="en", slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome.mp3
        myobj.save("welcome.mp3")

        # Playing the converted file
        os.system("start welcome.mp3")

