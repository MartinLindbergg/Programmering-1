'''
#Exempel 1
total = 0
for counter in range(100):
  total += 10
  print(total)


#Exempel 2
for i in range(10):
  print(i)


#Exempel 3

x = range(3, 20, 2)
for i in x:
    print(i)
'''

#exempel 4
start = int(input("Type starting value: "))
step = int(input("Type Increcement: "))
stop = int(input("Type stop value: "))

for value in range(start, stop, step):
    print(value)
