#Given a string s, find the length of the 
#longest substring without repeating characters.
#Example
#Input: s = "bbbbb"
#Output: 1
#Input: s = "pwwkew"
#Output: 3


# Function to find the length of the longest substring without repeating characters
def longest_substring(s):
    start = 0
    max_length = 0
    seen = {}
    # Dictionary to store the last seen index of each character
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start: 
            # Check if the character has been seen and is within the current substring
            start = seen[char] + 1 
        seen[char] = i
        
        max_length = max(max_length, i - start + 1)
 
    return max_length


print(longest_substring("bbbbb"))   
print(longest_substring("pwwkew"))  
