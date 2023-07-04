#The factorial
def factorial(digit):
  result=1
  for x in range(digit,0,-1):
    print(f"{x} ",end='')
    result*=x
  return result
#Divisors
def divisors(digit):
  list=[]
  for x in range(digit,0,-1):
    if digit% x== 0:
      list.append(x)
  return list
#Revers the String
def reversStrings(str):
  return str[len(str)::-1]
# Return even numbers
def evens(list):
  evens_list=[]
  for x in list:
    if x%2==0:
      evens_list.append(x)
  return evens_list
#Check password
def checkPassword(str):
  uppercase=False
  number=False
  character=False
  length=len(str)>=8
  for s in str:
    if s.isupper():
      uppercase=True
    if s.isnumeric():
      number=True
    if not s.isnumeric() and not s.isalpha():
      character=True
    if uppercase and number and character and length:
      return "Strong password"
  return "Weak password"
# Valid IPv4 address
def isAdress(str):
  periods_numbers=str.count('.')==3 
  period_1=str.find('.')
  period_2=str.find('.',period_1+1)
  period_3=str.find('.',period_2+1)
  periods_distance=period_2-period_1>1 and period_3-period_2>1
  if str.count('.')>3:
    return "extra period"
  if not periods_distance:
    return "consecutive periods"
  periods=periods_numbers and periods_distance
  str_list=str.split('.')
  list_Validation=len(str_list)==4
  if not periods_numbers or not list_Validation:
    return "missing octet"
  number_validations=True
  
  for i in str_list:
    if len(i)>1:
      if  i[1:].isnumeric() and i[0]=='-':
          return "negative number"
    if i.isnumeric():
      number_validations *=0>=int(i)<=255
      if  (len(i)>1 and (int(i[0])==0)):
        if int(i[0])<int(i[1]):
          return "leading zero in octet "
        if len(i)>2:
          if int(i[0])==int(i[1])>int(i[2]):
            return "leading zero in octet "
      elif 255<int(i):
        return "octet value too large"
  if periods and list_Validation and number_validations:
    return "extra period"
      
             
def main():
  print(f"\n{factorial(int(input('Enter a digit to give you it factorial: ')))}")
  print(f"{divisors(int(input('Enter a digit to give you it divisors: ')))}")
  print(reversStrings(input('Enter a String to reverse: ')))
  list_1=[1, 2, 3, 4, 5, 6]
  list_2=[5, 3, 18, 4, 2, 7, 10]
  list_3=[5, 3, 11, 5, 1, 7, 27]
  print(evens(list_1))
  print(evens(list_2))
  print(evens(list_3))
  print(checkPassword("Hello5?world"))
  print(checkPassword("password"))
  print(checkPassword("Password123"))
  print(isAdress("192.168.1.-1"))
main()