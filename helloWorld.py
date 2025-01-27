# print("Hello world!")
# print(1,000,000)
# print(100000000)

# red_bucket = "I am Nisha"
# del red_bucket
# print(red_bucket)
# print(5==4)

# Thomas_age = 3
# age_at_kindergarten = 5

def age_calculator(age, age_at_kindergarten):
    if age == age_at_kindergarten:
        print("Enjoy Kindergarten!")
    elif age < age_at_kindergarten:
        print("Enjoy your stay at home time!")
    else:
        print("Go to a higher grade")

def how_old_will_i_be_in_years(age, n):
    myAge = age+n
    return myAge

age_calculator(5, 5)
age_calculator(4, 5)
age_calculator(8, 5)

print ("I will be ", how_old_will_i_be_in_years(43, 10), "years old in 10 years")

x=0
while (x<5):
    print(x)
    x= x+1

for x in range (5, 10):
    print(x)
