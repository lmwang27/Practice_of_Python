"""
Use map reduce to build inverted index for given documents.
Example
Look at the program.

"""


class Document:
    def __init__(self, m_id, content):
        self.id = m_id
        self.content = content


class InvertedIndex:
    """
    # @param {Document} value is a document
    """
    def mapper(self, value):
        for word in value.content.split():
            yield word, value.id

    def reducer(self,key,values):
        # Please use 'yield key, value' here
        yield key, sorted(list(set(values)))


if __name__ == "__main__":
    input = [{"id": 1, "content": "This is the content of document1"},
             {"id": 2, "content": "This is the content of document2"}]

    word_map = {}

    test = InvertedIndex()

"""
    for data in input:
        for word, m_id in test.mapper(data):
            word_map.setdefault(word, []).append(m_id)

    for word in word_map:
        print(word, word_map[word])
"""
