"""
write a program to display sum of number from  1 to n
"""

number = int(input("enter number :"))

total = 0

for i in range(1,number+1):
  
  total+=i
  
print(total)