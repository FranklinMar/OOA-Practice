import string
import timeit
import random
import os

f = open("WorkPrac3\\text.txt", "w")
strin = ""
while os.stat("WorkPrac3\\text.txt").st_size < 52428800-1:
    f.write("".join(random.choices(string.ascii_lowercase, k=random.randint(0, 10))))
    f.write("".join(random.choices(string.digits, k=random.randint(0, 10))))
    f.write("".join(random.choices(string.ascii_lowercase, k=random.randint(0, 10))))
    f.write('\n')
    
f.write('\0')

d = """
filename = "WorkPrac3/text.txt"
text = open(filename, 'r').readlines()

s = 0
for i in text:
    if i.strip().isdigit():
        s += int(i.strip())
"""
print(timeit.timeit(d, number=14))

d = """
filename = "WorkPrac3/text.txt"
s = 0
for i in open(filename, 'r'):
    if i.strip().isdigit():
        s += int(i.strip())
"""
print(timeit.timeit(d, number=14))

d = """
filename = "WorkPrac3/text.txt"
s = 0
s = sum(int(i.strip()) for i in open(filename, 'r') if i.strip().isdigit())
"""
print(timeit.timeit(d, number=14))
