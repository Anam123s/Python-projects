import random
#random module is necesary for generating any random number or letter
print("Welcome to password generator 😜")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols=['!','@','#','$','%','^','&','*','(',')','+','-','*','/']

numbers=['1','2','3','4','5','6','7','8','9','0']

no_letters=int(input("How many letters do you want in your password: "))
no_symbols=int(input("How many symbols do you want: "))
no_numbers=int(input("How many numbers do you want: "))

password=[]
#as the range only works till n-1 so we had done +1 for that 
for i in range(1,no_letters+1):
    fun=random.choice(letters)
    password+=fun


for i in range(1,no_symbols+1):
    fun=random.choice(symbols)
    password+=fun


for i in range(1,no_numbers+1):
    fun=random.choice(numbers)
    password+=fun

#shuffle is used to shuffle all the character to generate strong passwrd
random.shuffle(password)
new_pass=""
for i in password:
    new_pass+=i
print(new_pass)
