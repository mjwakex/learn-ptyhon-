#tuples - immutable, fixed length, can be heterogenous
def showTuples() :
    a = (1, 1.0, 'a', "hello") #heterogenous tuple
    print(a[0]) #accessing elements the same as lists
    b = (1, 2.0, 'b', "world")
    c = ((a[0],b[0]), (a[1],b[1])) #len will be 2 
    print(c)
    # can be indexed, aliced and combined
    print(a[0:2]) #will print (1,1.0)
    print(a[:4]) #print the first 4 elements
    #we can also use zip whoch will work the same as tuple c
    d = list(zip(a,b))
    print(d)
    #can also convert lost to tuple and visa-versa
    e = tuple([1,2,3])
    print(e)
    f = list((42, "hello", True))
    print(f)
    #iterrating over tuples
    for i in a:
        print(i)
    
#sets - no duplicate elements, can be heterogenous
def showSets():
    numbers = [1,2,3,4,5,4,5]
    uniqueNumbers = set(numbers)
    print(numbers)
    print(uniqueNumbers)
    print(1 in uniqueNumbers) #use in to see if member of set
    #union and intersection of sets
    moreUniqueNumbers = set([1,7,8,5,3,8,9,10])
    print(uniqueNumbers.union(moreUniqueNumbers)) #print all the numbers
    print(uniqueNumbers.intersection(moreUniqueNumbers))


#dictionaries - key-value pairs, keys are unique, lookup value assosiated with a key
def showDicts(): 
    alphabet = {1: 'a', 2: 'b', 3: 'c'}
    print(type(alphabet)) #dict
    print(1 in alphabet) #check if key in dict
    print(alphabet[1]) #get value from key
    alphabet[3] = 'd' #modify element 
    del alphabet[2] #delete element
    alphabet[5] = 'e' #add new key-value pair
    print(alphabet.keys()) #print all keys
    #iterate over a dict
    for i in alphabet.keys():
        print(i, alphabet[i]) #iterate over keys
    for k, v in alphabet.items():
        print(k, v) #iterate over items, k-v pair will be in tuples
        

    


