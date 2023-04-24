# 1. In this kata, You will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    return [i for i in l if isinstance(i, int)]     #0(1) constant
    
# Time complexity is constant

# 2. You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?
# Write a simple function to check if the string contains the word hallo in different languages.
# These are the languages of the possible people you met the night before: hello - english, ciao - italian, salut - french, hallo - german, hola - spanish, 
# ahoj - czech republic, czesc - polish

def validate_hello(greetings):
    valid_hello = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'] #0(N) linear
    for word in valid_hello: #0(N) linear
        if word in greetings.lower(): #0(N) linear
            return True
    return False
    
# Time complexity is linear

# 3. Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.
# Example: Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

def flatten_and_sort(array):
    flat_arr = [] #0(1) constant
    for sub_arr in array: #0(N) linear
        for num in sub_arr: #0(N) linear
            flat_arr.append(num) #0(1) constant
    return sorted(flat_arr) #0(1) constant
    
# Time complexity are both linear and constant
