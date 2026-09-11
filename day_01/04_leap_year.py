"""
write a program to chk year is leap year or not

"""

year = int(input("enter a year :"))

if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
  
  print(True)
  
else:
  
  print(False)