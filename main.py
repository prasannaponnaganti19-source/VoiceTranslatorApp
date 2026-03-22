from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class VoiceTranslatorApp(App):
    def build(self):
        layout = BoxLayout()
        layout.add_widget(
            Label(
                text="App is running successfully ✅",
                font_size="20sp"
            )
        )
        return layout


if __name__ == "__main__":
    VoiceTranslatorApp().run()
