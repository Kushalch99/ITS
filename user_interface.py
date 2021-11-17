from helper_module import stringify_frac
from tutor_module import start_tutoring

def get_user_input():
  input_frac = { 'num': 0, 'den': 0 }
  while True:
    try:
      # TODO: Voice to Text
      input_str = input(' Enter your solution : ')
      variables = input_str.split('/')
      input_frac['num'] = int(variables[0])
      input_frac['den'] = int(variables[1])
      return input_frac
    except:
      print('Incorrect input format. Please provide num/den format input. E.g ' + stringify_frac({'num': 3, 'den': 4}))
      continue

def user_input_gcd():
  while True:
    try:
      input_str = input('Enter the greatest divisor : ')
      input_gcd = int(input_str)
      return input_gcd
    except:
      print('Incorrect input format')
      continue
    
def user_input_lcm():
  while True:
    try:
      input_str = input('Enter the common multiple : ')
      input_cm = int(input_str)
      return input_cm
    except:
      print('Incorrect input format')
      continue    

def print_screen(string):
  # TODO: text to voice
  print(string)

def start():
  start_tutoring()

if __name__ == '__main__':
  start()
