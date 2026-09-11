

"""
write a program to print largest of three numbers

"""

number_1 = int(input("eneter number 1 :"))
number_2 = int(input("eneter number 2 :"))
number_3 = int(input("eneter number 3 :"))

if number_1>number_2 and number_1>number_3:
  
  print("largest is",number_1)
  
elif number_2>number_1 and number_2>number_3:
  
  print("largest is",number_2)
  
else:
  
  print("largest is",number_3)
    