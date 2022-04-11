from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

recognizer = sr.Recognizer()
engine = pyttsx3.init()

'''
The dictionary responsible for the pronunciation of the translated text. 
It is configured personally, in the absence of language installation, voice acting will be performed in the language set as defolt in Windows.
'''
voice_lang_dict = {
    'be': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0',
    'en': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
    'fr': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0',
    'de': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0',
    'it': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0',
    'ja': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0',
    'ko': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0',
    'pt': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0',
    'ru': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0',
    'es': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0',
    'zh-tw': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0'
}


class Container(BoxLayout):
    def trans(self): # The function accepts the recognized text, translates it and returns it in the form of text and voiceover.
        lng = self.ids.to_lang.text
        translator = Translator()
        translate_text = translator.translate(self.ids.input_text.text, dest=lng)
        result = translate_text.text

        print(result)
        self.ids.output_text.text = result
        if lng in voice_lang_dict:
            engine.setProperty('voice', voice_lang_dict[lng])
        else:
            engine.setProperty('voice', voice_lang_dict['en'])
        engine.say(str(result))
        engine.runAndWait()

    def record(self): # The function accepts your voice and returns recognized text.
        with sr.Microphone() as source:
            print('Говорите:')
            audio = recognizer.listen(source)
        try:
            print('Обработка...')
            recognize_txt = recognizer.recognize_google(audio, language=self.ids.from_lang.text)
            print('Распозано:', recognize_txt)
            self.ids.input_text.text = recognize_txt
            return recognize_txt
        except Exception as ex:
            print(ex)


class TranslateApp(MDApp):
    def build(self):
        return Container()


TranslateApp().run()
