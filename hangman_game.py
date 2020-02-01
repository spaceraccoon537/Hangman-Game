import sys
word=input("Enter the word: ")
a=[]
str1=word
unique=[]
for char in str1[::]:
    if char not in unique:
        unique.append(char)
length=len(word)
length_uni=len(unique)
for i in range(length):
    a=a+['_']
print(a)
print("")
guesses=int(input("Enter the number of guesses: "))
while(guesses>0):
    b=0
    for k in range(length_uni):
        for s in range(len(a)):
            if(a[s]=='_'):
                b=b+1
        if(b==0):
            print("@@@@@@@@@@@@@YOU WIN@@@@@@@@@@@@@@@@")
            sys.exit()
        guess=input("Enter the word you think: ")
        print(b)
        count=0
        for k in range(length):
            if(word[k]==guess):
                count=1
                a[k]=word[k]
        if(count==1):
            print(a)
            print("Guesses=",guesses)
            if(guesses<=0):
                print("!!!!!!!!!!!!YOU LOSE!!!!!!!!!!!!!!")
        else:
            guesses=guesses-1
            print(a)
            print("Guesses=",guesses)
            if(guesses<=0):
                print("!!!!!!!!!!!!YOU LOSE!!!!!!!!!!!!!!")
                print("The word was: ",word)
                sys.exit()
print(a)
print("@@@@@@@@@@@@@YOU WIN@@@@@@@@@@@@@@@@")
