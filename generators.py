#generators are functions that produce a sequence of values
#use a method called "lazy generation", yielding one element at a time

def count_from(n):
    while True:
        yield n
        n += 1

for i in count_from(1):
    if i < 11:
        print(i, end=' ') #end specifies what you want at the end of the statement, default is \n
    else:
        break

#can also do generator comprehension - this returns another generator NOT a list
print("\n")
squares = (n*n for n in count_from(1))

for j in squares:
    if j <= 1000:
        print(j, end=' ')
    else:
        break



#not sure why i satrted to use multi-lines sometimes haha
"""
generators will only run when used as an iterator
yield is like return but aloows another continuation cycle
"""