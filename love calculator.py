print("welcome to the love calculator")
first_name=input("what is the first name?: ")
second_name=input("what is the second name?: ")

combined_name= first_name+second_name
combined_lower= combined_name.lower()

#check count in inputs
t=combined_lower.count("t")
r=combined_lower.count("r")
u=combined_lower.count("u")
e=combined_lower.count("e")

first_digit = int(t+r+u+e)

l=combined_lower.count("l")
o=combined_lower.count("o")
v=combined_lower.count("v")
e=combined_lower.count("e")


second_digit = int(l+o+v+e)

combined_digits = int(str(first_digit) + str(second_digit))

print ("your score is:", combined_digits)
if combined_digits <10 or combined_digits >90:
    print ("you got together like coke and mentos")
elif combined_digits >=40 and combined_digits <= 50:
    print(" you go alright together")
else: pass

