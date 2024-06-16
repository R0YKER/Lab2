
def task0(number1, number2):
    result = number1 + number2
    return result

def task1(number1, znak, number2):
if znak == '>':
return number1 > number2
  elif znak == '<':
return number1 < number2
    elif znak == '>=':
return number1 >= number2
  elif znak == '<=':
return number1 <= number2
  elif znak == '==':
return number1 == number2
  elif znak == '!=':
return number1 != number2
  else:
    return False  

def task2(text, number):
return len(text) > number

def task3(number1, number2, number3):
return number1 == number2 == number3

print(task0(5, 3))
print(task1(5, '>', 3))
print(task2('hello', 3))
print(task3(2, 2, 2))
