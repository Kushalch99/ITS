import random
import math

def generate_ques(last_state):
  if last_state == None:
      frac1, frac2 = generate_frac(0)  
      next_level = 0
  else:
    if last_state['correct'] == 2:
      frac1, frac2 = generate_ques(last_state['level'] + 1)
      next_level = last_state['level']+1
    else:
      frac1, frac2 = generate_ques(last_state['level'])
      next_level = last_state['level']
  return frac1, frac2, next_level

def generate_frac(level):
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

def solution(frac1, frac2):
  lcm = math.lcm(frac1['den'], frac2['den'])
  final_num = frac1['num']*(lcm / frac1['den']) + frac2['num']*(lcm / frac2['den']) 
  gcd = math.gcd(int(final_num), lcm)
  final_num = int(final_num/gcd)
  final_den = int(lcm/gcd)
  solution_frac = { 'num': final_num, 'den': final_den }
  return solution_frac
