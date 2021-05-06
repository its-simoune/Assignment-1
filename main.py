 Question 1
 Question = 'Please write your first and last name :)'
 print(Question)
 Name = input()
 Switch = Name.find(' ')
 print(Name[Switch:], Name[:Switch])

 Question 2
 x = int(input()) # x is number input
 if x % 2 != 0:
  # print('Number is odd')
 elif x == 0:
   print('Number is a zero')
 else:
   print('Number is even')

 Question 3
x = int(input())
for i in range(1, 31 +1):
  if x == i:
    print('January', x)
for j in range(32, 59 + 1):
  if x == j:
    print('February', x)
for k in range(60, 90 + 1):
  if x == k:
    print('March', x)
for l in range(91, 121 + 1):
  if x == l:
    print('April', x)
for m in range(122, 151 + 1):
  if x == m:
    print('May', x)
for n in range(152, 181 + 1):
  if x == n:
    print('June', x)
for b in range(182, 212 + 1):
  if x == b:
    print('July', x)
for v in range(213, 243 + 1):
  if x == v:
    print('August', x)
for h in range(244, 273 + 1):
  if x == h:
    print('September', x)
for u in range(274, 305 + 1):
  if x == u:
    print('October', x)
for y in range(306, 335 + 1):
  if x == y:
    print('November', x)
for t in range(336, 365 + 1):
  if x == t:
    print('December', x)

 Question 4
 a = 5
 i = 0
 for i in range(a, 0, -1):
     for j in range(i, 0, -1):
       print(j, end = "")
     print(" ")

 Question 5
 Question = 'What is the maximum number of your wished pattern?'
 print(Question)
 b = int(input())
 i = 0
 for i in range(a, 0, -1):
     for j in range(i, 0, -1):
       print(j, end = "")
     print(" ")

 Extra:
x = int(input())

if x == 1:
  print('Day 1, Monday')
elif x == 2:
  print('Day 2, Tuesday')
elif x == 3:
  print('Day 3, Wednesday')
elif x == 4:
  print('Day 4, Thursday')
elif x == 5:
  print('Day 5, Friday')
elif x == 6:
  print('Day 6, Saturday')
elif x == 7:
  print('Day 7, Sunday')
else:
  print(' ')