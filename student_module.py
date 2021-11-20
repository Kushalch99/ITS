state_stack = []
attempts = 0

def update_state(next_level, was_solved, last_state):
  if last_state != None and last_state['level'] == next_level:
    next_state_correct = last_state['correct'] + was_solved
    next_state_incorrect = last_state['incorrect'] + 1 - was_solved
  else:
    next_state_correct = was_solved
    next_state_incorrect = 1 - was_solved
  current_state = { 'level': next_level, 'correct': next_state_correct, 'incorrect': next_state_incorrect }
  if next_state_incorrect == 5:
    return 1
  state_stack.append(current_state)
  return 0

def update_attempts():
  global attempts
  attempts+=1
