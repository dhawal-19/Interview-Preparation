"""
Title: Find anagrams.

Problem: Given a string s and a non-empty string p,
         find all the start indices of p's anagrams in s.

         Strings consists of lowercase English letters only and
         the length of both strings s and p will not be larger than 20,100.

         The order of output does not matter.

Execution: python find_anagrams.py
"""
from collections import Counter


def find_anagrams(s: str, p: str):
    """Function for finding anagrams."""
    result_list = []
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p) - 1])

    for i in range(len(p) - 1, len(s)):

        # Include a new character in the window.
        s_counter[s[i]] += 1

        # This step is O(1), since there are at most 26 English letters.
        if s_counter == p_counter:
            # Append the starting index.
            result_list.append(i - len(p) + 1)

        # Decrease the count of oldest character in the window.
        s_counter[s[i - len(p) + 1]] -= 1
        if s_counter[[i - len(p) + 1]] == 0:
            # Remove the count if it is zero.
            del s_counter[s[i - len(p) + 1]]
    return result_list


if __name__ == '__main__':
    print(find_anagrams("abcabc", "abc"))
