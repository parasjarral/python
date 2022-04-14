# defining a function 
# Syntax "def"+ variable_name + ()
# in () you can add any arguments if you want

#1
# def age_p():
#     print("Assalamu Aliakum")
#     print("What is your age")
#     print("My age is 25")
    
# age_p()

# # 2
# def na_p():
#     gr="Assalamu Aliakum"
#     wh="What is your Name"
#     na="My name is Muhammad Paras"
#     print("",gr,"\n",wh,"\n",na)

# na_p()



# 3 define and add if elif and else statement in function

joining_age=5

def age_sch(given_age,na):
    if joining_age == given_age :
        print(na," you can join the School")
    elif given_age>joining_age:
        print(na," you can go to high school")
    elif given_age <=2 :
        print(na," you are a baby and it take some time to get in the school")
    else:
        print(na," you are Too Child ")


age_sch(int(input("What is your age ? ")),input("What is your Name ? "))

# 4
# def futr(age):
#     n_age=age+10
#     return n_age

# future=futr(25)
# print(future)
