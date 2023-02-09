from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage

import random
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout




# class MainApp(App):
#     def build(self):
#         img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
#                          size_hint = (1, .5),
#                          pos_hint = ({'center_x': .5, 'center_y': .5})
#                          )
#         label= Label(text="Hello Wolrd",
#                      size_hint = (.5, .5),
#                      pos_hint = ({'center_x': .5, 'center_y': .5})
#                      )
#         return img



red= [1,0,0,1]
green= [0,1,0,1]
blue= [0,0,1,1]
purlpe= [1,0,1,1]




class ExBoxLayout(App):
    def build (self):
        layout = BoxLayout(orientation='vertical')
        colors= [red, green, blue, purlpe]


        for i in range(5):
            btn = Button(text=f'Este é o botão {i+1}',background_color= random.choice(colors))

            layout.add_widget(btn)

            
        return layout


if __name__ == "__main__":
    app= ExBoxLayout()
    app.run()