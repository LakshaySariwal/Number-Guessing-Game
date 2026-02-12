
import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    
    a=int(input("guess a number here : "))
    if(a>n):
        print(" guess a lower number please")
        guesses +=1
    elif(a<n):
        print("guess a higher number please")
        guesses +=1

print(f"you have guessed the number {n} correctly after {guesses} attempts")