import random as r

letters = "qwertyuiopasdfghjklzxcvbnm"
uletters = letters.upper()
nums = "0123456789"
simbols = "!@#$%&"

def generate(lenght,count):
    passwords = []
    while len(passwords) < count:
        passwd = ""
        while len(passwd) != lenght:
            x = r.choice([letters,uletters,nums,simbols])
            passwd += r.choice(list(x))
        passwords.append(passwd)
    return passwords
    

a = int(input("password lenght: "))
b = int(input("how many passwords print? : "))
list_of_passwords = generate(a,b)
n = 1
for i in list_of_passwords:
    print(f"{n}) {i}")
    n += 1
