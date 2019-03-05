# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:17:01 2019

@author: Sharmila
"""

from kivy.app import App
 
from kivy.uix.button import Button
 
class KivyButton(App):
 
    def build(self):
 
        return Button(text="Welcome to LikeGeeks!", background_color=(155,0,51,53))
 
KivyButton().run()
