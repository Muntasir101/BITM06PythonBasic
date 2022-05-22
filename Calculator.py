#calculator-CUSTOM
def calculator():
  a=float(input("enter the first num: "))
  b=float(input("enter the second num: "))
  op=input("enter the desired opeation (sum/sub/mul/div): ")
  s= a+b
  su= a-b
  m= a*b
  d= a/b
  if op =='sum':
     print("Summation of the Numbers: ", s)
  elif op == 'sub':
     print("Subtarction of the Numbers: ",su)
  elif op == 'mul':
     print(" Multiplication of the Numbers:", m)
  elif op == 'div':
     print("Division of the Numbers: ", d)
  else:
     print("Invalid Opea")
calculator()