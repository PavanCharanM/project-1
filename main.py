

from kivy.app import App as app
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.graphics import Color


class Myapp(app):
    def exit(self,instance):
        app.get_running_app().stop()
    def xcho(self,instance):
        self.sound6.play()
    def so_is(self , instance):
        self.sound5.play()
    def katchisera(self,instance):
        self.sound1.play()
    def cheri(self,instance):
        self.sound2.play()
    def closeup(self,instance):
        self.sound3.play()
    def metamor(self,instance):
        self.sound4.play()
    def pausesound(self,instance):
        if self.sound1:
            self.sound1.stop()
        if self.sound2:
            self.sound2.stop()
        if self.sound3:
            self.sound3.stop()
        if self.sound4:
            self.sound4.stop()
        if self.sound5:
            self.sound5.stop()
        if self.sound6:
            self.sound6.stop()
    def build(self):
        self.sound6 = SoundLoader.load(
            "/home/pavancharan/Desktop/lafs/Musics/xcho ты и я Remix [ slowed Reverb ].mp3")
        self.sound5 = SoundLoader.load(
           "/home/pavancharan/Desktop/lafs/Musics/So_is_Gone_is_Gone___Full_Song___Dj___2020(256k).mp3")
        self.sound4 = SoundLoader.load(
            "/home/pavancharan/Desktop/lafs/Musics/Metamorphosis.mp3")
        self.sound3 = SoundLoader.load(
            "/home/pavancharan/Desktop/lafs/Musics/Close.mp3")
        self.sound1 = SoundLoader.load(
            "/home/pavancharan/Desktop/lafs/Musics/Y2meta.app - Sai Abhyankkar - Katchi Sera (Music Video) Samyuktha Ken Royson Think Indie (320 kbps).mp3")
        self.sound2 = SoundLoader.load(
            '/home/pavancharan/Desktop/lafs/Musics/Y2meta.app - Modern Talking - Cheri Cheri Lady (Official Music Video) (320 kbps).mp3')
        layout = FloatLayout()
        # Add background image
        background = AsyncImage(source='/home/pavancharan/Desktop/lafs/Images/kivybg.jpg', allow_stretch=True,keep_ratio = False)
        layout.add_widget(background)
        button = Button(text="KatchiSera.Mp3" , color = (1,0,0,1),size_hint = (None,None), size = (200,60), pos = (5,100), background_color=(0,0,0,0),on_press = self.katchisera)
        button2 = Button(text="Cheri Cheri Lady.mp3",color = (1,0,0,1),size_hint = (None,None), size = (200,60), pos = (5,170), background_color=(0,0,0,0),on_press = self.cheri)
        button4 = Button(text="CLose Up.Mp3" ,color = (1,0,0,1),size_hint =(None,None) , size = (200,60), pos = (5 ,240),background_color=(0,0,0,0),on_press = self.closeup)
        button5 = Button(text = "Metamorphisis" ,color = (1,0,0,1),size_hint = (None,None), size = (200,60), pos = (5,100), background_color=(0,0,0,0),on_press = self.metamor)
        button6 = Button(text = " So Is Gone Is Gone.mp3",color = (1,0,0,1),size_hint = (None,None), size = (200,60), pos = (5,300), background_color=(0,0,0,0) , on_press = self.so_is)
        button7 = Button(text = "xcho ты и я-(slowedReverb).mp3",color = (1,0,0,1),size_hint = (None,None), size = (200,60), pos = (30,360), background_color=(0,0,0,0) , on_press = self.xcho)
        button3 = Button(text="Pause",color = (1,1,1,3), size_hint=(None, None), size=(200, 100), pos=(5, 0),background_color=(0, 0, 0, 0), on_press=self.pausesound)
        button8 = Button(text = "EXIT" ,size_hint=(None, None), size=(150, 30), pos=(650, 570), on_press = self.exit)
        layout.add_widget(button)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button6)
        layout.add_widget(button7)
        layout.add_widget((button8))
        return layout
Myapp().run()




