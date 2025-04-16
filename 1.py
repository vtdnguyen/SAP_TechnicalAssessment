from collections import Counter

def firstUniqChar_1(s) -> int:
      # Using a dictionary to count the frequency of each character in the string
      string_count = {}

      for c in s:
            string_count[c] = string_count.get(c, 0) + 1
            
      # Iterating through the map to find the first unique character
      for key, value in string_count.items():
            if value == 1:
                return key
      return None

def firstUniqChar_2(s) -> int:
      # Using Counter to count the frequency of each character in the string
      string_count = Counter(s)
      # Using a generator expression to find the first unique character
      # and returning it directly
      return next((n for n in s if string_count[n] == 1),None)

print(firstUniqChar_1("spstaar")) 
print(firstUniqChar_2("aabbcc"))
