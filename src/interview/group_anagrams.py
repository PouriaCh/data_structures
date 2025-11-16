"""Group words that are anagrams of each other.

Args:
    strings: Iterable of lowercase words.

Returns:
    List of lists where each sub-list contains the words that share the same
    character multiset.

Example:
    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
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

if __name__ == "__main__":
    print("1st set:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print("\n2nd set:")
    print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

    print("\n3rd set:")
    print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

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
