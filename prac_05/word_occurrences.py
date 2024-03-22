"""
Word Occurrences
Estimate: 30 minutes
Actual: 25 minutes
"""

word_to_count = {}
lengths = []

text = input("Text: ")
phrases = text.split(" ")
for text in phrases:
    if text in word_to_count.keys():
        word_to_count[text] += 1
    else:
        word_to_count[text] = 1

list_words = word_to_count.keys()
sorted_words = sorted(list_words)

for phrases in word_to_count.keys():
    length = len(phrases)
    lengths.append(length)
    width = max(lengths)

for text in sorted_words:
    print(f"{text:<{width}}: {word_to_count[text]}")
