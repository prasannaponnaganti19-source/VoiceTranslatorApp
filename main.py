from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread

import threading

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator

# Android permissions
from android.permissions import request_permissions, Permission


class RootLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(
            text="Press Start and Speak",
            font_size=22
        )
        self.add_widget(self.label)

        self.button = Button(
            text="Start Listening",
            size_hint=(1, 0.3),
            font_size=20
        )
        self.button.bind(on_press=self.start_listening)
        self.add_widget(self.button)

    def start_listening(self, instance):
        self.label.text = "Listening..."
        threading.Thread(target=self.listen_and_translate).start()

    def listen_and_translate(self):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            translated = GoogleTranslator(source="auto", target="en").translate(text)

            tts = gTTS(translated)
            tts.save("voice.mp3")
            playsound("voice.mp3")

            self.update_label(f"You said:\n{text}")

        except Exception as e:
            self.update_label("Error. Please try again.")

    @mainthread
    def update_label(self, text):
        self.label.text = text


class VoiceTranslatorApp(App):
    def build(self):
        request_permissions([
            Permission.RECORD_AUDIO,
            Permission.INTERNET
        ])
        return RootLayout()


if __name__ == "__main__":
    VoiceTranslatorApp().run()
