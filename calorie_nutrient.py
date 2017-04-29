
import kivy
import os
import threading
import math

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.uix.textinput import TextInput

global error
global add_

add_ = -1
x = 0
global weight_text_input 
global height_text_input 
global ages_text_input
               
global carbohydrate
global cooked_rice
global protein
global grilled_chicken
global fat
global oil
weight_text_input =''
height_text_input =''
ages_text_input=''

class SampBoxLayout(BoxLayout):
    weight_text_input = ObjectProperty()
    height_text_input = ObjectProperty()
    ages_text_input = ObjectProperty()
    text_input = ObjectProperty()
    target_ = ObjectProperty()
    act = ObjectProperty()
    sex = ObjectProperty()
    carbohydate = ObjectProperty()
    rice = ObjectProperty()
    cholesterol = ObjectProperty()
    mg = ObjectProperty()
    protein = ObjectProperty()
    chickleg = ObjectProperty()
    fat = ObjectProperty()
    oil = ObjectProperty()
    wat = ObjectProperty()
    fib = ObjectProperty()
    
    
    def sexs(self, value):
        global x
        if value == "Male":
            x = 1
        elif value == "Female":
            x = 2
            
    def target(self, value):
        global add_ 
        if value == "Decrese":
            add_ = 0
        elif value == "Increse":
            add_ = 2
        else:
            add_ = 1

    
    def act_rate(self, value):
        global y
        if value == "Least":
            y = 1.2
        elif value == "Little (1-3 hr./w)":
            y = 1.375
        elif value == "Medium (3-5 hr/w)":
            y = 1.55
        elif value == "High (1-2 hr/d)":
            y = 1.725
        else:
            y = 1.9
        
    

    def calculated(self, *args):
        global cal
        global water
        error = False
        if x == 0:
            error = True
        if x == 1:
            try:
                if float(self.weight_text_input.text) < 0 or float(self.height_text_input.text)<0 or float(self.ages_text_input.text) < 0 or float(self.ages_text_input.text) >= 100 or float(self.height_text_input.text)<= 50:
                    error = True
                bmr = int(66.5 + (13.7 * float(self.weight_text_input.text)) + (5 * int(self.height_text_input.text)) - (6.8 * int(self.ages_text_input.text)))
                water = "3 liters = 13 glasses"
                if bmr == int(66.5):
                    bmr = 0
                    water = "0 liters = 0 glasses"
                

            except ValueError:
                error = True
            

        elif x == 2:
            try:
                if float(self.weight_text_input.text) < 0 or float(self.height_text_input.text)<0 or float(self.ages_text_input.text) < 0 or float(self.ages_text_input.text) >= 100 or float(self.height_text_input.text)<= 50:
                    error = True
                bmr = int(447.593 + (9.247 * float(self.weight_text_input.text)) + (3.098 * int(self.height_text_input.text)) - (4.33 * int(self.ages_text_input.text)))
                water = "2.2 liters = 9 glasses"
                if bmr == int(447.593):
                    bmr = 0
                    water = "0 liters = 0 glasses"
                
            except ValueError:
                error = True
           

            
                
       
        if add_ == 1:
            try:
                cal = str(int((bmr * y)))
             
            except UnboundLocalError:
                pass
            except NameError:
                pass
        elif add_ == 2:
            try:
                cal = str(int((bmr * y)+ (0.2 * (bmr * y))))
    
            except UnboundLocalError:
                pass
            except NameError:
                pass
        else:
            try:
                cal = str(int((bmr * y) - (0.2 * (bmr * y))))

            except UnboundLocalError:
                pass
            except NameError:
                pass
        try:
            cal = math.ceil(float(cal))
            
        
            if add_ == 0:
                temp1 = 0.4
                temp2 = 0.3
                temp3 = 0.3
            else:
                temp1 = 0.55
                temp2 = 0.2
                temp3 = 0.25

            carbohydrate = str((float(cal) * temp1) // 4)
            cooked_rice = str(float(carbohydrate) / 17)
            protein = str((float(cal) * temp2) // 4)
            grilled_chicken = str(float(protein) / 51.3)
            fat = str((float(cal) * temp3) // 9)
            oil = str(float(fat) / 14)

            
        
            if not error :
                self.text_input.text = str(cal)
                self.carbohydate.text = str(math.ceil(float(carbohydrate))) + ' g.'
                self.rice.text = str(math.ceil(float(cooked_rice))) + ' ladle.'
                self.protein.text = str(math.ceil(float(protein))) + ' g.'
                self.chickleg.text = str(math.ceil(float(grilled_chicken))) + ' leg(s)'
                self.fat.text = str(math.ceil(float(fat))) + ' g.'
                self.oil.text = str(math.ceil(float(oil))) + '  tablespoon(s)'
                self.wat.text = str(water)                          
                
                if bmr == int() or bmr == int():
                    self.fib.text = '0 g.'
                    self.mg.text = "0 mg."
                else:
                    self.fib.text = '25 g.'
                    self.mg.text = "less than 300 mg."
        except NameError:
            pass
        
         
class SampleApp(App):
    icon = 'TOP-LOGO-Black.png'
    title = 'Calory & Nutrient Calculator'
    def build(self):
        Window.size = 700, 650
        Window.clearcolor = 1,1,1,1
        return SampBoxLayout()


sample_app = SampleApp()
sample_app.run()

while error:
    sample_app.run()
