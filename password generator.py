import random
import string
def genpass():
    print("Generated password:")
    for i in passw:
        print(i,end='')
    passw.clear()
def numpass():
    n=int(input("Enter no of characters required:"))
    for i in range(n):
        r=random.randint(0,9)
        passw.append(r)
    genpass()
    global runmas
    runmas=input("\nContinue?(yes/no) *case sensitive*:")
def alphanum():
    n=int(input("Enter no of characters required:"))
    for i in range(n):
        x=random.randint(1,2)
        if x==1:
            r=random.randint(0,9)
            passw.append(r)
        elif x==2:
            r=random.choice(string.ascii_letters)
            passw.append(r)
    genpass()
    global runmas
    runmas=input("\nContinue?(yes/no) *case sensitive*:")
def run():
    choice=int(input("Enter choice from menu(1,2 or 3):"))
    if choice==1:
        numpass()
    elif choice==2:
        alphpass()
    elif choice==3:
        alphanum()
    else:
        print("Invalid Input")
        
print("Generated password:")
print("Password Generator")
passw=[]
#print(random.choice(string.ascii_letters)) = random letter
#ascii_lowercase or ascii_upercase
def alphpass():
    n=int(input("Enter no of characters required:"))
    for i in range(n):
        r=random.choice(string.ascii_letters)
        passw.append(r)
    genpass()
    global runmas
    runmas=input("\nContinue?(yes/no) *case sensitive*:")
print("MENU")
print("1. Number only")
print("2. Alphabet only")
print("3. AlphaNumeric")
runmas=input("Continue?(yes/no) *case sensitive*:")
while runmas=='yes':
    run()
if runmas!='yes':
    print("program terminated")
