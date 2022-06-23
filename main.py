from itertools import cycle

import speedtest
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()



kivy.require('1.0.6')



class MainApp(App):

    def change_text(self, instance):
        self.label.text = f"Speed: {(download/1024)/1024} Mb/s \n Upload Speed : {(upload/1024)/1024} Mb/s"

    def build(self):
        self.label = Label(text="")

        layout = BoxLayout(padding=10)

        button = Button(text='Speed Test',
                        size_hint=(.3, .3),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.change_text)


        layout.add_widget(self.label)
        layout.add_widget(button)


        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()