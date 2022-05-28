# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def cleaning_word(word):
    word = word.strip("")
    word=sorted(word)
    while " " in word:
        word.remove(" ")
    print(word)


def find_anagram(word, anagram):
    if cleaning_word(word) == cleaning_word(anagram):
        isAnagram = True
        print("These two sets of words are an anagram.")
    else:
        isAnagram = False
        print("These two sets of words are not an anagram")
    return isAnagram

print("Please enter the first word:")
word1 = input()
print("Please enter the second word:")
word2 = input()
find_anagram(word1, word2)

