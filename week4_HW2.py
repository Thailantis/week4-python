# 1. Reverse the list below in-place using an in-place algorithm. For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_list(words):
    left = 0
    right = len(words) - 1

    while left < right:
      # Reverse the strings at the same time.
        words[left], words[right] = words[right][::-1], words[left][::-1]

        words[left], words[right] = words[right], words[left]

        left += 1
        right -= 1

reverse_list(words)

print(words)

# 2. Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key 
# and the value as the amount of times that word appears in the string.
#Should output:
#{'a': 5,
#'abstract': 1,
#'an': 3,
#'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def distinct_thesaurus(a_text):
  words = a_text.lower().split()

  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
      return len(word_counts), word_counts
    

num_words, word_counts = distinct_thesaurus(a_text)
print("Number of distinct word:", num_words)
print("Word counts:", word_counts)
  
# 3. Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.
# Hint: Linear Searching will require searching a list for a given number.

arr = [10,23,45,70,11,15]
target = 70

def linear_search(arr, target):
  
  for i in range(len(arr)): #O(N)
    if arr[i] == target: #O(N)
        return i #O(1)
    else:
        return -1 #O(1)

result = linear_search(arr, target)

print(result)
# Time complexity is #O(N) linear
