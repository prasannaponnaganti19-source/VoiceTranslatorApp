import threading
import time
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound


class CallScreen(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(orientation="vertical", padding=30, spacing=25)

        self.call_active = False

        Window.clearcolor = (0.05, 0.15, 0.30, 1)
        with self.canvas.before:
            Color(0.05, 0.15, 0.30, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        self.name = Label(
            text="🦆 Bhathu Guddu 🦆",
            font_size="36sp",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.25),
            halign="center",
            valign="middle"
        )
        self.name.bind(size=self.name.setter("text_size"))

        self.number = Label(
            text="+91 95507 57884\nAndhra Pradesh Mobile",
            font_size="20sp",
            color=(1, 1, 1, 0.85),
            size_hint=(1, 0.15),
            halign="center",
            valign="middle"
        )
        self.number.bind(size=self.number.setter("text_size"))

        self.status = Label(
            text="Incoming Call",
            font_size="18sp",
            color=(0.7, 0.9, 1, 1),
            size_hint=(1, 0.1)
        )

        self.lang_spinner = Spinner(
            text="English",
            values=("English", "Telugu", "Hindi", "Tamil", "Kannada", "Malayalam"),
            size_hint=(1, 0.12)
        )

        self.log = Label(
            text="",
            font_size="16sp",
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            halign="center",
            valign="middle"
        )
        self.log.bind(size=self.log.setter("text_size"))

        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=30)

        self.answer_btn = Button(
            text="Answer",
            background_color=(0, 0.7, 0.3, 1),
            font_size="20sp"
        )
        self.end_btn = Button(
            text="End",
            background_color=(0.9, 0.2, 0.2, 1),
            font_size="20sp"
        )

        self.answer_btn.bind(on_press=self.start_call)
        self.end_btn.bind(on_press=self.end_call)

        btn_layout.add_widget(self.answer_btn)
        btn_layout.add_widget(self.end_btn)

        self.add_widget(self.name)
        self.add_widget(self.number)
        self.add_widget(self.status)
        self.add_widget(self.lang_spinner)
        self.add_widget(self.log)
        self.add_widget(btn_layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def start_call(self, instance):
        if self.call_active:
            return
        self.call_active = True
        self.status.text = "Call Connected 🎙️ Speak now"
        threading.Thread(target=self.live_translate, daemon=True).start()

    def end_call(self, instance):
        self.call_active = False
        self.status.text = "Call Ended"
        self.log.text = ""

    def live_translate(self):
        recognizer = sr.Recognizer()

        lang_map = {
            "English": "en",
            "Telugu": "te",
            "Hindi": "hi",
            "Tamil": "ta",
            "Kannada": "kn",
            "Malayalam": "ml"
        }

        while self.call_active:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=6)

                # AUTO language detection
                spoken_text = recognizer.recognize_google(audio)

                target_lang = lang_map[self.lang_spinner.text]

                translated_text = GoogleTranslator(
                    source="auto",
                    target=target_lang
                ).translate(spoken_text)

                # Optional log (can remove if you want)
                self.log.text = f"Speaking in {self.lang_spinner.text}..."

                # Speak ONLY selected language
                tts = gTTS(text=translated_text, lang=target_lang)
                tts.save("call_audio.mp3")
                playsound("call_audio.mp3")

                os.remove("call_audio.mp3")
                time.sleep(0.3)

            except Exception as e:
                print(e)
                continue


class CallApp(App):
    def build(self):
        return CallScreen()


if _name_ == "_main_":
    CallApp().run()
