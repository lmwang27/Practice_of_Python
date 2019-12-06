"""
Using map reduce to count word frequency.

https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html#Example%3A+WordCount+v1.0

Example 1:

Input:
    chunk1: "Google Bye GoodBye Hadoop code"
    chunk2: "lintcode code Bye"

Output:
    Bye: 2
    GoodBye: 1
    Google: 1
    Hadoop: 1
    code: 2
    lintcode: 1
Example 2:

Input:
    chunk1: "Lintcode is so so good"

Output:
    Lintcode: 1
    good: 1
    is: 1
    so: 2
"""

"""
• Step1 Input
• Step2 Split
• Step3 Map 实现怎么把文章切分成单词
• Step4 Partition sort
• Step5 Fetch + Merge
• Step6 Reduce 实现怎么把单词统一在一起 
• Step7 Output
"""

class WordCount:
    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    chunk1 = "Google Bye GoodBye Hadopp lintcode"
    chunk2 = "lintcode Google code"
    chunk3 = "Bye Bye Google"

    test = WordCount()

    word_map = {}
    for word, count in test.mapper(chunk1):
        word_map.setdefault(word, []).append(count)
    for word in word_map:
        print(word, word_map[word])
    for word, count in test.mapper(chunk2):
        word_map.setdefault(word, []).append(count)
    for word in word_map:
        print(word, word_map[word])
    for word, count in test.mapper(chunk3):
        word_map.setdefault(word, []).append(count)
    for word in word_map:
        print(word, word_map[word])

    results = {}

    for word in word_map:
        results[word] = sum(word_map[word])

    for word in results:
        print(word, results[word])



"""
When to use yield instead of return in Python?
The yield statement suspends function’s execution and 
sends a value back to caller, but retains enough state to 
enable function to resume where it is left off. When resumed, 
the function continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, rather them 
computing them at once and sending them back like a list.

Let’s see with an example:
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 
    


Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.
"""