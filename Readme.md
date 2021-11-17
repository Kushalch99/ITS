# Intellingent Tutoring Systen
  Intelligent tutoring system to teach elementary mathematics to visually impaired children.
--------------
--------------
Levels
0: Denominator is same, simply add the numerators (2 ques) <br/>
1: Denominator is different but the gcd for them is 1 (2 ques)<br/>
2: Denominator is different but the gcd for them is not 1 (2 ques)<br/>
--------------
--------------
frac -> { num: , den: } <br/>
state -> { level: , correct: , incorrect: } <br/>
state_stack -> stack of the state, the top indicates the latest level and the correct and incorrect answers in that level <br/>
--------------
