"""
LAB: ANAGRAM DETECTOR
GOAL: Write a python program that can detect two words that are anagrams.
"""

def anagram(s1, s2):
    s1 = sorted(s1.replace(" ", ""))  #sort the iterable into a sorted list
    s2 = sorted(s2.replace(" ", ""))) #sort the iterable into a sorted list
    print(s1) #bug check
    print(s2) #bug check
    if s1 == s2:
       print("This is an anagram")
    else:
       print("This is not an anagram")

word1 = input("enter word 1:\n>>:")
word2 = input("enter word 2:\n>>:")

# print(word1) #bug checker
# print(word2) #bug checker
anagram(word1, word2)
