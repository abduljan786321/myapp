from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="Hello! Yeh mera pehla APK hai.", font_size='20sp')
        btn = Button(text="Mujhe dabao", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_press)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_press(self, instance):
        self.label.text = "Button dabaya! Kaam kar raha hai."

MyApp().run()
