"""
You have been given an array of strings, where each string may contain only lowercase English letters.
You need to write a function group_anagrams(strings) that groups the anagrams in the array together
using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], 
the function should return [["eat","tea","ate"],["tan","nat"],["bat"]]
because the first three strings are anagrams of each other, the next two strings
are anagrams of each other, and the last string has no anagrams in the input array.
"""

def group_anagrams(strings):
    all_strings_hash_list = {}

    for string in strings:
        hash_table = {char: True for char in string}
        sorted_hash_string = str(sorted(hash_table))
        
        if not all_strings_hash_list.get(sorted_hash_string):
            all_strings_hash_list[sorted_hash_string] = [string]
        else:
            all_strings_hash_list[sorted_hash_string].append(string)
    
    return list(all_strings_hash_list.values())
######################################

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
