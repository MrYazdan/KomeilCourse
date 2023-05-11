n = 23

# Control-flow 

# if n > 12:
# 	print("Bozorgtar az 12")
# elif n > 15:
# 	print("Bozorgtar az 15")
# elif n > 20:
# 	print("Bozorgtar az 20")
# else:
# 	print("Koochik tar az 12")

# if n > 12:
# 	print("Bozorgtar az 12")
# if n > 15:
# 	print("Bozorgtar az 15")
# if n > 20:
# 	print("Bozorgtar az 20")
# else:
# 	print("Koochik tar az 12")

n = 23

# if n > 12:
# 	print("Bozorgtar az 12")

# 	if n > 15:
# 		print("Bozorgtar az 15")
# 	elif n > 20:
# 		print("Bozorgtar az 20")
# else:
# 	print("Koochik tar az 12")

# Loops

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for
n = 0

# for i in 'salam abolfazl :)':
# for i in True:
# for i in [12,323,4354,234,656,2342]: 

# range(100) -> 0 -> 100-1
# range(10, 100) -> 10 -> 100-1
# range(10, 101, 10) -> 10, 20, ... 100
# range(start, stop, step)



# for i in range(100, 10, -5):
# 	n = n + 1

# 	print("N:",n,"=> ",i) 

"""
Tamrin: 
shekl zir ra ba adad delkhah bein 1 ta 100
besazid:

mesal:
n = 10

*
**
***
****
*****
******
*******
********
*********
**********

# 2

soale ghabl ra be shekl heram besazid:

mesal:
n = 7 

   *
  ***
 *****
*******

"""

# n = 7
# for i in range(1,n+1, 2):
# 	print((((n-i)//2)*' ')+('*'*i))
# 	print(('*'*i).center(n))


"""

#3

n = 7

phonix os
remix os
android 86x

   *
  ***
 *****
*******
 *****
  ***
   *

"""

# tazamani ke adad fard bashad:
# adad ba 3 jam shaval
# ba adad zoj - meghdar chap shavad!

# res = 0
# while True:
# 	n = int(input("Enter a number: "))

# 	if n % 2 != 0:
# 		res += 3
# 	else:
# 		break
# print(res)


number = int(input())
n = 1

while n < number:
	print((n * '@').center(number))
	n += 2 # n = n - 2

n = number

while n > 0:
	print((n * '@').center(number))
	n -= 2 # n = n - 2



