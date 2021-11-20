from helper_module import stringify_frac
from tutor_module import start_tutoring
import pyglet
from time import sleep
import os

def get_user_input():
  input_frac = { 'num': 0, 'den': 0 }
  while True:
    try:
      print_screen(' Enter your solution ')
      input_str = input()
      variables = input_str.split('/')
      input_frac['num'] = int(variables[0])
      input_frac['den'] = int(variables[1])
      return input_frac
    except:
      print_screen('Incorrect input format. Please provide num/den format input. E.g ' + stringify_frac({'num': 3, 'den': 4}))
      continue

def user_input_gcd():
  while True:
    try:
      print_screen('Enter the greatest divisor: ')
      input_str = input()
      input_gcd = int(input_str)
      return input_gcd
    except:
      print_screen('Incorrect input format')
      continue
    
def user_input_lcm():
  while True:
    try:
      print_screen('Enter the common multiple: ')
      input_str = input()
      input_cm = int(input_str)
      return input_cm
    except:
      print_screen('Incorrect input format')
      continue    

def print_screen(string):
  # TODO: text to voice
  print(string)
  from gtts import gTTS
  tts = gTTS(string, lang='en')
  file = 'text_to_audio.mp3'
  tts.save(file)
  music = pyglet.media.load(file, streaming=False)
  music.play()
  sleep(music.duration) #prevent from killing
  os.remove(file) #remove temperory file


def start():
  start_tutoring()

if __name__ == '__main__':
  start()
# print_screen("hello")
