from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import os 
from kivymd.uix.dialog import MDDialog


Builder.load_file('style.kv')

class Style(MDBoxLayout):

    def az_dialog(self,title=None,text=None,widget=None):
        try:
            d=MDDialog()
            d.title=title
            d.text=text
            try:
                d.add_widget(widget)
            except:
                pass 
            d.open()
        except:
            pass

    def get_address(self,address):
        try:
            address=address[-1]
            return address
        except:
            None  

    def select(self,address):
        self.run_file(self.get_address(address))

    def run_file(self,address):
        try:
            os.system(fr'{address}')
        except:
            None

    def about(self):
        self.az_dialog('About','AliasgharZahdyan\nAZ')

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.primary_hue='900'
        self.theme_cls.theme_style='Dark'

        return Style()
    
MainApp().run()


