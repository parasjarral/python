# while loop 
# for loop

# While loop

# x=0
# while x<5:
#     print(x)
#     x=x+1


# for loop

# for x in range(5,10):
#     print(x)


# array 

days=["Monday", "Tuesday", "Wednesday","Thursday", "Friday","Satuarday","Sunday"]

for d in days:
    # if d=="Friday":   # break the line 
    #     break
    if d=="Friday":
        continue        # skip the friday
    print(d)