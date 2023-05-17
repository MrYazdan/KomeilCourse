"""
Tamrin:
 - barname adadi bein 1 ta 100 ra entekhab konad :
 - 10 shans be bazikon bedahad
 - ta zamani ke shans dashte bashad, mitavanad hads bezanad
 - agar adad karbar bishtar ya kamtar bood , gizaresh dahad
 - bazikon barande adad ra peida mikonad
 - dar soorat bakht ya bord, Bazi tamam shavad
"""

# from random import randint
# number = randint(1,100)

# shans = 10

# while shans > 0:

# 	voroodi = int(input(str(10 - shans+1) + ") hads shoma: "))
# 	shans = shans - 1

# 	if voroodi > number:
# 		print("Adad barname koochektare :)")
# 	elif voroodi < number:
# 		print("Adad barname bozorgtare :)")
# 	else:
# 		print("Shoma bordi ^_^")
# 		break
# else:
# 	print("Shoma bakhti :(")

# input()

# List
numbers = [12,2,4,6,7,8,1,0,45,52,100]
alphabets = ['a', 'a', 'b']
other = [True, 1, 0.75, 'Salam'] 

# print(numbers[0]) # 12
# print(numbers[1]) # 2
# print(numbers[-1]) # 100
# print(numbers[-2]) # 52
# print(numbers[2:5]) # [4,6,7]
# print(numbers[2:-1]) # [4,6,7,8,1,0,45,52]
# print(numbers[2:]) # [4,6,7,8,1,0,45,52,100]
# print(numbers[2:7:2]) # [4,7,1]
# print(numbers[2::-1]) # reverse

# print(numbers[::-1]) # [100, 52, 45, 0, 1, 8, 7, 6, 4, 2, 12]
# print(numbers[::-2]) # [100, 45, 1, 7, 4, 12]
# print(numbers[::-3]) # [100,0,7,2]
# print(numbers[::-1][::2]) # [100, 45, 1, 7, 4, 12]

# print(numbers[1:10:2][3]) # 0
# print(numbers[1:10:2][::-1][3]) # 6

# Append
books = ["shahname"]

# 1: 
# books += ["boostan"]
books += ["boostan", "golestan"]

# 2:
books.append('leyli & majnoon')
# books.append('kelile & demneh', 'masnavi') # Error

# Length -> andaze, tool

print(len(books))
# print(len(books[80])) # Out OF Range
