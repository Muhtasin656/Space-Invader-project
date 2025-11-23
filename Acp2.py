import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower = "abcdefghijklmnopqrstuvwxyz"

nums = "0123456789"

chars = upper + lower + nums

password = ""

for i in range(8): # password length = 8:

   password += random.choice(chars)

print(password)