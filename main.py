from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image, AsyncImage
from kivymd.uix.textfield import MDTextField
import json
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from decimal import Decimal
from kivy.properties import ObjectProperty

import requests

screen_helper = """
ScreenManager:
    MenuScreen:
    LoginScreen:
    SignUpScreen:
    SignUpInfoScreen
    SkipScreen:
    MenuTwoScreen
    BolusScreen:
    SettingsScreen:
    ChangeSettingsScreen:
    HelpScreen:
    LogoutScreen:

<MenuScreen>:
    name: 'Menu'
    MDLabel:
        text:"Strubby's Diabetic Management System"
        #with halign in center, you only have to set pos_hint with the y coordinate
        halign:'center' 
        pos_hint:{'center_y':0.6}
        theme_text_color: 'Custom'
        text_color: (0/255.0,151/255.0,243/255.0,1)
        font_style: 'H6'
        
    MDLabel: 
        text:"By: Non-Functional Pancreas Inc."
        pos_hint:{'center_x': 0.55, 'center_y': 0.1}
        size_hint:(1,1)
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        font_style:'Subtitle1'   
    
    MDFloatingActionButton:
        icon:'heart'
        md_bg_color: app.theme_cls.primary_color
        size_hint: (0.1,0.1)
        halign: 'center'
        pos_hint:{'center_x':0.5,'center_y':0.75}
        
        
    MDRectangleFlatButton:
        text:'Login'
        pos_hint: {'center_x':0.5, 'center_y':0.45 }
        on_press: 
            root.manager.current = 'Login'
            root.manager.transition.direction = 'left'
        
    MDRectangleFlatButton:
        text:'Sign Up'
        pos_hint: {'center_x':0.5, 'center_y':0.35 }
        on_press: 
            root.manager.current = 'SignUp'
            root.manager.transition.direction = 'left'
        
    MDRectangleFlatButton:
        text:'Skip'
        pos_hint: {'center_x':0.5, 'center_y':0.25 }
        on_press:
            root.manager.current = 'Skip'    
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name: 'Login'
    MDLabel:
        text:'Please Enter your login info:'
        halign: 'center'
        pos_hint: {'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
        
    MDTextField:
        id:login_username
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint: (0.7,0.1)
        hint_text: 'Username:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        
    MDTextField:
        id:login_password
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint: (0.7,0.1)
        hint_text: 'Password:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        password: True
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Menu'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Login'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: 
            app.login()
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'up'
            
            
<SignUpScreen>:
    id:SignUp 
    name: 'SignUp'
    MDLabel:
        text:'Please Enter your info:'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)    
        
    MDTextField:
        id:signup_username
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint: (0.7,0.1)
        hint_text: 'Username:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        
    MDTextField:
        id:signup_password
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint: (0.7,0.1)
        hint_text: 'Password:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True  
        password: True
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Menu'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Sign Up'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: 
            app.signup()
            root.manager.current = 'SignUpInfo'
            root.manager.transition.direction = 'right'
           
            
<SignUpInfoScreen>:
    name: 'SignUpInfo'
    MDLabel:
        text:'Please Enter your info:'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDTextField:
        id:isf
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint: (0.7,0.1)
        hint_text: 'Insulin Sensitivity Factor (ISF):'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        
    MDTextField:
        id:icr
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.7,0.1)
        hint_text: 'Insulin/Carb Ratio:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True  
        
    MDTextField:
        id:target
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.7,0.1)
        hint_text: 'What is your target BG?'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        input_filter: 'int'
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Menu'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Submit'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: 
            app.signupInfo()
            root.manager.current = 'Login'
            root.manager.transition.direction = 'down'
        
<SkipScreen>:
    name: 'Skip'
    MDLabel:
        text:'Please Enter your info:'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDTextField:
        id:isf
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint: (0.7,0.1)
        hint_text: 'Insulin Sensitivity Factor (ISF):'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        input_filter: 'int'
        
    MDTextField:
        id:icr
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.7,0.1)
        hint_text: 'Insulin/Carb Ratio:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        input_filter: 'int'  
        
    MDTextField:
        id:target
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.7,0.1)
        hint_text: 'What is your target BG?'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        input_filter: 'int'
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Menu'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Submit'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: 
            app.skip()
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'up'
            
<MenuTwoScreen>:
    name:'Menu2'
    
    MDLabel:
        text:'Select a Function'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDRaisedButton:
        text:'Bolus'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: 
            root.manager.current = 'Bolus'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Settings'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.45}
        on_press: 
            root.manager.current = 'Settings'
            root.manager.transition.direction = 'right'
            
            
    MDRectangleFlatIconButton:
        text:'Help'
        icon:'account-question'
        size_hint: (0.325,0.0595)
        halign: 'center'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press: 
            root.manager.current = 'Help'
            root.manager.transition.direction = 'right'   
            
    MDRectangleFlatIconButton:
        text:'Logout'
        icon:'account'
        size_hint: (0.325,0.0595)
        halign: 'center'
        pos_hint: {'center_x':0.7,'center_y':0.2}
        on_press: 
            root.manager.current = 'Logout'
            root.manager.transition.direction = 'right'
            
<BolusScreen>:
    name: 'Bolus'
    textbox:answer_txt
    
    MDLabel:
        text:'Bolus'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDTextField:
        id:blood_glucose
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint: (0.5,0.1)
        hint_text: 'BG:'
        icon_right: 'blood-bag'
        icon_right_color: app.theme_cls.primary_color
        input_filter: 'int'  
        
    MDTextField:
        id:carbs_consumed
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint: (0.5,0.1)
        hint_text: 'Carbs:'
        icon_right: 'food-fork-drink'
        icon_right_color: app.theme_cls.primary_color
        input_filter: 'int'
    
    MDLabel:
        id:answer_txt
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        halign: 'center'
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
    
    MDRectangleFlatButton:
        text:'Back'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press: 
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'left'   
            
    MDRectangleFlatButton:
        text:'Calculate'
        pos_hint: {'center_x':0.7,'center_y':0.2}
        on_press: 
            app.bolus()
            
<SettingsScreen>:
    name: 'Settings'
    id:settings
    
    MDLabel:
        text:'Settings'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        font_style: 'H4'
                     
    MDRectangleFlatButton:
        text:'Back'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: 
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'left'
            
    MDRectangleFlatButton:
        text:'Change Settings:'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'ChangeSettings'
            root.manager.transition.direction = 'right'

<ChangeSettingsScreen>:
    name: 'ChangeSettings'
    
    MDLabel:
        text:'Please Enter your new info:'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDTextField:
        id:isf
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint: (0.7,0.1)
        hint_text: 'New Insulin Sensitivity Factor (ISF):'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        
    MDTextField:
        id:icr
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.7,0.1)
        hint_text: 'New Insulin/Carb Ratio:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True  
        
    MDTextField:
        id:target
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.7,0.1)
        hint_text: 'New target BG:'
        helper_text: 'Required'
        helper_text_mode: 'on_error' 
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        input_filter: 'int'
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Settings'
            root.manager.transition.direction = 'right'
            
    MDRaisedButton:
        text:'Submit'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: 
            app.changeSettings()
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'down'
            
<HelpScreen>:
    name: 'Help'
    
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    
    MDLabel:
        text:'Help!'
        halign: 'center'
        pos_hint:{'center_y': 0.9}
        font_style: 'H1'
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
    
    MDLabel:
        text:'Bolus:'
        halign: 'center'
        pos_hint:{'center_y': 0.7}
        font_style: 'H4'
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
    
    MDLabel:
        text:'A single dose of a drug or other medicinal preparation given all at once (in this case Insulin).'
        halign: 'center'
        pos_hint:{'center_y': 0.6}
        font_style: 'H6'
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDRaisedButton:
        text:'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: 
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'left'
            
<LogoutScreen>:
    name: 'Logout'
    
    MDLabel:
        text:'Are you sure you want to logout?'
        halign: 'center'
        pos_hint:{'center_y': 0.75}
        theme_text_color:'Custom'
        text_color:(0 / 255.0, 151 / 255.0, 243 / 255.0, 1)
        
    MDRectangleFlatButton:
        text:'Yes'
        pos_hint: {'center_x':0.7,'center_y':0.2}
        on_press: 
            root.manager.current = 'Menu'
            root.manager.transition.direction = 'down'
        
    MDRectangleFlatButton:
        text:'No'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press: 
            root.manager.current = 'Menu2'
            root.manager.transition.direction = 'left'

"""

class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class SignUpInfoScreen(Screen):
    pass

class SkipScreen(Screen):
    pass

class MenuTwoScreen(Screen):
    pass

class BolusScreen(Screen):
    pass

class BolusDialogScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class LogoutScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class ChangeSettingsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(SignUpScreen(name='SignUp'))
sm.add_widget(SignUpInfoScreen(name='SignUpInfo'))
sm.add_widget(SkipScreen(name='Skip'))
sm.add_widget(MenuTwoScreen(name='Menu2'))
sm.add_widget(BolusScreen(name='Bolus'))
sm.add_widget(BolusDialogScreen(name='BolusDialog'))
sm.add_widget(SettingsScreen(name='Settings'))
sm.add_widget(ChangeSettingsScreen(name='ChangeSettings'))
sm.add_widget(HelpScreen(name='Help'))
sm.add_widget(LogoutScreen(name='Logout'))


class SDBMSApp(MDApp):


    def build(self):
        # Dark theme for the GUI
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen


        # todo 1.)Finish Signup system
        # todo 2.)Add database (JSON) and link to user input
        # todo 3.)Dev Login System
        # todo 4.)Design settings screen/function
        # todo 5.)Design graph screen/function


#Method for signing up
    def signup(self):
        #store = JsonStore('UserInfo.json')
        self.signupUsername = self.root.get_screen('SignUp').ids.signup_username.text
        self.signupPassword = self.root.get_screen('SignUp').ids.signup_password.text
        #print (self.signupUsername)
        #print (self.signupPassword)

#Method for login
    def login(self):
        self.loginUsername = self.root.get_screen('Login').ids.login_username.text
        self.loginPassword = self.root.get_screen('Login').ids.login_password.text

        if self.loginUsername == self.signupUsername and self.loginPassword == self.signupPassword:
            self.root.current = 'Menu2'



#Method for signup info!
    def signupInfo(self):
        self.icr = int(self.root.get_screen('SignUpInfo').ids.icr.text)
        self.isf = int(self.root.get_screen('SignUpInfo').ids.isf.text)
        self.target = int(self.root.get_screen('SignUpInfo').ids.target.text)

        print(self.icr)
        print(self.isf)
        print(self.target)

#Method for skip function and info
    def skip(self):
        self.isf = int(self.root.get_screen('Skip').ids.isf.text)
        self.icr = int(self.root.get_screen('Skip').ids.icr.text)
        self.target = int(self.root.get_screen('Skip').ids.target.text)

#Bolus function
    def bolus(self):
        bloodGlucose = int(self.root.get_screen('Bolus').ids.blood_glucose.text)
        carbs = int(self.root.get_screen('Bolus').ids.carbs_consumed.text)

        if self.root.get_screen('Bolus').ids.blood_glucose.text != '':
            self.bolus = (carbs/self.icr) + ((bloodGlucose-self.target)/self.isf)
            print (str(self.bolus))
            self.root.get_screen('Bolus').ids.answer_txt.text = str(self.bolus) + " Units"
            bloodGlucose = int(self.root.get_screen('Bolus').ids.blood_glucose.text)
            carbs = int(self.root.get_screen('Bolus').ids.carbs_consumed.text)



#Method for changing settings
    def changeSettings(self):
        self.isf = int(self.root.get_screen('ChangeSettings').ids.isf.text)
        self.icr = int(self.root.get_screen('ChangeSettings').ids.icr.text)
        self.target = int(self.root.get_screen('ChangeSettings').ids.target.text)



SDBMSApp().run()

