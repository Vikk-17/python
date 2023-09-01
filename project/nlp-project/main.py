from nltk.book import * 

# saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']

# tokens = set(saying)
# print(tokens)

# tokens = sorted(tokens)
# print(tokens)

# tokens[-2:]
# print(tokens)


# print(text1)

fdist1 = FreqDist(text1)
print(fdist1)

vocabulary1 = fdist1.keys()
# print(vocabulary1)
vocabulary1[:50]
print(vocabulary1)