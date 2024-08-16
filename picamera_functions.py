#!/usr/bin/python

#Import modules
from time import sleep
from picamera import PiCamera
from datetime import datetime
from guizero import App, PushButton, Text, Window, Picture, ButtonGroup
import sys
import glob
import os

def update_gui():
    #settings_window.hide()
    take_pic.enable()
    set_pic.enable()
    #new_pic.enable()
    
    camera.start_preview(fullscreen=False, window=(190,10,500,500))
    
#def slider_changed(slider_value):
#    slider_message.value = slider_value
#    global tiny_window_height
#    tiny_window_height = slider_value

def change_exp():
    global what_is_selected
    global activities
    what_is_selected.value = activities.value
    

def settings():
    #global tiny_window_height
    settings_window.show(wait = True)
    close_sets.show()
    
    what_is_selected.show()
    what_is_selected.enable()
    
    exp_choice.show()
    exp_choice.enable()
    
#    slider.show()
#    slider.enable()
#    slider_message.show()
#    slider_message.enable()
    close_sets.enable()
    camera.start_preview(fullscreen=False, window=(430,230,275,275))
    
    
def close_settings():
    settings_window.hide()
#    close_sets.hide()
#    slider.hide()
#    slider.disable()
#    slider_message.hide()
#    slider_message.disable()
    
    what_is_selected.hide()
    what_is_selected.disable()
    
    exp_choice.hide()
    exp_choice.disable()
    
    exp_choice.show()
    exp_choice.enable()
    
    update_gui()
    
def close_play():
    play_window.hide()
    close_player.hide()
    next_pic.hide()
    previous_pic.hide()
    
    close_player.disable()
    next_pic.disable()
    previous_pic.disable()
    
    update_gui()
    
def open_player():
    camera.stop_preview()
    play_window.show(wait = True)
    close_player.show()
    next_pic.show()
    previous_pic.show()
    
    close_player.enable()
    next_pic.enable()
    previous_pic.enable()
    
    global piclist 
    piclist = sorted(glob.glob("./*" + filetype), key=os.path.getmtime)
    global pic_number
    pic_number = -1
    
    current_pic = piclist[pic_number]
    
    dispimg.image = current_pic
    dispimg.show()
    
#def view_picture():
    
    
def next_picture():
    global pic_number
    pic_number = pic_number - 1
    current_pic = piclist[pic_number]
    dispimg.image = current_pic
    
def previous_picture():
    global pic_number
    pic_number = pic_number + 1
    current_pic = piclist[pic_number]
    dispimg.image = current_pic

def take_picture():
    global output
    camera.stop_preview()
    output = datetime.now().strftime("IMG-%Y%m%d_%H%M%S")
    camera.capture(output + filetype)
    
    update_gui()
    
def take_lapse():
    camera.stop_preview()
    camera.close()
    for i in range(90):
        with picamera.PiCamera() as camera:
            camera.resolution = (3280,2464)
            sleep(1) # Camera warm-up time
            output = datetime.now().strftime("IMG-%Y%m%d_%H%M%S")
            camera.capture(output + filetype)
        # Capture one image every 30 secs
        sleep(29)
    
    
def quit_camera():
    camera.stop_preview()
    camera.close()
    sys.exit()
    #update_gui()

camera = PiCamera()
camera.resolution = (3280,2464)
camera.rotation = (270)


filetype = '.jpg'
exp_mode = 'auto'
exp_modelist = ''

app = App("Infrapi Camera", 720, 480,layout="grid")

#app = App("Infrapi", 720, 480,layout="grid")
#message = Text(app, 'Test')
#new_pic = PushButton(app, command=new_picture, text="New Picture", grid=[0,1], width=20,height=4)
take_pic = PushButton(app, command=take_picture, text="Take Picture", grid=[0,1], width=20,height=4)
play_pic = PushButton(app, command=open_player, text="Play", grid=[0,2], width=20,height=4)
set_pic = PushButton(app, command=settings, text="Settings", grid=[0,3], width=20,height=4)
quit_pic = PushButton(app, command=quit_camera, text="Quit", grid=[0,4], width=20,height=4)

settings_window = Window(app, "Settings", height=720,width=480,layout="grid",visible=False)
exp_choice = ButtonGroup(settings_window, options=['auto','off','night','sports'], selected='auto',grid=[0,2],visible=False,enabled=False,command=change_exp)
what_is_selected = Text(settings_window, text="auto",visible=False,enabled=False,grid=[0,3])
#slider = Slider(settings_window, grid=[0,2], start=200,end=480, visible=False,enabled=False, command=slider_changed)
#slider_message = Text(settings_window, visible=False,enabled=False,grid=[0,1])
close_sets = PushButton(settings_window, command=close_settings, text="Back", grid=[0,0], width=20,height=4,visible=False)

play_window = Window(app, "Play", height=720,width=480,layout="grid",visible=False)
next_pic = PushButton(play_window, command=next_picture, text="next >", grid=[0,0], width=20,height=4,visible=False)
previous_pic = PushButton(play_window, command=previous_picture, text="< previous", grid=[0,2], width=20,height=4,visible=False)
close_player = PushButton(play_window, command=close_play, text="Back", grid=[0,1], width=20,height=4,visible=False)
dispimg = Picture(play_window, grid=[1,0,1,3],height=300,width=400,visible=False)

update_gui()

app.display()

#camera.stop_preview()
#camera.close()
#app.exit_full_screen()
