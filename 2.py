from collections import Counter

def countFrequency_1(s) -> map:
    string_count = {}

    for char in s:
        # Using the get method to handle characters not yet in the dictionary
        string_count[char] = string_count.get(char, 0) + 1
    
    return string_count

def countFrequency_2(s) -> map:

    string_count = Counter(s)
    # Converting the Counter object to a dictionary and returning it
    return dict(string_count)

print(countFrequency_1("sapstar"))
print(countFrequency_2("aaabbbbcc"))