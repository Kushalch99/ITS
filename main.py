'''
Levels
0: Denominator is same, simply add the numerators (1 ques)
1: Denominator is different but the gcd for them is 1 (2 ques)
2: Denominator is different but the gcd for them is not 1 (2 ques)
'''

'''
frac -> { num: , den: }
state -> { level: , correct: , incorrect: }
state_stack -> stack of the state, the top indicates the latest level and the correct and incorrect answers in that level
'''

import random
import math

state_stack = []

def generate_frac():
  num = random.randint(1, 8)
  den = random.randint(num+1, 9)
  return { 'num': num, 'den': den }

def stringify_frac(frac):
  return str(frac['num']) + '/' + str(frac['den'])

def solution(frac1, frac2):
  lcm = math.lcm(frac1['den'], frac2['den'])
  final_num = frac1['num']*(lcm / frac1['den']) + frac2['num']*(lcm / frac2['den']) 
  gcd = math.gcd(int(final_num), lcm)
  final_num = int(final_num/gcd)
  final_den = int(lcm/gcd)
  solution_frac = { 'num': final_num, 'den': final_den }
  return solution_frac

def solve_cm(num1, num2):
  print('Let\'s try to find the common multiple of ' + str(num1) + ' and ' + str(num2))
  input_cm = 0
  incorrect_attempt = 0
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
      incorrect_attempt+=1
      if incorrect_attempt == 2:
        print('I think you are stuck! Try multiplying both the numbers')
      elif incorrect_attempt == 3:
        print('One of the common multiple is ' + str(num1*num2))
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
  incorrect_attempt = 0
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
      return 1
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
        print('Your input is incorrect!')
        if incorrect_attempt == 0:
          print('Let\'s try to break it down')
          solve_cm(frac1['den'], frac2['den'])
        incorrect_attempt+=1
        if incorrect_attempt == 3:
          print('I think you are stuck')
          print('The solution is : ' + stringify_frac(solution_frac))
          return 0 

def generate_ques(level):
  num1 = random.randint(1, 9)
  num2 = random.randint(1, 9)
  if level == 0:
    den =  random.randint(1, 9)
    return { 'num': num1, 'den': den }, { 'num': num2, 'den': den }
  if level == 1:
    den1 = random.randint(1, 9)
    den2 = den1*random.randint(1, 9)
    return { 'num': num1, 'den': den1 }, { 'num': num2, 'den': den2 }
  if level == 2:
    den1 = random.randint(1, 9)
    den2 = random.randint(1, 9)
    while den2%den1 == 0:
      den2 = random.randint(1, 9)
    return { 'num': num1, 'den': den1 }, { 'num': num2, 'den': den2 }

def start_tutoring():
  next_level = -1
  last_state = None
  while True:
    if len(state_stack) == 0:
      frac1, frac2 = generate_ques(0)  
      next_level = 0
    else:
      last_state = state_stack[-1]
      if last_state['correct'] == 2:
        frac1, frac2 = generate_ques(last_state['level'] + 1)
        next_level = last_state['level']+1
      else:
        frac1, frac2 = generate_ques(last_state['level'])
        next_level = last_state['level']
    print('Solve : ' + stringify_frac(frac1) + " + " + stringify_frac(frac2))
    solution_frac = solution(frac1, frac2)
    was_solved = solve(frac1, frac2, solution_frac)
    if last_state != None and last_state['level'] == next_level:
      next_state_correct = last_state['correct'] + was_solved
      next_state_incorrect = last_state['incorrect'] + was_solved
    else:
      next_state_correct = was_solved
      next_state_incorrect = was_solved
    current_state = { 'level': next_level, 'correct': next_state_correct, 'incorrect': next_state_incorrect }
    if next_state_incorrect == 5:
      print('Please learn addition first!')
      break
    state_stack.append(current_state)
  return

if __name__ == "__main__":
  start_tutoring()
