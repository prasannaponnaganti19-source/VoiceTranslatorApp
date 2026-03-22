from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from deep_translator import GoogleTranslator


class VoiceTranslatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.input_text = TextInput(
            hint_text="Enter text in English",
            multiline=True,
            size_hint=(1, 0.3)
        )

        self.translate_btn = Button(
            text="Translate to Hindi",
            size_hint=(1, 0.2)
        )
        self.translate_btn.bind(on_press=self.translate_text)

        self.output_label = Label(
            text="Translated text will appear here",
            size_hint=(1, 0.5)
        )

        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.translate_btn)
        self.layout.add_widget(self.output_label)

        return self.layout

    def translate_text(self, instance):
        text = self.input_text.text.strip()
        if not text:
            self.output_label.text = "Please enter some text"
            return

        try:
            translated = GoogleTranslator(source="en", target="hi").translate(text)
            self.output_label.text = translated
        except Exception as e:
            self.output_label.text = "Translation failed"


if __name__ == "__main__":
    VoiceTranslatorApp().run()
