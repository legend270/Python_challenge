#Day3 of the 90 days challenge

#user's age as input
age = int(input("Enter your age: "))

#checking for eligibility
if age < 18:
    print("You are too young to vote.")
elif age >=18 and age < 21:
    print("You are eligible to vote but not for all candidates ")
else:
    print("You are eligible to vote and access all candidates ")
    
#check eligibility for senior citizen retirement 20
if age >+ 60:
    print("You are eligible for senior citizen retirement")