import random
import string

num = int(input("Пожалуйста, введите:"))
password = ''.join(random.sample(string.digits + string.ascii_letters,num))
print(password)