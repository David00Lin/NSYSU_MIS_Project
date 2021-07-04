# -*- coding: utf-8 -*-
import time
from slackbot.bot import respond_to, listen_to
import re
import subprocess
from functions import camera
from functions import upload
from functions import moist
from functions import temperature

# おはようテスト
@listen_to('good morning')
@respond_to('good morning')
def ohayou(message, *something):
    message.reply('good morning sir!')
    
@listen_to('hello')
@respond_to('hello')
def functions(message, *something):
    message.reply('Hello sir!\n'
                  'What service do you want?\n'
                  '-*turn on camera*\n'
                  '-*moist*\n'
                  '-*temper*\n')
    
@listen_to('turn on camera')
@respond_to('turn on camera')
def bedroom_camera_on(message, *something):
    #subprocess.run(["/home/pi/Desktop/home work/Final_Project/slack/camera.py" , "on"])
    camera.test()
    time.sleep(1)
    upload.main()
    message.reply('yes, sir!')
    
@listen_to('moist')
@respond_to('moist')
def sitsudo(message, *something):
    #subprocess.run(["/home/pi/Desktop/home work/Final_Project/slack/camera.py" , "on"])
    rep = moist.moist()
    message.reply("%s"%rep)
    
@listen_to('temperature')
@respond_to('temperature')
def ondo(message, *something):
    #subprocess.run(["/home/pi/Desktop/home work/Final_Project/slack/camera.py" , "on"])
    rep = temperature.temperature()
    message.reply("%s"%rep)