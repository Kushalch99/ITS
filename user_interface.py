from helper_module import stringify_frac
from tutor_module import start_tutoring
import pyglet
from time import sleep
import os
import speech_recognition as sr
sample_rate = 48000
chunk_size = 2048
device_id = 0
r = sr.Recognizer()
def audio_input():
  while True:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
          chunk_size = chunk_size) as source:
      r.adjust_for_ambient_noise(source)
      r.pause_threshold = 1  
      try:
        audio = r.listen(source)
        text = r.recognize_google(audio, language="en-GB")
        print("you said: " + text)
        number = int(text)
        return number
      except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio. Please try again")
      except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0} . Please try again!".format(e))
      except:
        print("Error listenting to the voice ! Please try again!")
          
def get_user_input():
  input_frac = { 'num': 0, 'den': 0 }
  print_screen('Enter the numerator')
  input_frac['num'] = audio_input()
  print_screen('Enter the denominator')
  input_frac['den'] = audio_input()
  return input_frac
      
def user_input_gcd():
  print_screen('Enter the greatest divisor: ')
  input_gcd = audio_input()
  return input_gcd
    
def user_input_lcm():
  print_screen('Enter the common multiple: ')
  input_cm = audio_input()
  return input_cm
  

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
