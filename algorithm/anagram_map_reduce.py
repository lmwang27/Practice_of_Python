"""
Use Map Reduce to find anagrams in a given list of words.
Example 1:

Input: "lint lint lnit ln"
Output:
  ["lint", "lint", "lnit"]
  ["ln"]
Example 2:

Input: "ab ba cab"
Output:
  ["ab", "ba"]
  ["cab"]

"""


class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value' here
        for word in line.split():
            yield ''.join(sorted(list(word))), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, list(values)
