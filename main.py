import random
import math

def generate_frac():
  num = random.randint(1, 9)
  den = random.randint(num+1, 9)
  return { 'num': num, 'den': den }

def stringify_frac(frac):
  return str(frac['num']) + '/' + str(frac['den'])

def solution(frac1, frac2, lcm):
  final_num = frac1['num']*(lcm / frac1['den']) + frac2['num']*(lcm / frac2['den']) 
  gcd = math.gcd(int(final_num), lcm)
  final_num = int(final_num/gcd)
  final_den = int(lcm/gcd)
  solution_frac = { 'num': final_num, 'den': final_den }
  return solution_frac

def solve_cm(num1, num2):
  print('Let\'s try to find the common multiple of ' + str(num1) + ' and ' + str(num2))
  input_cm = 0
  while True:
    try:
      input_str = input('Enter the common multiple : ')
      input_cm = int(input_str)
    except:
      print('Incorrect input format')
      continue
    if input_cm%num1 == 0 and input_cm%num2 == 0:
      print('Correct ' + str(input_cm) + ' is a common multiple of ' + str(num1) + ' and ' + str(num2))
      print(' Use this multiple to solve the problem ')
      return
    else:
      print('Incorrect! Try Again!')


def solve_gcd(num1, num2):
  gcd = math.gcd(num1, num2)
  print('Let\'s try to find the greatest divisor of ' + str(num1) + ' and ' + str(num2))
  input_gcd = 0
  while True:
    try:
      input_str = input('Enter the greatest divisor : ')
      input_gcd = int(input_str)
    except:
      print('Incorrect input format')
      continue
    if input_gcd == gcd:
      print('Correct ' + str(input_gcd) + ' is the greatest divisor of  ' + str(num1) + ' and ' + str(num2))
      print(' Use this gcd to reduce the fraction ')
      return
    else:
      print('Incorrect! Try Again!')


def solve(frac1, frac2, solution_frac):
  input_frac = { 'num': 0, 'den': 0 }
  while True:
    try:
      input_str = input(' Enter your solution : ')
      variables = input_str.split('/')
      input_frac['num'] = int(variables[0])
      input_frac['den'] = int(variables[1])
    except:
      print('Incorrect input format. Please provide num/den format input. E.g ' + stringify_frac({'num': 3, 'den': 4}))
      continue
    if input_frac['num'] == solution_frac['num'] and input_frac['den'] == solution_frac['den'] :
      print('Excellent! This is the correct answer!')
      return
    elif input_frac['den'] == solution_frac['den']:
      print('The LCM of both denominators are correct, but the numerator is wrong. Try again!')
    elif input_frac['den']%solution_frac['den'] == 0:
      ratio = int(input_frac['den']/solution_frac['den'])
      if input_frac['num'] == solution_frac['num']*ratio:
        print('The solution is correct but not minimal, let\'s try to reduce the fraction')
        solve_gcd(input_frac['num'], input_frac['den'])
      else:
        print('The common multiple of denominators is correct but not minimal, Numerators are wrong.')
    else:
      if frac1['num']+frac2['num'] == input_frac['num'] and frac1['den']+frac2['den'] == input_frac['den']:
        print('Adding numerators and denominators in not the correct method')
      else:
        print('Your input is incorrect, let\'s try to break it down')
        solve_cm(frac1['den'], frac2['den'])

if __name__ == "__main__":
  frac1 = generate_frac()
  frac2 = generate_frac()
  lcm = math.lcm(frac1['den'], frac2['den'])
  solution_frac = solution(frac1, frac2, lcm)
  print('Solve : ' + stringify_frac(frac1) + ' + ' + stringify_frac(frac2))
  solve(frac1, frac2, solution_frac)
