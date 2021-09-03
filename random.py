import random
import string
random.choice(string.ascii_uppercase)
n=input()
b=n[::-1]
print(random.choice(string.ascii_uppercase)+b)
