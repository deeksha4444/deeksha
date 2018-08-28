number1= int(input('enter number1: '))
a=3
a=a+1.0
print(a)

b=10
c=b>9
print(c)



import random
number = random.randint(1,10)
guesses=0
while guesses<3:
    guess= int(input('enter a number from 1 to 10: '))
    guesses=guesses+1
    print('this is your %d guesses' %guesses)
    if guess < number:
        print('you guessed too low')
    elif guess > number:
        print('you guessed too high')
    elif guess==number:
        break
if guess == number:
   print('wow! you got it right good job')

if guess != number:
       print("The secret number was", number)
 hn 