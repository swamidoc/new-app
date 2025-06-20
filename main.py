# main.py

try:
    long  # Ensure compatibility for Cython/PyJNIus if long doesn't exist (Python 3)
except NameError:
    long = int

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from viewer import DicomViewerScreen

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        viewer_screen = DicomViewerScreen(name='viewer')
        viewer_screen.build_ui()
        sm.add_widget(viewer_screen)
        return sm

if __name__ == '__main__':
    MainApp().run()

