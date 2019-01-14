#The second tutorial of PYTeach covers Conditionals and Looping
#Below are multiple examples of loops and conditionals and how to use them

#If Statement
x = 3
if x = 3:
	print("x = 3")

#If...Else Statements
y = 4

if y == 5:
	print("y = 5")
else:
	print("y is not 5")

#If...Elif
z = 3

if z == 1:
	print("z = 1")
elif z == 2:
	print("z = 2")
elif z == 3:
	print("z = 3")

#Nested if
a = 30

if a < 100:
	if a % 2 == 0:
		print("a is less than 100 and is divisable by 2")

#While Loop
b = 0

while b < 5:
	print("b is", b)
	b += 1

#For loop

for i in range(0, 4):
	print("i is", i)

#Nested Loop
#Below prints triangle using nested loops
for i in range(0, n):
    for j in range(0, i+1):
        print("* ",end="")
        print("\r")
