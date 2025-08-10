#Given two words, beginWord and endWord, and a dictionary of words wordList, return the 
# number of words in the shortest transformation sequence from beginWord to endWord, such that:
#Only one letter can be changed at a time.
#Each transformed word must exist in the word list.
#Return 0 if no such sequence exists.
#All words have the same length and consist of lowercase letters only.
#beginWord is not considered a transformed word and may not be in wordList.

#Example:
#Input:
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5


 #function to find the length of the shortest transformation sequence from beginWord to endWord
def ladder_length_simple(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    # Function to check if two words are different by exactly one letter
    def one_letter_diff(w1, w2):
        return sum(a != b for a, b in zip(w1, w2)) == 1
     
     
    def dfs(word, visited):
        if word == endWord:
            return 1
        shortest = float('inf')
        for w in wordList:
            if w not in visited and one_letter_diff(word, w):
                visited.add(w)
                steps = dfs(w, visited)
                if steps:
                    shortest = min(shortest, 1 + steps)
                visited.remove(w)
        return shortest if shortest != float('inf') else 0
    
    return dfs(beginWord, {beginWord})

print(ladder_length_simple("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
