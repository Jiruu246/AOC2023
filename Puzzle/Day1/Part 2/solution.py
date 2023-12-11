import sys

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dict_numbers = {"one": "1", "two": "2", "three": "3", "four":"4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

lines = sys.stdin.read().strip().splitlines()        

def findFirstNum(array_of_element, search_string):
    res = ""
    pos = -1
    for element in array_of_element:
        new_pos = search_string.find(element)
        if new_pos != -1 and (pos < 0 or new_pos < pos):
            pos = new_pos
            res = element

    if pos == -1:
        print("Cannot find any number in ", search_string)
    return res     

Sum = 0
for line in lines:
    firstNum = findFirstNum(numbers + word_numbers, line)
    firstNum = dict_numbers.get(firstNum, firstNum)

    flipped_word_numbers = [element[::-1] for element in word_numbers]

    secondNum = findFirstNum(numbers + flipped_word_numbers, line[::-1])[::-1]
    secondNum = dict_numbers.get(secondNum, secondNum)
    
    Sum += int(firstNum + secondNum)
print("Sum: ", Sum)
