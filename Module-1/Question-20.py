#20. Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user.
# To generate a password, randomly take some words from the user input and then include numbers,
# special characters and capital letters to generate the password. Also, keep a check that password
# length is more than 8 characters.   Note: Include Exception handling wherever required. Also, make
# a ‘User’ class and store the details like user id, name and password of each user as a tuple.

import random
import string

n = "dev"
word = list(n)

m = 3
num = []
for i in range(0,m):
    num.append(random.randint(0,9))

l=3
chars = []
for i in range(0,l):
    chars.append(random.choice(string.ascii_letters))
chars.append(random.choice(string.ascii_uppercase))


sp = []
o=2
for i in range(0,o):
    sp.append(random.choice(string.punctuation))

password=word+sp+chars+num
random.shuffle(password)
# print(password)

class user:
    uid = 0
    name = ""
    password = []
    save = list()
    def info(self,uid,name,password):
        self.uid = uid
        self.name = name
        self.passowrd = password
        self.save.append(uid)
        self.save.append(name)
        self.save.append(password)
        l2 = tuple(self.save)
        print(l2)

a = user()
a.info(12,"dev",password)