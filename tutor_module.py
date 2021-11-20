from student_module import state_stack, attempts, update_state, update_attempts
from expert_module import generate_ques, solution
from helper_module import stringify_frac
import math

def solve_cm(num1, num2):
  from user_interface import user_input_lcm, print_screen
  print_screen('Let\'s try to find the common multiple of ' + str(num1) + ' and ' + str(num2))
  input_cm = user_input_lcm()
  if input_cm%num1 == 0 and input_cm%num2 == 0:
    print_screen('Correct ' + str(input_cm) + ' is a common multiple of ' + str(num1) + ' and ' + str(num2))
    print_screen(' Use this multiple to solve the problem ')
    return
  else:
    print_screen('Incorrect! Try Again!')
    solve_cm(num1, num2)

def solve_gcd(num1, num2):
  from user_interface import user_input_gcd, print_screen
  gcd = math.gcd(num1, num2)
  print_screen('Let\'s try to find the greatest divisor of ' + str(num1) + ' and ' + str(num2))
  input_gcd = user_input_gcd()
  if input_gcd == gcd:
    print_screen('Correct ' + str(input_gcd) + ' is the greatest divisor of  ' + str(num1) + ' and ' + str(num2))
    print_screen(' Use this gcd to reduce the fraction ')
    return
  else:
    print_screen('Incorrect! Try Again!')
    solve_gcd(num1, num2)


def start_tutoring(): 
  from user_interface import print_screen
  last_state = None if len(state_stack) == 0 else state_stack[-1]
  frac1, frac2, next_level = generate_ques(last_state)
  if next_level == -1:
    print_screen('Congratulations! You have completed the Assignment.')
    return
  print_screen('Solve : ' + stringify_frac(frac1) + " + " + stringify_frac(frac2))
  solution_frac = solution(frac1, frac2)
  was_solved = solve(frac1, frac2, solution_frac)
  exit_tutoring = update_state(next_level, was_solved, last_state)
  if exit_tutoring == 1:
    print_screen('Read the lesson and try again!')
    return
  return start_tutoring()

def solve(frac1, frac2, solution_frac):
  from user_interface import get_user_input, print_screen
  global attempts
  input_frac = get_user_input()
  if input_frac['num'] == solution_frac['num'] and input_frac['den'] == solution_frac['den'] :
    print_screen('Excellent! This is the correct answer!')
    return 1
  elif input_frac['den'] == solution_frac['den']:
    print_screen('The LCM of both denominators are correct, but the numerator is wrong. Try again!')
    return solve(frac1, frac2, solution_frac)
  elif input_frac['den']%solution_frac['den'] == 0:
    ratio = int(input_frac['den']/solution_frac['den'])
    if input_frac['num'] == solution_frac['num']*ratio:
      print_screen('The solution is correct but not minimal, let\'s try to reduce the fraction')
      solve_gcd(input_frac['num'], input_frac['den'])
      return solve(frac1, frac2, solution_frac)
    else:
      print_screen('The common multiple of denominators is correct but not minimal, Numerators are wrong.')
      return solve(frac1, frac2, solution_frac)
  else:
    if frac1['num']+frac2['num'] == input_frac['num'] and frac1['den']+frac2['den'] == input_frac['den']:
      print_screen('Adding numerators and denominators in not the correct method')
      return solve(frac1, frac2, solution_frac)
    else:
      print_screen('Your input is incorrect!')
      if attempts == 0:
        print_screen('Let\'s try to break it down')
        solve_cm(frac1['den'], frac2['den'])
        update_attempts()
        return solve(frac1, frac2, solution_frac)
      if attempts == 3:
        print_screen('I think you are stuck')
        print_screen('The solution is : ' + stringify_frac(solution_frac))
        return 0 
  
