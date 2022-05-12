# Given an array of characters and another array of words, find an efficient algorithm that can tell which words can be formed with the characters of the array.
 
# Example: 
chars = ['t','e','g','r','a','o','a','m','t','z','i']; 
words = ['gomeria','arroz','tarta']; # true - false - true

def getCharCount(chars):

    charCount = {}
    for char in chars:
        if char in charCount:
            charCount[char] = charCount[char] + 1
        else:
            charCount[char] = 1

    return charCount
    
def processWord(word, charCount):
    usedChar =  {}
    for char in word:
        if char not in charCount:
            return False
        else:
            if char in usedChar:
                usedChar[char] = usedChar[char] + 1
            else:
                usedChar[char] = 1

            if usedChar[char] > charCount[char]:
                return False
    return True

def checkWords(chars, words):
    charCount = getCharCount(chars)
    for word in words:
        print(processWord(word,charCount))



print(checkWords(chars, words))

