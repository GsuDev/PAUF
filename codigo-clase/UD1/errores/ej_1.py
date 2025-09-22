
userInput = input("Dame un numero para hacerle x3\n")

try:
  res = int(userInput) * 3
  print(res)
except Exception as e:
  print("ERROR-Hermano, un numero no un string")
  
