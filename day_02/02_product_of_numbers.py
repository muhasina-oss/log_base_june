"""
write a program to display product of number from  1 to n
"""

number = int(input("enter number :"))

product = 1

for i in range(1,number+1):
  
  product*=i
  
print(product)